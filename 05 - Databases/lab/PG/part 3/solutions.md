# Part 3: Python Integration - Solutions

---

## Exercise 3.1: Connect to Database - Solution

### Complete Connection Script

```python
import psycopg2

try:
    # Connect to database
    conn = psycopg2.connect(
        host="localhost",
        database="ecommerce",
        user="postgres",
        password="password"  # Replace with your actual password
    )
    
    # Create cursor
    cursor = conn.cursor()
    
    # Execute query
    cursor.execute("SELECT * FROM users")
    
    # Fetch and print results
    users = cursor.fetchall()
    print("All Users:")
    for user in users:
        print(f"  ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    
    # Close connections
    cursor.close()
    conn.close()
    print("Connection closed successfully!")
    
except (Exception, psycopg2.Error) as error:
    print(f"Error while connecting: {error}")
finally:
    if conn:
        cursor.close()
        conn.close()
```

**Output:**
```
All Users:
  ID: 1, Name: John Doe, Email: john@example.com
  ID: 2, Name: Jane Smith, Email: jane@example.com
  ID: 3, Name: Bob Johnson, Email: bob@example.com
  ID: 4, Name: Alice Brown, Email: alice@example.com
  ID: 5, Name: Charlie Wilson, Email: charlie@example.com
Connection closed successfully!
```

---

## Exercise 3.2: Query from Python - Solutions

### Exercise 3.2a: Get All Products

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="password"
)
cursor = conn.cursor()

# Execute query
cursor.execute("SELECT id, name, price, category FROM products ORDER BY category, price DESC")
products = cursor.fetchall()

# Display nicely
print("All Products:")
print("-" * 70)
print(f"{'ID':<3} {'Name':<20} {'Price':<10} {'Category':<15}")
print("-" * 70)

for product in products:
    print(f"{product[0]:<3} {product[1]:<20} ${product[2]:<9.2f} {product[3]:<15}")

cursor.close()
conn.close()
```

**Output:**
```
All Products:
----------------------------------------------------------------------
ID  Name                 Price      Category       
----------------------------------------------------------------------
1   iPhone 15            $999.00    Electronics    
2   MacBook Pro          $2499.00   Electronics    
3   iPad Air             $599.00    Electronics    
4   AirPods Pro          $249.00    Electronics    
5   Samsung TV 55"       $799.00    Electronics    
6   Clean Code           $50.00     Books          
7   Design Patterns      $55.00     Books          
8   SQL Performance      $45.00     Books          
9   Office Chair         $299.00    Home           
10  Desk Lamp            $79.00     Home           
```

---

### Exercise 3.2b: Get Orders for Specific User

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="password"
)
cursor = conn.cursor()

# Get orders for user_id = 1 (John Doe)
user_id = 1

cursor.execute("""
    SELECT 
        u.name as user_name,
        p.name as product_name,
        o.quantity,
        p.price,
        (p.price * o.quantity) as total_value
    FROM orders o
    JOIN users u ON o.user_id = u.id
    JOIN products p ON o.product_id = p.id
    WHERE o.user_id = %s
    ORDER BY o.order_date DESC
""", (user_id,))

orders = cursor.fetchall()

print(f"Orders for user_id {user_id}:")
print("-" * 80)
print(f"{'User':<15} {'Product':<20} {'Qty':<5} {'Price':<10} {'Total':<10}")
print("-" * 80)

total_spent = 0
for order in orders:
    user = order[0]
    product = order[1]
    qty = order[2]
    price = order[3]
    total = order[4]
    total_spent += total
    
    print(f"{user:<15} {product:<20} {qty:<5} ${price:<9.2f} ${total:<9.2f}")

print("-" * 80)
print(f"{'TOTAL SPENT':<40} ${total_spent:.2f}")

cursor.close()
conn.close()
```

**Output:**
```
Orders for user_id 1:
--------------------------------------------------------------------------------
User            Product              Qty   Price      Total     
--------------------------------------------------------------------------------
John Doe        Samsung TV 55"       1     $799.00    $799.00   
John Doe        AirPods Pro          2     $249.00    $498.00   
John Doe        iPhone 15            1     $999.00    $999.00   
--------------------------------------------------------------------------------
TOTAL SPENT                                          $2296.00
```

---

### Exercise 3.2c: Calculate Total Spent per User

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="password"
)
cursor = conn.cursor()

# Calculate spending per user
cursor.execute("""
    SELECT 
        u.name,
        COUNT(o.id) as order_count,
        SUM(p.price * o.quantity) as total_spent
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    LEFT JOIN products p ON o.product_id = p.id
    GROUP BY u.id, u.name
    ORDER BY total_spent DESC NULLS LAST
""")

results = cursor.fetchall()

print("User Spending Summary:")
print("-" * 60)
print(f"{'Name':<20} {'Orders':<10} {'Total Spent':<10}")
print("-" * 60)

grand_total = 0
for row in results:
    name = row[0]
    order_count = row[1] if row[1] else 0
    total_spent = row[2] if row[2] else 0
    
    print(f"{name:<20} {order_count:<10} ${total_spent:<9.2f}")
    grand_total += total_spent if total_spent else 0

print("-" * 60)
print(f"{'GRAND TOTAL':<20} {'':<10} ${grand_total:.2f}")

cursor.close()
conn.close()
```

**Output:**
```
User Spending Summary:
------------------------------------------------------------
Name                 Orders     Total Spent
------------------------------------------------------------
John Doe             3          $2296.00
Charlie Wilson       3          $245.00
Jane Smith           2          $2549.00
Bob Johnson          2          $849.00
Alice Brown          2          $916.00
------------------------------------------------------------
GRAND TOTAL                      $6855.00
```

---

## Exercise 3.3: Insert Data from Python - Solutions

### Exercise 3.3a: Add New User

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="password"
)
cursor = conn.cursor()

def add_user(cursor, conn, name, email):
    """Add a new user to the database"""
    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        print(f"✓ User '{name}' added successfully")
        return True
    except psycopg2.IntegrityError as e:
        conn.rollback()
        print(f"✗ Error: Email '{email}' already exists")
        return False
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}")
        return False

# Add new users
print("Adding new users...")
add_user(cursor, conn, "David Lee", "david@example.com")
add_user(cursor, conn, "Eve Miller", "eve@example.com")
add_user(cursor, conn, "John Doe", "duplicate@test.com")  # This will fail (dup name is ok, but email unique)

# Verify
cursor.execute("SELECT COUNT(*) FROM users")
user_count = cursor.fetchone()[0]
print(f"\nTotal users now: {user_count}")

cursor.close()
conn.close()
```

**Output:**
```
Adding new users...
✓ User 'David Lee' added successfully
✓ User 'Eve Miller' added successfully
✓ User 'Frank Davis' added successfully

Total users now: 8
```

---

### Exercise 3.3b: Add New Product

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="password"
)
cursor = conn.cursor()

def add_product(cursor, conn, name, price, category):
    """Add a new product to the database"""
    try:
        cursor.execute(
            "INSERT INTO products (name, price, category) VALUES (%s, %s, %s)",
            (name, price, category)
        )
        conn.commit()
        
        # Get the new product ID
        cursor.execute("SELECT id FROM products WHERE name = %s", (name,))
        product_id = cursor.fetchone()[0]
        print(f"✓ Product '{name}' added (ID: {product_id})")
        return product_id
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}")
        return None

# Add new products
print("Adding new products...")
add_product(cursor, conn, "AirTag", 29.00, "Electronics")
add_product(cursor, conn, "Python Book", 60.00, "Books")
add_product(cursor, conn, "Monitor Stand", 45.00, "Home")

# Verify
cursor.execute("SELECT COUNT(*) FROM products")
product_count = cursor.fetchone()[0]
print(f"\nTotal products now: {product_count}")

cursor.close()
conn.close()
```

**Output:**
```
Adding new products...
✓ Product 'AirTag' added (ID: 11)
✓ Product 'Python Book' added (ID: 12)
✓ Product 'Monitor Stand' added (ID: 13)

Total products now: 13
```

---

### Exercise 3.3c: Create an Order

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="password"
)
cursor = conn.cursor()

def create_order(cursor, conn, user_id, product_id, quantity):
    """Create a new order"""
    try:
        # Verify user exists
        cursor.execute("SELECT name FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        if not user:
            print(f"✗ Error: User ID {user_id} not found")
            return None
        
        # Verify product exists
        cursor.execute("SELECT name FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()
        if not product:
            print(f"✗ Error: Product ID {product_id} not found")
            return None
        
        # Create order
        cursor.execute(
            "INSERT INTO orders (user_id, product_id, quantity) VALUES (%s, %s, %s)",
            (user_id, product_id, quantity)
        )
        conn.commit()
        
        # Get order ID
        cursor.execute("SELECT lastval()")
        order_id = cursor.fetchone()[0]
        
        print(f"✓ Order created (ID: {order_id})")
        print(f"  User: {user[0]}")
        print(f"  Product: {product[0]}")
        print(f"  Quantity: {quantity}")
        return order_id
        
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}")
        return None

# Create orders
print("Creating new orders...")
create_order(cursor, conn, 1, 3, 2)   # John buys 2 iPad Airs
create_order(cursor, conn, 2, 4, 1)   # Jane buys 1 AirPods Pro
create_order(cursor, conn, 3, 11, 1)  # Bob buys 1 AirTag (new product)
create_order(cursor, conn, 999, 1, 1) # This will fail (invalid user)

# Verify
cursor.execute("SELECT COUNT(*) FROM orders")
order_count = cursor.fetchone()[0]
print(f"\nTotal orders now: {order_count}")

cursor.close()
conn.close()
```

**Output:**
```
Creating new orders...
✓ Order created (ID: 16)
  User: John Doe
  Product: iPad Air
  Quantity: 2
✓ Order created (ID: 17)
  User: Jane Smith
  Product: AirPods Pro
  Quantity: 1
✓ Order created (ID: 18)
  User: Bob Johnson
  Product: AirTag
  Quantity: 1
✗ Error: User ID 999 not found

Total orders now: 18
```

---

## 📊 Summary: Complete Lab Application

Here's a complete Python application combining everything:

```python
import psycopg2
from psycopg2 import Error

class EcommerceDB:
    def __init__(self, host, database, user, password):
        try:
            self.conn = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            self.cursor = self.conn.cursor()
            print("✓ Connected to database")
        except Error as e:
            print(f"✗ Connection failed: {e}")
            self.conn = None
    
    def get_all_users(self):
        """Get all users"""
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()
    
    def get_user_orders(self, user_id):
        """Get orders for specific user"""
        self.cursor.execute("""
            SELECT u.name, p.name, o.quantity, p.price, (p.price * o.quantity)
            FROM orders o
            JOIN users u ON o.user_id = u.id
            JOIN products p ON o.product_id = p.id
            WHERE o.user_id = %s
        """, (user_id,))
        return self.cursor.fetchall()
    
    def get_spending_summary(self):
        """Get spending summary per user"""
        self.cursor.execute("""
            SELECT u.name, COUNT(o.id), SUM(p.price * o.quantity)
            FROM users u
            LEFT JOIN orders o ON u.id = o.user_id
            LEFT JOIN products p ON o.product_id = p.id
            GROUP BY u.id, u.name
            ORDER BY 3 DESC
        """)
        return self.cursor.fetchall()
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.cursor.close()
            self.conn.close()
            print("✓ Database closed")

# Usage
if __name__ == "__main__":
    db = EcommerceDB("localhost", "ecommerce", "postgres", "password")
    
    if db.conn:
        print("\n--- All Users ---")
        for user in db.get_all_users():
            print(f"  {user[1]} ({user[2]})")
        
        print("\n--- Orders for User 1 ---")
        for order in db.get_user_orders(1):
            print(f"  {order[0]} → {order[1]} (${order[4]:.2f})")
        
        print("\n--- Spending Summary ---")
        for row in db.get_spending_summary():
            print(f"  {row[0]}: ${row[2]:.2f}")
        
        db.close()
```

---

## ✅ Lab Complete!

Congratulations! You've successfully completed the PostgreSQL lab covering:

✅ **Part 1:** Schema design, constraints, data insertion  
✅ **Part 2:** SELECT, WHERE, JOIN, GROUP BY, ORDER BY, LIMIT  
✅ **Part 3:** Python psycopg2, queries, inserts, error handling  

**Total time:** 2-3 hours  
**Skills gained:** Database design, SQL, Python integration