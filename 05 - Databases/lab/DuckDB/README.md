# DuckDB Lab: Essentials

## 🎯 Lab Overview

**Name:** DuckDB Analytics: End-to-End Data Pipeline

**Difficulty:** Beginner-Intermediate  
**Prerequisites:** Basic SQL (from PostgreSQL lab helpful but optional)

---

## 📚 What You'll Learn

✅ Multi-format data loading (CSV, Parquet, JSON)  
✅ ETL (Extract, Transform, Load) pipeline design  
✅ Complex analytical queries (time-series, cohorts)  
✅ Window functions and aggregates  
✅ Pandas integration for data analysis  
✅ Performance optimization and benchmarking  

---

## 🏗️ Lab Structure

**Single comprehensive exercise** with 5 integrated sub-tasks:

1. **Data Loading** - Load CSV/Parquet files into tables
2. **Data Transformation** - ETL pipeline with cleaning
3. **Analytical Queries** - 5 business intelligence queries
4. **Pandas Export** - Export to DataFrames for analysis
5. **Performance Analysis** - Benchmarking and optimization

---

## 🚀 Quick Start

### 1. Install DuckDB

```bash
pip install duckdb pandas
```

### 2. Verify Installation

```bash
python -c "import duckdb; print(duckdb.__version__)"
```

### 3. Start Lab

```bash
python
>>> import duckdb
>>> duckdb.query("SELECT 1").show()
# Should return: 1
```

---

## 📋 Exercise Overview

You'll build a **complete analytics pipeline** for an e-commerce platform:

- **Users:** 1,000 sample users (signups over 2 years)
- **Products:** 500 sample products (various categories)
- **Orders:** 5,000 sample orders (transactions)
- **Build:** Analytics system with trend analysis, customer insights, performance

---

## 🎯 Learning Path

```
Start → Sub-Task 1 → Sub-Task 2 → Sub-Task 3 → Sub-Task 4 → Sub-Task 5 → Complete!
```

---

## 📂 Lab Files

- `README.md` - This file
- `instructions/` - Exercise with 5 integrated sub-tasks (start here!)
- `solutions/` - Complete Python/SQL code
- `starter-code/demo.py` - Runnable complete demo
- `sample-data/` - CSV files (users, products, orders)

---

## ✅ How to Use This Lab

1. **Read exercise instructions** and follow them
2. **Download sample data** from `sample-data/`
3. **Try implementing** in Python with DuckDB
4. **Check solutions** if stuck

---

## 🎓 What You'll Build

By the end, you'll have:

✅ Loaded 3 data sources (CSV files)  
✅ Transformed and cleaned raw data  
✅ Written 5 complex analytical queries  
✅ Analyzed results with Pandas  
✅ Compared performance (CSV vs Parquet)  
✅ Understood when to use DuckDB vs PostgreSQL  

---

## 💡 Tips

- Start with small datasets, scale up
- Use `.show()` to visualize results
- Convert to DataFrames for further analysis
- Compare query times between CSV and Parquet
- Experiment with different aggregations

---

## 📞 Quick Reference

**Common DuckDB Commands:**
- `read_csv_auto()` - Auto-detect CSV schema
- `read_parquet()` - Load Parquet files
- `read_json()` - Load JSON files
- `CREATE TABLE AS SELECT` - Create table from query
- `SELECT ... GROUP BY` - Aggregation
- `SELECT ... OVER (...)` - Window functions
- `COPY ... TO` - Export data

---

## Ready?

Start with: `instructions/exercise-analytics-pipeline.md`

Good luck! 🚀

