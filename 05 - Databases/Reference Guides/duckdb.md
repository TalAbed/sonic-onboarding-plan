# DuckDB Reference Guide

## 📖 Complete DuckDB Quick Reference

A comprehensive guide for DuckDB SQL queries, Python integration, and analytics patterns.

---

## 🗄️ Table of Contents
1. [Getting Started](#getting-started)
2. [SQL Fundamentals](#sql-fundamentals)
3. [Loading Data](#loading-data)
4. [Query Operations](#query-operations)
5. [Window Functions](#window-functions)
6. [Aggregations](#aggregations)
7. [Pandas Integration](#pandas-integration)
8. [Python API](#python-api)
9. [ETL Patterns](#etl-patterns)
10. [Performance Tips](#performance-tips)

---

## Getting Started

### Installation

```bash
# Install via pip
pip install duckdb

# Check version
duckdb --version

# Interactive shell
duckdb

# Create/connect to database
duckdb my_database.duckdb
```

### Basic Operations

```python
import duckdb

# Connect to in-memory database
con = duckdb.connect(':memory:')

# Connect to file-based database
con = duckdb.connect('my_database.duckdb')

# Execute simple query
result = con.execute("SELECT 1 as number").fetchall()

# Execute and get DataFrame
df = con.execute("SELECT * FROM some_table").df()

# Close connection
con.close()
```

---

## SQL Fundamentals

### Basic SELECT

```sql
-- Select all columns
SELECT * FROM table_name;

-- Select specific columns
SELECT column1, column2 FROM table_name;

-- Select with aliases
SELECT column1 AS col1, column2 AS col2 FROM table_name;

-- Select with WHERE clause
SELECT * FROM users WHERE age > 25;

-- Select with LIMIT
SELECT * FROM users LIMIT 10;

-- Select DISTINCT
SELECT DISTINCT city FROM users;

-- Select with ORDER BY
SELECT * FROM users ORDER BY age DESC;

-- Select with multiple ORDER BY
SELECT * FROM users ORDER BY city, age DESC;
```

### CRUD Operations

```sql
-- CREATE TABLE
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    age INTEGER,
    email VARCHAR,
    created_at TIMESTAMP
);

-- INSERT
INSERT INTO users (id, name, age, email) 
VALUES (1, 'John', 30, 'john@example.com');

-- INSERT multiple rows
INSERT INTO users VALUES
(2, 'Jane', 28, 'jane@example.com', NOW()),
(3, 'Bob', 35, 'bob@example.com', NOW());

-- UPDATE
UPDATE users SET age = 31 WHERE id = 1;

-- DELETE
DELETE FROM users WHERE id = 1;

-- DROP TABLE
DROP TABLE users;
```

### Data Types

| Type | Description | Example |
|------|-------------|---------|
| `INTEGER` | Whole numbers | `123` |
| `BIGINT` | Large integers | `9223372036854775807` |
| `DECIMAL(p,s)` | Fixed-point | `123.45` |
| `FLOAT` | Floating-point | `3.14` |
| `VARCHAR` | Text | `'hello'` |
| `TEXT` | Large text | Long articles |
| `BOOLEAN` | True/False | `true` |
| `DATE` | Date only | `'2024-01-22'` |
| `TIMESTAMP` | DateTime | `'2024-01-22 14:30:00'` |
| `INTERVAL` | Time span | `'1 year'` |
| `ARRAY` | Array | `[1, 2, 3]` |
| `STRUCT` | Named fields | `{'x': 1, 'y': 2}` |

---

## Loading Data

### From CSV Files

```sql
-- Read CSV directly
SELECT * FROM read_csv_auto('data.csv');

-- Read with specific options
SELECT * FROM read_csv('data.csv', 
    delimiter=',',
    header=true,
    skip=1
);

-- Read from URL
SELECT * FROM read_csv('https://example.com/data.csv');

-- Create table from CSV
CREATE TABLE users AS 
SELECT * FROM read_csv_auto('users.csv');
```

### From Parquet Files

```sql
-- Read Parquet file
SELECT * FROM read_parquet('data.parquet');

-- Create table from Parquet
CREATE TABLE sales AS
SELECT * FROM read_parquet('sales.parquet');

-- Read from S3 (with HTTPFs extension)
SELECT * FROM read_parquet('s3://bucket/data.parquet');
```

### From JSON Files

```sql
-- Read JSON file
SELECT * FROM read_json_auto('data.json');

-- Read newline-delimited JSON
SELECT * FROM read_ndjson('data.ndjson');

-- With options
SELECT * FROM read_json('data.json', 
    format='array',
    ignore_errors=true
);
```

### From URLs and APIs

```sql
-- Read from URL
SELECT * FROM read_csv('https://example.com/data.csv');

-- With HTTPFs extension
SELECT * FROM read_parquet('https://example.com/data.parquet');
```

---

## Query Operations

### WHERE Clauses

```sql
-- Comparison
SELECT * FROM users WHERE age > 25;
SELECT * FROM users WHERE age >= 25;
SELECT * FROM users WHERE age = 25;
SELECT * FROM users WHERE age <> 25;

-- String matching
SELECT * FROM users WHERE name LIKE 'J%';
SELECT * FROM users WHERE name LIKE '%son';
SELECT * FROM users WHERE name ILIKE 'john%';  -- Case-insensitive

-- IN operator
SELECT * FROM users WHERE id IN (1, 2, 3);

-- BETWEEN
SELECT * FROM users WHERE age BETWEEN 25 AND 35;

-- IS NULL
SELECT * FROM users WHERE phone IS NULL;

-- Logical operators
SELECT * FROM users WHERE age > 25 AND city = 'New York';
SELECT * FROM users WHERE age < 20 OR age > 65;
SELECT * FROM users WHERE NOT (age < 18);
```

### Joins

```sql
-- INNER JOIN
SELECT u.name, o.total 
FROM users u
JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN
SELECT u.name, o.total 
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- FULL OUTER JOIN
SELECT u.name, o.total 
FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;

-- CROSS JOIN
SELECT u.name, p.name 
FROM users u
CROSS JOIN products p;

-- Multiple joins
SELECT u.name, o.total, p.name
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;
```

### Subqueries

```sql
-- Subquery in WHERE
SELECT * FROM users
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- Subquery in FROM
SELECT * FROM (
    SELECT user_id, COUNT(*) as order_count 
    FROM orders 
    GROUP BY user_id
) user_stats
WHERE order_count > 5;

-- Correlated subquery
SELECT u.name,
    (SELECT COUNT(*) FROM orders WHERE user_id = u.id) as order_count
FROM users u;
```

### Common Table Expressions (CTE)

```sql
-- Basic CTE
WITH user_stats AS (
    SELECT user_id, COUNT(*) as order_count
    FROM orders
    GROUP BY user_id
)
SELECT u.name, us.order_count
FROM users u
JOIN user_stats us ON u.id = us.user_id;

-- Multiple CTEs
WITH monthly_sales AS (
    SELECT DATE_TRUNC('month', order_date) as month, SUM(total) as sales
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
),
yearly_sales AS (
    SELECT DATE_TRUNC('year', order_date) as year, SUM(total) as sales
    FROM orders
    GROUP BY DATE_TRUNC('year', order_date)
)
SELECT * FROM monthly_sales
UNION ALL
SELECT * FROM yearly_sales;

-- Recursive CTE
WITH RECURSIVE numbers AS (
    SELECT 1 as n
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 100
)
SELECT * FROM numbers;
```

---

## Window Functions

### Ranking Functions

```sql
-- ROW_NUMBER: Sequential numbering
SELECT name, salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as rank
FROM employees;

-- RANK: Rank with gaps for ties
SELECT name, salary,
    RANK() OVER (ORDER BY salary DESC) as rank
FROM employees;

-- DENSE_RANK: Rank without gaps
SELECT name, salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) as rank
FROM employees;

-- NTILE: Divide into groups
SELECT name, salary,
    NTILE(4) OVER (ORDER BY salary) as quartile
FROM employees;

-- Partition by department
SELECT department, name, salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM employees;
```

### Aggregate Window Functions

```sql
-- Running total
SELECT date, amount,
    SUM(amount) OVER (ORDER BY date) as running_total
FROM transactions;

-- Moving average
SELECT date, price,
    AVG(price) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as moving_avg_7day
FROM stock_prices;

-- Average by partition
SELECT employee, salary,
    AVG(salary) OVER (PARTITION BY department) as dept_avg_salary
FROM employees;

-- Min/Max in window
SELECT date, price,
    MIN(price) OVER (ORDER BY date) as min_price_so_far,
    MAX(price) OVER (ORDER BY date) as max_price_so_far
FROM stock_prices;
```

### Offset Functions

```sql
-- LAG: Previous row value
SELECT date, price,
    LAG(price) OVER (ORDER BY date) as prev_price,
    price - LAG(price) OVER (ORDER BY date) as price_change
FROM stock_prices;

-- LEAD: Next row value
SELECT date, price,
    LEAD(price) OVER (ORDER BY date) as next_price
FROM stock_prices;

-- FIRST_VALUE/LAST_VALUE
SELECT date, price,
    FIRST_VALUE(price) OVER (ORDER BY date) as first_price,
    LAST_VALUE(price) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as last_price
FROM stock_prices;
```

---

## Aggregations

### Basic Aggregates

```sql
-- COUNT
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT city) FROM users;

-- SUM
SELECT SUM(amount) FROM orders;

-- AVG
SELECT AVG(price) FROM products;

-- MIN/MAX
SELECT MIN(age), MAX(age) FROM users;

-- STRING_AGG (concatenate strings)
SELECT STRING_AGG(name, ', ') FROM users;

-- ARRAY_AGG (collect into array)
SELECT ARRAY_AGG(id) FROM users;
```

### GROUP BY

```sql
-- Basic grouping
SELECT city, COUNT(*) as user_count 
FROM users 
GROUP BY city;

-- Multiple columns
SELECT city, age, COUNT(*) as count
FROM users
GROUP BY city, age;

-- With HAVING
SELECT city, COUNT(*) as user_count
FROM users
GROUP BY city
HAVING COUNT(*) > 10;

-- Complex aggregation
SELECT 
    city,
    COUNT(*) as user_count,
    AVG(age) as avg_age,
    MIN(age) as min_age,
    MAX(age) as max_age
FROM users
GROUP BY city
ORDER BY user_count DESC;
```

### Time-Based Aggregation

```sql
-- Daily totals
SELECT DATE(order_date) as day, SUM(total) as daily_sales
FROM orders
GROUP BY DATE(order_date);

-- Monthly totals
SELECT DATE_TRUNC('month', order_date) as month, SUM(total) as monthly_sales
FROM orders
GROUP BY DATE_TRUNC('month', order_date);

-- Yearly totals
SELECT YEAR(order_date) as year, SUM(total) as yearly_sales
FROM orders
GROUP BY YEAR(order_date);
```

---

## Pandas Integration

### Reading from Pandas

```python
import pandas as pd
import duckdb

# Create DataFrame
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Bob'],
    'age': [30, 28, 35],
    'city': ['New York', 'London', 'Paris']
})

# Query DataFrame directly
result = duckdb.query("SELECT * FROM df WHERE age > 25").df()

# Filter using DuckDB
result = duckdb.query("SELECT name, age FROM df WHERE city = 'London'").df()

# Aggregation
stats = duckdb.query("""
    SELECT city, COUNT(*) as count, AVG(age) as avg_age
    FROM df
    GROUP BY city
""").df()
```

### Writing to Pandas

```python
import duckdb
import pandas as pd

# Read from database to DataFrame
con = duckdb.connect('data.duckdb')
df = con.execute("SELECT * FROM users WHERE age > 25").df()

# Work with DataFrame
df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 50, 100])

# Write back to DuckDB
con.execute("CREATE TABLE age_groups AS SELECT * FROM df")
```

### Data Type Mapping

```
Pandas Type → DuckDB Type
numpy.int64 → BIGINT
numpy.float64 → DOUBLE
object (string) → VARCHAR
datetime64 → TIMESTAMP
bool → BOOLEAN
category → VARCHAR
```

---

## Python API

### Connection and Execution

```python
import duckdb

# In-memory database
con = duckdb.connect(':memory:')

# File-based database
con = duckdb.connect('data.duckdb')

# Execute query
result = con.execute("SELECT * FROM users").fetchall()

# Fetch as DataFrame
df = con.execute("SELECT * FROM users").df()

# Fetch as dictionary
records = con.execute("SELECT * FROM users").fetchall()
dict_list = [dict(row) for row in records]

# Execute with parameters
con.execute("SELECT * FROM users WHERE age > ?", [25])

# Close connection
con.close()
```

### Creating Tables

```python
import duckdb
import pandas as pd

con = duckdb.connect(':memory:')

# Create from SQL
con.execute("""
    CREATE TABLE users (
        id INTEGER,
        name VARCHAR,
        age INTEGER
    )
""")

# Create from DataFrame
df = pd.DataFrame({'id': [1, 2, 3], 'name': ['a', 'b', 'c']})
con.execute("CREATE TABLE from_df AS SELECT * FROM df")

# Create view
con.execute("""
    CREATE VIEW adult_users AS
    SELECT * FROM users WHERE age >= 18
""")
```

### Inserting Data

```python
import duckdb

con = duckdb.connect(':memory:')

# Single insert
con.execute("INSERT INTO users VALUES (1, 'John', 30)")

# Multiple inserts
con.execute("""
    INSERT INTO users VALUES
    (2, 'Jane', 28),
    (3, 'Bob', 35)
""")

# Insert from DataFrame
df = pd.DataFrame({'id': [4, 5], 'name': ['Alice', 'Charlie'], 'age': [26, 40]})
con.execute("INSERT INTO users SELECT * FROM df")
```

### Reading Files

```python
import duckdb

con = duckdb.connect(':memory:')

# CSV
df = con.execute("SELECT * FROM read_csv('data.csv')").df()

# Parquet
df = con.execute("SELECT * FROM read_parquet('data.parquet')").df()

# JSON
df = con.execute("SELECT * FROM read_json('data.json')").df()

# Multiple files (glob pattern)
df = con.execute("SELECT * FROM read_csv('data/*.csv')").df()
```

### Writing Files

```python
import duckdb

con = duckdb.connect(':memory:')

# Write to CSV
con.execute("COPY (SELECT * FROM users) TO 'output.csv' (FORMAT CSV)")

# Write to Parquet
con.execute("COPY (SELECT * FROM users) TO 'output.parquet' (FORMAT PARQUET)")

# Write to JSON
con.execute("COPY (SELECT * FROM users) TO 'output.json' (FORMAT JSON)")
```

---

## ETL Patterns

### Extract, Transform, Load

```python
import duckdb
import pandas as pd

def etl_pipeline():
    con = duckdb.connect('data.duckdb')
    
    # EXTRACT: Load data
    df_raw = con.execute("SELECT * FROM read_csv('raw_data.csv')").df()
    
    # TRANSFORM: Process data
    df_clean = df_raw.copy()
    df_clean['age'] = df_clean['age'].astype(int)
    df_clean['created_at'] = pd.to_datetime(df_clean['created_at'])
    df_clean = df_clean.dropna()
    
    # Validate data
    con.execute("CREATE TABLE raw_data AS SELECT * FROM df_raw")
    con.execute("CREATE TABLE clean_data AS SELECT * FROM df_clean")
    
    # LOAD: Write results
    con.execute("COPY (SELECT * FROM clean_data) TO 'clean_data.parquet' (FORMAT PARQUET)")
    
    return con

# Run ETL
con = etl_pipeline()
```

### Data Validation

```python
import duckdb

def validate_data(df):
    con = duckdb.connect(':memory:')
    con.execute("CREATE TABLE data AS SELECT * FROM df")
    
    # Check for nulls
    nulls = con.execute("""
        SELECT column_name, COUNT(*) as null_count
        FROM (SELECT * FROM data WHERE column_name IS NULL)
        GROUP BY column_name
    """).df()
    
    # Check for duplicates
    duplicates = con.execute("""
        SELECT COUNT(*) - COUNT(DISTINCT id) as duplicate_count
        FROM data
    """).df()
    
    # Check value ranges
    ranges = con.execute("""
        SELECT 
            MIN(age) as min_age,
            MAX(age) as max_age,
            AVG(age) as avg_age
        FROM data
    """).df()
    
    return {'nulls': nulls, 'duplicates': duplicates, 'ranges': ranges}
```

### Data Integration from Multiple Sources

```python
import duckdb

def integrate_data():
    con = duckdb.connect('data.duckdb')
    
    # Load from different sources
    users = con.execute("SELECT * FROM read_csv('users.csv')").df()
    orders = con.execute("SELECT * FROM read_parquet('orders.parquet')").df()
    products = con.execute("SELECT * FROM read_json('products.json')").df()
    
    # Create tables
    con.execute("CREATE TABLE users_data AS SELECT * FROM users")
    con.execute("CREATE TABLE orders_data AS SELECT * FROM orders")
    con.execute("CREATE TABLE products_data AS SELECT * FROM products")
    
    # Join and aggregate
    result = con.execute("""
        SELECT 
            u.id,
            u.name,
            COUNT(o.id) as order_count,
            SUM(o.total) as total_spent
        FROM users_data u
        LEFT JOIN orders_data o ON u.id = o.user_id
        GROUP BY u.id, u.name
        ORDER BY total_spent DESC
    """).df()
    
    return result

data = integrate_data()
```

---

## Performance Tips

### Best Practices

```
1. Use Parquet format (columnar, compressed)
2. Use EXPLAIN to analyze queries
3. Create indexes for frequently filtered columns
4. Use window functions for analytics
5. Use CTEs for readable, reusable queries
6. Partition large datasets
7. Use compression
8. Materialize intermediate results
```

### Query Optimization

```sql
-- EXPLAIN query plan
EXPLAIN SELECT * FROM large_table WHERE age > 25;

-- Create index
CREATE INDEX idx_age ON users(age);

-- Analyze statistics
ANALYZE users;

-- Use appropriate data types
-- Bad: CREATE TABLE users (age VARCHAR)
-- Good: CREATE TABLE users (age INTEGER)
```

### Memory Management

```python
import duckdb

con = duckdb.connect(':memory:')

# For large datasets, use file-based database
con_file = duckdb.connect('large_data.duckdb')

# Stream results instead of loading all
for batch in con.execute("SELECT * FROM huge_table").batches():
    process_batch(batch)

# Use LIMIT during development
con.execute("SELECT * FROM large_table LIMIT 1000")
```

### Extension Management

```python
import duckdb

con = duckdb.connect(':memory:')

# Load extensions
con.execute("INSTALL httpfs")
con.execute("LOAD httpfs")

# List loaded extensions
extensions = con.execute("SELECT * FROM duckdb_extensions()").df()

# Use extension features
con.execute("SELECT * FROM read_parquet('s3://bucket/file.parquet')")
```

---

## Common Queries

### Data Exploration

```sql
-- Table structure
SELECT * FROM information_schema.tables;

-- Column info
SELECT column_name, data_type 
FROM information_schema.columns
WHERE table_name = 'users';

-- Data preview
SELECT * FROM table_name LIMIT 100;

-- Data summary
SELECT 
    COUNT(*) as row_count,
    COUNT(DISTINCT id) as unique_ids
FROM table_name;
```

### Time Series Analysis

```sql
-- Daily aggregation
SELECT DATE(date_column) as day, SUM(amount) as daily_total
FROM transactions
GROUP BY DATE(date_column)
ORDER BY day;

-- Year-over-year comparison
SELECT 
    YEAR(date_column) as year,
    MONTH(date_column) as month,
    SUM(amount) as total
FROM transactions
GROUP BY YEAR(date_column), MONTH(date_column)
ORDER BY year, month;

-- Rolling average
SELECT 
    date_column,
    amount,
    AVG(amount) OVER (ORDER BY date_column ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as rolling_avg_7day
FROM transactions
ORDER BY date_column;
```

---

## Summary

This reference guide covers:
- ✅ SQL fundamentals in DuckDB
- ✅ Loading data from multiple formats
- ✅ Query operations and joins
- ✅ Window functions and aggregations
- ✅ Pandas integration
- ✅ Python API usage
- ✅ ETL patterns
- ✅ Performance optimization

For more: https://duckdb.org/docs/

