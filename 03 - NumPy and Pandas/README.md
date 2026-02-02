# NumPy & Pandas Fundamentals

Welcome to the NumPy and pandas section of the Sonic DE team's onboarding program! These two libraries are the cornerstone of data manipulation in Python and are essential for modern data engineering.

## What Are NumPy and Pandas?

**NumPy** (Numerical Python) is a library for numerical computing. It provides:
- Powerful multi-dimensional arrays
- High-performance mathematical operations
- Vectorized computation (fast operations on entire arrays)
- Foundation for almost all scientific computing in Python

**pandas** is a library for data manipulation and analysis. It provides:
- DataFrames (tabular data like Excel spreadsheets)
- Series (one-dimensional labeled data)
- Tools for cleaning, filtering, and transforming data
- Integration with file formats (CSV, Excel, SQL, Parquet)
- Advanced operations like grouping, merging, and pivoting

### Why Both Matter

NumPy is the **mathematical foundation** - you work with numbers and arrays.  
pandas is the **practical tool** - you work with real-world data in tabular format.

In Sonic specifically, you'll use:
- **NumPy**: Processing numerical metrics, calculations, transformations
- **pandas**: Loading event data, cleaning pipelines, aggregating statistics

---

## Why This Matters for Data Engineering

Data engineering is fundamentally about **moving and transforming data at scale**. NumPy and pandas are how you:
- Load data from files and databases
- Clean and validate data quality
- Filter and transform events
- Compute statistics and aggregations
- Prepare data for downstream systems
- Debug data pipeline issues

Without these skills, you'd be manually processing data with loops and conditionals—much slower and error-prone.

---

## Your Learning Path

This module takes you from zero NumPy/pandas knowledge to practical proficiency. Follow these steps in order:

### Step 1: Watch the NumPy Video

Start with a focused introduction to NumPy:

**Video**: [Learn NumPy in 1 Hour](https://www.youtube.com/watch?v=VXU4LSAQDSc)  
*Duration*: ~1 hour  
*By*: Bro Code

This video covers:
- What NumPy is and why it matters
- Creating arrays (1D, 2D, 3D)
- Array attributes and data types
- Indexing and slicing
- Arithmetic operations
- Broadcasting
- Aggregate functions (sum, mean, max, etc.)
- Filtering and boolean indexing
- Random number generation

> **Tip**: This is a dense 1 hour. Pause frequently to understand concepts. NumPy is powerful but requires careful learning.

---

### Step 2: Watch the pandas Video

Build on NumPy fundamentals with practical data manipulation:

**Video**: [Complete Pandas Tutorial](https://www.youtube.com/watch?v=2uvysYbKdjM)  
*Duration*: ~1.5 hours  
*By*: Keith Galli (Recently Updated)

This video covers:
- What pandas is and why it matters
- Series and DataFrames
- Loading data (CSV, Excel, Parquet)
- Accessing data (.head, .tail, .loc, .iloc, .at, .iat)
- Filtering and selecting subsets
- String operations
- DateTime operations
- Adding and removing columns
- Merging and concatenating datasets
- Handling missing values
- Grouping and aggregation
- Pivot tables
- Advanced operations (shift, rank, rolling, cumsum)
- Pandas 2.0 new features

> **Tip**: This video covers a lot of ground. Focus on the fundamentals first (Series, DataFrames, loading). Don't worry about advanced features yet.

---

### Step 3: Practice with 100 Pandas Puzzles

Reinforce your pandas knowledge with structured, progressive challenges:

**Resource**: [100 Pandas Puzzles Repository](https://github.com/ajcr/100-pandas-puzzles)  
*Format*: Jupyter Notebooks  
*Difficulty*: Easy → Medium → Hard

**How to use**:
1. Clone the repository: `git clone https://github.com/ajcr/100-pandas-puzzles.git`
2. Start Jupyter: `jupyter notebook`
3. Open `puzzles.ipynb` (blank version)
4. Work through puzzles from Easy section to the Hard section. We trust you to know how to progress at a pace that is right for you.
5. Compare your answers with `puzzles-solutions.ipynb`

**What you'll learn**:
- Real-world data scenarios
- Different ways to solve the same problem
- Common pandas patterns and idioms
- Data transformation workflows

> **Recommendation**: Complete at least 15-20 puzzles from different sections. These reinforce fundamentals and build confidence.

---

### Step 4: Practice NumPy with Curated Exercises

Strengthen your NumPy skills with well-organized exercises:

**Resource**: [PyNative - 50 NumPy Exercises](https://pynative.com/python-numpy-exercise/)  
*Format*: Web-based  
*Difficulty*: Beginner to Advanced

**How to use**:
1. Visit the website
2. Start with beginner exercises
3. Work through each section
4. Check your solutions against provided answers

**What you'll learn**:
- Array creation and manipulation
- Mathematical operations
- Indexing and slicing patterns
- Real-world NumPy applications

> **Recommendation**: Complete at least 15-20 puzzles from different sections. These reinforce fundamentals and build confidence.

---

### Step 5: Complete the Sonic NumPy/Pandas Lab

Apply your skills to realistic data engineering scenarios:

The lab includes practical exercises that simulate real DE work:
- Processing event data with NumPy
- Loading and exploring datasets with pandas
- Data cleaning and validation
- Aggregation and analysis

---

## Key Concepts You'll Learn

By the end of this module, you should understand:

✅ **NumPy Arrays**: Multi-dimensional arrays, dtypes, shape, and indexing  
✅ **Array Operations**: Vectorized math, broadcasting, ufuncs  
✅ **pandas Series**: One-dimensional labeled data  
✅ **pandas DataFrames**: Tabular data structure  
✅ **Data Loading**: Reading CSV, Excel, and other formats  
✅ **Data Selection**: .loc, .iloc, boolean indexing  
✅ **Data Cleaning**: Handling missing values, duplicates  
✅ **Data Transformation**: Adding columns, string operations, datetime  
✅ **Aggregation**: GroupBy, pivot tables, statistics  
✅ **Data Combination**: Merging, concatenating datasets  

---

## Learning Resources Summary

| Resource | Type | Time | Purpose |
|----------|------|------|---------|
| Bro Code NumPy Video | Video | 1 hour | Foundational understanding |
| Keith Galli Pandas Video | Video | 1.5 hours | Practical pandas skills |
| 100 Pandas Puzzles | Practice | 2-3 hours | Reinforce pandas patterns |
| PyNative NumPy Exercises | Practice | 1-2 hours | Strengthen NumPy skills |
| Sonic NumPy/Pandas Lab | Lab | 1-2 hours | Apply real-world scenarios |
| **TOTAL** | | **6-8 hours** | Mastery of both libraries |

---

## Prerequisites

- ✅ Completed Python Fundamentals (Exercises 1-4)
- ✅ Understand loops, functions, and basic data structures
- ✅ Comfortable writing and running Python files
- ⚠️ No prior NumPy/pandas experience required!

---

## Important Notes

### NumPy vs pandas

**Use NumPy when**:
- Working with pure numerical data
- Performing mathematical operations
- Need maximum performance
- Working with multi-dimensional data

**Use pandas when**:
- Working with real datasets (CSV, Excel, databases)
- Need to combine multiple data sources
- Cleaning and transforming data
- Need labeled rows and columns

**Most real work**: You use both together. NumPy under the hood, pandas at the surface.

### Common Beginner Mistakes

❌ **Don't**: Try to memorize all functions  
✅ **Do**: Learn the core patterns and look up specifics when needed

❌ **Don't**: Skip the practice puzzles and jump to advanced topics  
✅ **Do**: Work through puzzles progressively to build intuition

❌ **Don't**: Use pandas for simple numerical arrays  
✅ **Do**: Use NumPy for arrays, pandas for tabular data

❌ **Don't**: Ignore data types and dtypes  
✅ **Do**: Pay attention to data types—they affect performance and correctness

---

## After You Finish This Module

Once you've watched videos, practiced puzzles, and completed the lab:

1. **You'll understand** NumPy and pandas fundamentals deeply
2. **You'll be comfortable** loading, cleaning, and transforming data
3. **You'll recognize** common data patterns and how to handle them
4. **You'll have tools** to explore and understand any dataset

---

## Important: Practice is Everything

These libraries are **best learned by doing**. Watching videos teaches you what's possible. Puzzles teach you how to apply it. Only practice builds real skill.

Don't just watch—code along with videos. Don't just read puzzles—solve them yourself before looking at solutions.

---

## Learning Mindset

NumPy and pandas are powerful tools with **many ways to accomplish the same task**. Your goal isn't to find the "right" way—it's to:
- Understand the fundamentals
- Write code that works
- Learn better approaches over time
- Build intuition for data

The pandas documentation says: "There may be multiple ways to do the same thing." That's not a bug—it's a feature. It means flexibility.

---

## Next Steps

Ready to dive in? Here's your start:

1. ✅ Watch the [NumPy video](https://www.youtube.com/watch?v=VXU4LSAQDSc) (1 hour)
2. ✅ Watch the [pandas video](https://www.youtube.com/watch?v=2uvysYbKdjM) (1.5 hours)
3. ✅ Clone and start [100 Pandas Puzzles](https://github.com/ajcr/100-pandas-puzzles)
4. ✅ Work through [PyNative NumPy Exercises](https://pynative.com/python-numpy-exercise/)
5. ✅ Move to the Sonic NumPy/Pandas Lab

---

**You're about to learn the most practical tools in data engineering.** NumPy and pandas are in your future—let's master them! 🚀📊

Good luck, and welcome to the world of data transformation! 🐍
