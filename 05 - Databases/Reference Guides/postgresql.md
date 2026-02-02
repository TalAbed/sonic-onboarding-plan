# PostgreSQL Reference Guide

## 📖 Complete PostgreSQL Quick Reference

A comprehensive guide for SQL queries, database design, and Python integration.

---

## 🗄️ Table of Contents
1. [Basic SQL Syntax](#basic-sql-syntax)
2. [Data Types](#data-types)
3. [Schema Design](#schema-design)
4. [Queries](#queries)
5. [Joins](#joins)
6. [Aggregation](#aggregation)
7. [Transactions](#transactions)
8. [Indexes](#indexes)
9. [Python Integration](#python-integration)
10. [Performance Tips](#performance-tips)

---

## Basic SQL Syntax

### Connection
```sql
-- Connect from command line
psql -U username -d database_name -h localhost

-- Create database
CREATE DATABASE my_app;

-- Drop database
DROP DATABASE my_app;

-- Connect to database
\c my_app
```

### Basic CRUD Operations

**CREATE (INSERT)**
```sql
-- Insert single row
INSERT INTO users (name, email, age) 
VALUES ('John Doe', 'john@example.com', 30);

-- Insert multiple rows
INSERT INTO users (name, email, age) VALUES
('Jane Doe', 'jane@example.com', 28),
('Bob Smith', 'bob@example.com', 35);

-- Insert with RETURNING (get inserted values)
INSERT INTO users (name, email) 
VALUES ('Alice', 'alice@example.com')
RETURNING id, name;
```

**READ (SELECT)**
```sql
-- Select all columns
SELECT * FROM users;

-- Select specific columns
SELECT id, name, email FROM users;

-- Select with WHERE clause
SELECT * FROM users WHERE age > 25;

-- Select with aliases
SELECT id AS user_id, name AS full_name FROM users;

-- Select DISTINCT values
SELECT DISTINCT city FROM users;

-- LIMIT and OFFSET
SELECT * FROM users LIMIT 10;
SELECT * FROM users LIMIT 10 OFFSET 5;
```

**UPDATE**
```sql
-- Update single row
UPDATE users SET age = 31 WHERE id = 1;

-- Update multiple columns
UPDATE users SET age = 31, city = 'New York' WHERE id = 1;

-- Update with RETURNING
UPDATE users SET age = age + 1 WHERE age < 30 RETURNING *;
```

**DELETE**
```sql
-- Delete specific row
DELETE FROM users WHERE id = 1;

-- Delete with RETURNING
DELETE FROM users WHERE age < 18 RETURNING *;

-- Delete all rows (use with caution!)
DELETE FROM users;
```

---

## Data Types

### Common Data Types

| Type | Description | Example |
|------|-------------|---------|
| `INTEGER` | Whole numbers | `123`, `-45` |
| `BIGINT` | Large integers | `9223372036854775807` |
| `DECIMAL(p,s)` | Fixed-point numbers | `123.45` (p=5, s=2) |
| `FLOAT` | Floating-point numbers | `3.14159` |
| `VARCHAR(n)` | Variable-length text | `'Hello'` |
| `TEXT` | Unlimited text | Long articles |
| `BOOLEAN` | True/False | `true`, `false` |
| `DATE` | Date only | `'2024-01-22'` |
| `TIME` | Time only | `'14:30:00'` |
| `TIMESTAMP` | Date and time | `'2024-01-22 14:30:00'` |
| `UUID` | Unique identifier | `'550e8400-e29b-41d4-a716-446655440000'` |
| `JSON` | JSON data | `'{"key": "value"}'` |
| `ARRAY` | Array of values | `ARRAY[1,2,3]` |

### Type Casting
```sql
-- Cast to different type
SELECT CAST('123' AS INTEGER);
SELECT '123'::INTEGER;

-- Convert timestamp to date
SELECT CAST(NOW() AS DATE);
```

---

## Schema Design

### Creating Tables

**Basic Table**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Table with Constraints**
```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    stock INTEGER DEFAULT 0,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Table with Foreign Key**
```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    total DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Constraints

```sql
-- PRIMARY KEY: Unique identifier for each row
CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100));

-- UNIQUE: Ensure column values are unique
CREATE TABLE users (email VARCHAR(100) UNIQUE);

-- NOT NULL: Column cannot be empty
CREATE TABLE users (name VARCHAR(100) NOT NULL);

-- CHECK: Ensure values meet condition
CREATE TABLE products (price DECIMAL(10,2) CHECK (price > 0));

-- DEFAULT: Set default value
CREATE TABLE users (created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

-- FOREIGN KEY: Reference another table
CREATE TABLE orders (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);
```

### Relationships

**One-to-Many** (1:N)
```sql
CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100));
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    amount DECIMAL(10, 2)
);
-- One user can have many orders
```

**Many-to-Many** (N:M)
```sql
CREATE TABLE students (id SERIAL PRIMARY KEY, name VARCHAR(100));
CREATE TABLE courses (id SERIAL PRIMARY KEY, title VARCHAR(100));
CREATE TABLE enrollments (
    student_id INTEGER REFERENCES students(id),
    course_id INTEGER REFERENCES courses(id),
    PRIMARY KEY (student_id, course_id)
);
-- Many students can take many courses
```

### Altering Tables

```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Drop column
ALTER TABLE users DROP COLUMN phone;

-- Rename column
ALTER TABLE users RENAME COLUMN email TO email_address;

-- Add constraint
ALTER TABLE users ADD CONSTRAINT unique_email UNIQUE (email);

-- Drop constraint
ALTER TABLE users DROP CONSTRAINT unique_email;

-- Change column type
ALTER TABLE users ALTER COLUMN age TYPE VARCHAR(3);
```

---

## Queries

### WHERE Clauses

```sql
-- Comparison operators
SELECT * FROM users WHERE age > 25;
SELECT * FROM users WHERE age >= 25;
SELECT * FROM users WHERE age = 25;
SELECT * FROM users WHERE age <> 25; -- Not equal

-- String matching
SELECT * FROM users WHERE name LIKE 'J%'; -- Starts with J
SELECT * FROM users WHERE name LIKE '%son'; -- Ends with son
SELECT * FROM users WHERE name LIKE '%oh%'; -- Contains oh

-- IN operator
SELECT * FROM users WHERE id IN (1, 2, 3);

-- BETWEEN operator
SELECT * FROM users WHERE age BETWEEN 25 AND 35;

-- IS NULL
SELECT * FROM users WHERE phone IS NULL;

-- Logical operators
SELECT * FROM users WHERE age > 25 AND city = 'New York';
SELECT * FROM users WHERE age < 20 OR age > 65;
SELECT * FROM users WHERE NOT (age < 18);
```

### Sorting and Limiting

```sql
-- ORDER BY ascending
SELECT * FROM users ORDER BY age;

-- ORDER BY descending
SELECT * FROM users ORDER BY age DESC;

-- Multiple columns
SELECT * FROM users ORDER BY city, age DESC;

-- LIMIT results
SELECT * FROM users LIMIT 10;

-- OFFSET (skip rows)
SELECT * FROM users LIMIT 10 OFFSET 20;

-- FETCH (SQL standard)
SELECT * FROM users FETCH FIRST 10 ROWS ONLY;
```

### Advanced Queries

```sql
-- Subquery in WHERE
SELECT * FROM users 
WHERE id IN (SELECT user_id FROM orders WHERE total > 100);

-- Subquery in FROM
SELECT * FROM (
    SELECT user_id, COUNT(*) as order_count FROM orders GROUP BY user_id
) user_orders WHERE order_count > 5;

-- Common Table Expression (CTE)
WITH user_orders AS (
    SELECT user_id, COUNT(*) as order_count FROM orders GROUP BY user_id
)
SELECT u.name, uo.order_count FROM users u
JOIN user_orders uo ON u.id = uo.user_id
WHERE uo.order_count > 5;
```

---

## Joins

### INNER JOIN
```sql
-- Returns rows that match in both tables
SELECT users.name, orders.total 
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- Shorthand (INNER is default)
SELECT u.name, o.total FROM users u
JOIN orders o ON u.id = o.user_id;
```

### LEFT JOIN
```sql
-- Returns all rows from left table, matching rows from right
SELECT u.name, o.total FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- Find users with no orders
SELECT u.name FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

### RIGHT JOIN
```sql
-- Returns all rows from right table, matching rows from left
SELECT u.name, o.total FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

### FULL OUTER JOIN
```sql
-- Returns rows from both tables
SELECT u.name, o.total FROM users u
FULL OUTER JOIN orders o ON u.id = o.user_id;
```

### CROSS JOIN
```sql
-- Cartesian product (all combinations)
SELECT u.name, p.name FROM users u
CROSS JOIN products p;
```

### Multiple Joins
```sql
SELECT u.name, o.total, p.name
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;
```

---

## Aggregation

### Aggregate Functions

```sql
-- COUNT: Number of rows
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT city) FROM users; -- Distinct values

-- SUM: Total
SELECT SUM(total) FROM orders;

-- AVG: Average
SELECT AVG(age) FROM users;

-- MIN: Minimum value
SELECT MIN(price) FROM products;

-- MAX: Maximum value
SELECT MAX(price) FROM products;

-- STRING_AGG: Concatenate strings
SELECT STRING_AGG(name, ', ') FROM users;
```

### GROUP BY

```sql
-- Group by single column
SELECT city, COUNT(*) as user_count FROM users GROUP BY city;

-- Group by multiple columns
SELECT city, age, COUNT(*) FROM users GROUP BY city, age;

-- Having clause (filter groups)
SELECT city, COUNT(*) as count FROM users 
GROUP BY city HAVING COUNT(*) > 5;

-- Complex aggregation
SELECT 
    city,
    COUNT(*) as user_count,
    AVG(age) as avg_age,
    MAX(age) as max_age
FROM users
GROUP BY city
HAVING COUNT(*) > 10
ORDER BY user_count DESC;
```

### Window Functions

```sql
-- ROW_NUMBER: Sequential number within partition
SELECT name, salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as rank
FROM employees;

-- RANK: Rank with ties
SELECT name, salary,
    RANK() OVER (ORDER BY salary DESC) as rank
FROM employees;

-- LAG/LEAD: Access previous/next row
SELECT name, salary,
    LAG(salary) OVER (ORDER BY name) as prev_salary,
    LEAD(salary) OVER (ORDER BY name) as next_salary
FROM employees;

-- Partition by
SELECT name, department, salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank
FROM employees;
```

---

## Transactions

### ACID Properties

```sql
-- Start transaction
BEGIN;

-- Multiple operations
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Commit (save changes)
COMMIT;

-- Rollback (undo changes)
ROLLBACK;
```

### Savepoints

```sql
BEGIN;
INSERT INTO users (name) VALUES ('John');
SAVEPOINT sp1;

INSERT INTO users (name) VALUES ('Jane');
ROLLBACK TO sp1; -- Only roll back to savepoint

COMMIT;
```

### Isolation Levels

```sql
-- Set isolation level
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

BEGIN;
-- Operations here
COMMIT;

-- Levels: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE
```

---

## Indexes

### Creating Indexes

```sql
-- Single column index
CREATE INDEX idx_email ON users(email);

-- Multi-column index
CREATE INDEX idx_city_age ON users(city, age);

-- Unique index
CREATE UNIQUE INDEX idx_username ON users(username);

-- Partial index (conditional)
CREATE INDEX idx_active_users ON users(id) WHERE active = true;

-- Full-text search index
CREATE INDEX idx_name_fts ON users USING GIN(to_tsvector('english', name));
```

### Managing Indexes

```sql
-- List indexes
\d users

-- Drop index
DROP INDEX idx_email;

-- Analyze table (updates statistics)
ANALYZE users;

-- Explain query plan (see if index is used)
EXPLAIN SELECT * FROM users WHERE email = 'john@example.com';

-- Verbose explain
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'john@example.com';
```

### Performance Tips

```sql
-- Use EXPLAIN to find slow queries
EXPLAIN (ANALYZE, BUFFERS) 
SELECT u.name, COUNT(o.id)
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;

-- Create indexes on columns used in WHERE, JOIN, ORDER BY
CREATE INDEX idx_user_id ON orders(user_id);
CREATE INDEX idx_order_date ON orders(created_at);

-- Avoid functions in WHERE (prevents index use)
-- Bad: SELECT * FROM users WHERE LOWER(email) = 'john@example.com'
-- Good: SELECT * FROM users WHERE email = 'john@example.com'
```

---

## Python Integration

### psycopg2 (Low-level)

```python
import psycopg2

# Connect to database
conn = psycopg2.connect(
    host="localhost",
    database="my_app",
    user="postgres",
    password="password"
)

cursor = conn.cursor()

# Execute query
cursor.execute("SELECT * FROM users WHERE age > %s", (25,))
results = cursor.fetchall()

# Fetch results
cursor.execute("SELECT * FROM users")
one_row = cursor.fetchone()      # Get one row
many_rows = cursor.fetchmany(5)  # Get 5 rows
all_rows = cursor.fetchall()     # Get all remaining rows

# Insert data
cursor.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    ("John Doe", "john@example.com")
)
conn.commit()

# Close
cursor.close()
conn.close()
```

### SQLAlchemy (High-level ORM)

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session
from datetime import datetime

# Create engine
engine = create_engine('postgresql://user:password@localhost/my_app')

# Define models
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    orders = relationship("Order", back_populates="user")

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    total = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="orders")

# Create tables
Base.metadata.create_all(engine)

# Query examples
session = Session(engine)

# Create
user = User(name="John", email="john@example.com", age=30)
session.add(user)
session.commit()

# Read
users = session.query(User).all()
user = session.query(User).filter_by(email="john@example.com").first()

# Update
user = session.query(User).filter_by(id=1).first()
user.age = 31
session.commit()

# Delete
session.delete(user)
session.commit()

# Join query
results = session.query(User, Order).join(Order).filter(Order.total > 100).all()

# Close
session.close()
```

### Connection Pooling

```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

# Create engine with connection pooling
engine = create_engine(
    'postgresql://user:password@localhost/my_app',
    poolclass=QueuePool,
    pool_size=5,           # Number of connections to keep in pool
    max_overflow=10,       # Additional connections when needed
    pool_recycle=3600      # Recycle connections after 1 hour
)
```

### Error Handling

```python
import psycopg2
from psycopg2 import sql

try:
    conn = psycopg2.connect(database="my_app", user="postgres")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)",
                  ("John", "john@example.com"))
    conn.commit()
    
except psycopg2.IntegrityError as e:
    conn.rollback()
    print(f"Unique constraint violation: {e}")
    
except psycopg2.OperationalError as e:
    print(f"Cannot connect to database: {e}")
    
except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
    
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
```

---

## Performance Tips

### Query Optimization

```sql
-- 1. Use indexes on frequently queried columns
CREATE INDEX idx_email ON users(email);

-- 2. Avoid SELECT * (select only needed columns)
-- Bad: SELECT * FROM users
-- Good: SELECT id, name, email FROM users

-- 3. Use LIMIT to reduce data
SELECT * FROM large_table LIMIT 100;

-- 4. Avoid functions in WHERE (use index)
-- Bad: SELECT * FROM users WHERE LOWER(email) = 'john@example.com'
-- Good: SELECT * FROM users WHERE email = 'john@example.com'

-- 5. Use EXISTS for checking existence
-- Better: SELECT * FROM users WHERE EXISTS (SELECT 1 FROM orders WHERE user_id = users.id)
-- Than: SELECT * FROM users WHERE id IN (SELECT user_id FROM orders)
```

### Common Issues and Solutions

```
Problem: Query is slow
Solution: 
  1. Run EXPLAIN ANALYZE
  2. Check if indexes exist
  3. Update statistics: ANALYZE table_name
  4. Rewrite query to be more efficient

Problem: Connection pool exhausted
Solution:
  1. Increase pool_size parameter
  2. Set pool_recycle to close old connections
  3. Check for connection leaks (ensure close() is called)

Problem: Disk space full
Solution:
  1. Delete old data
  2. VACUUM FULL table_name (reorganize data)
  3. Expand disk space
```

---

## Useful psql Commands

```bash
# Connect to database
psql -U postgres -d my_app

# List databases
\l

# List tables
\dt

# Describe table
\d table_name

# List indexes
\di

# Show schema of table
\d+ table_name

# Exit
\q

# Execute SQL from file
\i /path/to/file.sql

# Toggle expanded output
\x

# Format output as CSV
\f ','
\a

# Show query execution time
\timing
```

---

## Common Patterns

### Pagination

```sql
-- Get page 2 (10 items per page)
SELECT * FROM users 
ORDER BY id 
LIMIT 10 OFFSET ((2 - 1) * 10);
```

### Auto-increment ID

```sql
-- Using SERIAL type
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

-- Get last inserted ID
INSERT INTO users (name) VALUES ('John') RETURNING id;
```

### Soft Delete

```sql
-- Add deleted_at column
ALTER TABLE users ADD COLUMN deleted_at TIMESTAMP;

-- Soft delete
UPDATE users SET deleted_at = NOW() WHERE id = 1;

-- Query active records
SELECT * FROM users WHERE deleted_at IS NULL;
```

### Audit Trail

```sql
-- Create audit table
CREATE TABLE users_audit (
    id SERIAL,
    user_id INTEGER,
    action VARCHAR(50),
    old_value TEXT,
    new_value TEXT,
    changed_at TIMESTAMP DEFAULT NOW()
);

-- Trigger for audit
CREATE TRIGGER users_audit_trigger
AFTER UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION log_audit_change();
```

---

## Summary

This reference guide covers:
- ✅ Basic SQL operations (CRUD)
- ✅ Data types and constraints
- ✅ Schema design and relationships
- ✅ Complex queries and joins
- ✅ Aggregation and grouping
- ✅ Transactions
- ✅ Indexes and performance
- ✅ Python integration
- ✅ Common patterns

For more information, visit: https://www.postgresql.org/docs/

