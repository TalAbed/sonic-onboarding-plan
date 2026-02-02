# Part 3: Python Integration - Instructions

**Time:** 30 minutes  
**Exercises:** 3  
**Objective:** Connect to database and execute queries from Python

---

## Exercise 3.1: Connect to Database with psycopg2

**Objective:** Establish a connection to PostgreSQL and execute a simple query

### Prerequisites

Install psycopg2:
```bash
pip install psycopg2-binary
```

### Exercise 3.1: Basic Connection

**Task:** Connect to the ecommerce database and fetch all users

**Steps:**

Step 1: Import psycopg2
```python
import psycopg2
```

Step 2: Connect to database
```python
conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="password"  # Replace with your actual password
)
```

Step 3: Create cursor
```python
cursor = conn.cursor()
```

Step 4: Execute query
```python
cursor.execute("SELECT * FROM users")
```

Step 5: Fetch results
```python
users = cursor.fetchall()
for user in users:
    print(user)
```

Step 6: Close connections
```python
cursor.close()
conn.close()
```

### Expected Output

```
(1, 'John Doe', 'john@example.com', '2024-01-15...')
(2, 'Jane Smith', 'jane@example.com', '2024-01-15...')
(3, 'Bob Johnson', 'bob@example.com', '2024-01-15...')
(4, 'Alice Brown', 'alice@example.com', '2024-01-15...')
(5, 'Charlie Wilson', 'charlie@example.com', '2024-01-15...')
```

### Questions

1. What does `cursor` do?
2. What's the difference between `fetchall()`, `fetchone()`, and `fetchmany()`?
3. Why close the connection at the end?

---

## Exercise 3.2: Query from Python - Multiple Queries

**Objective:** Execute different queries and process results

### Exercise 3.2a: Get All Products

**Task:** Fetch all products and display them nicely

**Expected Output:**
```
ID: 1, Name: iPhone 15, Price: 999, Category: Electronics
ID: 2, Name: MacBook Pro, Price: 2499, Category: Electronics
...
```

---

### Exercise 3.2b: Get Orders for Specific User

**Task:** Find all orders for user_id = 1 with product details

**Hints:**

- Use a JOIN query and parametrized query
- Use `%s` for placeholders (safe against SQL injection)
- Pass values as tuple: `(user_id,)`

**Expected Output:**
```
User: John Doe, Product: iPhone 15, Qty: 1, Total: $999
User: John Doe, Product: AirPods Pro, Qty: 2, Total: $498
...
```

---

### Exercise 3.2c: Calculate Total Spent per User

**Task:** Show each user and their total spending

**Expected Output:**
```
Jane Smith: 2 orders, $2549 spent
Alice Brown: 2 orders, $916 spent
...
```

---

## Exercise 3.3: Insert Data from Python

**Objective:** Add new data to database using Python

### Exercise 3.3a: Add a New User

**Task:** Create a function to add a new user

**Example:**

```python
def add_user(cursor, conn, name, email):
    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()  # Save to database
        print(f"User '{name}' added successfully")
    except psycopg2.IntegrityError as e:
        conn.rollback()  # Undo the insert
        print(f"Error: Email already exists or invalid")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

# Example usage:
add_user(cursor, conn, "David Lee", "david@example.com")
add_user(cursor, conn, "Eve Miller", "eve@example.com")
```

**Key Points:**
- Use `INSERT INTO` with parametrized values
- Always `commit()` after INSERT
- Use `try/except` for error handling
- Use `rollback()` if something fails

---

### Exercise 3.3b: Add a New Product

**Task:** Create a function to add a new product

---

### Exercise 3.3c: Create an Order

**Task:** Add an order for a user

---

## 📋 Checklist

Before completing Part 3, verify you can:

- [ ] Install and import psycopg2
- [ ] Connect to PostgreSQL database
- [ ] Create a cursor
- [ ] Execute SELECT queries
- [ ] Fetch results (fetchall, fetchone)
- [ ] Use parametrized queries (with %s)
- [ ] Display results in Python
- [ ] Insert new data
- [ ] Commit changes
- [ ] Handle errors with try/except
- [ ] Rollback on errors
- [ ] Close connections

---

## 🎯 Complete Lab Script

Here's a complete Python script combining all parts:

```python
import psycopg2

# Connect to database
conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="password"
)
cursor = conn.cursor()

print("=" * 50)
print("PostgreSQL Lab - Python Integration")
print("=" * 50)

# 1. Get all users
print("\n1. All Users:")
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
for user in users:
    print(f"  {user[1]} ({user[2]})")

# 2. Get products by category
print("\n2. Electronics Products:")
cursor.execute("SELECT name, price FROM products WHERE category = 'Electronics'")
products = cursor.fetchall()
for product in products:
    print(f"  {product[0]}: ${product[1]}")

# 3. User spending
print("\n3. User Spending Summary:")
cursor.execute("""
    SELECT u.name, COUNT(o.id), SUM(p.price * o.quantity)
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    LEFT JOIN products p ON o.product_id = p.id
    GROUP BY u.id, u.name
    ORDER BY 3 DESC
""")
results = cursor.fetchall()
for row in results:
    if row[2]:
        print(f"  {row[0]}: {row[1]} orders, ${row[2]}")

# 4. Add new user
print("\n4. Adding new user...")
cursor.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    ("Frank Davis", "frank@example.com")
)
conn.commit()
print("  New user added!")

# Close
cursor.close()
conn.close()
print("\n" + "=" * 50)
print("Complete!")
```

---

## Next Step

Congratulations! You've completed all 3 parts of the lab!

Move to: `solutions/part-3-python-solution.md` to see complete examples.

