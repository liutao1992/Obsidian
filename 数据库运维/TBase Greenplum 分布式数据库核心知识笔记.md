---
title: TBase / Greenplum 分布式数据库核心架构与 OOM 排查笔记
date: 2025-06-18
tags:
  - database
  - tbase
  - greenplum
  - distributed-database
  - oom
  - architecture
  - troubleshooting
aliases:
  - TBase Greenplum 核心架构与 OOM 排查
---

# TBase / Greenplum 分布式数据库核心架构与 OOM 排查笔记

## 一、整体架构

TBase / Greenplum 是基于 PostgreSQL 的**分布式数据库**。

核心思想：

> 将数据分布到多个节点，通过多个节点并行计算，提高大规模数据处理能力。

整体架构：

```text
                 Client
                    |
                    |
              Coordinator
              （协调节点）
                    |
        -------------------------
        |           |           |
    Segment1    Segment2    Segment3
    （执行节点） （执行节点） （执行节点）

```

核心组件：

| 组件                | 职责                 |
| ----------------- | ------------------ |
| Coordinator       | 接收 SQL、生成执行计划、协调执行 |
| Segment           | 存储数据、执行计算          |
| Data Distribution | 决定数据如何分布到 Segment  |

---

# 二、Coordinator（协调节点）

## 1. 定义

Coordinator 是数据库的入口。

类似：

> 分布式数据库的大脑。

客户端所有请求首先进入 Coordinator。

---

## 2. 主要职责

### （1）接收 SQL

例如：

```sql
select *
from alarm
where device_id = 100;
```

请求：

```
Client
 |
 v
Coordinator
```

---

### （2）生成执行计划

Coordinator 分析：

* 表在哪里
* 数据在哪些 Segment
* 是否需要 Join
* 是否需要排序
* 是否需要数据重新分布

生成：

```
Query Plan
```

---

### （3）分发任务

例如：

三个 Segment：

```
        Coordinator

             |
 --------------------------
 |            |             |

 S1           S2            S3

```

Coordinator 将执行计划发送给 Segment。

---

### （4）汇总结果

Segment：

```
S1 返回 1000 条

S2 返回 2000 条

S3 返回 3000 条
```

Coordinator：

```
合并结果

↓

返回客户端
```

---

# 三、Segment（执行节点）

## 1. 定义

Segment 是：

> 真正保存数据并执行 SQL 的节点。

可以理解为：

```
一个独立 PostgreSQL 实例
```

每个 Segment 拥有：

* CPU
* 内存
* 磁盘
* PostgreSQL 进程

例如：

```
服务器A

 PostgreSQL
      |
   Segment1


服务器B

 PostgreSQL
      |
   Segment2


服务器C

 PostgreSQL
      |
   Segment3

```

---

# 四、数据如何存储到 Segment？

核心机制：

## 数据分片（Data Distribution）

创建表：

```sql
create table device
(
 id bigint,
 name varchar
)
distributed by(id);
```

数据库根据：

```
hash(id)
```

决定数据去哪。

例如：

三个 Segment：

```
hash(id)%3
```

数据：

| id | Segment  |
| -- | -------- |
| 1  | Segment1 |
| 2  | Segment2 |
| 3  | Segment3 |
| 4  | Segment1 |
| 5  | Segment2 |

最终：

```
          device

             |

       hash(id)

             |

 ----------------------

 S1       S2       S3

1,4      2,5       3

```

---

# 五、SQL 执行流程

以：

```sql
select count(*)
from alarm;
```

为例。

## 第一步

客户端发送 SQL：

```
Client

  |

Coordinator

```

---

## 第二步

Coordinator 分析：

```
alarm 表分布在三个 Segment
```

生成：

```
Aggregate Plan
```

---

## 第三步

发送任务：

```
             Coordinator


                 count(*)

                    |

 --------------------------------

 S1             S2             S3


 count          count          count

```

---

## 第四步

Segment 本地计算：

```
S1:

100万


S2:

200万


S3:

300万

```

---

## 第五步

Coordinator 汇总：

```
100万
+
200万
+
300万

=

600万
```

返回：

```
6000000
```

---

# 六、Segment 为什么容易出现 OOM？

因为：

> SQL 真正执行发生在 Segment。

例如：

```sql
select *
from alarm
order by create_time;
```

执行：

```
Coordinator

     |

分发任务

     |

----------------

S1       S2       S3


排序     排序     排序

```

如果：

```
S1 正常

S2 正常

S3 数据量巨大
```

那么：

```
S3 内存耗尽

↓

整个 SQL 失败
```

---

# 七、常见 Segment 内存爆炸 SQL

## 1. ORDER BY

例如：

```sql
select *
from alarm
order by time;
```

执行：

```
扫描数据

↓

排序

↓

返回
```

排序需要大量：

```
Sort Buffer
```

---

## 2. JOIN

例如：

```sql
select *
from A
join B
on A.id=B.id;
```

可能：

```
读取小表

↓

建立 Hash Table

↓

匹配大表
```

Hash Table 在内存中。

大表 JOIN：

容易 OOM。

---

## 3. GROUP BY

例如：

```sql
select
device_id,
count(*)
from alarm
group by device_id;
```

内部：

```
device_id

    |

Hash Table

    |

count
```

如果分组数量巨大：

消耗大量内存。

---

## 4. DISTINCT

例如：

```sql
select distinct device_id
from alarm;
```

可能：

```
排序去重

或者

Hash 去重
```

---

# 八、Vmem Limit（数据库内存保护机制）

错误：

```
Vmem limit reached
```

含义：

> Segment 使用内存超过数据库限制。

注意：

不是：

```
Java OOM
```

不是：

```
Linux OOM
```

而是：

```
数据库自身限制
```

---

## 示例

配置：

```
gp_vmem_protect_limit = 8GB
```

当前：

```
Segment 已使用 8190MB
```

继续申请：

```
8MB
```

结果：

```
8190 + 8 > 8192

↓

拒绝申请

↓

OOM
```

---

# 九、本次异常分析

异常：

```
failed to acquire resources on one or more segments

FATAL: Out of memory

Vmem limit reached
```

含义：

流程：

```
Java

 |

JDBC

 |

Coordinator

 |

生成执行计划

 |

Segment执行SQL

 |

Sort / Join / Aggregate

 |

申请内存

 |

超过Vmem限制

 |

Segment失败

 |

SQL失败

```

---

# 十、为什么提示申请几 MB 失败？

例如：

```
failed to allocate 8389018 bytes
```

约：

```
8MB
```

并不是：

```
8MB导致OOM
```

真实情况：

```
之前已经使用大量内存

↓

剩余空间=0

↓

最后8MB申请失败
```

---

# 十一、Segment 数据倾斜（Data Skew）

## 定义

数据没有均匀分布。

正常：

```
S1 10GB

S2 10GB

S3 10GB
```

异常：

```
S1 10GB

S2 10GB

S3 100GB
```

结果：

```
S3:

CPU高

IO高

内存高

容易OOM
```

---

## 常见原因

分布键选择错误。

例如：

错误：

```sql
distributed by(status)
```

因为：

```
status:

SUCCESS
FAILED
RUNNING

```

只有少量值。

大量数据集中到少数 Segment。

---

# 十二、问题排查流程

## 1. 找 SQL

第一优先级：

找到真正执行失败 SQL。

---

## 2. 查看执行计划

执行：

```sql
EXPLAIN ANALYZE
SQL;
```

重点关注：

### Sort

```
Sort
```

### Hash Join

```
Hash Join
```

### HashAggregate

```
HashAggregate
```

### Motion

```
Redistribute Motion
```

---

## 3. 查看数据量

```sql
select count(*)
from table;
```

关注：

* 百万级
* 千万级
* 亿级

---

## 4. 检查索引

重点：

WHERE：

```
where device_id
```

JOIN：

```
on id
```

ORDER：

```
order by time
```

---

## 5. 检查资源配置

关注：

```sql
show gp_vmem_protect_limit;

show work_mem;

show statement_mem;
```

---

# 十三、优化方向

## 优先优化 SQL

不要：

```sql
select *
from huge_table;
```

改：

```sql
select id,name
from huge_table
limit 1000;
```

---

## 分页查询

避免：

```
一次返回百万数据
```

使用：

```
limit

游标分页

where id > lastId
```

---

## 减少 JOIN 数据量

先过滤：

```sql
select *
from alarm
where time > now()-interval '1 day'
```

再 JOIN。

---

## 最后才调整资源

增加：

```
gp_vmem_protect_limit

statement_mem

work_mem
```

原因：

资源增加不能解决错误 SQL。

---

# 十四、核心认知总结

## 1.

> Coordinator 负责协调，Segment 负责真正执行。

## 2.

> 分布式数据库 SQL 性能问题，最终大部分发生在 Segment。

## 3.

> 一个 Segment 出问题，会导致整个 SQL 失败。

## 4.

> `Vmem limit reached` 表示数据库执行 SQL 时超过内存限制，不是 JVM 问题。

## 5.

遇到：

```
failed to acquire resources on one or more segments
+
Vmem limit reached
```

排查顺序：

```
SQL
 ↓
执行计划
 ↓
Segment数据分布
 ↓
数据量
 ↓
资源配置
```

核心思想：

> 分析 TBase / Greenplum 问题时，不能只看应用层，要理解 SQL 最终如何被 Coordinator 分发到 Segment，以及 Segment 如何消耗 CPU、IO 和内存。
