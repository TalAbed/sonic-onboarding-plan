# Part 2: Query Operations - Instructions

**Time:** 45 minutes - 1 hour  
**Exercises:** 4  
**Objective:** Write queries to retrieve and analyze data

---

## Exercise 2.1: Basic SELECT with Filtering (WHERE)

**Objective:** Write SELECT queries with WHERE clauses to filter data

### Exercise 2.1a: Find Products by Category

**Task:** Find all products in the "Electronics" category

---

### Exercise 2.1b: Find Expensive Products

**Task:** Find all products costing more than $500

**Question:** How would you find products between $100-$500?

---

### Exercise 2.1c: Find Recent Orders

**Task:** Find all orders from the last 7 days

**Questions:**
- What is INTERVAL in PostgreSQL?
- How would you find orders from a specific month?

---

### Exercise 2.1d: Find Specific User Orders

**Task:** Find all orders made by user_id = 1 (John Doe)

**Questions:**
- How do you filter by ID?
- What if you wanted to find orders by user name instead?

---

## Exercise 2.2: JOINs - Connect Multiple Tables

**Objective:** Query across multiple tables using JOINs

### Exercise 2.2a: Orders with User and Product Details

**Task:** Find all orders with user names and product names

**Expected result format:**
```
user_name      | product_name      | quantity | order_date
John Doe       | iPhone 15         | 1        | 2024-01-15
John Doe       | AirPods Pro       | 2        | 2024-01-16
...
```

**Questions:**
- What does ON mean in JOIN?
- Why do we need aliases (like o, u, p)?
- What's the difference between JOIN and other join types?

---

### Exercise 2.2b: Find Orders with Total Value

**Task:** Calculate the total value of each order (quantity × price)

**Hints:**
1. SELECT: user name, product name, quantity, price
2. Calculate: (p.price * o.quantity) as total_value
3. JOIN: orders → users → products
4. ORDER BY total_value DESC (largest orders first)

**Expected result format:**
```
user_name | product_name  | quantity | price | total_value
Jane      | MacBook Pro   | 1        | 2499  | 2499
Alice     | Desk Lamp     | 3        | 79    | 237
...
```

**Questions:**
- How do you do math in SQL?
- What does "AS" do?

---

### Exercise 2.2c: Find Products That Have Never Been Ordered

**Task:** Find all products with no orders (using LEFT JOIN)

**Expected result:** Products that weren't in sample orders

**Questions:**
- What's the difference between JOIN and LEFT JOIN?
- Why use LEFT JOIN instead of regular JOIN?

---

## Exercise 2.3: GROUP BY & Aggregation

**Objective:** Use aggregation functions to analyze data

### Exercise 2.3a: Count Orders per User

**Task:** How many orders has each user made?

**Expected result:**
```
name            | order_count
John Doe        | 3
Jane Smith      | 2
Bob Johnson     | 2
Alice Brown     | 2
Charlie Wilson  | 3
```

**Questions:**
- What does COUNT(o.id) do?
- Why use LEFT JOIN instead of regular JOIN?
- Why GROUP BY u.id, u.name?

---

### Exercise 2.3b: Total Revenue per Category

**Task:** Calculate total revenue for each category

**Expected result:**
```
category     | total_revenue
Electronics  | 8000
Books        | 240
Home         | 775
```

**Questions:**
- What does SUM() do?
- How do you calculate revenue from price and quantity?
- Why GROUP BY category?

---

### Exercise 2.3c: Average Price per Category

**Task:** Find average product price in each category

**Expected result:**
```
category     | avg_price
Electronics  | 809.40
Books        | 50.00
Home         | 189.00
```

---

## Exercise 2.4: ORDER BY & LIMIT

**Objective:** Sort and limit query results

### Exercise 2.4a: Top 5 Most Expensive Products

**Task:** Show 5 most expensive products

**Expected result:**
```
name           | price
MacBook Pro    | 2499
iPhone 15      | 999
Samsung TV 55" | 799
iPad Air       | 599
Office Chair   | 299
```

**Questions:**
- What happens if there are fewer than 5 results?

---

### Exercise 2.4b: Top 3 Users by Order Count

**Task:** Find users who made the most orders

**Expected result:**
```
name           | order_count
John Doe       | 3
Charlie Wilson | 3
Jane Smith     | 2
```

**Questions:**
- How do you combine GROUP BY with ORDER BY and LIMIT?
- What if 2 users have the same order count?

---

## 📋 Checklist

Before moving to Part 3, verify you can:

- [ ] Write SELECT with WHERE filtering
- [ ] Use text and numeric comparisons in WHERE
- [ ] Use INTERVAL for date filtering
- [ ] JOIN 2-3 tables together
- [ ] Calculate derived values (total_value)
- [ ] Use LEFT JOIN to find missing data
- [ ] Use COUNT() aggregate function
- [ ] Use SUM() and AVG() functions
- [ ] GROUP BY single and multiple columns
- [ ] Use ORDER BY for sorting
- [ ] Use LIMIT to restrict results
- [ ] Combine GROUP BY, ORDER BY, and LIMIT