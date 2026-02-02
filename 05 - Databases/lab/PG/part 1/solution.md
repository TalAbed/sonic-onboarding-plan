# Part 1: Schema Design & Sample Data - Solutions

---

## Exercise 1.1: Create Database Tables - Solution

### Step 1: Create Users Table

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```

**Explanation:**
- `SERIAL PRIMARY KEY` - Auto-incrementing unique identifier
- `VARCHAR(100) NOT NULL` - Text field, required, max 100 chars
- `UNIQUE NOT NULL` - Email must be unique and required
- `DEFAULT NOW()` - Automatically set to current timestamp

### Step 2: Create Products Table

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(50)
);
```

**Explanation:**
- `DECIMAL(10,2)` - Fixed-point number with 10 total digits, 2 decimal places
- `category` - Optional field (no NOT NULL constraint)

### Step 3: Create Orders Table

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id),
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity INTEGER NOT NULL DEFAULT 1,
    order_date TIMESTAMP DEFAULT NOW()
);
```

**Explanation:**
- `REFERENCES users(id)` - Foreign key constraint linking to users table
- `DEFAULT 1` - Default quantity is 1 if not specified
- `NOT NULL` - These fields are required

### Verify Tables

```sql
-- Check table structure
\d users
\d products
\d orders

-- View constraints
\d+ orders
```

**Expected output for \d orders:**
```
                        Table "public.orders"
   Column   |            Type             | Collation | Nullable | Default
------------+-----------------------------+-----------+----------+---------
 id         | integer                     |           | not null | nextval(...)
 user_id    | integer                     |           | not null |
 product_id | integer                     |           | not null |
 quantity   | integer                     |           | not null | 1
 order_date | timestamp without time zone |           |          | now()
```

---

## Exercise 1.2: Insert Sample Data - Solution

### Step 1: Insert Users

```sql
INSERT INTO users (name, email) VALUES
('John Doe', 'john@example.com'),
('Jane Smith', 'jane@example.com'),
('Bob Johnson', 'bob@example.com'),
('Alice Brown', 'alice@example.com'),
('Charlie Wilson', 'charlie@example.com');
```

### Step 2: Insert Products

```sql
INSERT INTO products (name, price, category) VALUES
('iPhone 15', 999.00, 'Electronics'),
('MacBook Pro', 2499.00, 'Electronics'),
('iPad Air', 599.00, 'Electronics'),
('AirPods Pro', 249.00, 'Electronics'),
('Samsung TV 55"', 799.00, 'Electronics'),
('Clean Code', 50.00, 'Books'),
('Design Patterns', 55.00, 'Books'),
('SQL Performance', 45.00, 'Books'),
('Office Chair', 299.00, 'Home'),
('Desk Lamp', 79.00, 'Home');
```

### Step 3: Insert Orders

```sql
INSERT INTO orders (user_id, product_id, quantity) VALUES
(1, 1, 1),   -- John bought 1 iPhone 15
(1, 4, 2),   -- John bought 2 AirPods Pro
(2, 2, 1),   -- Jane bought 1 MacBook Pro
(2, 6, 1),   -- Jane bought 1 Clean Code book
(3, 5, 1),   -- Bob bought 1 Samsung TV
(3, 9, 1),   -- Bob bought 1 Office Chair
(4, 3, 1),   -- Alice bought 1 iPad Air
(4, 10, 3),  -- Alice bought 3 Desk Lamps
(5, 7, 2),   -- Charlie bought 2 Design Patterns books
(5, 8, 1),   -- Charlie bought 1 SQL Performance book
(1, 5, 1),   -- John bought 1 Samsung TV
(2, 3, 1),   -- Jane bought 1 iPad Air
(3, 6, 1),   -- Bob bought 1 Clean Code book
(4, 2, 1),   -- Alice bought 1 MacBook Pro
(5, 9, 1);   -- Charlie bought 1 Office Chair
```

### Verify Data

```sql
-- Count records in each table
SELECT COUNT(*) as user_count FROM users;
SELECT COUNT(*) as product_count FROM products;
SELECT COUNT(*) as order_count FROM orders;
```

**Expected results:**
```
user_count    = 5
product_count = 10
order_count   = 15
```

### View All Data

```sql
-- View all users
SELECT * FROM users;

-- View all products
SELECT * FROM products;

-- View all orders
SELECT * FROM orders;
```

### Test Constraints

These should FAIL (demonstrating constraints work):

```sql
-- This should fail: email is UNIQUE
INSERT INTO users (name, email) VALUES
('Duplicate User', 'john@example.com');

-- This should fail: email is NOT NULL
INSERT INTO users (name, email) VALUES
('No Email', NULL);

-- This should fail: name is NOT NULL
INSERT INTO users (name, email) VALUES
(NULL, 'noname@example.com');

-- This should fail: invalid user_id (foreign key)
INSERT INTO orders (user_id, product_id, quantity) VALUES
(999, 1, 1);  -- user_id 999 doesn't exist

-- This should fail: invalid product_id (foreign key)
INSERT INTO orders (user_id, product_id, quantity) VALUES
(1, 999, 1);  -- product_id 999 doesn't exist
```

---

## 📊 Summary

**Tables Created:**
- ✅ users (5 rows)
- ✅ products (10 rows)
- ✅ orders (15 rows)

**Constraints Verified:**
- ✅ Primary keys work
- ✅ Foreign keys work
- ✅ UNIQUE constraint works
- ✅ NOT NULL constraint works
- ✅ DEFAULT values work

**What You Learned:**
- Creating tables with proper structure
- Defining constraints (PK, FK, UNIQUE, NOT NULL)
- Setting default values
- Understanding data types
- Inserting data with proper references

---

## Next Step

Move to: `part-2-queries.md` to write queries against this data!
