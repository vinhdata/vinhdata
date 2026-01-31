---
date: 2026-01-29
categories:
  - Databases
tags:
  - mysql
  - mysql-client
  - cli
  - cheatsheet
---

# MySQL CLI Cheat Sheet (`mysql`)

A practical cheat sheet for the `mysql` client: connect, inspect, troubleshoot, and export.

<!-- more -->

## Connect

Basic connection:

```bash
mysql -h <host> -P 3306 -u <user> -p
```

Connect to a specific database:

```bash
mysql -h <host> -P 3306 -u <user> -p <db>
```

From a defaults file (avoids putting passwords in shell history):

```ini
# ~/.my.cnf
[client]
user=myuser
password=mypassword
host=127.0.0.1
port=3306
```

Then:

```bash
mysql
```

## Session basics

```sql
SELECT VERSION();
SELECT DATABASE();
SHOW DATABASES;
USE <db>;
SHOW TABLES;
```

Helpful client commands:

```sql
\s         -- status
\u <db>    -- use database
\G         -- vertical output (append to a query)
```

## Inspect schema

Tables and columns:

```sql
SHOW TABLE STATUS;
SHOW COLUMNS FROM <table>;
DESCRIBE <table>;
```

Show create statement:

```sql
SHOW CREATE TABLE <table>\G
SHOW CREATE VIEW <view>\G
```

Indexes:

```sql
SHOW INDEX FROM <table>;
```

## Users & privileges

List users:

```sql
SELECT user, host FROM mysql.user;
```

Show grants:

```sql
SHOW GRANTS FOR '<user>'@'<host>';
```

## Performance / troubleshooting

Current running queries:

```sql
SHOW FULL PROCESSLIST;
```

Kill a query:

```sql
KILL <process_id>;
```

Check locks (InnoDB):

```sql
SHOW ENGINE INNODB STATUS\G
```

Explain a query:

```sql
EXPLAIN SELECT ...;
EXPLAIN ANALYZE SELECT ...;  -- MySQL 8+
```

## Common safe exports

Export a database with `mysqldump`:

```bash
mysqldump -h <host> -P 3306 -u <user> -p --databases <db> > dump.sql
```

Export a single table:

```bash
mysqldump -h <host> -P 3306 -u <user> -p <db> <table> > table.sql
```

Import:

```bash
mysql -h <host> -P 3306 -u <user> -p <db> < dump.sql
```

## Handy one-liners

Run a query non-interactively:

```bash
mysql -h <host> -P 3306 -u <user> -p -D <db> -e "SELECT NOW();"
```

Pretty vertical output:

```bash
mysql -h <host> -u <user> -p -D <db> -e "SHOW PROCESSLIST\\G"
```
