# DuckDB Lab: Complete Solutions

This file contains complete Python/SQL implementations for all 5 sub-tasks.

---

## Sub-Task 1: Data Loading Solution

```python
import duckdb
import pandas as pd

# Initialize DuckDB connection (in-memory database)
db = duckdb.sql

# Sub-Task 1: Data Loading
print("=" * 70)
print("SUB-TASK 1: Data Loading")
print("=" * 70)

# Load users table
print("\n1. Loading users.csv:")
db.execute("CREATE TABLE users AS SELECT * FROM read_csv_auto('sample-data/users.csv')")
user_count = db.execute("SELECT COUNT(*) as count FROM users").fetchall()[0][0]
print(f"   ✓ Loaded {user_count} users")

# Load products table
print("\n2. Loading products.csv:")
db.execute("CREATE TABLE products AS SELECT * FROM read_csv_auto('sample-data/products.csv')")
product_count = db.execute("SELECT COUNT(*) as count FROM products").fetchall()[0][0]
print(f"   ✓ Loaded {product_count} products")

# Load orders table
print("\n3. Loading orders.csv:")
db.execute("CREATE TABLE orders AS SELECT * FROM read_csv_auto('sample-data/orders.csv')")
order_count = db.execute("SELECT COUNT(*) as count FROM orders").fetchall()[0][0]
print(f"   ✓ Loaded {order_count} orders")

# Verify with explicit types (example)
print("\n4. Loading products with explicit types:")
db.execute("""
    CREATE TABLE products_typed AS 
    SELECT 
        product_id,
        name,
        CAST(price AS DECIMAL(10,2)) as price,
        category
    FROM read_csv_auto('sample-data/products.csv')
""")
print("   ✓ Loaded with explicit type casting")

# Display sample data
print("\n5. Sample data from each table:")
print("\n   USERS (first 3):")
users_sample = db.execute("SELECT * FROM users LIMIT 3").fetchdf()
print(users_sample.to_string())

print("\n   PRODUCTS (first 3):")
products_sample = db.execute("SELECT * FROM products LIMIT 3").fetchdf()
print(products_sample.to_string())

print("\n   ORDERS (first 3):")
orders_sample = db.execute("SELECT * FROM orders LIMIT 3").fetchdf()
print(orders_sample.to_string())

# Verify row counts
print("\n6. Row count verification:")
counts = db.execute("""
    SELECT 
        'users' as table_name, COUNT(*) as count FROM users
    UNION ALL
    SELECT 
        'products' as table_name, COUNT(*) as count FROM products
    UNION ALL
    SELECT 
        'orders' as table_name, COUNT(*) as count FROM orders
""").fetchdf()
print(counts.to_string())
```

---

## Sub-Task 2: Data Transformation Solution

```python
# Sub-Task 2: Data Transformation
print("\n" + "=" * 70)
print("SUB-TASK 2: Data Transformation")
print("=" * 70)

# Extract date components from users
print("\n1. Extracting date components from signup_date:")
db.execute("""
    CREATE TABLE users_transformed AS
    SELECT 
        user_id,
        username,
        country,
        signup_date,
        YEAR(signup_date) as signup_year,
        MONTH(signup_date) as signup_month,
        DAY(signup_date) as signup_day
    FROM users
""")
user_dates = db.execute("""
    SELECT DISTINCT signup_year, signup_month FROM users_transformed 
    ORDER BY signup_year, signup_month
""").fetchdf()
print("   ✓ Date components extracted")
print(f"   Years: {user_dates['signup_year'].unique()}")
print(f"   Months: {user_dates['signup_month'].unique()}")

# Add price tiers to products
print("\n2. Categorizing products by price tier:")
db.execute("""
    CREATE TABLE products_transformed AS
    SELECT 
        product_id,
        name,
        price,
        category,
        CASE 
            WHEN price < 100 THEN 'Budget'
            WHEN price < 500 THEN 'Mid-range'
            WHEN price < 1000 THEN 'Premium'
            ELSE 'Ultra-premium'
        END as price_tier
    FROM products
""")
price_tiers = db.execute("""
    SELECT price_tier, COUNT(*) as count 
    FROM products_transformed 
    GROUP BY price_tier 
    ORDER BY price_tier
""").fetchdf()
print("   ✓ Price tiers added")
print(price_tiers.to_string())

# Handle NULL values
print("\n3. Handling NULL values:")
null_counts = db.execute("""
    SELECT 
        COUNT(*) - COUNT(country) as null_countries,
        COUNT(*) as total_rows
    FROM users
""").fetchdf()
print(f"   NULL countries: {null_counts['null_countries'].values[0]}")

db.execute("""
    CREATE TABLE users_clean AS
    SELECT 
        user_id,
        username,
        COALESCE(country, 'Other') as country,
        signup_date
    FROM users
""")
print("   ✓ NULL values handled with COALESCE")

# Create orders staging table
print("\n4. Creating orders staging table:")
db.execute("""
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
    WHERE order_date IS NOT NULL
""")
staging_count = db.execute("SELECT COUNT(*) as count FROM orders_staging").fetchall()[0][0]
print(f"   ✓ Staging table created with {staging_count} rows")

# Data quality check
print("\n5. Data quality check:")
quality_check = db.execute("""
    SELECT 
        COUNT(*) as total_rows,
        COUNT(DISTINCT user_id) as unique_users,
        COUNT(DISTINCT product_id) as unique_products,
        MIN(order_date) as earliest_order,
        MAX(order_date) as latest_order
    FROM orders
""").fetchdf()
print(quality_check.to_string())
```

---

## Sub-Task 3: Analytical Queries Solution

```python
# Sub-Task 3: Analytical Queries
print("\n" + "=" * 70)
print("SUB-TASK 3: Analytical Queries")
print("=" * 70)

# Query 1: Monthly Revenue Trend
print("\n1. MONTHLY REVENUE TREND:")
monthly_revenue = db.execute("""
    SELECT 
        DATE_TRUNC('month', order_date) as month,
        COUNT(*) as total_orders,
        SUM(amount) as revenue,
        AVG(amount) as avg_order_value,
        MAX(amount) as max_order_value
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
    ORDER BY month DESC
    LIMIT 12
""").fetchdf()
print(monthly_revenue.to_string())

# Query 2: Top 10 Products
print("\n2. TOP 10 PRODUCTS BY REVENUE:")
top_products = db.execute("""
    SELECT 
        p.product_id,
        p.name,
        p.category,
        COUNT(o.order_id) as order_count,
        SUM(o.amount) as total_revenue,
        AVG(o.amount) as avg_order_value
    FROM products p
    LEFT JOIN orders o ON p.product_id = o.product_id
    GROUP BY p.product_id, p.name, p.category
    ORDER BY total_revenue DESC NULLS LAST
    LIMIT 10
""").fetchdf()
print(top_products.to_string())

# Query 3: Customer Lifetime Value
print("\n3. TOP 20 CUSTOMERS BY LIFETIME VALUE:")
top_customers = db.execute("""
    SELECT 
        u.user_id,
        u.username,
        COUNT(o.order_id) as order_count,
        SUM(o.amount) as lifetime_value,
        AVG(o.amount) as avg_order_value,
        MIN(o.order_date) as first_order,
        MAX(o.order_date) as last_order,
        DATEDIFF('day', MIN(o.order_date), MAX(o.order_date)) as days_active
    FROM users u
    LEFT JOIN orders o ON u.user_id = o.user_id
    GROUP BY u.user_id, u.username
    ORDER BY lifetime_value DESC NULLS LAST
    LIMIT 20
""").fetchdf()
print(top_customers.to_string())

# Query 4: Cohort Analysis
print("\n4. COHORT ANALYSIS (By Signup Month):")
cohort_analysis = db.execute("""
    SELECT 
        DATE_TRUNC('month', u.signup_date) as signup_cohort,
        COUNT(DISTINCT u.user_id) as cohort_size,
        COUNT(DISTINCT o.user_id) as users_with_orders,
        COUNT(o.order_id) as total_orders,
        SUM(o.amount) as cohort_revenue,
        ROUND(100.0 * COUNT(DISTINCT o.user_id) / NULLIF(COUNT(DISTINCT u.user_id), 0), 2) as conversion_pct
    FROM users u
    LEFT JOIN orders o ON u.user_id = o.user_id
    GROUP BY DATE_TRUNC('month', u.signup_date)
    ORDER BY signup_cohort DESC
""").fetchdf()
print(cohort_analysis.to_string())

# Query 5: Order Distribution (Percentiles)
print("\n5. ORDER VALUE DISTRIBUTION (Percentiles):")
distribution = db.execute("""
    SELECT 
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY amount) as p25,
        PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY amount) as p50_median,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY amount) as p75,
        PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY amount) as p90,
        PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY amount) as p99,
        MIN(amount) as min_amount,
        MAX(amount) as max_amount,
        AVG(amount) as avg_amount,
        STDDEV(amount) as std_dev
    FROM orders
""").fetchdf()
print(distribution.to_string())
```

---

## Sub-Task 4: Pandas Export Solution

```python
# Sub-Task 4: Pandas Export
print("\n" + "=" * 70)
print("SUB-TASK 4: Pandas Export")
print("=" * 70)

# Export monthly revenue to DataFrame
print("\n1. Exporting monthly revenue to DataFrame:")
revenue_df = db.execute("""
    SELECT 
        DATE_TRUNC('month', order_date) as month,
        COUNT(*) as total_orders,
        SUM(amount) as revenue
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
    ORDER BY month
""").fetchdf()
print(f"   ✓ Exported {len(revenue_df)} months of data")

# Statistics
print("\n2. Revenue statistics:")
stats = {
    'Mean': revenue_df['revenue'].mean(),
    'Median': revenue_df['revenue'].median(),
    'Std Dev': revenue_df['revenue'].std(),
    'Min': revenue_df['revenue'].min(),
    'Max': revenue_df['revenue'].max(),
}
for stat_name, stat_value in stats.items():
    print(f"   {stat_name}: ${stat_value:,.2f}")

# Month-over-month growth
print("\n3. Month-over-month growth:")
revenue_df['revenue_growth_pct'] = revenue_df['revenue'].pct_change() * 100
growth_summary = revenue_df[['month', 'revenue', 'revenue_growth_pct']].tail(6)
print(growth_summary.to_string())

# Export top products to CSV
print("\n4. Exporting top 20 products to CSV:")
top_products_df = db.execute("""
    SELECT 
        p.product_id,
        p.name,
        p.category,
        COUNT(o.order_id) as order_count,
        SUM(o.amount) as total_revenue
    FROM products p
    LEFT JOIN orders o ON p.product_id = o.product_id
    GROUP BY p.product_id, p.name, p.category
    ORDER BY total_revenue DESC NULLS LAST
    LIMIT 20
""").fetchdf()
top_products_df.to_csv('output/top_products.csv', index=False)
print(f"   ✓ Exported to output/top_products.csv")

# Export cohort analysis to Parquet
print("\n5. Exporting cohort analysis to Parquet:")
cohort_df = db.execute("""
    SELECT 
        DATE_TRUNC('month', u.signup_date) as signup_cohort,
        COUNT(DISTINCT u.user_id) as cohort_size,
        COUNT(DISTINCT o.user_id) as users_with_orders,
        SUM(o.amount) as cohort_revenue
    FROM users u
    LEFT JOIN orders o ON u.user_id = o.user_id
    GROUP BY DATE_TRUNC('month', u.signup_date)
    ORDER BY signup_cohort DESC
""").fetchdf()
cohort_df.to_parquet('output/cohort_analysis.parquet')
print(f"   ✓ Exported to output/cohort_analysis.parquet")

# Export CLV with user info
print("\n6. Exporting customer lifetime value:")
clv_df = db.execute("""
    SELECT 
        u.user_id,
        u.username,
        u.country,
        COUNT(o.order_id) as order_count,
        SUM(o.amount) as lifetime_value,
        AVG(o.amount) as avg_order_value
    FROM users u
    LEFT JOIN orders o ON u.user_id = o.user_id
    GROUP BY u.user_id, u.username, u.country
    ORDER BY lifetime_value DESC NULLS LAST
    LIMIT 100
""").fetchdf()
clv_df.to_csv('output/top_customers.csv', index=False)
print(f"   ✓ Exported top 100 customers to CSV")
```

---

## Sub-Task 5: Performance Analysis Solution

```python
import time
import os

# Sub-Task 5: Performance Analysis
print("\n" + "=" * 70)
print("SUB-TASK 5: Performance Analysis")
print("=" * 70)

# Convert CSV to Parquet for comparison
print("\n1. Converting orders.csv to Parquet:")
db.execute("""
    COPY (SELECT * FROM read_csv_auto('sample-data/orders.csv')) 
    TO 'sample-data/orders.parquet' (FORMAT PARQUET)
""")
print("   ✓ Converted to Parquet format")

# File size comparison
print("\n2. File size comparison:")
csv_file = 'sample-data/orders.csv'
parquet_file = 'sample-data/orders.parquet'

csv_size = os.path.getsize(csv_file) / (1024 * 1024)
parquet_size = os.path.getsize(parquet_file) / (1024 * 1024)
compression_ratio = (1 - parquet_size / csv_size) * 100

print(f"   CSV size: {csv_size:.2f} MB")
print(f"   Parquet size: {parquet_size:.2f} MB")
print(f"   Compression: {compression_ratio:.1f}%")

# Simple query benchmark
print("\n3. Simple query benchmark (COUNT):")
queries = {
    "CSV": "SELECT COUNT(*) FROM read_csv_auto('sample-data/orders.csv')",
    "Parquet": "SELECT COUNT(*) FROM read_parquet('sample-data/orders.parquet')"
}

for source, query in queries.items():
    times = []
    for i in range(3):
        start = time.time()
        result = db.execute(query).fetchall()
        elapsed = time.time() - start
        times.append(elapsed)
    
    avg_time = sum(times) / len(times)
    print(f"   {source}: {avg_time*1000:.2f}ms (avg of 3 runs)")

# Complex query benchmark
print("\n4. Complex query benchmark (GROUP BY):")
csv_query = """
    SELECT MONTH(order_date), SUM(amount), COUNT(*) 
    FROM read_csv_auto('sample-data/orders.csv')
    GROUP BY MONTH(order_date)
"""
parquet_query = """
    SELECT MONTH(order_date), SUM(amount), COUNT(*) 
    FROM read_parquet('sample-data/orders.parquet')
    GROUP BY MONTH(order_date)
"""

for name, query in [("CSV", csv_query), ("Parquet", parquet_query)]:
    times = []
    for i in range(3):
        start = time.time()
        result = db.execute(query).fetchall()
        elapsed = time.time() - start
        times.append(elapsed)
    
    avg_time = sum(times) / len(times)
    print(f"   {name}: {avg_time*1000:.2f}ms (avg of 3 runs)")

# Full table scan
print("\n5. Full table scan benchmark:")
for name, query in [("CSV", "SELECT SUM(amount) FROM read_csv_auto('sample-data/orders.csv')"),
                     ("Parquet", "SELECT SUM(amount) FROM read_parquet('sample-data/orders.parquet')")]:
    times = []
    for i in range(3):
        start = time.time()
        result = db.execute(query).fetchall()
        elapsed = time.time() - start
        times.append(elapsed)
    
    avg_time = sum(times) / len(times)
    print(f"   {name}: {avg_time*1000:.2f}ms (avg of 3 runs)")

# Summary and recommendations
print("\n6. Performance Summary & Recommendations:")
print("""
   CSV Advantages:
   • Universal format, compatible with all tools
   • Human-readable, easy to inspect
   • Good for one-time analysis
   
   Parquet Advantages:
   • Faster queries (columnar format)
   • Smaller file size (compression)
   • Better for large datasets
   • Best for repeated analysis
   
   Recommendations:
   • Use CSV for data import/export
   • Use Parquet for data storage
   • Use DuckDB for ad-hoc analysis
   • Use PostgreSQL for operational data
""")
```

---

## Complete Integration Test

```python
# Integration Summary
print("\n" + "=" * 70)
print("COMPLETE ANALYTICS PIPELINE SUMMARY")
print("=" * 70)

print("\n📊 DATA SOURCES:")
print(f"   ✓ Users: {db.execute('SELECT COUNT(*) FROM users').fetchall()[0][0]} records")
print(f"   ✓ Products: {db.execute('SELECT COUNT(*) FROM products').fetchall()[0][0]} records")
print(f"   ✓ Orders: {db.execute('SELECT COUNT(*) FROM orders').fetchall()[0][0]} records")

print("\n🔄 TRANSFORMATIONS:")
print(f"   ✓ Date components extracted")
print(f"   ✓ Price tiers created (4 categories)")
print(f"   ✓ NULL values handled")
print(f"   ✓ Staging tables created")

print("\n📈 ANALYSIS:")
print(f"   ✓ Monthly revenue trends")
print(f"   ✓ Top 10 products identified")
print(f"   ✓ Customer lifetime value calculated")
print(f"   ✓ Cohort analysis completed")
print(f"   ✓ Distribution percentiles computed")

print("\n💾 EXPORTS:")
print(f"   ✓ Revenue to DataFrame")
print(f"   ✓ Top products to CSV")
print(f"   ✓ Cohort data to Parquet")
print(f"   ✓ CLV to CSV")

print("\n⚡ PERFORMANCE:")
print(f"   ✓ CSV vs Parquet benchmarked")
print(f"   ✓ File sizes compared")
print(f"   ✓ Query times measured")
print(f"   ✓ Compression ratio calculated")

print("\n" + "=" * 70)
print("✅ COMPLETE ANALYTICS PIPELINE FINISHED!")
print("=" * 70)
print("""
You've built a production-ready analytics system:
  • Loaded data from multiple sources
  • Cleaned and transformed data
  • Extracted meaningful insights
  • Exported for further analysis
  • Optimized performance
  
Ready for real-world analytics! 🚀
""")
```

---

## Running This Solution

```bash
# Save as duckdb_lab_solution.py
python duckdb_lab_solution.py

# Should execute all 5 sub-tasks
# Output: 500+ lines of analytics results
```

---

## Key Concepts Demonstrated

✅ **Data Loading:** Multi-format (CSV, Parquet)  
✅ **Transformation:** Date extraction, categorization, cleaning  
✅ **SQL Queries:** Aggregates, JOINs, window functions, percentiles  
✅ **Time-Series:** Monthly trends, cohort analysis  
✅ **Pandas:** DataFrame export, statistics  
✅ **Performance:** Benchmarking, optimization  
✅ **Trade-offs:** CSV vs Parquet, DuckDB vs PostgreSQL  

