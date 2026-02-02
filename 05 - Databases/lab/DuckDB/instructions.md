# DuckDB Lab: Exercise Instructions

**Time:** 1.5-2 hours  
**Format:** 5 integrated sub-tasks (all in one exercise)  
**Objective:** Build a complete analytics pipeline

---

## Overview: Build an Analytics Pipeline

You're building an end-to-end data analytics system for an e-commerce platform. Your goal is to implement 5 key components that work together:

1. Load data from multiple sources (CSV files)
2. Transform and clean data (ETL)
3. Run analytical queries (BI)
4. Export results for further analysis
5. Analyze performance and trade-offs

**Sample Data:**
- 1,000 users (signup dates, countries)
- 500 products (prices, categories)
- 5,000 orders (order dates, amounts, quantities)

---

## Sub-Task 1: Data Loading

**Objective:** Load data from CSV/Parquet files

### The Challenge

You need to load data from 3 CSV files and make them queryable. Then try Parquet format to understand trade-offs.

### Hints

**Step 1: Load CSV files with auto-detected schema**

DuckDB can auto-detect column types from CSV files.

```sql
-- Auto-detect schema and load into table
CREATE TABLE users AS 
SELECT * FROM read_csv_auto('users.csv');

-- View the data
SELECT * FROM users LIMIT 5;
```

**Step 2: Load with explicit types (if needed)**

```sql
CREATE TABLE products AS 
SELECT 
    product_id,
    name,
    CAST(price AS DECIMAL(10,2)) as price,
    category
FROM read_csv('products.csv', 
    delim=',',
    header=true
);
```

**Step 3: Verify data**

```sql
SELECT COUNT(*) as total_users FROM users;
SELECT COUNT(*) as total_products FROM products;
SELECT COUNT(*) as total_orders FROM orders;
```

### Your Tasks

1. Create table from `users.csv`:
   - Columns: user_id, username, country, signup_date
   - 1,000 rows expected

2. Create table from `products.csv`:
   - Columns: product_id, name, price, category
   - 500 rows expected

3. Create table from `orders.csv`:
   - Columns: order_id, user_id, product_id, order_date, amount
   - 5,000 rows expected

4. Verify row counts for each table

5. Display first 5 rows from each table

6. (Optional) Convert orders.csv to Parquet and load

### Validation

```sql
SELECT COUNT(*) FROM users;           -- Should be 1000
SELECT COUNT(*) FROM products;        -- Should be 500
SELECT COUNT(*) FROM orders;          -- Should be 5000
SELECT * FROM users LIMIT 3;
SELECT * FROM products LIMIT 3;
```

---

## Sub-Task 2: Data Transformation

**Objective:** Clean and transform raw data (ETL)

### The Challenge

Implement data cleaning:
- Extract date parts (year, month, day)
- Categorize products by price tiers
- Handle missing data
- Create staging table with transformed data

### Hints

**Step 1: Extract date components**

```sql
SELECT 
    YEAR(signup_date) as signup_year,
    MONTH(signup_date) as signup_month,
    signup_date
FROM users
LIMIT 5;
```

**Step 2: Create price tiers (CASE WHEN)**

```sql
SELECT 
    product_id,
    name,
    price,
    CASE 
        WHEN price < 100 THEN 'Budget'
        WHEN price < 500 THEN 'Mid-range'
        WHEN price < 1000 THEN 'Premium'
        ELSE 'Ultra-premium'
    END as price_tier
FROM products;
```

**Step 3: Handle missing data (COALESCE)**

```sql
SELECT 
    user_id,
    COALESCE(username, 'Unknown') as username,
    COALESCE(country, 'Other') as country
FROM users;
```

**Step 4: Create staging table**

```sql
CREATE TABLE orders_staging AS
SELECT 
    order_id,
    user_id,
    product_id,
    order_date,
    YEAR(order_date) as order_year,
    MONTH(order_date) as order_month,
    amount
FROM orders
WHERE order_date IS NOT NULL;
```

### Your Tasks

1. Extract year and month from all signup_dates in users table

2. Add price_tier column to products:
   - Budget: < $100
   - Mid-range: $100-499
   - Premium: $500-999
   - Ultra-premium: >= $1000

3. Handle any NULL values in country (use 'Other')

4. Create staging table for orders with year/month extracted

5. Create staging table for users with year/month from signup_date

6. Verify data quality (count NULL values)

### Validation

```sql
SELECT DISTINCT YEAR(signup_date) FROM users;  -- Should show years
SELECT DISTINCT price_tier FROM products;       -- Should show 4 tiers
SELECT COUNT(*) FROM orders_staging;            -- Should be 5000
```

### Questions

- Why create a staging table instead of querying raw data?
- What other transformations might be needed?
- How would you handle duplicate records?

---

## Sub-Task 3: Analytical Queries

**Objective:** Answer business questions with SQL

### The Challenge

Write 5 complex analytical queries to extract insights:

1. **Monthly Revenue Trend** - Time-series analysis
2. **Top 10 Products** - Rank by revenue
3. **Customer Lifetime Value** - CLV analysis
4. **Cohort Analysis** - By signup month
5. **Order Distribution** - Percentiles

### Your Tasks

1. **Monthly Revenue Trend** - Show revenue by month for last 12 months

2. **Top Products** - Which 10 products generated most revenue?

3. **Top Customers** - Show top 20 customers by lifetime value

4. **Cohort Retention** - How many users from each signup month made purchases?

5. **Distribution** - What's the distribution of order values?

### Validation

```sql
-- Each query should return results
-- Monthly revenue should show trends
-- Top products should match expectations
-- CLV should show customer segments
-- Percentiles should show distribution
```

### Questions

- Which product categories are most profitable?
- Are there seasonal trends in orders?
- What's the average lifetime value?
- Which cohorts have best retention?

---

## Sub-Task 4: Pandas Export

**Objective:** Export results to Pandas DataFrames

### The Challenge

Export query results to Pandas for further analysis and statistics.

### Your Tasks

1. Export monthly revenue to DataFrame

2. Calculate statistics:
   - Mean revenue
   - Median revenue
   - Revenue growth (month-over-month)

3. Export top 20 products to CSV

4. Export cohort analysis to Parquet

5. Create visualization (optional):
   - Plot monthly revenue trend
   - Plot top products bar chart

### Validation

```python
# All exports should succeed
assert revenue_df.shape[0] > 0
assert len(revenue_df.columns) > 0

# Files should exist
import os
assert os.path.exists('monthly_revenue.csv')
```

### Questions

- Why export to Parquet instead of CSV?
- What's the file size difference?
- Which format is faster to load?

---

## Sub-Task 5: Performance Analysis

**Objective:** Benchmark and optimize

### The Challenge

Compare CSV vs Parquet performance and understand when to use each.

### Hints

**Step 1: Time CSV queries**

```python
import time
import duckdb

# Time CSV query
start = time.time()
result = duckdb.query("SELECT COUNT(*) FROM read_csv_auto('orders.csv')").fetchall()
csv_time = time.time() - start
print(f"CSV query time: {csv_time:.4f}s")
```

**Step 2: Time Parquet queries**

```python
start = time.time()
result = duckdb.query("SELECT COUNT(*) FROM read_parquet('orders.parquet')").fetchall()
parquet_time = time.time() - start
print(f"Parquet query time: {parquet_time:.4f}s")
```

**Step 3: Compare file sizes**

```python
import os
csv_size = os.path.getsize('orders.csv') / (1024 * 1024)  # MB
parquet_size = os.path.getsize('orders.parquet') / (1024 * 1024)  # MB
print(f"CSV size: {csv_size:.2f} MB")
print(f"Parquet size: {parquet_size:.2f} MB")
```

**Step 4: Complex query performance**

```python
# Run 5 different queries on CSV and Parquet
queries = [
    "SELECT COUNT(*) FROM orders",
    "SELECT SUM(amount) FROM orders",
    "SELECT * FROM orders WHERE amount > 100",
    "SELECT MONTH(order_date), SUM(amount) FROM orders GROUP BY MONTH(order_date)",
    "SELECT user_id, SUM(amount) FROM orders GROUP BY user_id"
]

for query in queries:
    # Time on CSV table
    csv_start = time.time()
    duckdb.query(f"SELECT ... FROM read_csv_auto('orders.csv')").fetchall()
    csv_time = time.time() - csv_start
    
    # Time on Parquet table
    parquet_start = time.time()
    duckdb.query(f"SELECT ... FROM read_parquet('orders.parquet')").fetchall()
    parquet_time = time.time() - parquet_start
    
    print(f"Query: {csv_time:.4f}s (CSV) vs {parquet_time:.4f}s (Parquet)")
```

### Your Tasks

1. Create `orders.parquet` from `orders.csv`

2. Benchmark simple query (COUNT(*)):
   - Time CSV version
   - Time Parquet version

3. Benchmark complex query (GROUP BY):
   - Time CSV version
   - Time Parquet version

4. Compare file sizes:
   - CSV size in MB
   - Parquet size in MB
   - Compression ratio

5. Document findings:
   - Which is faster?
   - When to use each?
   - Storage vs speed trade-offs

### Validation

```python
# Benchmark results
print(f"CSV faster by: {(parquet_time - csv_time) / parquet_time * 100:.1f}%")
print(f"Space saved: {(1 - parquet_size/csv_size) * 100:.1f}%")
```

### Questions

- Why is Parquet faster?
- When should you use CSV vs Parquet?
- What about in production?

---

## 📋 Completion Checklist

After completing all 5 sub-tasks, verify:

- [ ] Sub-Task 1: 3 tables loaded from CSV (1000, 500, 5000 rows)
- [ ] Sub-Task 2: Data cleaned and transformed
- [ ] Sub-Task 3: 5 analytical queries return results
- [ ] Sub-Task 4: Results exported to Pandas
- [ ] Sub-Task 5: Performance benchmarked

---

## Tips

- Use `.show()` to display results
- Convert to DataFrame with `.df()`
- Use `EXPLAIN` to see query plans
- Start with LIMIT 5 to check data
- Time your queries with `time.time()`

---

Good luck! 🚀

