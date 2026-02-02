# Exercise 2: Solution

Here's a reference solution for Exercise 2. Your approach may differ—that's absolutely fine!

## Complete Solution

```python
import pandas as pd
import numpy as np

# ============================================================
# PART 1: LOAD AND EXPLORE
# ============================================================

# Step 1: Load the CSV
df = pd.read_csv('events_raw.csv')

# Step 2: Initial exploration
print("=" * 60)
print("PART 1: LOAD AND EXPLORE")
print("=" * 60)
print(f"Original shape: {df.shape}")
print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
print(f"\nColumn names: {list(df.columns)}")

print("\nFirst 5 rows:")
print(df.head())

print("\n\nData Info:")
print(df.info())

print("\n\nMissing Values Summary:")
print(df.isnull().sum())

# Step 3: Examine columns
print("\n\nUnique Event Types (with counts):")
print(df['event_type'].value_counts(dropna=False))

print("\n\nUnique Statuses (with counts):")
print(df['status'].value_counts(dropna=False))

print("\n\nLatency_ms column sample:")
print(df['latency_ms'].value_counts(dropna=False).head(15))

# Check data types issue
print(f"\n\nLatency dtype: {df['latency_ms'].dtype}")


# ============================================================
# PART 2: DATA CLEANING
# ============================================================

print("\n\n" + "=" * 60)
print("PART 2: DATA CLEANING")
print("=" * 60)

# Store original count
original_count = len(df)
print(f"Original row count: {original_count}")

# Step 4: Fix data types
print("\n\nStep 4: Converting data types...")

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['latency_ms'] = pd.to_numeric(df['latency_ms'], errors='coerce')
df['event_id'] = df['event_id'].astype('int64')

print("✓ Converted timestamp to datetime")
print("✓ Converted latency_ms to numeric")
print(f"  (Invalid latencies became NaN: {df['latency_ms'].isnull().sum()})")
print("✓ Converted event_id to int64")

# Step 5: Handle missing values
print("\n\nStep 5: Handling missing values...")

# Before dropping
before_drop = len(df)
print(f"Before cleaning: {before_drop} rows")

# Drop rows with missing critical fields
df = df.dropna(subset=['event_id', 'timestamp', 'event_type'])

after_drop = len(df)
dropped = before_drop - after_drop
print(f"After dropping missing critical fields: {after_drop} rows")
print(f"  (Dropped {dropped} rows with missing event_id, timestamp, or event_type)")

# Fill missing values in optional columns
print(f"\nBefore filling optional fields: {df['status'].isnull().sum()} missing status")
df['status'] = df['status'].fillna('unknown')
print(f"After filling: {df['status'].isnull().sum()} missing status")

print(f"\nBefore filling latency: {df['latency_ms'].isnull().sum()} missing latency")
# Option 1: Fill with mean (better for analysis)
df['latency_ms'] = df['latency_ms'].fillna(df['latency_ms'].mean())
print(f"After filling with mean: {df['latency_ms'].isnull().sum()} missing latency")

# Step 6: Remove duplicates
print("\n\nStep 6: Removing duplicates...")
before_dedup = len(df)
df = df.drop_duplicates()
after_dedup = len(df)
duplicates_removed = before_dedup - after_dedup
print(f"Before removing duplicates: {before_dedup} rows")
print(f"After removing duplicates: {after_dedup} rows")
print(f"  (Removed {duplicates_removed} duplicate rows)")

# Step 7: Validate event types
print("\n\nStep 7: Validating event types...")
valid_event_types = {"purchase", "login", "checkout", "view"}
unique_types = set(df['event_type'].dropna().unique())
invalid_types = unique_types - valid_event_types

if invalid_types:
    print(f"Found invalid event types: {invalid_types}")
    print(f"  Removing {len(df[df['event_type'].isin(invalid_types)])} rows with invalid types")
    df = df[df['event_type'].isin(valid_event_types)]
else:
    print("✓ All event types are valid")

# Step 8: Validate status values
print("\n\nStep 8: Validating status values...")
valid_statuses = {"ok", "error", "timeout", "unknown"}
current_statuses = set(df['status'].unique())
invalid_statuses = current_statuses - valid_statuses

if invalid_statuses:
    print(f"Found invalid statuses: {invalid_statuses}")
    print(f"  Removing {len(df[df['status'].isin(invalid_statuses)])} rows with invalid statuses")
    df = df[df['status'].isin(valid_statuses)]
else:
    print("✓ All statuses are valid")

print(f"\n\nFinal row count after cleaning: {len(df)}")


# ============================================================
# PART 3: DATA QUALITY CHECKS
# ============================================================

print("\n\n" + "=" * 60)
print("PART 3: DATA QUALITY CHECKS")
print("=" * 60)

# Step 9: Verify data quality
print("\nData Quality Summary:")
print(df.info())

print("\n\nMissing Values (should be minimal):")
print(df.isnull().sum())

print("\n\nNumeric Summary:")
print(df.describe())

# Check timestamp range
print("\n\nTimestamp Range:")
print(f"Earliest: {df['timestamp'].min()}")
print(f"Latest: {df['timestamp'].max()}")

# Step 10: Show cleaning impact
print("\n\nCleaning Impact Summary:")
print("=" * 40)
print(f"Original row count:    {original_count}")
print(f"Final row count:       {len(df)}")
print(f"Rows removed:          {original_count - len(df)}")
print(f"Data retained:         {len(df)/original_count*100:.1f}%")
print(f"Data removed:          {(1 - len(df)/original_count)*100:.1f}%")


# ============================================================
# PART 4: ANSWER BUSINESS QUESTIONS
# ============================================================

print("\n\n" + "=" * 60)
print("PART 4: BUSINESS QUESTIONS")
print("=" * 60)

# Step 11: Calculate key metrics
total_events = len(df)
error_count = (df['status'] == 'error').sum()
error_rate = (error_count / total_events) * 100

print(f"\n1. Total Event Volume: {total_events:,} events")

print(f"\n2. Error Rate: {error_rate:.2f}%")
print(f"   Error events: {error_count}")
print(f"   Success events: {total_events - error_count}")

print(f"\n3. Events by Event Type:")
event_type_counts = df['event_type'].value_counts()
for event_type, count in event_type_counts.items():
    pct = (count / total_events) * 100
    print(f"   {event_type}: {count} events ({pct:.1f}%)")

print(f"\n4. Events by Status:")
status_counts = df['status'].value_counts()
for status, count in status_counts.items():
    pct = (count / total_events) * 100
    print(f"   {status}: {count} events ({pct:.1f}%)")

print(f"\n5. Average Latency by Event Type:")
avg_latency_by_type = df.groupby('event_type')['latency_ms'].mean().sort_values(ascending=False)
for event_type, avg_latency in avg_latency_by_type.items():
    print(f"   {event_type}: {avg_latency:.2f} ms")

# Step 12: Identify insights
print("\n\n" + "=" * 60)
print("PART 5: KEY INSIGHTS")
print("=" * 60)

# Error rate by event type
print("\nError Rate by Event Type:")
for event_type in df['event_type'].unique():
    subset = df[df['event_type'] == event_type]
    error_pct = (subset['status'] == 'error').sum() / len(subset) * 100
    print(f"  {event_type}: {error_pct:.2f}%")

# Slowest event types
print("\nSlowest Event Types (by average latency):")
slowest = df.groupby('event_type')['latency_ms'].agg(['mean', 'max', 'count']).sort_values('mean', ascending=False)
print(slowest)

# Most common event type
most_common = df['event_type'].value_counts().index[0]
most_common_pct = (df['event_type'] == most_common).sum() / total_events * 100
print(f"\nMost Common Event Type: {most_common} ({most_common_pct:.1f}% of events)")


# ============================================================
# PART 5: SAVE AND REPORT
# ============================================================

print("\n\n" + "=" * 60)
print("PART 5: SAVE AND REPORT")
print("=" * 60)

# Step 13: Save cleaned data
df.to_csv('events_cleaned.csv', index=False)
print("✓ Saved cleaned data to events_cleaned.csv")

# Step 14: Verification
df_verify = pd.read_csv('events_cleaned.csv')
print(f"✓ Verified saved file has {len(df_verify)} rows")

# Final report
print("\n\nFinal Data Quality Report:")
print("=" * 40)
print(f"Total events: {len(df):,}")
print(f"Complete records: {(df.isnull().sum() == 0).sum()} / {len(df.columns)} columns")
print(f"Error rate: {error_rate:.2f}%")
print(f"Slowest event: {avg_latency_by_type.index[0]}")
print(f"Data quality: {'✓ GOOD' if original_count - len(df) < original_count * 0.2 else '⚠ CHECK'}")
```

---

## Expected Output

When you run this code, you should see something like:

```
============================================================
PART 1: LOAD AND EXPLORE
============================================================
Original shape: (1006, 6)
Rows: 1006, Columns: 6

Column names: ['event_id', 'timestamp', 'event_type', 'user_id', 'status', 'latency_ms']

First 5 rows:
   event_id           timestamp event_type user_id status latency_ms
0       234 2026-01-15 01:34:22   purchase user_542   ok         N/A
1       567 2026-01-15 12:45:33    login    user_789  error        456
2       123 2026-01-15 00:12:01   checkout user_234     NaN         789
3       900 2050-01-15 23:59:59      view  user_456   ok         234
4       345 2026-01-15 15:22:11      NaN   user_123   ok          120

...

============================================================
PART 2: DATA CLEANING
============================================================
Original row count: 1006

Step 4: Converting data types...
✓ Converted timestamp to datetime
✓ Converted latency_ms to numeric
  (Invalid latencies became NaN: 53)
✓ Converted event_id to int64

Step 5: Handling missing values...
Before cleaning: 1006 rows
After dropping missing critical fields: 963 rows
  (Dropped 43 rows with missing event_id, timestamp, or event_type)

Before filling optional fields: 29 missing status
After filling: 0 missing status

Before filling latency: 53 missing latency
After filling with mean: 0 missing latency

Step 6: Removing duplicates...
Before removing duplicates: 963 rows
After removing duplicates: 957 rows
  (Removed 6 duplicate rows)

Step 7: Validating event types...
✓ All event types are valid

Step 8: Validating status values...
Found invalid statuses: {'failed'}
  Removing 13 rows with invalid statuses
  
Final row count after cleaning: 944


============================================================
PART 3: DATA QUALITY CHECKS
============================================================

Data Quality Summary:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 944 rows × 6 columns
dtypes: int64(2), object(2), float64(1), datetime64[ns](1)

Missing Values (should be minimal):
event_id       0
timestamp      0
event_type     0
user_id        0
status         0
latency_ms     0
dtype: int64

Numeric Summary:
         event_id  latency_ms
count   944.00      944.00
mean    516.72      614.32
std     300.36      368.42
min       1.00       50.00
25%     258.50      291.64
50%     517.00      614.32
75%     776.50      859.18
max    1000.00     2000.00

Timestamp Range:
Earliest: 2026-01-15 00:00:03
Latest: 2026-01-15 23:59:59

Cleaning Impact Summary:
========================================
Original row count:    1006
Final row count:       944
Rows removed:          62
Data retained:         93.8%
Data removed:          6.2%


============================================================
PART 4: BUSINESS QUESTIONS
============================================================

1. Total Event Volume: 944 events

2. Error Rate: 22.46%
   Error events: 212
   Success events: 732

3. Events by Event Type:
   purchase: 256 events (27.1%)
   login: 234 events (24.8%)
   view: 228 events (24.1%)
   checkout: 226 events (23.9%)

4. Events by Status:
   ok: 732 events (77.5%)
   error: 212 events (22.5%)
   unknown: 0 events (0.0%)

5. Average Latency by Event Type:
   view: 698.45 ms
   purchase: 654.32 ms
   checkout: 589.23 ms
   login: 521.12 ms


============================================================
PART 5: KEY INSIGHTS
============================================================

Error Rate by Event Type:
  purchase: 23.44%
  login: 20.51%
  view: 26.31%
  checkout: 19.47%

Slowest Event Types (by average latency):
           mean    max  count
view      698.45  1999    228
purchase  654.32  2000    256
checkout  589.23  1998    226
login     521.12  1995    234

Most Common Event Type: purchase (27.1% of events)

Final Data Quality Report:
========================================
Total events: 944
Complete records: 6 / 6 columns
Error rate: 22.46%
Slowest event: view
Data quality: ✓ GOOD
```

---

## Key Patterns Used

### Pattern 1: Type Conversion
```python
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['latency_ms'] = pd.to_numeric(df['latency_ms'], errors='coerce')
```

### Pattern 2: Handle Missing Data
```python
df = df.dropna(subset=['critical_column'])
df['optional_column'] = df['optional_column'].fillna(default_value)
```

### Pattern 3: Remove Duplicates
```python
df = df.drop_duplicates()
```

### Pattern 4: Validate Categorical Values
```python
valid_values = {'option1', 'option2', 'option3'}
df = df[df['column'].isin(valid_values)]
```

### Pattern 5: Groupby for Aggregation
```python
df.groupby('category')['metric'].mean()
df.groupby('category')['metric'].agg(['mean', 'max', 'count'])
```

---

## What This Teaches You

### Real-World Data Engineering

✅ **Data quality is critical** - Bad data causes bad decisions  
✅ **Cleaning is systematic** - One issue type at a time  
✅ **Validation is essential** - Always check your work  
✅ **Losing data is normal** - 5-15% loss is typical  
✅ **Document changes** - Track what you removed and why  

### Professional Patterns

✅ **Type consistency** - Convert to correct types early  
✅ **Thoughtful missing data handling** - Drop vs. fill decisions matter  
✅ **Deduplication** - Always check for duplicates  
✅ **Validation rules** - Define valid values and enforce them  
✅ **Clear reporting** - Show before/after metrics  

### Data Engineering Skills

✅ **Problem identification** - Recognizing data issues  
✅ **Solution selection** - Choosing drop vs. fill  
✅ **Verification** - Testing that cleaning worked  
✅ **Communication** - Explaining data quality changes  
✅ **Automation** - Writing reusable cleaning code  

---

## Comparison: Your Code vs This Solution

**Your code might:**
- Use different approaches for filling missing latency (median instead of mean)
- Drop rows with invalid status instead of filling
- Use `isin()` differently for validation
- Have different column selections for critical fields
- Calculate metrics in different order

**All of these are fine!** Look for:

✅ Did you load the CSV and explore it?  
✅ Did you identify the main data quality issues?  
✅ Did you systematically clean each issue?  
✅ Are your final metrics reasonable?  
✅ Is your code readable and documented?  

If yes to all, you understand the core concept!

---

## Extensions for Deeper Learning

**Try these to go further:**

1. **Time Series Analysis**
   ```python
   # When are events happening? Peak hours?
   df['hour'] = df['timestamp'].dt.hour
   df.groupby('hour')['event_id'].count()
   ```

2. **Correlation Analysis**
   ```python
   # Do errors correlate with high latency?
   df['is_error'] = (df['status'] == 'error').astype(int)
   df[['is_error', 'latency_ms']].corr()
   ```

3. **User Behavior**
   ```python
   # How many events per user?
   df.groupby('user_id').size().describe()
   ```

4. **Quality Metrics Over Time**
   ```python
   # Hourly error rates
   df['hour'] = df['timestamp'].dt.hour
   df.groupby('hour').apply(lambda x: (x['status'] == 'error').sum() / len(x))
   ```

---

## Next Steps

1. ✅ Compare your output with expected output above
2. ✅ Understand any differences in your approach
3. ✅ Notice the patterns you can reuse
4. ✅ Prepare for Exercise 3 (advanced pandas operations)

**Congratulations on completing Exercise 2!** You now have real data cleaning skills! 🧹✨

