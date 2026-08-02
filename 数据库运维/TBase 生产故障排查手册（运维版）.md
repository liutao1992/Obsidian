
下面这份是我比较推荐的 **《TBase 生产故障排查手册（运维版）》**，按照真实生产事故的排查思路整理，而不是单纯堆 SQL。

---

# 故障1：应用无法获取数据库连接

典型报错：

```java
HikariPool-1 - Connection is not available
request timed out after 30000ms
```

---

## 排查步骤

### Step1 查看数据库连接数

```sql
SELECT COUNT(*)
FROM pg_stat_activity;
```

```sql
SHOW max_connections;
```

判断：

```text
当前连接数 < max_connections
    ↓
数据库连接未打满
    ↓
排查连接池
```

---

### Step2 查看连接池状态

查看 Micrometer：

```text
hikaricp.connections.active
hikaricp.connections.idle
hikaricp.connections.pending
```

判断：

```text
active=10
idle=0
pending持续增长
```

连接池耗尽。

---

### Step3 查看长事务

```sql
SELECT
    pid,
    now()-xact_start duration,
    query
FROM pg_stat_activity
WHERE xact_start IS NOT NULL
ORDER BY duration DESC;
```

---

### Step4 查看锁等待

```sql
SELECT
    pid,
    wait_event_type,
    wait_event,
    query
FROM pg_stat_activity
WHERE wait_event_type='Lock';
```

---

## 常见根因

|原因|概率|
|---|---|
|Connection未关闭|★★★★★|
|长事务|★★★★★|
|死锁|★★★|
|连接池太小|★★★|

---

# 故障2：SQL突然变慢

现象：

```text
原来100ms
变成30秒
```

---

## Step1 找出慢SQL

```sql
SELECT
    pid,
    now()-query_start duration,
    query
FROM pg_stat_activity
WHERE state='active'
ORDER BY duration DESC;
```

---

## Step2 查看执行计划

```sql
EXPLAIN ANALYZE
SELECT ...
```

---

## 判断

### 出现

```text
Seq Scan
```

说明：

```text
未走索引
```

---

### 出现

```text
Rows Removed by Filter
```

大量数据被过滤。

---

### 出现

```text
Hash Join
```

数据量太大。

---

# 故障3：锁等待

现象：

```text
SQL一直不返回
```

---

## 查看等待锁

```sql
SELECT
    pid,
    wait_event_type,
    wait_event,
    query
FROM pg_stat_activity
WHERE wait_event_type='Lock';
```

---

## 查看谁阻塞谁

```sql
SELECT
    blocked.pid blocked_pid,
    blocked.query blocked_sql,
    blocking.pid blocking_pid,
    blocking.query blocking_sql
FROM pg_stat_activity blocked
JOIN pg_stat_activity blocking
ON blocking.pid = ANY(pg_blocking_pids(blocked.pid));
```

---

## 处理

取消阻塞SQL：

```sql
SELECT pg_cancel_backend(pid);
```

或者：

```sql
SELECT pg_terminate_backend(pid);
```

---

# 故障4：死锁

典型日志：

```text
deadlock detected
```

---

## 排查

查看日志：

```text
Process 100 waits for ShareLock
Process 200 waits for ShareLock
```

例如：

事务A：

```sql
UPDATE device
SET ...
WHERE id=1;
```

事务B：

```sql
UPDATE device
SET ...
WHERE id=2;
```

随后：

```sql
A更新2
B更新1
```

产生死锁。

---

## 解决

统一加锁顺序：

```text
始终按照ID升序更新
```

---

# 故障5：数据库CPU 100%

---

## 查看最耗CPU SQL

```sql
SELECT
    pid,
    query,
    now()-query_start duration
FROM pg_stat_activity
WHERE state='active'
ORDER BY duration DESC;
```

---

Linux：

```bash
top
```

找到：

```text
postgres
```

---

## 查看执行计划

```sql
EXPLAIN ANALYZE
```

重点关注：

```text
Seq Scan
Nested Loop
```

---

# 故障6：磁盘空间暴涨

---

## 查看数据库大小

```sql
SELECT
    datname,
    pg_size_pretty(pg_database_size(datname))
FROM pg_database;
```

---

## 查看最大表

```sql
SELECT
    relname,
    pg_size_pretty(pg_total_relation_size(oid))
FROM pg_class
WHERE relkind='r'
ORDER BY pg_total_relation_size(oid) DESC;
```

---

## 查看死元组

```sql
SELECT
    relname,
    n_live_tup,
    n_dead_tup
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;
```

---

## 处理

```sql
VACUUM ANALYZE 表名;
```

---

# 故障7：TBase节点异常

---

## 查看节点

```sql
SELECT
    node_name,
    node_type,
    node_host
FROM pgxc_node;
```

---

## 检查Coordinator

```sql
SELECT 1;
```

无法执行：

```text
Coordinator异常
```

---

## 检查DataNode

```sql
EXPLAIN VERBOSE
SELECT *
FROM sync_task;
```

查看是否能访问所有节点。

---

# 故障8：数据倾斜

TBase最常见问题之一。

---

例如：

```sql
DISTRIBUTE BY HASH(vendor_code)
```

但：

```text
vendor_code
TDWY
```

只有一个值。

---

结果：

```text
dn001 5000万
dn002 0
dn003 0
```

---

## 查看分布

```sql
SELECT
    pgxc_node_str(),
    COUNT(*)
FROM sync_task
GROUP BY 1;
```

---

## 判断

差异超过：

```text
20%
```

就要关注。

---

# 故障9：同步任务堆积

你们项目非常容易出现。

---

## 查看任务状态

```sql
SELECT
    status,
    COUNT(*)
FROM sync_task
GROUP BY status;
```

---

## 查看运行超时任务

```sql
SELECT *
FROM sync_task
WHERE status='RUNNING'
AND update_time <
    now()-interval '30 minute';
```

---

## 查看失败任务

```sql
SELECT *
FROM sync_task
WHERE status='FAILED';
```

---

# 故障10：生产巡检（每天执行）

## 连接数

```sql
SELECT COUNT(*)
FROM pg_stat_activity;
```

---

## 长事务

```sql
SELECT
    pid,
    now()-xact_start
FROM pg_stat_activity
WHERE xact_start IS NOT NULL;
```

---

## 锁等待

```sql
SELECT *
FROM pg_locks
WHERE NOT granted;
```

---

## 当前慢SQL

```sql
SELECT
    pid,
    now()-query_start duration,
    query
FROM pg_stat_activity
WHERE state='active'
ORDER BY duration DESC;
```

---

## 最大表

```sql
SELECT
    relname,
    pg_size_pretty(pg_total_relation_size(oid))
FROM pg_class
WHERE relkind='r'
ORDER BY pg_total_relation_size(oid) DESC
LIMIT 20;
```

---

# DBA故障处理口诀

```text
连接问题
    ↓
pg_stat_activity

SQL慢
    ↓
EXPLAIN ANALYZE

锁问题
    ↓
pg_locks

容量问题
    ↓
pg_total_relation_size

连接池问题
    ↓
Hikari Metrics

TBase问题
    ↓
pgxc_node

同步平台问题
    ↓
sync_task状态表
```

对于你目前的数据同步平台（任务调度、分页同步、对账补账、TBase），下一步最值得学习的是：

1. PostgreSQL/TBase 执行计划（EXPLAIN）
    
2. 锁与事务（FOR UPDATE SKIP LOCKED）
    
3. HikariCP 连接池排障
    
4. TBase 分布键与数据倾斜
    
5. 慢 SQL 调优
    

这五块能解决你们线上 80% 以上的数据库故障。