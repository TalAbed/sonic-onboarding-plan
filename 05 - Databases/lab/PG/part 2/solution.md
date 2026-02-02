# Part 2: Query Operations - Solutions

---

## Exercise 2.1: Basic SELECT with Filtering - Solutions

### Exercise 2.1a: Find Products by Category

```sql
SELECT * FROM products 
WHERE category = 'Electronics';
```

**Result:** 5 rows
```
 id |      name       | price | category
----+-----------------+-------+-------------
  1 | iPhone 15       | 999   | Electronics
  2 | MacBook Pro     | 2499  | Electronics
  3 | iPad Air        | 599   | Electronics
  4 | AirPods Pro     | 249   | Electronics
  5 | Samsung TV 55"  | 799   | Electronics
```

---

### Exercise 2.1b: Find Expensive Products

```sql
SELECT name, price FROM products 
WHERE price > 500
ORDER BY price DESC;
```

**Result:** 4 rows
```
      name       | price
-----------------+-------
 MacBook Pro     | 2499
 iPhone 15       | 999
 Samsung TV 55"  | 799
 iPad Air        | 599
```

---

### Exercise 2.1c: Find Recent Orders

```sql
SELECT * FROM orders 
WHERE order_date >= NOW() - INTERVAL '7 days'
ORDER BY order_date DESC;
```

**Explanation:**
- `NOW()` - Current date/time
- `INTERVAL '7 days'` - 7-day interval
- `NOW() - INTERVAL '7 days'` - 7 days ago
- `>=` - Greater than or equal

**Note:** If all test data is recent, this may return all orders.

---

### Exercise 2.1d: Find Specific User Orders

```sql
SELECT * FROM orders 
WHERE user_id = 1
ORDER BY order_date DESC;
```

**Result:** 3 rows (John Doe's orders)
```
 id | user_id | product_id | quantity | order_date
----+---------+------------+----------+---------------------
  1 |       1 |          1 |        1 | 2024-01-15...
  2 |       1 |          4 |        2 | 2024-01-16...
 11 |       1 |          5 |        1 | 2024-01-17...
```

---

## Exercise 2.2: JOINs - Solutions

### Exercise 2.2a: Orders with User and Product Details

```sql
SELECT 
    u.name as user_name,
    p.name as product_name,
    o.quantity,
    o.order_date
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN products p ON o.product_id = p.id
ORDER BY o.order_date DESC;
```

**Result:**
```
  user_name    |   product_name   | quantity | order_date
----------------+------------------+----------+---------------------
 John Doe       | AirPods Pro      |        2 | 2024-01-16...
 John Doe       | iPhone 15        |        1 | 2024-01-15...
 Jane Smith     | Design Patterns  |        1 | 2024-01-15...
 Alice Brown    | Desk Lamp        |        3 | 2024-01-15...
 ...
```

**Key Points:**
- `o`, `u`, `p` are aliases (shorter names)
- `JOIN` connects tables on matching conditions
- `ON o.user_id = u.id` - Match orders to users

---

### Exercise 2.2b: Find Orders with Total Value

```sql
SELECT 
    u.name as user_name,
    p.name as product_name,
    o.quantity,
    p.price,
    (p.price * o.quantity) as total_value
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN products p ON o.product_id = p.id
ORDER BY total_value DESC;
```

**Result:**
```
 user_name  |   product_name    | quantity | price  | total_value
-------------+-------------------+----------+--------+-------------
 Jane Smith  | MacBook Pro       |        1 |   2499 |        2499
 John Doe    | Samsung TV 55"    |        1 |    799 |         799
 Alice Brown | MacBook Pro       |        1 |   2499 |        2499
 Bob Johnson | Samsung TV 55"    |        1 |    799 |         799
 John Doe    | AirPods Pro       |        2 |    249 |         498
 ...
```

---

### Exercise 2.2c: Find Products Never Ordered

```sql
SELECT DISTINCT p.* 
FROM products p
LEFT JOIN orders o ON p.id = o.product_id
WHERE o.id IS NULL;
```

**Explanation:**
- `LEFT JOIN` - Keeps all products, even without orders
- `IS NULL` - Find rows where orders.id is NULL (no orders)
- `DISTINCT` - Avoid duplicates

**Note:** With our sample data, all products have been ordered, so this may return 0 rows.

---

## Exercise 2.3: GROUP BY & Aggregation - Solutions

### Exercise 2.3a: Count Orders per User

```sql
SELECT 
    u.name,
    COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
ORDER BY order_count DESC;
```

**Result:**
```
    name      | order_count
---------------+-------------
 John Doe      |           3
 Charlie Wilson|           3
 Jane Smith    |           2
 Bob Johnson   |           2
 Alice Brown   |           2
```

**Key Points:**
- `COUNT(o.id)` - Counts non-NULL order IDs
- `GROUP BY u.id, u.name` - Group results by user
- `LEFT JOIN` - Include users with 0 orders (if any)

---

### Exercise 2.3b: Total Revenue per Category

```sql
SELECT 
    p.category,
    SUM(p.price * o.quantity) as total_revenue
FROM orders o
JOIN products p ON o.product_id = p.id
GROUP BY p.category
ORDER BY total_revenue DESC;
```

**Result:**
```
  category   | total_revenue
--------------+---------------
 Electronics  |      8000
 Books        |       240
 Home         |       775
```

**Key Points:**
- `SUM()` - Adds up values
- `p.price * o.quantity` - Revenue per order
- `GROUP BY category` - Group by product category

---

### Exercise 2.3c: Average Price per Category

```sql
SELECT 
    category,
    AVG(price) as avg_price
FROM products
GROUP BY category
ORDER BY avg_price DESC;
```

**Result:**
```
  category   |    avg_price
--------------+-----------------
 Electronics  |  809.4000000000
 Books        | 50.00000000
 Home         | 189.0000000000
```

**Key Points:**
- `AVG()` - Calculates average
- Much simpler (no JOIN needed, just products table)

---

## Exercise 2.4: ORDER BY & LIMIT - Solutions

### Exercise 2.4a: Top 5 Most Expensive Products

```sql
SELECT name, price FROM products 
ORDER BY price DESC 
LIMIT 5;
```

**Result:**
```
      name       | price
-----------------+-------
 MacBook Pro     | 2499
 iPhone 15       | 999
 Samsung TV 55"  | 799
 iPad Air        | 599
 Office Chair    | 299
```

**Key Points:**
- `ORDER BY price DESC` - Sort by price, highest first
- `LIMIT 5` - Return only 5 rows

---

### Exercise 2.4b: Top 3 Users by Order Count

```sql
SELECT 
    u.name,
    COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
ORDER BY order_count DESC
LIMIT 3;
```

**Result:**
```
    name      | order_count
---------------+-------------
 John Doe      |           3
 Charlie Wilson|           3
 Jane Smith    |           2
```

**Key Points:**
- Combines GROUP BY, ORDER BY, and LIMIT
- Same query as 2.3a, but with LIMIT 3

---

## 📊 Summary of Queries

| Exercise | Concept | Key Function |
|----------|---------|--------------|
| 2.1a | WHERE text filtering | WHERE category = 'X' |
| 2.1b | WHERE numeric filtering | WHERE price > X |
| 2.1c | WHERE date filtering | INTERVAL '7 days' |
| 2.1d | WHERE ID filtering | WHERE user_id = X |
| 2.2a | JOIN 2-3 tables | JOIN ... ON |
| 2.2b | Derived columns | (price * qty) as |
| 2.2c | LEFT JOIN with NULL | WHERE ... IS NULL |
| 2.3a | COUNT aggregation | COUNT(id) |
| 2.3b | SUM with calculation | SUM(price * qty) |
| 2.3c | AVG aggregation | AVG(price) |
| 2.4a | ORDER BY DESC + LIMIT | LIMIT 5 |
| 2.4b | Complex query | GROUP BY + ORDER BY + LIMIT |

---

## Key SQL Concepts Covered

✅ WHERE clauses (text, numeric, date filtering)  
✅ JOINs (connecting 2-3 tables)  
✅ LEFT JOIN (finding missing data)  
✅ GROUP BY (aggregating results)  
✅ Aggregate functions (COUNT, SUM, AVG)  
✅ ORDER BY (sorting results)  
✅ LIMIT (restricting result count)  
✅ Derived columns (calculating new values)