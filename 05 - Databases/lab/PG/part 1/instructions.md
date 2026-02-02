# Part 1: Schema Design & Sample Data - Instructions

**Time:** 45 minutes - 1 hour  
**Exercises:** 2  
**Objective:** Create database tables and populate with sample data

---

## Exercise 1.1: Create Database Tables

**Objective:** Create 3 tables with proper constraints

Follow these steps to create the schema:

**Step 1: Create Users Table**
- Table name: `users`
- Column 1: `id` - SERIAL (auto-incrementing) PRIMARY KEY
- Column 2: `name` - VARCHAR(100) NOT NULL
- Column 3: `email` - VARCHAR(100) UNIQUE NOT NULL
- Column 4: `created_at` - TIMESTAMP DEFAULT NOW()

**Step 2: Create Products Table**
- Table name: `products`
- Column 1: `id` - SERIAL PRIMARY KEY
- Column 2: `name` - VARCHAR(100) NOT NULL
- Column 3: `price` - DECIMAL(10,2) NOT NULL
- Column 4: `category` - VARCHAR(50)

**Step 3: Create Orders Table**
- Table name: `orders`
- Column 1: `id` - SERIAL PRIMARY KEY
- Column 2: `user_id` - INTEGER NOT NULL with FOREIGN KEY reference to users(id)
- Column 3: `product_id` - INTEGER NOT NULL with FOREIGN KEY reference to products(id)
- Column 4: `quantity` - INTEGER NOT NULL DEFAULT 1
- Column 5: `order_date` - TIMESTAMP DEFAULT NOW()

### Questions to Consider

1. Why do we use SERIAL instead of just INTEGER?
2. Why is email marked as UNIQUE?
3. What does DEFAULT NOW() do?
4. What is the purpose of FOREIGN KEY constraints?

### Validation

Run these commands to verify your tables:

```sql
-- Check table structure
\d users
\d products
\d orders

-- Try inserting invalid data (should fail)
-- This tests your constraints
INSERT INTO users (name) VALUES ('Test');  -- Should fail (no email)
INSERT INTO users (email, name) VALUES ('duplicate@test.com', 'User1');
INSERT INTO users (email, name) VALUES ('duplicate@test.com', 'User2');  -- Should fail (duplicate)
```

---

## Exercise 1.2: Insert Sample Data

**Objective:** Populate tables with realistic sample data

### Sample Data to Insert

**5 Users:**
1. John Doe (john@example.com)
2. Jane Smith (jane@example.com)
3. Bob Johnson (bob@example.com)
4. Alice Brown (alice@example.com)
5. Charlie Wilson (charlie@example.com)

**10 Products (2-3 categories):**

**Electronics (5 products):**
- iPhone 15 - $999
- MacBook Pro - $2499
- iPad Air - $599
- AirPods Pro - $249
- Samsung TV 55" - $799

**Books (3 products):**
- "Clean Code" - $50
- "Design Patterns" - $55
- "SQL Performance" - $45

**Home (2 products):**
- Office Chair - $299
- Desk Lamp - $79

**15 Orders (mix across users and products):**
- User 1 → iPhone 15 (qty: 1)
- User 1 → AirPods Pro (qty: 2)
- User 2 → MacBook Pro (qty: 1)
- User 2 → "Clean Code" (qty: 1)
- User 3 → Samsung TV 55" (qty: 1)
- User 3 → Office Chair (qty: 1)
- User 4 → iPad Air (qty: 1)
- User 4 → Desk Lamp (qty: 3)
- User 5 → "Design Patterns" (qty: 2)
- User 5 → "SQL Performance" (qty: 1)
- User 1 → Samsung TV 55" (qty: 1)
- User 2 → iPad Air (qty: 1)
- User 3 → "Clean Code" (qty: 1)
- User 4 → MacBook Pro (qty: 1)
- User 5 → Office Chair (qty: 1)

### Validation

```sql
-- Count total records
SELECT COUNT(*) as user_count FROM users;
SELECT COUNT(*) as product_count FROM products;
SELECT COUNT(*) as order_count FROM orders;

-- Should show:
-- user_count = 5
-- product_count = 10
-- order_count = 15

-- View all data
SELECT * FROM users;
SELECT * FROM products;
SELECT * FROM orders;
```

### Questions to Consider

1. Why do we insert users and products before orders?
2. What happens if we try to insert an order with an invalid user_id?
3. How can we view the data we just inserted?

---

## 📋 Checklist

Before moving to Part 2, verify:

- [ ] Users table created with all columns
- [ ] Products table created with all columns
- [ ] Orders table created with foreign keys
- [ ] 5 users inserted
- [ ] 10 products inserted
- [ ] 15 orders inserted
- [ ] All validation queries pass
- [ ] Constraints are working (try duplicate email)

---

## 🎯 Next Step

Once Part 1 is complete, move to: `part-2-queries.md`

Good luck! 🚀

