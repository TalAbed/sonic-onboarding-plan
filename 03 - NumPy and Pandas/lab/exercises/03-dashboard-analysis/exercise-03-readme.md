# Exercise 3: Advanced Pandas - Merging & Feature Engineering

Welcome to the final exercise! You'll combine data from multiple sources and create insights through feature engineering.

## What You'll Do

You have **three datasets**:
1. Cleaned events data (from Exercise 2)
2. User profile information (who are the users?)
3. System performance data (overall system health)

Your job is to:

1. Load all three CSV files
2. Merge datasets intelligently
3. Create derived features (feature engineering)
4. Answer complex business questions
5. Build an analysis that combines multiple data sources

## Why This Matters

**This is what real data engineering looks like.** In production:
- Data lives in multiple tables/systems
- You must join them correctly
- Creating good features drives business value
- Complex analysis requires combining many sources

This exercise teaches the final piece: turning raw data into insights at scale.

## Difficulty: Intermediate-Advanced

## Concepts Covered:
- ✅ Loading multiple CSVs
- ✅ Merging DataFrames (inner, left, right joins)
- ✅ Understanding join behavior and data loss
- ✅ Feature engineering (creating new columns)
- ✅ Aggregation and groupby operations
- ✅ Pivot tables for reshaping data
- ✅ Handling merge conflicts and duplicates
- ✅ Building analysis pipelines
- ✅ Telling stories with data

## How to Approach This

1. **Read this file completely** - Understand the data relationships
2. **Follow instructions file** - Step-by-step guide
3. **Write your own code** - Build the analysis from scratch
4. **Test frequently** - Print intermediate results
5. **Compare with solution file** - Learn professional patterns

## Learning Objectives

By the end of this exercise, you will:

✅ Confidently merge multiple data sources  
✅ Understand join types and their impacts  
✅ Create meaningful features from raw data  
✅ Build analysis pipelines that combine multiple operations  
✅ Extract business value from complex datasets  
✅ Think like a data engineer working with production systems  

## Data Structure

### Dataset 1: events_cleaned.csv
```
event_id, timestamp, event_type, user_id, status, latency_ms
(from Exercise 2—cleaned event data)
```

### Dataset 2: users.csv
```
user_id, name, region, signup_date, account_type, email
(static user information)
```

### Dataset 3: system_metrics.csv
```
timestamp, cpu_usage, memory_usage, error_rate, events_per_second
(system-wide performance snapshots)
```

## Key Concepts

### Joining Data

Real data lives in multiple tables. You'll learn:

```python
# Left join: Keep all rows from left, add matching data from right
merged = df_left.merge(df_right, on='user_id', how='left')

# Inner join: Keep only matching rows
merged = df_left.merge(df_right, on='user_id', how='inner')

# Left join with multiple keys
merged = events.merge(users, on='user_id', how='left')
```

### Feature Engineering

Creating new columns that tell stories:

```python
# Categorize users
df['user_tier'] = df['total_events'].apply(
    lambda x: 'power' if x > 100 else 'regular'
)

# Calculate user metrics
df['error_rate_by_user'] = df['errors'] / df['total_events']

# Time-based features
df['days_since_signup'] = (df['today'] - df['signup_date']).dt.days
```

## Before You Start

Make sure you have:
- ✅ Completed Exercise 1 (NumPy)
- ✅ Completed Exercise 2 (pandas basics + cleaning)
- ✅ Read pandas Fundamentals Reference Guide
- ✅ pandas and NumPy installed
- ✅ The files: events_cleaned.csv, users.csv, system_metrics.csv

## Tips for Success

✅ **Start with exploration** - Use head(), info(), describe() on all three datasets first  
✅ **Understand the joins** - Know which rows will be lost in each join type  
✅ **Feature engineering mindset** - Think about what would be useful to know  
✅ **Test your joins** - Check dimensions before/after merging  
✅ **Build incrementally** - Don't try everything at once  
✅ **Document your logic** - Comments explain WHY you created each feature  

## Ready?

1. Open [exercise-03-instructions.md](./exercise-03-instructions.md) - Follow the step-by-step guide
2. Work in PyCharm or Jupyter notebook
3. Load all three CSV files
4. Explore relationships between datasets
5. Create features and answer business questions
6. Compare your approach with [exercise-03-solution.md](exercise-03-solution.md)

**Let's build real insights!** 📊🚀

