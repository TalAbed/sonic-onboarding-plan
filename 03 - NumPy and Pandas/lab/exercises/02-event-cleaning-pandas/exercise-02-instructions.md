# Exercise 2: Instructions

Follow these steps to complete Exercise 2. Work through each part systematically. Don't look at solution.md until you've tried your best!

## Part 1: Load and Explore

### Step 1: Load the CSV File

Load the raw event data from `events_raw.csv`.

**Your task:**
- Use pandas to load the CSV file
- Store it in a variable called `df`
- Print the first few rows to see what you're working with

**What to check:**
- How many rows?
- How many columns?
- What are the column names?

### Step 2: Explore the Data

Get a comprehensive view of what you have.

**Your task:**
- Use `.info()` to see column types and missing values
- Use `.describe()` to see statistical summary
- Examine dtypes of each column
- Identify which columns have missing values

**Hints:**
- Look at the "non-null" counts to find missing data
- Some columns may have wrong data types

**What to look for:**
- Which columns have NaN/missing values?
- Are data types correct? (timestamps should be datetime, not string)
- Are there any suspicious values?

### Step 3: Examine Column by Column

Look at actual values in each column.

**Your task:**
- Print unique values for categorical columns (event_type, status)
- Print sample values from numeric columns
- Check min/max of latency_ms
- Look for invalid or suspicious values

**What to look for:**
- Are there invalid statuses? (should be: "ok", "error", "timeout")
- Are latency values sensible? (should be positive integers)
- Are there suspicious timestamps? (future dates? way in the past?)
- What event types exist?

---

## Part 2: Data Cleaning

### Step 4: Fix Data Types

Convert columns to appropriate types.

**Your task:**
- Convert 'timestamp' column to datetime type
- Convert 'latency_ms' to numeric (handle "N/A" and invalid values)
- Ensure 'event_id' is integer type

**Hints:**
- `pd.to_datetime()` converts to datetime
- `pd.to_numeric()` with `errors='coerce'` converts invalid values to NaN
- Use `.astype()` for simple type conversions like int
- After conversion, check with `.info()` to verify

**What to expect:**
- Timestamp column should show "datetime64" type
- Latency should be numeric (float or int)
- Some latency values may become NaN if they were "N/A"
- Invalid values get converted to NaN—that's OK for now

### Step 5: Handle Missing Values

Deal with NaN/missing data appropriately.

**Your task:**
1. Check which columns have missing values (use `.isnull().sum()`)
2. For critical columns (event_id, timestamp, event_type):
   - Remove rows with missing values
3. For optional columns (status, latency_ms):
   - Fill missing values with reasonable defaults

**Hints:**
- `.fillna()` fills missing values with a default
  - For status: consider "unknown" as default
  - For latency_ms: consider filling with the mean, median, or "0"

**Questions to answer:**
- How many rows had missing event_type? (dropped them)
- How many had missing status? (filled them)
- How many had missing latency? (filled them)
- How many rows remain after cleaning?

### Step 6: Remove Duplicates

Clean up exact duplicate rows.

**Your task:**
- Check if there are duplicate rows using `.duplicated()`
- Remove exact duplicates using `.drop_duplicates()`
- Print how many were removed

**Hints:**
- `.duplicated()` marks rows that are exact copies of earlier rows
- `.duplicated().sum()` counts total duplicates
- `.drop_duplicates()` removes them (keeps first occurrence by default)
- Use `.drop_duplicates(subset=[...])` to consider only specific columns if needed

**What to expect:**
- Some duplicate rows should exist (intentionally added to the data)
- Print count before and after to see impact

### Step 7: Validate Event Types

Ensure only valid event types exist.

**Your task:**
- List all unique event types using `.unique()`
- Check if all values are valid: "purchase", "login", "checkout", "view"
- If invalid types exist, either:
  - Drop rows with invalid types, OR
  - Replace with "unknown"
- Your choice—think about what makes sense

**Hints:**
- Valid types are: "purchase", "login", "checkout", "view"
- Look for typos, extra spaces, case differences
- If you find invalid ones, use `.isin()` for boolean filtering

**What to check:**
- Are all values in the list legitimate?
- Are there any NaN remaining? (should have filled them)

### Step 8: Validate Status Values

Ensure only valid statuses exist.

**Your task:**
- List all unique status values
- Valid statuses are: "ok", "error", "timeout", "unknown" (if you filled with it)
- Remove or fix any invalid statuses

**Hints:**
- Similar approach to Step 7
- Use `.value_counts()` to see frequency
- Invalid values should be rare
- Consider: should you drop these rows or flag them differently?

---

## Part 3: Data Quality Checks

### Step 9: Verify Data Quality

Make sure your cleaned data looks good.

**Your task:**
- Print summary statistics (use `.describe()` again)
- Check for remaining NaN values (should be very few or zero)
- Verify column data types are correct
- Check that timestamp range makes sense

**Hints:**
- Compare with original `.describe()` output
- Use `.isnull().sum()` to verify no critical missing data
- Use `.info()` to confirm all dtypes
- Print min/max timestamps to verify time range

**What to verify:**
- No NaN in critical columns?
- Timestamps in reasonable range? (all recent, not in past/future)
- Latency values positive? (min >= 0 or filled appropriately)
- Event counts make sense?

### Step 10: Show Cleaning Impact

Demonstrate the data quality improvement.

**Your task:**
- Create a summary showing:
  - Original row count
  - Rows removed (missing data, duplicates, invalid values)
  - Final row count
  - Percentage of data retained

**Hints:**
- Keep track of row counts at each step
- Print before/after for each cleaning operation
- Calculate retention rate: (final rows / original rows) * 100

**What to show:**
- How much data did you lose to cleaning?
- Is that percentage reasonable? (usually 5-15% in real data)

---

## Part 4: Answer Business Questions

### Step 11: Calculate Key Metrics

Answer important business questions about the events.

**Your task:**
Calculate and print:

1. **Total event volume**
   - How many events were processed?

2. **Error rate**
   - What percentage have status "error"?
   - Hint: Use boolean filtering and division

3. **Breakdown by event type**
   - Count of events per event type
   - Hint: Use `.value_counts()` on event_type column

4. **Breakdown by status**
   - Count of events per status
   - Hint: Use `.value_counts()` on status column

5. **Average latency by event type**
   - Which event types are slowest?
   - Hint: Use `.groupby('event_type')['latency_ms'].mean()`

**Hints:**
- Use `.sum()` and division for rates/percentages
- Use `.value_counts()` for frequency counts
- Use `.groupby().mean()` for averages by group
- Format numbers nicely (2 decimal places for percentages)

**What to present:**
- Show each metric clearly labeled
- Include units (events, percentage, milliseconds, etc.)
- Explain what each metric means for the business

### Step 12: Identify Key Insights

Find interesting patterns in the data.

**Your task:**
- Which event type has the highest error rate?
- Which event type is slowest (highest average latency)?
- Is there a correlation between event type and errors?
- What's the most common event type?

**Hints:**
- Use filtering and groupby operations
- Compare error rates across event types
- Compare latencies across event types
- Think about what these patterns mean

**What to analyze:**
- Are certain event types more error-prone?
- Do slow events also have high error rates?
- Is the data distributed fairly or skewed?

---

## Part 5: Save and Present

### Step 13: Save Cleaned Data

Export your cleaned dataset.

**Your task:**
- Save the cleaned dataframe to a new CSV file
- Name it `events_cleaned.csv`
- Verify it was saved by reading it back in

**Hints:**
- Use `index=False` to avoid saving the index column
- Read it back to verify

### Step 14: Create Summary Report

Write a brief summary of your cleaning work.

**Your task:**
Print a summary showing:
- Original vs. cleaned row counts
- Data quality improvements made
- Key metrics discovered
- Any warnings or concerns about the data

**Hints:**
- Use print statements to create a formatted report
- Make it readable with headers and clear sections
- Include numbers and percentages

---

## Summary Checklist

Before comparing with the solution:

- ✅ Loaded CSV and explored with head(), info(), describe()
- ✅ Converted data types (datetime, numeric)
- ✅ Removed rows with missing critical columns
- ✅ Filled missing values in optional columns
- ✅ Removed duplicate rows
- ✅ Validated event_type and status values
- ✅ Checked for invalid/suspicious data
- ✅ Calculated total events, error rate, breakdown by type/status
- ✅ Found average latency by event type
- ✅ Saved cleaned CSV
- ✅ Created summary report

If you've done all this, you're ready to compare with solution.md!

---

## Hints for Common Issues

**Problem: "latency_ms" column is object type (string)**
- Use `pd.to_numeric(..., errors='coerce')` to convert
- This turns "N/A" and invalid values into NaN

**Problem: Timestamp column isn't recognized as datetime**
- Use `pd.to_datetime(df['timestamp'])`
- May need to specify format: `pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')`

**Problem: How do I remove rows with missing values in specific columns?**
- Use `.dropna(subset=['column1', 'column2'])`
- This only removes rows where those specific columns are missing

**Problem: How do I fill missing values with different defaults?**
- For one column: `df['column'] = df['column'].fillna('default_value')`
- For multiple: `df.fillna({'col1': 'val1', 'col2': 'val2'})`

**Problem: My error rate doesn't match my expected percentage**
- Make sure you're dividing by total rows, not just error count
- Verify you included rows with 'unknown' status in the total

---

## Next Steps

1. Work through all 14 steps
2. Test frequently with print statements
3. Verify data quality at each stage
4. Compare your approach with [exercise-02-solution.md](exercise-02-solution.md)
5. Prepare for Exercise 3

**Good luck!** You're learning real data engineering skills! 🚀

