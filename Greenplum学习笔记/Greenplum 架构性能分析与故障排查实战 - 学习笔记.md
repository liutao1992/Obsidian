---
title: Greenplum 架构、性能分析与故障排查实战 — 学习笔记
date: 2025-06-18
tags:
  - greenplum
  - database
  - learning
  - notes
  - architecture
  - performance
  - troubleshooting
  - oom
  - mpp
aliases:
  - Greenplum 学习笔记
  - GP 实战学习笔记
---

# Greenplum 架构、性能分析与故障排查实战 — 学习笔记

> **个人学习目标**：培养能够独立分析和定位 Greenplum 线上问题的高级后端工程师能力，而非传统 DBA。
> 
> **学习风格**：原理 + 实验 + 真实案例。

---

## 学习定位

| 维度 | 说明 |
| ---- | ---- |
| 面向对象 | Java / Spring Boot 后端工程师，日常与 Greenplum 打交道 |
| 核心目标 | 看懂执行计划、定位性能瓶颈、独立排查 OOM 等线上故障 |
| 学习方法 | 理论 → 实验 → 案例 → 源码（可选） |
| 最终产出 | 个人 [[Greenplum CaseBook]] |

> [!important] 核心认知
> 这门课不是教你怎么安装维护数据库，而是教你怎么**理解 Greenplum 的行为**，从而写出对的 SQL、快速定位线上问题。

---

## 阶段总览

```text
第一阶段：基础架构
    ↓
第二阶段：分布式执行原理
    ↓
第三阶段：SQL 执行计划分析
    ↓
第四阶段：GPORCA 优化器
    ↓
第五阶段：资源管理
    ↓
第六阶段：性能分析
    ↓
第七阶段：线上故障分析
    ↓
第八阶段：源码阅读（可选）
    ↓
第九阶段：案例库建设（持续）
```

---

# 第一阶段：Greenplum 基础架构

> **目标**：理解 Greenplum 为什么这样设计。

## 第 1 章 Greenplum 整体架构

- Greenplum 简介
- MPP（Massively Parallel Processing）架构
- Shared Nothing 架构
- Greenplum 与 PostgreSQL 的区别
- Greenplum 与 MySQL、Oracle 的区别

**实验**：安装 Greenplum、登录数据库、查看系统架构

---

## 第 2 章 集群组成

- Coordinator 的职责
- Segment 的职责
- Mirror 与故障切换
- Master Catalog
- `gp_segment_configuration`

**实验**：

- 查看 Segment 状态
- 查看集群配置
- 观察 Coordinator 如何调度 SQL

---

## 第 3 章 数据存储

- Heap Table
- AO（Append-Optimized）Table
- AOCO Table
- Append Only 原理
- `VACUUM` 与 `ANALYZE`

**实验**：建立不同类型的表，对比存储行为

---

# 第二阶段：分布式执行原理（核心）

> **目标**：理解 SQL 为什么这样执行。

## 第 4 章 Distribution Key

- Hash Distribution
- Random Distribution
- Distribution Policy
- 如何选择 Distribution Key

**实验**：

- 建立 `Student`、`Score`、`Course` 表
- 观察不同 Distribution Key 对执行计划的影响

---

## 第 5 章 Motion（★★★★★）

> [!warning] 重点
> Motion 是 Greenplum 最大的性能开销之一，必须掌握。

- Gather Motion
- Broadcast Motion
- Redistribute Motion

**必须掌握**：

- 什么时候出现 `Redistribute Motion`
- 什么时候出现 `Broadcast Motion`

**实验**：人为制造 Broadcast、Redistribute、Gather，观察执行计划

---

## 第 6 章 Slice

- 什么是 Slice
- Slice 如何划分
- Segment 如何执行 Slice
- Motion 与 Slice 的关系

**实验**：分析执行计划中的 `(slice1) (slice2) (slice3)` 含义

---

# 第三阶段：SQL 执行计划分析（★★★★★）

> **目标**：任何执行计划都能读懂。

## 第 7 章 EXPLAIN

- `cost`
- `rows`
- `width`
- `loops`
- `actual rows`
- `actual time`

**重点**：为什么 `rows != actual rows`

---

## 第 8 章 Scan

- Seq Scan
- Index Scan
- Bitmap Index Scan
- Bitmap Heap Scan

**重点**：什么时候索引反而不用

---

## 第 9 章 Join

- Nested Loop
- Hash Join
- Merge Join

**重点**：

- 为什么 ORCA 倾向选择 Hash Join
- 什么时候 Merge Join 更快

---

## 第 10 章 Aggregate

- HashAggregate
- GroupAggregate

**重点**：为什么 `GROUP BY` 可能导致 OOM

---

## 第 11 章 Sort

- Quicksort
- External Sort
- Disk Sort

**重点**：什么时候 Sort 开始写磁盘

---

# 第四阶段：GPORCA 优化器（★★★★★）

> **目标**：理解数据库为什么这样选择执行计划。

## 第 12 章 GPORCA

- ORCA 工作流程
- Cost Model
- Join Order
- Predicate Pushdown

---

## 第 13 章 Statistics

- `ANALYZE`
- Histogram
- MCV（Most Common Values）
- NDV（Number of Distinct Values）

**重点**：统计信息错误为什么会导致错误执行计划

---

## 第 14 章 SQL Rewrite

- Predicate Pushdown
- 子查询优化
- 等价 SQL 改写

---

# 第五阶段：资源管理（★★★★★）

> **目标**：理解 OOM 为什么发生。

## 第 15 章 Memory

- `work_mem`
- `statement_mem`
- `gp_vmem_protect_limit`

**重点**：

- 为什么 Sort 申请内存
- 为什么 Hash 申请内存

---

## 第 16 章 Resource Queue / Resource Group

- Resource Queue
- Resource Group
- CPU / Memory / Concurrency 限制

---

## 第 17 章 Executor Memory

- 如何看 `Executor Memory`
- `Memory Usage` 与 `Memory Wanted`

**重点**：

```text
Memory used: 128000kB
```

不一定表示 SQL 用了 128MB

---

# 第六阶段：性能分析（★★★★★）

> **目标**：知道 SQL 为什么慢。

## 第 18 章 Data Skew

- 数据倾斜
- Motion 倾斜
- Join 倾斜

**实验**：故意让 90% 数据落到 Segment0，观察影响

---

## 第 19 章 Motion Optimization

- 如何减少 Motion
- 通过 Distribution Key 优化
- 避免不必要的 Redistribute

---

## 第 20 章 SQL 优化

- 什么时候拆 SQL
- 什么时候用 JOIN
- 什么时候用 CTE
- 什么时候用物化视图（Materialized View）

---

# 第七阶段：线上故障分析（★★★★★）

> **目标**：形成标准排查流程。

## 第 21 章 OOM 排查

**案例**：`Vmem limit reached`

学习定位：

- SQL
- Segment
- Memory
- Resource Queue

**排查流程**：

```text
SQL
 ↓
执行计划
 ↓
Segment 数据分布
 ↓
数据量
 ↓
资源配置
```

---

## 第 22 章 慢查询分析

**案例**：SQL 执行 30 分钟

- 如何抓取慢 SQL
- 如何分析执行计划瓶颈
- 如何验证优化效果

---

## 第 23 章 锁与并发

- Lock
- Deadlock
- Wait Event

**常用视图**：

```sql
pg_locks
pg_stat_activity
```

---

## 第 24 章 Segment 故障

- Segment Down 的现象
- 如何恢复
- Mirror 切换机制

---

# 第八阶段：源码阅读（可选）

> **目标**：结合执行计划，理解底层实现。

推荐模块：

```text
optimizer/   —— 优化器
executor/    —— 执行器
motion/      —— Motion 实现
resource/    —— 资源管理
catalog/     —— 元数据
```

**学习方法**：

| 今天学什么 | 看哪里 |
| --------- | ------ |
| Hash Join | Executor 中的 Hash Join |
| Motion | Motion 节点 |
| Aggregate | Aggregate 执行节点 |
| Sort | Sort 执行节点 |

---

# 第九阶段：案例库建设（持续积累）

> **目标**：建立个人 [[Greenplum CaseBook]]。

## 案例统一格式

```text
案例编号：GP-001

问题：
Vmem limit reached

现象：
SQL 执行失败

日志：
......

执行计划：
......

原因分析：
......

最终原因：
......

解决方案：
......

涉及知识：
✔ Motion
✔ Hash Join
✔ Resource Queue
✔ Vmem
✔ Segment
```

## 建议积累的典型案例

| 编号 | 案例主题 | 核心知识点 |
| ---- | -------- | ---------- |
| GP-001 | Vmem limit reached | Vmem、Memory、Segment |
| GP-002 | Redistribute Motion 导致 SQL 变慢 | Motion、Distribution Key |
| GP-003 | Data Skew 导致 Segment 打满 | Skew、Segment 负载 |
| GP-004 | 统计信息失效导致 ORCA 误判 | Statistics、ANALYZE、ORCA |
| GP-005 | Hash Join 与 Nested Loop 切换 | Join、Statistics |
| GP-006 | Resource Group 导致查询被限流 | Resource Group、Concurrency |
| GP-007 | Segment 故障恢复 | Mirror、Segment、HA |
| GP-008 | 大事务导致 VACUUM 延迟 | VACUUM、Transaction、AO Table |

---

# 实验维度设计

每章都建议配一个实验，形成 **理论 + 实验 + 案例** 的闭环。

| 章节 | 理论 | 实验 |
| ---- | ---- | ---- |
| Distribution Key | 为什么选择分布键 | 创建不同分布键的表，对比执行计划 |
| Motion | 三种 Motion 的原理 | 人为制造 Gather、Broadcast、Redistribute |
| Hash Join | 工作机制 | 调整数据量观察 Hash Join 与 Nested Loop 切换 |
| Statistics | ANALYZE 的作用 | 删除统计信息再重新收集，对比执行计划 |
| Memory | work_mem、statement_mem | 调整参数观察 Sort、Hash 的变化 |
| Data Skew | 数据倾斜 | 构造倾斜数据，观察某个 Segment 的负载变化 |
| OOM | Vmem 原理 | 在受控环境下模拟内存压力，分析日志和执行计划 |

---

# 学习路径建议

```text
1. 先通读第一阶段 ~ 第三阶段，建立整体认知
2. 重点精读 Motion、Slice、EXPLAIN、Join、Aggregate、Sort
3. 配合实验反复观察执行计划变化
4. 遇到线上问题，按标准流程排查并写入 CaseBook
5. 定期回看案例库，总结共性问题
6. 有余力时，选择性阅读源码加深理解
```

---

# 相关笔记

- [[TBase Greenplum 分布式数据库核心架构与 OOM 排查笔记]]
- [[Greenplum CaseBook]]
- [[Greenplum 常用 SQL 与视图]]
- [[Greenplum 执行计划节点速查]]
