
下面这份是我按照 **PostgreSQL/TBase 生产运维场景** 整理的《TBase 运维 SQL 手册》。重点针对你目前的数据同步平台场景（Spring Boot + Hikari + TBase + XXL-JOB），覆盖：

- 连接池故障
    
- 慢SQL
    
- 锁等待
    
- 死锁
    
- 长事务
    
- 索引分析
    
- 表空间
    
- 存储容量
    
- TBase集群节点
    
- 数据倾斜
    

---

# 1. 连接数排查

## 查看最大连接数

```sql
SHOW max_connections;
```

---

## 查看当前连接数

```sql
SELECT COUNT(*)
FROM pg_stat_activity;
```

---

## 查看连接使用率

```sql
SELECT
    COUNT(*) current_connections,
    setting::int max_connections,
    ROUND(
        COUNT(*) * 100.0 / setting::int,
        2
    ) usage_percent
FROM pg_stat_activity,
     pg_settings
WHERE name='max_connections'
GROUP BY setting;
```

---

## 按应用统计连接数

```sql
SELECT
    application_name,
    COUNT(*) cnt
FROM pg_stat_activity
GROUP BY application_name
ORDER BY cnt DESC;
```

结果：

```text
sync-engine      50
xxl-job          20
DBeaver           3
```

---

## 按用户统计连接

```sql
SELECT
    usename,
    COUNT(*)
FROM pg_stat_activity
GROUP BY usename
ORDER BY COUNT(*) DESC;
```

---

# 2. 长事务排查

生产事故最高频原因之一。

---

## 查看长事务

```sql
SELECT
    pid,
    usename,
    application_name,
    xact_start,
    now() - xact_start duration,
    query
FROM pg_stat_activity
WHERE xact_start IS NOT NULL
ORDER BY duration DESC;
```

重点关注：

```text
duration > 10min
```

---

## 查看 idle in transaction

```sql
SELECT
    pid,
    usename,
    application_name,
    state,
    now() - state_change idle_time,
    query
FROM pg_stat_activity
WHERE state='idle in transaction';
```

这种连接最危险。

---

# 3. 当前执行SQL

## 查看活跃SQL

```sql
SELECT
    pid,
    usename,
    application_name,
    state,
    query_start,
    now()-query_start duration,
    query
FROM pg_stat_activity
WHERE state='active'
ORDER BY duration DESC;
```

---

## 查看执行超过30秒SQL

```sql
SELECT
    pid,
    usename,
    application_name,
    now()-query_start duration,
    query
FROM pg_stat_activity
WHERE now()-query_start > interval '30 seconds';
```

---

# 4. 锁等待排查

## 查看等待锁

```sql
SELECT
    pid,
    usename,
    wait_event_type,
    wait_event,
    query
FROM pg_stat_activity
WHERE wait_event_type='Lock';
```

---

## 查看未获得锁

```sql
SELECT *
FROM pg_locks
WHERE NOT granted;
```

---

## 谁阻塞了谁

生产最常用SQL：

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

# 5. 强制终止会话

## 查看PID

```sql
SELECT pid, usename, query
FROM pg_stat_activity;
```

---

## 终止SQL

```sql
SELECT pg_cancel_backend(pid);
```

只取消SQL。

---

## 杀掉连接

```sql
SELECT pg_terminate_backend(pid);
```

直接断开会话。

---

# 6. 数据库容量

## 查看数据库大小

```sql
SELECT
    datname,
    pg_size_pretty(pg_database_size(datname))
FROM pg_database
ORDER BY pg_database_size(datname) DESC;
```

---

## 查看最大表

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

## 查看索引大小

```sql
SELECT
    indexrelname,
    pg_size_pretty(pg_relation_size(indexrelid))
FROM pg_stat_user_indexes
ORDER BY pg_relation_size(indexrelid) DESC
LIMIT 20;
```

---

# 7. 索引运维

## 查看表索引

```sql
SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename='sync_task';
```

---

## 查看索引使用率

```sql
SELECT
    schemaname,
    relname,
    seq_scan,
    idx_scan,
    ROUND(
        idx_scan * 100.0 /
        NULLIF(seq_scan+idx_scan,0),
        2
    ) idx_percent
FROM pg_stat_user_tables;
```

---

## 查未使用索引

```sql
SELECT
    relname table_name,
    indexrelname index_name,
    idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan=0;
```

---

# 8. EXPLAIN分析

## 查看执行计划

```sql
EXPLAIN
SELECT *
FROM sync_task
WHERE status='PENDING';
```

---

## 查看真实执行

```sql
EXPLAIN ANALYZE
SELECT *
FROM sync_task
WHERE status='PENDING';
```

重点关注：

```text
Seq Scan
Index Scan
Bitmap Scan
```

---

# 9. VACUUM运维

## 查看膨胀表

```sql
SELECT
    relname,
    n_live_tup,
    n_dead_tup
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;
```

---

## 手工回收

```sql
VACUUM ANALYZE sync_task;
```

---

## 重建表

```sql
VACUUM FULL sync_task;
```

慎用，会锁表。

---

# 10. Hikari连接池故障排查

你的项目最常用。

---

## 数据库侧查看连接

```sql
SELECT
    pid,
    usename,
    application_name,
    client_addr,
    state
FROM pg_stat_activity;
```

---

## 查看应用连接

```sql
SELECT
    application_name,
    COUNT(*)
FROM pg_stat_activity
GROUP BY application_name;
```

建议配置：

```yaml
spring.datasource.hikari.pool-name=SyncPool
spring.datasource.hikari.register-mbeans=true
```

---

# 11. TBase集群运维

## 查看节点

```sql
SELECT *
FROM pgxc_node;
```

---

## 查看Coordinator

```sql
SELECT
    node_name,
    node_type,
    node_host
FROM pgxc_node;
```

---

结果类似：

```text
coord1    C
coord2    C
dn001     D
dn002     D
```

---

# 12. 数据倾斜排查

TBase特有。

---

查看各节点数据量：

```sql
SELECT
    pgxc_node_str(),
    COUNT(*)
FROM sync_task
GROUP BY 1;
```

理想：

```text
dn001 1000w
dn002 980w
dn003 1020w
```

异常：

```text
dn001 5000w
dn002 100w
dn003 200w
```

说明分布键设计失败。

---

# 13. 日常巡检SQL（建议收藏）

每天上线前执行：

```sql
-- 连接数
SELECT COUNT(*) FROM pg_stat_activity;

-- 长事务
SELECT pid, now()-xact_start
FROM pg_stat_activity
WHERE xact_start IS NOT NULL;

-- 锁等待
SELECT *
FROM pg_locks
WHERE NOT granted;

-- 最大表
SELECT
    relname,
    pg_size_pretty(pg_total_relation_size(oid))
FROM pg_class
WHERE relkind='r'
ORDER BY pg_total_relation_size(oid) DESC
LIMIT 10;

-- 死元组
SELECT
    relname,
    n_dead_tup
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC
LIMIT 10;

-- 当前活跃SQL
SELECT
    pid,
    now()-query_start,
    query
FROM pg_stat_activity
WHERE state='active';
```

对于你当前的工作，我建议再整理一份 **《TBase生产故障排查手册》**，按照“连接池耗尽、锁等待、死锁、慢SQL、数据倾斜、Coordinator故障、DataNode故障”等场景给出完整排查流程图，这会比单纯记SQL更接近实际运维工作。