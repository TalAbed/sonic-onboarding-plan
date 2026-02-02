# Exercise 2: Event Data Cleaning with Pandas

Welcome to your first real-world data engineering challenge! In this exercise, you'll load messy event data and clean it professionally.

## What You'll Do

You have a **CSV file of raw event data** from the Sonic pipeline. The data is intentionally messy (like real data!). Your job is to:

1. Load the CSV file with pandas
2. Explore and understand the data
3. Clean and validate the dataset
4. Handle missing values appropriately
5. Remove duplicates
6. Answer business questions about event patterns

## Why This Matters

**Real talk**: 80% of data engineering is data cleaning. This is the most common task you'll do.

Messy data causes:
- ❌ Incorrect analysis and wrong decisions
- ❌ System failures and bugs
- ❌ Lost trust in data quality
- ❌ Hours of debugging

Clean data enables:
- ✅ Reliable dashboards and reports
- ✅ Accurate decision-making
- ✅ Trustworthy systems
- ✅ Efficient downstream processing

This exercise teaches production-grade data cleaning patterns you'll use constantly.

## Business Context

The event data should help us understand:
- **Total event volume** - How many events processed?
- **Error rates** - What percentage failed?
- **Peak hours** - When is the system busiest?
- **Performance by event type** - Which events are slowest?
- **Data quality** - Are we missing critical information?

This is what product managers, operations teams, and engineers all need to know.

## Difficulty: Intermediate
## Concepts Covered:
- ✅ Loading CSV files with pandas
- ✅ DataFrame exploration (head, info, describe, dtypes)
- ✅ Data type conversion and validation
- ✅ Handling missing values (dropna, fillna)
- ✅ Removing duplicates
- ✅ Data quality checks
- ✅ Filtering and selection (boolean indexing)
- ✅ Basic groupby operations
- ✅ Answering questions with data

## How to Approach This

1. **Read this file** - Understand what messy data looks like
2. **Follow the instructions file** - Step-by-step without giving solutions
3. **Write your own code** - Don't peek at the solution yet
4. **Test frequently** - Print intermediate results
5. **Compare with solution file** - Learn professional patterns

## Learning Objectives

By the end of this exercise, you will:

✅ Confidently load and explore any CSV file  
✅ Identify common data quality issues  
✅ Apply industry-standard cleaning patterns  
✅ Validate that cleaned data is correct  
✅ Answer real business questions from data  
✅ Understand what "clean data" actually means  

## Data Structure

The CSV contains event data with these columns:

```
event_id       - Unique identifier (integer)
timestamp      - When it occurred (string: "YYYY-MM-DD HH:MM:SS")
event_type     - What type (string: "purchase", "login", "checkout", etc.)
user_id        - Which user (string: "user_123", "user_456", etc.)
status         - Success or failure (string: "ok", "error", "timeout")
latency_ms     - Response time (mixed: sometimes integer, sometimes string "N/A")
```

## What "Messy" Means

Real data has these problems:

```python
# Missing values
event_id,timestamp,event_type,user_id,status,latency_ms
1,2026-01-15 10:00:01,purchase,user_123,ok,120
2,2026-01-15 10:00:02,,user_456,error,        # empty event_type
3,2026-01-15 10:00:03,login,,ok,450           # empty user_id

# Type inconsistencies
4,2026-01-15 10:00:04,checkout,user_789,ok,500
5,2026-01-15 10:00:05,login,user_101,,N/A     # status missing, latency is string

# Duplicates
6,2026-01-15 10:00:06,purchase,user_202,ok,180
6,2026-01-15 10:00:06,purchase,user_202,ok,180  # exact duplicate!

# Invalid data
7,2026-01-15 10:00:07,purchase,user_303,invalid,600  # status is invalid
8,2050-01-15 10:00:08,login,user_404,ok,150          # timestamp in future!
```

Your job: Clean all this up to make it usable.

## Key Patterns You'll Learn

### Pattern 1: Load and Explore
```python
# Load CSV
df = pd.read_csv('events_raw.csv')

# Explore
df.head()           # First few rows
df.info()           # Column types and missing values
df.describe()       # Statistical summary
```

### Pattern 2: Type Conversion
```python
# Convert types
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['latency_ms'] = pd.to_numeric(df['latency_ms'], errors='coerce')
```

### Pattern 3: Handle Missing Data
```python
# Remove rows with missing critical fields
df = df.dropna(subset=['event_id', 'timestamp'])

# Fill optional fields with defaults
df['status'] = df['status'].fillna('unknown')
```

### Pattern 4: Answer Questions
```python
# Total events
total = len(df)

# Error rate
error_rate = (df['status'] == 'error').sum() / len(df)

# Average latency by event type
by_type = df.groupby('event_type')['latency_ms'].mean()
```

## Real-World Application

After this exercise, you'll:
- Validate data from external sources
- Build data pipelines that clean on load
- Debug data quality issues
- Create quality assurance checks
- Maintain data integrity over time

This is production data engineering.

## Before You Start

Make sure you have:
- ✅ Completed Exercise 1 (NumPy)
- ✅ Watched pandas video (Keith Galli - 1.5 hours)
- ✅ Read pandas Fundamentals Reference Guide
- ✅ pandas installed (`pip install pandas`)
- ✅ The file `events_raw.csv` in your exercise folder

## Tips for Success

✅ **Start with exploration** - Use head(), info(), describe() first  
✅ **Understand the problems** - Know what's wrong before fixing  
✅ **Clean systematically** - One type of issue at a time  
✅ **Validate each step** - Print counts and check data frequently  
✅ **Use reference guide** - It's there to help  
✅ **Don't just delete** - Think about whether to drop or fill  

## Ready?

1. Open [exercise-02-instructions.md](./exercise-02-instructions.md) - Follow the step-by-step guide
2. Work in PyCharm or Jupyter notebook
3. Load and explore `events_raw.csv`
4. Clean the data systematically
5. Answer the business questions
6. Compare your approach with [exercise-02-solution.md](./exercise-02-solution.md)

**Let's clean some data!** 🧹📊

