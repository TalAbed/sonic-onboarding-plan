# DuckDB Lab: Starter Code & Demo

Complete runnable Python script demonstrating all 5 sub-tasks.

---

## Quick Start

```bash
# Install dependencies
pip install duckdb pandas

# Run the demo
python demo.py
```

---

## Complete Demo Script

```python
#!/usr/bin/env python3
"""
DuckDB Lab: Complete Analytics Pipeline Demo

This script demonstrates all 5 sub-tasks:
1. Data Loading
2. Data Transformation
3. Analytical Queries
4. Pandas Export
5. Performance Analysis

Run: python demo.py
"""

import duckdb
import pandas as pd
import time
import os

# ============================================================================
# SETUP
# ============================================================================

def setup():
    """Initialize DuckDB and create sample data"""
    print("Setting up sample data...")
    
    # Create sample data if it doesn't exist
    create_sample_data()
    
    print("✓ DuckDB ready")
    return duckdb

def create_sample_data():
    """Create sample CSV files for the lab"""
    import csv
    from datetime import datetime, timedelta
    import random
    
    # Create sample-data directory
    os.makedirs('sample-data', exist_ok=True)
    
    # Generate users
    with open('sample-data/users.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['user_id', 'username', 'country', 'signup_date'])
        
        countries = ['USA', 'UK', 'Canada', 'Australia', 'Germany', 'France', 'India']
        start_date = datetime(2022, 1, 1)
        
        for i in range(1, 1001):
            country = random.choice(countries)
            signup_date = start_date + timedelta(days=random.randint(0, 730))
            writer.writerow([i, f'user_{i}', country, signup_date.date()])
    
    # Generate products
    with open('sample-data/products.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['product_id', 'name', 'price', 'category'])
        
        categories = ['Electronics', 'Clothing', 'Home', 'Sports', 'Books']
        products = [
            'iPhone 15', 'MacBook Pro', 'iPad Air', 'AirPods Pro', 'Samsung TV',
            'Laptop Stand', 'USB-C Cable', 'Monitor', 'Keyboard', 'Mouse',
            'T-Shirt', 'Jeans', 'Hoodie', 'Shoes', 'Hat',
            'Coffee Maker', 'Blender', 'Toaster', 'Microwave', 'Desk Lamp',
            'Running Shoes', 'Yoga Mat', 'Dumbbell Set', 'Bicycle', 'Tent',
            'Python Book', 'SQL Guide', 'Data Science', 'Machine Learning', 'Web Dev'
        ]
        
        for i in range(1, 501):
            name = products[i % len(products)] + f' {i}'
            price = random.uniform(10, 3000)
            category = random.choice(categories)
            writer.writerow([i, name, round(price, 2), category])
    
    # Generate orders
    with open('sample-data/orders.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['order_id', 'user_id', 'product_id', 'order_date', 'amount'])
        
        order_id = 1
        start_date = datetime(2022, 6, 1)
        
        for i in range(5000):
            user_id = random.randint(1, 1000)
            product_id = random.randint(1, 500)
            order_date = start_date + timedelta(days=random.randint(0, 580))
            amount = round(random.uniform(20, 2000), 2)
            
            writer.writerow([order_id, user_id, product_id, order_date.date(), amount])
            order_id += 1

# ============================================================================
# SUB-TASK 1: DATA LOADING
# ============================================================================

def task_1_data_loading(db):
    """Sub-Task 1: Load data from CSV files"""
    print("\n" + "=" * 70)
    print("SUB-TASK 1: Data Loading")
    print("=" * 70)
    
    # Load users
    print("\n1. Loading users.csv:")
    db.execute("CREATE TABLE users AS SELECT * FROM read_csv_auto('sample-data/users.csv')")
    user_count = db.execute("SELECT COUNT(*) FROM users").fetchall()[0][0]
    print(f"   ✓ Loaded {user_count} users")
    
    # Load products
    print("\n2. Loading products.csv:")
    db.execute("CREATE TABLE products AS SELECT * FROM read_csv_auto('sample-data/products.csv')")
    product_count = db.execute("SELECT COUNT(*) FROM products").fetchall()[0][0]
    print(f"   ✓ Loaded {product_count} products")
    
    # Load orders
    print("\n3. Loading orders.csv:")
    db.execute("CREATE TABLE orders AS SELECT * FROM read_csv_auto('sample-data/orders.csv')")
    order_count = db.execute("SELECT COUNT(*) FROM orders").fetchall()[0][0]
    print(f"   ✓ Loaded {order_count} orders")
    
    # Display samples
    print("\n4. Sample data:")
    print("\n   Users (first 2):")
    users = db.execute("SELECT * FROM users LIMIT 2").fetchdf()
    print(users.to_string(index=False))
    
    print("\n   Products (first 2):")
    products = db.execute("SELECT * FROM products LIMIT 2").fetchdf()
    print(products.to_string(index=False))
    
    print("\n   Orders (first 2):")
    orders = db.execute("SELECT * FROM orders LIMIT 2").fetchdf()
    print(orders.to_string(index=False))

# ============================================================================
# SUB-TASK 2: DATA TRANSFORMATION
# ============================================================================

def task_2_data_transformation(db):
    """Sub-Task 2: Transform and clean data"""
    print("\n" + "=" * 70)
    print("SUB-TASK 2: Data Transformation")
    print("=" * 70)
    
    # Extract date components
    print("\n1. Extracting date components from signup_date:")
    db.execute("""
        CREATE TABLE users_transformed AS
        SELECT 
            user_id,
            username,
            country,
            signup_date,
            YEAR(signup_date) as signup_year,
            MONTH(signup_date) as signup_month
        FROM users
    """)
    print("   ✓ Year and month extracted")
    
    # Add price tiers
    print("\n2. Creating price tiers for products:")
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
    
    tiers = db.execute("""
        SELECT price_tier, COUNT(*) as count 
        FROM products_transformed 
        GROUP BY price_tier
    """).fetchdf()
    print("   ✓ Price tiers created:")
    print(tiers.to_string(index=False))
    
    # Create orders staging
    print("\n3. Creating orders staging table:")
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
    
    staging_count = db.execute("SELECT COUNT(*) FROM orders_staging").fetchall()[0][0]
    print(f"   ✓ Staging table created with {staging_count} rows")

# ============================================================================
# SUB-TASK 3: ANALYTICAL QUERIES
# ============================================================================

def task_3_analytical_queries(db):
    """Sub-Task 3: Run business intelligence queries"""
    print("\n" + "=" * 70)
    print("SUB-TASK 3: Analytical Queries")
    print("=" * 70)
    
    # Query 1: Monthly Revenue
    print("\n1. MONTHLY REVENUE TREND (last 6 months):")
    monthly = db.execute("""
        SELECT 
            DATE_TRUNC('month', order_date) as month,
            COUNT(*) as orders,
            ROUND(SUM(amount), 2) as revenue,
            ROUND(AVG(amount), 2) as avg_value
        FROM orders
        GROUP BY DATE_TRUNC('month', order_date)
        ORDER BY month DESC
        LIMIT 6
    """).fetchdf()
    print(monthly.to_string(index=False))
    
    # Query 2: Top Products
    print("\n2. TOP 5 PRODUCTS BY REVENUE:")
    top_products = db.execute("""
        SELECT 
            p.name,
            p.category,
            COUNT(o.order_id) as orders,
            ROUND(SUM(o.amount), 2) as revenue
        FROM products p
        LEFT JOIN orders o ON p.product_id = o.product_id
        GROUP BY p.product_id, p.name, p.category
        ORDER BY revenue DESC NULLS LAST
        LIMIT 5
    """).fetchdf()
    print(top_products.to_string(index=False))
    
    # Query 3: Customer Lifetime Value
    print("\n3. TOP 5 CUSTOMERS BY LIFETIME VALUE:")
    clv = db.execute("""
        SELECT 
            u.username,
            u.country,
            COUNT(o.order_id) as order_count,
            ROUND(SUM(o.amount), 2) as ltv,
            ROUND(AVG(o.amount), 2) as avg_value
        FROM users u
        LEFT JOIN orders o ON u.user_id = o.user_id
        GROUP BY u.user_id, u.username, u.country
        ORDER BY ltv DESC NULLS LAST
        LIMIT 5
    """).fetchdf()
    print(clv.to_string(index=False))
    
    # Query 4: Cohort Analysis
    print("\n4. COHORT ANALYSIS (By signup month, first 4):")
    cohort = db.execute("""
        SELECT 
            DATE_TRUNC('month', u.signup_date) as cohort,
            COUNT(DISTINCT u.user_id) as users,
            COUNT(DISTINCT o.user_id) as with_orders,
            ROUND(SUM(o.amount), 2) as revenue
        FROM users u
        LEFT JOIN orders o ON u.user_id = o.user_id
        GROUP BY DATE_TRUNC('month', u.signup_date)
        ORDER BY cohort DESC
        LIMIT 4
    """).fetchdf()
    print(cohort.to_string(index=False))
    
    # Query 5: Distribution
    print("\n5. ORDER VALUE DISTRIBUTION:")
    dist = db.execute("""
        SELECT 
            ROUND(PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY amount), 2) as p25,
            ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY amount), 2) as p50,
            ROUND(PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY amount), 2) as p75,
            ROUND(AVG(amount), 2) as avg_amount,
            ROUND(MIN(amount), 2) as min_amount,
            ROUND(MAX(amount), 2) as max_amount
        FROM orders
    """).fetchdf()
    print(dist.to_string(index=False))

# ============================================================================
# SUB-TASK 4: PANDAS EXPORT
# ============================================================================

def task_4_pandas_export(db):
    """Sub-Task 4: Export to Pandas DataFrames"""
    print("\n" + "=" * 70)
    print("SUB-TASK 4: Pandas Export")
    print("=" * 70)
    
    # Export monthly revenue
    print("\n1. Exporting monthly revenue:")
    revenue_df = db.execute("""
        SELECT 
            DATE_TRUNC('month', order_date) as month,
            COUNT(*) as orders,
            ROUND(SUM(amount), 2) as revenue
        FROM orders
        GROUP BY DATE_TRUNC('month', order_date)
        ORDER BY month
    """).fetchdf()
    
    print(f"   ✓ Exported {len(revenue_df)} months")
    print(f"   Mean revenue: ${revenue_df['revenue'].mean():.2f}")
    print(f"   Median revenue: ${revenue_df['revenue'].median():.2f}")
    
    # Export top customers
    print("\n2. Exporting top 20 customers:")
    os.makedirs('output', exist_ok=True)
    
    clv_df = db.execute("""
        SELECT 
            u.username,
            u.country,
            COUNT(o.order_id) as orders,
            ROUND(SUM(o.amount), 2) as lifetime_value
        FROM users u
        LEFT JOIN orders o ON u.user_id = o.user_id
        GROUP BY u.user_id, u.username, u.country
        ORDER BY lifetime_value DESC NULLS LAST
        LIMIT 20
    """).fetchdf()
    
    clv_df.to_csv('output/top_customers.csv', index=False)
    print(f"   ✓ Exported to output/top_customers.csv")

# ============================================================================
# SUB-TASK 5: PERFORMANCE ANALYSIS
# ============================================================================

def task_5_performance_analysis(db):
    """Sub-Task 5: Benchmark and optimize"""
    print("\n" + "=" * 70)
    print("SUB-TASK 5: Performance Analysis")
    print("=" * 70)
    
    # File sizes
    print("\n1. File sizes:")
    csv_size = os.path.getsize('sample-data/orders.csv') / (1024 * 1024)
    print(f"   CSV: {csv_size:.2f} MB")
    
    # Simple query timing
    print("\n2. Query performance (COUNT):")
    start = time.time()
    result = db.execute("SELECT COUNT(*) FROM orders").fetchall()
    elapsed = time.time() - start
    print(f"   Count query: {elapsed*1000:.2f}ms")
    
    # Complex query
    print("\n3. Complex query (GROUP BY with JOIN):")
    start = time.time()
    result = db.execute("""
        SELECT p.category, COUNT(o.order_id), SUM(o.amount)
        FROM products p
        LEFT JOIN orders o ON p.product_id = o.product_id
        GROUP BY p.category
    """).fetchall()
    elapsed = time.time() - start
    print(f"   GROUP BY + JOIN: {elapsed*1000:.2f}ms")
    
    # Summary
    print("\n4. Performance characteristics:")
    print("""
       DuckDB is optimized for:
       • Analytical queries (OLAP)
       • Aggregations and JOINs
       • In-process computation
       • Ad-hoc analysis
       
       Best for:
       • Data scientists
       • Analytics
       • Reporting
       • Prototyping
    """)

# ============================================================================
# SUMMARY
# ============================================================================

def summary(db):
    """Show complete system summary"""
    print("\n" + "=" * 70)
    print("COMPLETE ANALYTICS PIPELINE SUMMARY")
    print("=" * 70)
    
    print("\n📊 DATA SOURCES:")
    user_count = db.execute("SELECT COUNT(*) FROM users").fetchall()[0][0]
    product_count = db.execute("SELECT COUNT(*) FROM products").fetchall()[0][0]
    order_count = db.execute("SELECT COUNT(*) FROM orders").fetchall()[0][0]
    
    print(f"   ✓ Users: {user_count}")
    print(f"   ✓ Products: {product_count}")
    print(f"   ✓ Orders: {order_count}")
    
    print("\n🔄 TRANSFORMATIONS:")
    print(f"   ✓ Date components extracted")
    print(f"   ✓ Price tiers created")
    print(f"   ✓ Staging tables built")
    
    print("\n📈 ANALYSIS:")
    total_revenue = db.execute("SELECT SUM(amount) FROM orders").fetchall()[0][0]
    avg_order = db.execute("SELECT AVG(amount) FROM orders").fetchall()[0][0]
    top_product = db.execute("""
        SELECT p.name FROM products p
        LEFT JOIN orders o ON p.product_id = o.product_id
        GROUP BY p.product_id, p.name
        ORDER BY SUM(o.amount) DESC LIMIT 1
    """).fetchall()[0][0]
    
    print(f"   ✓ Total revenue: ${total_revenue:,.2f}")
    print(f"   ✓ Average order: ${avg_order:.2f}")
    print(f"   ✓ Top product: {top_product}")
    
    print("\n💾 EXPORTS:")
    print(f"   ✓ Revenue to DataFrame")
    print(f"   ✓ Customers to CSV")
    
    print("\n" + "=" * 70)
    print("✅ COMPLETE ANALYTICS PIPELINE FINISHED!")
    print("=" * 70)
    print("""
You've built a production-ready analytics system:
  • Loaded data from multiple sources
  • Transformed and cleaned data
  • Extracted meaningful insights
  • Exported for further analysis
  • Analyzed performance
  
Ready for real-world analytics! 🚀
    """)

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("DUCKDB LAB: COMPLETE ANALYTICS PIPELINE")
    print("=" * 70)
    
    # Setup
    db = setup()
    
    # Run all 5 sub-tasks
    task_1_data_loading(db)
    task_2_data_transformation(db)
    task_3_analytical_queries(db)
    task_4_pandas_export(db)
    task_5_performance_analysis(db)
    
    # Show summary
    summary(db)
```

---

## How to Use

1. **Save as `demo.py`:**
   ```bash
   cp demo.py starter-code/demo.py
   ```

2. **Install dependencies:**
   ```bash
   pip install duckdb pandas
   ```

3. **Run the demo:**
   ```bash
   python demo.py
   ```

4. **Expected output:**
   - All 5 sub-tasks execute with detailed output
   - Shows queries and results
   - Displays analytics findings
   - ~400 lines of console output

---

## What This Demo Shows

✅ Data loading from multiple sources  
✅ Data transformation (ETL)  
✅ Complex analytical queries  
✅ Pandas DataFrames and export  
✅ Performance characteristics  
✅ Complete end-to-end pipeline  

---

## Customization

Students can:
- Modify query parameters
- Change time periods
- Add new analyses
- Create different visualizations
- Build custom pipelines

