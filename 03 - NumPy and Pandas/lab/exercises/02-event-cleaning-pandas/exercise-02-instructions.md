# Exercise 2: Instructions

Welcome to your first real-world data engineering challenge! In this exercise, you'll load messy event data and clean it professionally.

Follow these steps to complete Exercise 2. Work through each part systematically. Don't look at solution.md until you've tried your best!

## Part 1: Load and Explore

### Step 1: Load the CSV File

Load the raw event data from `events_raw.csv`.

**Your task:**
- Use pandas to load the CSV file
- Print the first few rows to see what you're working with
- How many rows?
- How many columns?
- What are the column names?

### Step 2: Explore the Data

Get a comprehensive view of what you have.

**Your task:**
- Use `.info()` to see column types and missing values
- Use `.describe()` to see statistical summary
- Examine dtypes of each column
- Which columns have NaN/missing values?
- Are data types correct? (timestamps should be datetime, not string), (no need to fix)
- Are there any suspicious values?

### Step 3: Examine Column by Column

Look at actual values in each column.

**Your task:**
- Print unique values for categorical columns (event_type, status)
- Print sample values from numeric columns
- Check min/max of latency_ms
- Are there invalid statuses? (should be: "ok", "error", "timeout")
- Are latency values sensible? (should be positive integers)
- What event types exist?

---

## Part 2: Data Cleaning

### Step 4: Fix Data Types

Convert columns to appropriate types.

**Your task:**
- Convert 'timestamp' column to datetime type
- Convert 'latency_ms' to numeric (handle "N/A" and invalid values)
- Ensure 'event_id' is integer type

**What to expect:**
- Timestamp column should show "datetime64" type
- Latency should be numeric (float or int)
- Some latency values may become NaN if they were "N/A"
- Invalid values get converted to NaN - that's OK for now

### Step 5: Handle Missing Values

Deal with NaN/missing data appropriately.

**Your task:**
1. Check which columns have missing values
2. For critical columns (event_id, timestamp, event_type):
   - Remove rows with missing values
3. For optional columns (status, latency_ms):
   - Fill missing values with reasonable defaults


### Step 6: Remove Duplicates

Clean up exact duplicate rows.

**Your task:**
- Check and remove exact duplicates


### Step 7: Validate Event Types

Ensure only valid event types exist.

**Your task:**
- Check if all values are valid: "purchase", "login", "checkout", "view"
- If invalid types exist, either:
  - Drop rows with invalid types, OR
  - Replace with "unknown"
- Your choice - think about what makes sense


### Step 8: Validate Status Values

Ensure only valid statuses exist.

**Your task:**
- Valid statuses are: "ok", "error", "timeout", "unknown" (if you filled with it)
- Remove or fix any invalid statuses

---

## Part 3: Answer Business Questions

### Step 9: Calculate Key Metrics

Answer important business questions about the events.

**Your task:**
Calculate and print:

1. **Total event volume**
   - How many events were processed?

2. **Error rate**
   - What percentage have status "error"?

3. **Breakdown by event type**
   - Count of events per event type

4. **Breakdown by status**
   - Count of events per status

5. **Average latency by event type**
   - Which event types are slowest?


### Step 10: Identify Key Insights

Find interesting patterns in the data.
Do this until you feel its enough.

**Your task:**
- Which event type has the highest error rate?
- Which event type is slowest (highest average latency)?
- Is there a correlation between event type and errors?
- What's the most common event type?

**What to analyze:**
- Are certain event types more error-prone?
- Do slow events also have high error rates?
- Is the data distributed fairly or skewed?

### Step 11:

Save the clean events into a file called `events_cleaned.csv`
