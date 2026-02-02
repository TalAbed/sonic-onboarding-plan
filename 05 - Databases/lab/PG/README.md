# PostgreSQL Lab: Essentials

## 🎯 Lab Overview

**Name:** PostgreSQL Essentials: Building a Simple E-Commerce Database

**Time:** 2-3 hours  
**Difficulty:** Beginner-Intermediate  
**Prerequisites:** Basic SQL knowledge (from reference guide)

---

## 📚 What You'll Learn

✅ Create database tables with constraints  
✅ Write SELECT queries with filtering  
✅ Use JOINs to connect multiple tables  
✅ Use GROUP BY for data aggregation  
✅ Connect and query from Python  

---

## 🚀 Quick Start

### 1. **Setup Database**
```bash
psql -U postgres
CREATE DATABASE ecommerce;
\c ecommerce
```

### 2. **Run Starter Code**
```bash
psql -U postgres -d ecommerce -f starter-code/setup.sql
```

### 3. **Follow the Parts**
- Part 1: Create schema and load data (45min-1h)
- Part 2: Write queries (45min-1h)
- Part 3: Python integration (30min)

---

## 📋 Lab Structure

### **Part 1: Schema Design & Sample Data**
- Create 3 tables: users, products, orders
- Understand foreign keys and constraints
- Insert sample data (5 users, 10 products, 15 orders)

### **Part 2: Query Operations**
- Write SELECT queries with WHERE
- Use JOINs to connect tables
- Aggregate data with GROUP BY
- Sort and limit results

### **Part 3: Python Integration**
- Connect to database with psycopg2
- Execute queries from Python code
- Insert data programmatically

---

## 📂 Lab Files

- `instructions/` - start here!
- `solutions/` - Step-by-step solutions
- `starter-code/` - Database setup
- `sample-data/` - Sample data for insertion

---

## ✅ How to Use This Lab

1. **Read exercise description** in `instructions/`
2. **Try solving it** in your PostgreSQL client
3. **Check solutions** in `solutions/` if stuck
4. **Run validation** to verify your work
5. **Move to next exercise**

---

## 🎯 Learning Path

```
Start → Part 1 (Schema) → Part 2 (Queries) → Part 3 (Python) → Complete!
```

**Estimated time per section:**
- Part 1: 45 min - 1 hour
- Part 2: 45 min - 1 hour  
- Part 3: 30 minutes

---

## 💡 Tips

- Use `\d` command to view table structure
- Keep postgresql-reference.md open for syntax
- Validate each exercise before moving on

---

## 📞 Reference

Need help? Check:
- `../postgresql-reference.md` - SQL syntax
- `../README.md` - Learning resources
- `solutions/` - Complete answers

---

## Ready?

Start with: `instructions/part-1-schema.md`

Good luck! 🚀

