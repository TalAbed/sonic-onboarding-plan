# Section 5: Databases (PostgreSQL, Redis, DuckDB) - README

## 📚 Welcome to Section 5: Databases

This section teaches you three essential databases for modern Python development:
- **PostgreSQL (PG):** Relational database for structured, persistent data
- **Redis:** In-memory cache for performance optimization
- **DuckDB:** Analytical database for fast SQL queries on data

---

## 🎯 Learning Outcomes

After completing this section, you will be able to:

✅ **PostgreSQL:**
- Design and normalize database schemas
- Write complex SQL queries with joins and aggregations
- Build Python applications with SQLAlchemy ORM
- Optimize queries with indexes and explain plans
- Handle transactions and data integrity

✅ **Redis:**
- Use Redis data structures (strings, lists, sets, hashes, sorted sets)
- Implement caching patterns and improve performance
- Build session management systems
- Use Pub/Sub for real-time messaging
- Understand when and how to use caching

✅ **DuckDB:**
- Query analytical data with SQL
- Integrate with Pandas and NumPy
- Build ETL pipelines
- Handle large datasets efficiently
- Understand OLTP vs OLAP databases

✅ **Integration:**
- Build a complete data stack (PG + Redis + DuckDB)
- Create real-world data applications
- Measure and optimize performance

---

## 📖 Learning Resources

### **Part 1: PostgreSQL**

**Official Documentation:**
- [PostgreSQL Official Tutorial](https://www.postgresql.org/docs/current/tutorial.html) - Official starting point
- [PostgreSQL Tutorial Website](https://www.pgtutorial.com) - Comprehensive guide from beginner to advanced

**Best Beginner Resources:**
1. **W3Schools PostgreSQL Tutorial**
   - URL: https://www.w3schools.com/postgresql/
   - Free, interactive, perfect for basics
   - Learn by doing with exercises

2. **Neon PostgreSQL Tutorial**
   - URL: https://neon.com/postgresql/tutorial
   - Getting started guide
   - Covers all fundamental concepts
   - Modern approach with cloud examples

3. **Instaclustr PostgreSQL Tutorial**
   - URL: https://www.instaclustr.com/education/postgresql/postgresql-tutorial-get-started-with-postgresql-in-4-easy-steps/
   - Installation guide for Windows and Ubuntu
   - Step-by-step setup
   - Configuration best practices

4. **GeeksforGeeks PostgreSQL Tutorial**
   - URL: https://www.geeksforgeeks.org/postgresql/postgresql-tutorial/
   - Comprehensive coverage
   - Structured lessons
   - Code examples

**Video Tutorials (YouTube):**

1. **PostgreSQL Tutorial for Beginners (FreeCodeCamp)**
   - Duration: ~4 hours
   - Instructor: Alexandru Cristian
   - Coverage: Installation, SELECT, WHERE, GROUP BY, aggregations
   - Recommended for: Getting started quickly
   - Link: https://www.youtube.com/watch?v=SpfIwlAYaKk

2. **PostgreSQL Full Course (Derek Banas)**
   - Duration: ~3.5 hours
   - Coverage: Complete from basics to advanced (PL/pgSQL, triggers, functions)
   - Topics: Schema design, joins, views, stored procedures, triggers
   - Recommended for: Comprehensive understanding
   - Link: https://www.youtube.com/watch?v=85pG_pDkITY

3. **PostgreSQL Tutorial - Full Course Part 1**
   - Duration: ~10 hours
   - Coverage: SQL basics to advanced (CTEs, views, transactions)
   - Structured learning path
   - Link: https://www.youtube.com/watch?v=6a24yzO1-ZU

**Key Topics to Learn:**
- Basic SQL (SELECT, WHERE, GROUP BY, ORDER BY)
- Database design and normalization
- Joins (INNER, LEFT, RIGHT, FULL)
- Aggregate functions
- Indexes and query optimization
- Transactions and ACID properties
- Python integration (psycopg2, SQLAlchemy)

---

### **Part 2: Redis**

**Official Resources:**
- [Redis Official Documentation](https://redis.io/docs/getting-started/) - Official docs
- [Redis Official Blog](https://redis.io/blog/faster-redis-client-library-support-for-client-side-caching/) - Latest features

**Best Beginner Resources:**

1. **DataCamp - Python Redis: A Beginner's Guide**
   - URL: https://www.datacamp.com/tutorial/python-redis-beginner-guide
   - Practical Python examples
   - Simple and clear explanations
   - Real-world caching patterns

2. **StackAcademic - How to Implement Caching in Python**
   - URL: https://blog.stackademic.com/how-to-implement-caching-in-python-15c23e198d58
   - Covers functools.lru_cache, Redis, and Memcached
   - Practical code examples
   - Use cases and comparisons

3. **Unlocking the Power of Caching**
   - URL: https://python.plainenglish.io/unlocking-the-power-of-caching-with-python-relational-database-redis-unleashed-12925a268dfa
   - SQLite + Redis integration
   - Performance optimization patterns
   - Real-world applications

**Video Tutorials (YouTube):**

1. **Redis Crash Course (Web Dev Simplified)**
   - Duration: ~20 minutes
   - Coverage: Basics, data structures, installation, real-world project
   - Best for: Quick introduction
   - Link: https://www.youtube.com/watch?v=jgpVdJB2sKQ

2. **Redis Tutorial for Beginners (The Net Ninja)**
   - Duration: Series (refreshed 2023)
   - Coverage: Redis as primary database, Redis Cloud, Next.js integration
   - Recommended for: Learning with modern frameworks
   - Link: https://www.youtube.com/watch?v=8sHCdz_tOjk

3. **Redis Tutorial - 90 Minutes Complete Course**
   - Duration: ~1.5-2 hours
   - Coverage: Installation, data structures, persistence, Pub/Sub, practical examples
   - Recommended for: Comprehensive beginner course
   - Link: https://www.youtube.com/watch?v=01ayoMa_19o

**Key Topics to Learn:**
- Redis data structures (strings, lists, sets, hashes, sorted sets)
- Basic commands (SET, GET, LPUSH, SADD, HSET, etc.)
- Key expiration and TTL
- Caching patterns (cache-aside, write-through)
- Pub/Sub messaging
- Persistence (AOF, RDB)
- Connection pooling in Python
- Session management

---

### **Part 3: DuckDB**

**Official Resources:**
- [DuckDB Official Documentation](https://duckdb.org) - Official docs with examples
- [MotherDuck Blog](https://motherduck.com/blog/duckdb-tutorial-for-beginners/) - DuckDB tutorial for beginners

**Best Beginner Resources:**

1. **Real Python - Querying the Database**
   - URL: https://realpython.com/python-duckdb/
   - Comprehensive Python integration guide
   - SQL queries on DataFrames
   - Perfect for data scientists

2. **Analytics Engineering - DuckDB Tutorial**
   - URL: https://analyticsengineering.com/resource/duckdb-tutorial-analytics-on-your-laptop/
   - OLAP concepts explained
   - In-process vs client-server
   - Performance benefits
   - Practical analytics examples

3. **DuckDB Tutorial For Beginners (MotherDuck Blog)**
   - URL: https://motherduck.com/blog/duckdb-tutorial-for-beginners/
   - Installation and workflow
   - First analytics project
   - Cloud integration (MotherDuck)

**Video Tutorials (YouTube):**

1. **DuckDB Tutorial For Beginners In 12 min**
   - Duration: ~12 minutes
   - Coverage: Installation, CLI, extensions, first project
   - Best for: Quick introduction
   - Link: https://www.youtube.com/watch?v=ZX5FdqzGT1E

2. **DuckDB Tutorial - Full Course for Beginners** 
   - Duration: ~25 minutes
   - Coverage: Why DuckDB, setup, loading CSVs, Pandas integration, Parquet files, S3
   - Recommended for: Comprehensive beginner guide
   - Link: https://www.youtube.com/watch?v=AjsB6lM2-zw

3. **DuckDB: The In-Process OLAP Engine** 
   - Duration: ~15 minutes
   - Coverage: Architecture, performance comparisons, use cases
   - Recommended for: Understanding concepts
   - Link: https://www.youtube.com/watch?v=ywkhVosFPC0

4. **DuckDB & MotherDuck for Beginners - Ultimate Guide**
   - Duration: ~35 minutes
   - Coverage: DuckDB basics, MotherDuck cloud, S3 integration, sharing
   - Recommended for: Comprehensive with cloud features
   - Link: https://www.youtube.com/watch?v=WYV8hvJOAQE

**Key Topics to Learn:**
- OLAP vs OLTP concepts
- In-process database architecture
- SQL queries on files (CSV, Parquet)
- Integration with Pandas/NumPy
- DuckDB CLI and Python API
- Extensions (httpfs for cloud storage)
- Performance optimization
- ETL pipelines
- Window functions and analytics

---

## 🗂️ Section Structure

```
section-5-databases/
├── README.md (this file)
├── reference-guides/
│   ├── postgresql-reference.md
│   ├── redis-reference.md
│   └── duckdb-reference.md
├── labs/
│   ├── lab-1-postgresql/ (exercises for Part 1)
│   ├── lab-2-redis/ (exercises for Part 2)
│   ├── lab-3-duckdb/ (exercises for Part 3)
│   └── lab-4-integrated-project/ (combine all three)
└── resources/
    ├── sample-data/
    ├── docker-compose.yml (for easy setup)
    └── requirements.txt (Python dependencies)
```

---

## 🚀 Getting Started

### **Prerequisites**
- Section 2 (Basic Python) ✅
- Section 3 (NumPy & Pandas) ✅
- Section 4 (Advanced Patterns) ✅
- Basic SQL knowledge (helpful but not required)

### **Installation**

**Option 1: Using Docker (Recommended)**
```bash
cd section-5-databases
docker-compose up -d
# This starts PostgreSQL, Redis, and DuckDB
```

**Option 2: Manual Installation**

**PostgreSQL:**
- Windows: https://www.postgresql.org/download/windows/

**Redis:**
- Windows: https://github.com/microsoftarchive/redis/releases

**DuckDB:**
```bash
pip install duckdb
```

**Python Packages:**
```bash
pip install -r requirements.txt
# Includes: psycopg2, redis, duckdb, sqlalchemy, pandas
```

---

## 🎯 Comparison: When to Use Each

### **PostgreSQL**
✅ When you need: Persistent, structured, relational data  
✅ Use for: Main application databases, complex relationships  
✅ Examples: User data, orders, products, relationships  
✅ Not for: Real-time caching, analytical queries only  

### **Redis**
✅ When you need: Fast, in-memory, frequently accessed data  
✅ Use for: Caching, sessions, real-time features  
✅ Examples: User sessions, cache, leaderboards, Pub/Sub  
✅ Not for: Persistent primary storage, complex queries  

### **DuckDB**
✅ When you need: Fast analytical queries on large datasets  
✅ Use for: Data analysis, reporting, ETL pipelines  
✅ Examples: Analytics, reporting, data exploration  
✅ Not for: Real-time transactions, small datasets (overhead)  

---

## 📋 Quick Command Reference

### **PostgreSQL Quick Start**
```bash
# Connect to PostgreSQL
psql -U postgres -d your_database

# Create database
CREATE DATABASE my_app;

# Create table
CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(100));

# Insert data
INSERT INTO users (name) VALUES ('John');

# Query data
SELECT * FROM users;
```

### **Redis Quick Start**
```bash
# Connect to Redis
redis-cli

# Basic commands
SET key value
GET key
LPUSH mylist item1
SADD myset member1

# Check keys
KEYS *

# Set expiration
EXPIRE key 3600
```

### **DuckDB Quick Start**
```python
import duckdb

# Connect to DuckDB
conn = duckdb.connect('my_database.duckdb')

# Query CSV file
result = conn.execute("SELECT * FROM read_csv_auto('data.csv')").fetchdf()

# Query Pandas DataFrame
df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [30, 25]})
result = conn.execute("SELECT * FROM df WHERE age > 25").fetchdf()
```

---

## 💡 Tips for Success

1. **Install Everything Early** - Set up all three databases before starting labs
2. **Follow the Order** - PostgreSQL → Redis → DuckDB (builds complexity)
3. **Use Docker** - Easier than manual installation
4. **Read the Docs** - Official documentation is your best friend
5. **Practice Queries** - Spend time writing and testing queries
6. **Real Data** - Use realistic data in your exercises
7. **Performance Matters** - Always measure before and after caching/optimization
8. **Build the Project** - The integrated project ties everything together

---

## Support & Resources

**Stuck?**
1. Check the reference guides first
2. Review the resource links
3. Watch the video tutorials again
4. Try the hands-on exercises

**Need More?**
- PostgreSQL: https://www.postgresql.org/docs/
- Redis: https://redis.io/docs/
- DuckDB: https://duckdb.org/docs/

---

## Happy learning! 🚀