# DuckDB Lab: Exercise Instructions


## Overview: Build an Analytics Pipeline

You're building an end-to-end data analytics system for an e-commerce platform. Your goal is to implement 5 key components that work together:

1. Load data from multiple sources (CSV files)
2. Transform and clean data (ETL)
3. Run analytical queries (BI)
4. Export results for further analysis
5. Analyze performance and trade-offs

---

## Sub-Task 1: Data Loading


### Your Tasks

1. Create table from `users.csv`:
   - Columns: user_id, username, country, signup_date

2. Create table from `products.csv`:
   - Columns: product_id, name, price, category

3. Create table from `orders.csv`:
   - Columns: order_id, user_id, product_id, order_date, amount

---

## Sub-Task 2: Data Transformation

**Objective:** Clean and transform raw data (ETL)

### Your Tasks

1. Extract year and month from all signup_dates in users table

2. Add price_tier column to products:
   - Budget: < $100
   - Mid-range: $100-499
   - Premium: $500-999
   - Ultra-premium: >= $1000

3. Handle any NULL values in country (use 'Other')

4. Create staging table for orders with year/month and price_tier

---

## Sub-Task 3: Analytical Queries

**Objective:** Answer business questions with SQL

### Your Tasks

1. **Monthly Revenue Trend** - Show revenue by month for last 12 months

2. **Top Products** - Which 10 products generated most revenue?

3. **Top Customers** - Show top 20 customers by lifetime value

5. **Distribution** - What's the distribution of order values? - show in histogram

---
