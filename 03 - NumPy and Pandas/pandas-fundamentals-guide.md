# Pandas Fundamentals Reference Guide

## Overview

This comprehensive guide covers essential pandas concepts every Sonic team member needs to know. Use this as a reference while learning and building data pipelines. Examples are practical and relevant to data engineering work.

pandas is the primary tool for data manipulation and analysis. It provides DataFrames (tabular data) and Series (labeled 1D data) that make working with real-world datasets intuitive and powerful.

## Table of Contents

1. [Installation and Setup](#installation-and-setup)
2. [Pandas Basics](#pandas-basics)
3. [Creating DataFrames and Series](#creating-dataframes-and-series)
4. [Loading Data](#loading-data)
5. [Accessing Data](#accessing-data)
6. [Data Selection and Filtering](#data-selection-and-filtering)
7. [Data Types and Conversion](#data-types-and-conversion)
8. [Adding and Removing Columns](#adding-and-removing-columns)
9. [Handling Missing Data](#handling-missing-data)
10. [Aggregation and Grouping](#aggregation-and-grouping)
11. [Merging and Joining](#merging-and-joining)
12. [String Operations](#string-operations)
13. [DateTime Operations](#datetime-operations)
14. [Pivot Tables and Reshaping](#pivot-tables-and-reshaping)
15. [Common Patterns for Data Engineering](#common-patterns-for-data-engineering)

---

## Installation and Setup

### Install pandas

```bash
# Using pip
pip install pandas

# Or using conda
conda install pandas
```

### Import pandas

```python
import pandas as pd          # Standard convention
import numpy as np           # Often used together
```

### Check Installation

```python
import pandas as pd
print(pd.__version__)        # Check version
```

---

## Pandas Basics

### Series vs DataFrame

**Series**: One-dimensional labeled array (like a column in Excel)

```python
import pandas as pd

# Create a Series
series = pd.Series([10, 20, 30, 40])
# 0    10
# 1    20
# 2    30
# 3    40

# Series with custom index
series = pd.Series([10, 20, 30, 40], 
                   index=['a', 'b', 'c', 'd'])
# a    10
# b    20
# c    30
# d    40
```

**DataFrame**: Two-dimensional labeled data (like a table/spreadsheet)

```python
# Create a DataFrame from dictionary
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [28, 35, 42],
    'salary': [75000, 85000, 95000]
}
df = pd.DataFrame(data)
#      name  age  salary
# 0   Alice   28   75000
# 1     Bob   35   85000
# 2 Charlie   42   95000
```

### Key Concepts

**Index**: Labels for rows (default: 0, 1, 2, ...)  
**Columns**: Labels for columns  
**Values**: The actual data  
**Shape**: (rows, columns)  
**dtypes**: Data type of each column

---

## Creating DataFrames and Series

### From Dictionaries

```python
# Dictionary of lists (most common)
data = {
    'event_id': [1, 2, 3, 4],
    'status': ['ok', 'error', 'ok', 'ok'],
    'latency_ms': [120, 900, 450, 200]
}
df = pd.DataFrame(data)

# Dictionary of Series
data = {
    'col1': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'col2': pd.Series([4, 5, 6], index=['a', 'b', 'c'])
}
df = pd.DataFrame(data)
```

### From Lists of Lists

```python
# List of lists
data = [
    [1, 'ok', 120],
    [2, 'error', 900],
    [3, 'ok', 450]
]
df = pd.DataFrame(data, 
                  columns=['event_id', 'status', 'latency_ms'])
```

### From NumPy Arrays

```python
import numpy as np
import pandas as pd

arr = np.random.rand(3, 4)
df = pd.DataFrame(arr, 
                  columns=['A', 'B', 'C', 'D'])
```

### From Lists of Dictionaries

```python
data = [
    {'name': 'Alice', 'age': 28, 'city': 'NYC'},
    {'name': 'Bob', 'age': 35, 'city': 'LA'},
    {'name': 'Charlie', 'age': 42, 'city': 'Chicago'}
]
df = pd.DataFrame(data)
```

### Empty DataFrame

```python
# Create empty with column names
df = pd.DataFrame(columns=['col1', 'col2', 'col3'])

# Add rows later
df = df.append({'col1': 1, 'col2': 2, 'col3': 3}, 
               ignore_index=True)
```

---

## Loading Data

### Read CSV

```python
# Basic read
df = pd.read_csv('data.csv')

# With options
df = pd.read_csv('data.csv',
                  delimiter=',',           # Column separator
                  header=0,                # Row number for column names
                  skiprows=2,              # Skip first 2 rows
                  nrows=100,               # Read only 100 rows
                  dtype={'age': int},      # Specify data types
                  na_values=['NA', '?'])   # Define missing values
```

### Read Excel

```python
# Read from Excel
df = pd.read_excel('data.xlsx', sheet_name=0)

# Multiple sheets
df1 = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df2 = pd.read_excel('data.xlsx', sheet_name='Sheet2')
```

### Read JSON

```python
df = pd.read_json('data.json')

# Orient parameter
df = pd.read_json('data.json', orient='records')
df = pd.read_json('data.json', orient='columns')
```

### Read Parquet

```python
# Fast columnar format (great for pipelines)
df = pd.read_parquet('data.parquet')
```

### Read from URL

```python
url = 'https://example.com/data.csv'
df = pd.read_csv(url)
```

### Read from Database (with SQLAlchemy)

```python
from sqlalchemy import create_engine

engine = create_engine('postgresql://user:password@localhost/dbname')
df = pd.read_sql_query('SELECT * FROM events', con=engine)
```

---

## Accessing Data

### Viewing Data

```python
df.head()              # First 5 rows
df.head(10)            # First 10 rows
df.tail()              # Last 5 rows
df.tail(10)            # Last 10 rows

df.info()              # Column names, types, missing values
df.describe()          # Statistical summary
df.shape               # (rows, columns)
df.columns             # Column names
df.index               # Row indices
df.dtypes              # Data type of each column
```

### Getting Single Column

```python
# Two equivalent ways
col = df['name']
col = df.name

# Returns a Series
# 0    Alice
# 1      Bob
# dtype: object
```

### Getting Single Row

```python
# By integer index
row = df.iloc[0]       # First row
row = df.iloc[-1]      # Last row

# Returns a Series with column names as index
# name       Alice
# age           28
# salary     75000
```

### Getting Single Cell

```python
# By label (row name, column name)
value = df.loc[0, 'name']      # 'Alice'
value = df.at[0, 'name']        # Same, faster

# By integer position
value = df.iloc[0, 0]           # First row, first column
value = df.iat[0, 0]            # Same, faster
```

### Getting Subsets

```python
# Multiple columns
subset = df[['name', 'age']]

# Multiple rows by label
subset = df.loc[0:2]            # Rows 0, 1, 2 (inclusive!)

# Multiple rows by position
subset = df.iloc[0:3]           # First 3 rows (exclusive end)

# Specific rows and columns
subset = df.loc[0:2, ['name', 'age']]
subset = df.iloc[0:3, [0, 1]]
```

---

## Data Selection and Filtering

### Simple Filtering

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [28, 35, 42],
    'salary': [75000, 85000, 95000]
})

# Single condition
high_earners = df[df['salary'] > 80000]

# Multiple conditions
young_rich = df[(df['age'] < 35) & (df['salary'] > 75000)]

# OR condition
outliers = df[(df['age'] < 25) | (df['salary'] > 90000)]

# NOT condition
low_earners = df[~(df['salary'] > 80000)]
```

### String Filtering

```python
# Contains
matches = df[df['name'].str.contains('Alice')]

# Starts with
matches = df[df['name'].str.startswith('A')]

# Equals
matches = df[df['name'] == 'Bob']

# Case-insensitive
matches = df[df['name'].str.lower() == 'alice']
```

### Using isin()

```python
# Filter for specific values
allowed = ['Alice', 'Bob']
filtered = df[df['name'].isin(allowed)]

# Inverse
not_allowed = df[~df['name'].isin(allowed)]
```

### Using query()

```python
# SQL-like syntax
filtered = df.query('age > 30 and salary > 80000')
filtered = df.query('name == "Alice"')
```

---

## Data Types and Conversion

### Check Data Types

```python
df.dtypes                    # Data type of each column

# Common types:
# int64: Integer
# float64: Floating point
# object: String or mixed
# bool: Boolean
# datetime64: DateTime
# category: Categorical
```

### Convert Data Types

```python
# To integer
df['age'] = df['age'].astype(int)

# To float
df['salary'] = df['salary'].astype(float)

# To string
df['id'] = df['id'].astype(str)

# To datetime
df['date'] = pd.to_datetime(df['date'])

# To category (saves memory)
df['status'] = df['status'].astype('category')
```

### Convert Strings to Numbers

```python
# String to int (with errors handling)
df['count'] = pd.to_numeric(df['count'], errors='coerce')
# errors='coerce' converts invalid values to NaN

# String to float
df['price'] = pd.to_numeric(df['price'], errors='coerce')
```

---

## Adding and Removing Columns

### Add New Column

```python
# Simple assignment
df['new_col'] = 10              # Add constant to all rows

# From calculation
df['total'] = df['quantity'] * df['price']

# From Series
df['new_col'] = pd.Series([1, 2, 3])

# From function
df['age_group'] = df['age'].apply(lambda x: 'young' if x < 30 else 'old')
```

### Rename Columns

```python
# Single column
df = df.rename(columns={'old_name': 'new_name'})

# Multiple columns
df = df.rename(columns={
    'col1': 'new_col1',
    'col2': 'new_col2'
})

# Rename all (uppercase)
df.columns = df.columns.str.upper()
```

### Drop Columns

```python
# Drop single column
df = df.drop('unwanted_col', axis=1)

# Drop multiple columns
df = df.drop(['col1', 'col2'], axis=1)

# Drop by position
df = df.drop(df.columns[0], axis=1)

# In-place (modify original)
df.drop('unwanted_col', axis=1, inplace=True)
```

### Drop Rows

```python
# Drop by index label
df = df.drop(0)              # Drop row 0
df = df.drop([0, 1, 2])      # Drop rows 0, 1, 2

# Drop by condition
df = df[df['age'] > 18]      # Keep only rows where age > 18

# Drop duplicates
df = df.drop_duplicates()    # Remove duplicate rows
df = df.drop_duplicates(subset=['id'])  # Remove duplicates of specific column
```

---

## Handling Missing Data

### Detect Missing Data

```python
# Check for NaN
df.isnull()                  # Boolean DataFrame showing NaN
df.notnull()                 # Opposite

# Count missing values
df.isnull().sum()            # Missing count per column
df.isnull().sum().sum()      # Total missing values

# Rows with any missing value
missing_rows = df[df.isnull().any(axis=1)]

# Rows with missing in specific column
missing = df[df['age'].isnull()]
```

### Handle Missing Data

```python
# Drop rows with any NaN
df = df.dropna()

# Drop rows with NaN in specific column
df = df.dropna(subset=['age'])

# Drop rows with all NaN
df = df.dropna(how='all')
```

### Fill Missing Data

```python
# Fill with constant value
df['age'] = df['age'].fillna(0)

# Fill with mean
df['age'] = df['age'].fillna(df['age'].mean())

# Fill with median
df['age'] = df['age'].fillna(df['age'].median())

# Forward fill (use previous value)
df['status'] = df['status'].fillna(method='ffill')

# Backward fill (use next value)
df['status'] = df['status'].fillna(method='bfill')

# Fill with different values per column
df = df.fillna({
    'age': 0,
    'status': 'unknown',
    'salary': df['salary'].mean()
})
```

---

## Aggregation and Grouping

### Basic Aggregation

```python
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Alice'],
    'department': ['sales', 'engineering', 'sales', 'sales'],
    'salary': [75000, 85000, 95000, 75000]
})

# Single aggregation
total = df['salary'].sum()           # 330000
avg = df['salary'].mean()            # 82500
count = df['salary'].count()         # 4
```

### GroupBy

```python
# Group by department
grouped = df.groupby('department')

# Get statistics per group
grouped['salary'].mean()
# department
# engineering    85000
# sales          81666.67

# Multiple aggregations
grouped['salary'].agg(['sum', 'mean', 'count'])
#            sum   mean  count
# department
# engineering    85000  85000      1
# sales         245000  81666.67    3

# Custom aggregation
grouped.agg({
    'salary': ['sum', 'mean'],
    'name': 'count'
})
```

### Multiple GroupBy

```python
# Group by multiple columns
grouped = df.groupby(['department', 'status'])

# Get statistics
grouped['salary'].mean()
```

### Named Aggregations

```python
grouped.agg(
    total_salary=('salary', 'sum'),
    avg_salary=('salary', 'mean'),
    num_employees=('name', 'count')
)
```

### Transform

```python
# Normalize within groups
df['normalized'] = df.groupby('department')['salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)

# Rank within groups
df['rank'] = df.groupby('department')['salary'].rank(ascending=False)
```

### Pivot Tables

```python
# Create pivot table
pivot = pd.pivot_table(
    df,
    values='salary',           # Values to aggregate
    index='department',        # Rows
    columns='status',          # Columns
    aggfunc='mean'             # Aggregation function
)

# Multiple aggregations
pivot = pd.pivot_table(
    df,
    values='salary',
    index='department',
    aggfunc=['mean', 'sum', 'count']
)
```

---

## Merging and Joining

### Inner Join

```python
df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'id': [1, 2, 4],
    'salary': [75000, 85000, 95000]
})

# Inner join (only matching rows)
merged = pd.merge(df1, df2, on='id', how='inner')
# id    name  salary
# 1   Alice   75000
# 2     Bob   85000
```

### Left Join

```python
# All rows from left, matching from right
merged = pd.merge(df1, df2, on='id', how='left')
# id     name  salary
# 1    Alice   75000.0
# 2      Bob   85000.0
# 3  Charlie      NaN
```

### Right Join

```python
# All rows from right, matching from left
merged = pd.merge(df1, df2, on='id', how='right')
# id      name  salary
# 1     Alice   75000
# 2       Bob   85000
# 4       NaN   95000
```

### Outer Join

```python
# All rows from both
merged = pd.merge(df1, df2, on='id', how='outer')
# id      name  salary
# 1     Alice   75000.0
# 2       Bob   85000.0
# 3   Charlie      NaN
# 4       NaN   95000.0
```

### Join on Different Columns

```python
merged = pd.merge(df1, df2, 
                  left_on='id_x', 
                  right_on='id_y', 
                  how='inner')
```

### Concatenate

```python
# Stack vertically (rows)
combined = pd.concat([df1, df2], ignore_index=True)

# Stack horizontally (columns)
combined = pd.concat([df1, df2], axis=1)
```

---

## String Operations

### Basic String Methods

```python
df = pd.DataFrame({'name': ['alice', 'BOB', 'Charlie']})

# Case conversion
df['name'].str.upper()       # ['ALICE', 'BOB', 'CHARLIE']
df['name'].str.lower()       # ['alice', 'bob', 'charlie']
df['name'].str.capitalize()  # ['Alice', 'Bob', 'Charlie']

# String length
df['name'].str.len()         # [5, 3, 7]

# Check conditions
df['name'].str.contains('a')
df['name'].str.startswith('a')
df['name'].str.endswith('e')
```

### String Splitting and Replacing

```python
# Split
df = pd.DataFrame({'text': ['a-b-c', 'x-y-z']})
df['text'].str.split('-')
# [['a', 'b', 'c'], ['x', 'y', 'z']]

# Replace
df['text'].str.replace('-', '_')
# ['a_b_c', 'x_y_z']

# Strip whitespace
df = pd.DataFrame({'text': ['  hello  ', 'world']})
df['text'].str.strip()
# ['hello', 'world']
```

### Extract and Get

```python
# Extract substring
df = pd.DataFrame({'code': ['A123', 'B456', 'C789']})
df['code'].str[0]           # First character
df['code'].str[1:]          # Everything after first

# Extract with regex
df['code'].str.extract(r'([A-Z])(\d+)')
# 0  1
# A  123
# B  456
# C  789
```

---

## DateTime Operations

### Create DateTime

```python
# From string
df['date'] = pd.to_datetime(df['date_str'])

# From separate columns
df['date'] = pd.to_datetime({
    'year': df['year'],
    'month': df['month'],
    'day': df['day']
})

# With specific format
df['date'] = pd.to_datetime(df['date_str'], 
                            format='%Y-%m-%d')

# Range of dates
dates = pd.date_range('2026-01-01', periods=10, freq='D')
```

### Extract Components

```python
df = pd.DataFrame({'date': pd.date_range('2026-01-01', periods=5)})

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['dayofweek'] = df['date'].dt.dayofweek
df['quarter'] = df['date'].dt.quarter
```

### Time Differences

```python
df = pd.DataFrame({
    'start': pd.to_datetime(['2026-01-01', '2026-01-02']),
    'end': pd.to_datetime(['2026-01-05', '2026-01-06'])
})

# Calculate difference
df['duration'] = df['end'] - df['start']
# Returns timedelta

# Convert to days, hours, etc.
df['days'] = df['duration'].dt.days
df['hours'] = df['duration'].dt.total_seconds() / 3600
```

### Resampling (Time Series)

```python
df = pd.DataFrame({
    'date': pd.date_range('2026-01-01', periods=30),
    'value': np.random.rand(30)
})
df.set_index('date', inplace=True)

# Resample to weekly average
weekly = df.resample('W').mean()

# Resample to monthly sum
monthly = df.resample('M').sum()

# Resample with multiple aggregations
stats = df.resample('W').agg({'value': ['mean', 'sum', 'std']})
```

---

## Pivot Tables and Reshaping

### Melt (Wide to Long)

```python
df = pd.DataFrame({
    'id': [1, 2, 3],
    'Q1': [100, 200, 300],
    'Q2': [150, 250, 350]
})

# Convert wide to long
melted = pd.melt(df, 
                 id_vars=['id'], 
                 value_vars=['Q1', 'Q2'],
                 var_name='quarter',
                 value_name='revenue')
#    id quarter  revenue
# 0   1      Q1      100
# 1   2      Q1      200
# 2   3      Q1      300
# 3   1      Q2      150
# 4   2      Q2      250
# 5   3      Q2      350
```

### Pivot (Long to Wide)

```python
df = pd.DataFrame({
    'id': [1, 1, 2, 2],
    'quarter': ['Q1', 'Q2', 'Q1', 'Q2'],
    'revenue': [100, 150, 200, 250]
})

# Convert long to wide
pivoted = df.pivot(index='id', 
                   columns='quarter', 
                   values='revenue')
# quarter  Q1   Q2
# id
# 1       100  150
# 2       200  250
```

### Stack and Unstack

```python
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['a', 'b', 'c'])

# Stack (wide to long)
stacked = df.stack()
# a  A    1
#    B    4
# b  A    2
#    B    5
# ...

# Unstack (long to wide)
unstacked = stacked.unstack()  # Back to original
```

---

## Common Patterns for Data Engineering

### Data Quality Checks

```python
def check_data_quality(df):
    """Check data quality and report issues."""
    
    # Check for null values
    nulls = df.isnull().sum()
    if nulls.sum() > 0:
        print(f"Missing values found: {nulls}")
    
    # Check for duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"Duplicate rows: {duplicates}")
    
    # Check data types
    print(f"Data types:\n{df.dtypes}")
    
    # Check shape
    print(f"Shape: {df.shape}")
    
    return df

# Usage
df = check_data_quality(df)
```

### Event Processing Pipeline

```python
# Load raw events
df = pd.read_csv('events.csv')

# Data type conversion
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['latency_ms'] = pd.to_numeric(df['latency_ms'])

# Remove invalid rows
df = df[df['latency_ms'] > 0]
df = df.dropna(subset=['user_id', 'event_type'])

# Add derived columns
df['hour'] = df['timestamp'].dt.hour
df['is_slow'] = df['latency_ms'] > 500

# Aggregate by hour
hourly = df.groupby('hour').agg({
    'user_id': 'count',           # Event count
    'latency_ms': ['mean', 'p95'],  # Latency stats
    'is_slow': 'sum'              # Slow event count
})

return hourly
```

### Data Cleaning Template

```python
def clean_data(df):
    """Standardize and clean data."""
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.dropna(subset=['id'])  # Required column
    df['status'] = df['status'].fillna('unknown')
    
    # Standardize text
    df['name'] = df['name'].str.strip().str.lower()
    
    # Convert types
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    
    # Remove outliers (keep within 3 standard deviations)
    df = df[(np.abs(df['amount'] - df['amount'].mean()) <= 3*df['amount'].std())]
    
    return df
```

### Performance Metrics Calculation

```python
# Events with performance data
df = pd.DataFrame({
    'timestamp': pd.date_range('2026-01-01', periods=100),
    'latency_ms': np.random.randint(50, 1000, 100),
    'status': np.random.choice(['ok', 'error'], 100)
})

# Calculate metrics
metrics = {
    'total_events': len(df),
    'error_count': (df['status'] == 'error').sum(),
    'error_rate': (df['status'] == 'error').mean(),
    'avg_latency': df['latency_ms'].mean(),
    'p50_latency': df['latency_ms'].quantile(0.5),
    'p95_latency': df['latency_ms'].quantile(0.95),
    'p99_latency': df['latency_ms'].quantile(0.99),
    'max_latency': df['latency_ms'].max()
}

print(metrics)
```

---

## Quick Reference

### Most Common Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `pd.read_csv()` | Load CSV | `pd.read_csv('file.csv')` |
| `df.head()` | View first rows | `df.head(10)` |
| `df.info()` | Column info | `df.info()` |
| `df[col]` | Get column | `df['name']` |
| `df.loc[]` | Access by label | `df.loc[0, 'name']` |
| `df.iloc[]` | Access by position | `df.iloc[0, 0]` |
| `df[condition]` | Filter rows | `df[df['age'] > 30]` |
| `df.dropna()` | Remove NaN | `df.dropna()` |
| `df.fillna()` | Fill NaN | `df.fillna(0)` |
| `df.groupby()` | Group by column | `df.groupby('dept').mean()` |
| `df.merge()` | Join DataFrames | `pd.merge(df1, df2)` |
| `df.concat()` | Combine DataFrames | `pd.concat([df1, df2])` |
| `df.sort_values()` | Sort | `df.sort_values('age')` |
| `df.drop()` | Remove rows/cols | `df.drop('col', axis=1)` |
| `df.rename()` | Rename columns | `df.rename(columns={})` |

---

## Next Steps

Once you're comfortable with these fundamentals:

1. **Practice** - Work through 100 pandas puzzles
2. **Read Code** - Look at how others use pandas
3. **Experiment** - Try combining these operations
4. **Real Projects** - Use in actual pipelines
5. **Advanced Topics** - Window functions, categorical data, etc.

---

## Important Notes

### pandas vs SQL

Many pandas operations map to SQL:

| pandas | SQL |
|--------|-----|
| `df[df['col'] > 5]` | `WHERE col > 5` |
| `df.groupby('col')` | `GROUP BY col` |
| `df.merge()` | `JOIN` |
| `df.sort_values()` | `ORDER BY` |
| `df['new'] = ...` | `SELECT ..., new_col AS new` |

### Performance Tips

- ✅ Use `dtype` parameter when reading (saves memory)
- ✅ Use `.loc` and `.iloc` instead of `.iterrows()`
- ✅ Use boolean indexing for filtering (not loops)
- ✅ Use `categorical` for repeated string values
- ✅ Use `read_parquet()` instead of CSV (faster, compressed)

### Common Gotchas

❌ **Don't**: Modify DataFrame while iterating  
✅ **Do**: Use vectorized operations

❌ **Don't**: Assume copy with `df2 = df1` (creates view)  
✅ **Do**: Use `df2 = df1.copy()` if modifying

❌ **Don't**: Use `.append()` in loops (slow)  
✅ **Do**: Build list and create DataFrame once

---

## Resources

- **Official Docs**: https://pandas.pydata.org/docs/
- **API Reference**: https://pandas.pydata.org/docs/reference/
- **100 Pandas Puzzles**: https://github.com/ajcr/100-pandas-puzzles

---

## Key Principle

**pandas is built for real-world data.** Messy, incomplete, complicated data. The library provides tools to handle all of it efficiently.

Once you internalize the core patterns (select, filter, group, aggregate), pandas becomes your superpower for data engineering! 🚀

