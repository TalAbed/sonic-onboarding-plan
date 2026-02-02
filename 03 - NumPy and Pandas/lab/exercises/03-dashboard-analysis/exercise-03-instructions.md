# Exercise 3: Instructions

Follow these steps to complete Exercise 3. This is the capstone exercise—combine everything you've learned!

## Part 1: Load and Explore All Datasets

### Step 1: Load All Three CSV Files

Load the three datasets into DataFrames.

**Your task:**
- Load `events_cleaned.csv` into `df_events`
- Load `users.csv` into `df_users`
- Load `system_metrics.csv` into `df_metrics`
- Store original row counts for comparison later

**What to check:**
- How many rows in each dataset?
- What columns are in each?
- Are there any obvious issues?

### Step 2: Explore Events Dataset

Examine the cleaned events data from Exercise 2.

**Your task:**
- Use `.head()`, `.info()`, `.describe()`
- Identify key columns (especially the join key: user_id)
- Check data types and missing values
- Count unique users and unique events

**Hints:**
- Use `.nunique()` to count unique values
- Check if event_id is unique per row

**What to find:**
- How many unique users?
- How many unique event types?
- Any missing values?

### Step 3: Explore Users Dataset

Examine the user profile information.

**Your task:**
- Use `.head()` to see sample users
- Check columns: user_id, region, account_type, signup_date
- Examine data types
- Look for missing values

**Hints:**
- Signup date might be string—note this for later
- Print unique regions
- Print unique account types

**What to find:**
- How many unique users?
- What regions are represented?
- What account types exist?

### Step 4: Explore System Metrics Dataset

Examine the system performance data.

**Your task:**
- Use `.head()` to see sample metrics
- Check columns: timestamp, cpu_usage, memory_usage, error_rate, events_per_second
- Examine the timestamp column format
- Check for gaps or anomalies in data

**Hints:**
- Timestamps might be string—note for later
- Look at ranges of numeric columns
- Check if metrics seem realistic

**What to find:**
- What time range does this cover?
- What are typical CPU/memory ranges?
- Any suspicious values?

---

## Part 2: Understanding Join Relationships

### Step 5: Understand the Join Keys

Identify how to connect the datasets.

**Your task:**
- Identify the join key between events and users
- Check if all event user_ids exist in users dataset
- Check if all users have events

**Hints:**
- Look at user_id column in both datasets
- Use `.isin()` to check if all values exist in other dataset
- Count how many events per user

**What to verify:**
- Is user_id unique in users dataset? (should be)
- Is user_id repeated in events dataset? (should be—multiple events per user)
- Are all event user_ids in users dataset?

### Step 6: Understand Events-Metrics Relationship

Events and metrics both have timestamps, but not every event has a matching metric.

**Your task:**
- Look at timestamp columns in both datasets
- Understand the granularity (events are per-event, metrics are system-wide)
- Note that metrics are aggregated (one row = one time period)

**Hints:**
- Events timestamp: specific time of each event
- Metrics timestamp: snapshot of system state (might be less frequent)
- You'll do a different kind of merge for this

**What to understand:**
- Should we do an inner or left join?
- What will we gain/lose with each approach?

---

## Part 3: Merging Datasets

### Step 7: Merge Events with Users

Join the cleaned events with user information.

**Your task:**
1. Merge df_events with df_users on user_id
2. Use a left join (keep all events, add user info when available)
3. Store result in df_merged
4. Verify the merge

**Hints:**
- Check the shape before/after
- Print a sample row to see joined data
- Count missing values in new columns

**What to verify:**
- Did the merge work?
- All event rows still there?
- User information added?
- Any missing user information?

### Step 8: Add System Metrics to Events

Connect events with system performance data by timestamp.

**Your task:**
1. Convert system_metrics timestamp to datetime
2. For each event, find the nearest system metrics snapshot
3. Merge events with metrics based on timestamp
4. Store in df_merged

**Hints:**
- Events and metrics have different timestamps
- You might need to round/bin timestamps
- Or use nearest-neighbor matching
- Or use a range condition (event timestamp >= metric timestamp)

**Complexity note:**
- Simple approach: round event timestamps to nearest metric time
- Advanced: use `.merge_asof()` for nearest-neighbor join

**What to consider:**
- Should events exactly match metric times? (probably not)
- What strategy makes sense? (round down? nearest?)

---

## Part 4: Feature Engineering

### Step 9: Create User Engagement Features

Calculate engagement metrics for each user.

**Your task:**
Create new columns (per user):
- `total_events`: how many events did this user generate?
- `error_count`: how many errors?
- `error_rate`: what percentage of events were errors?
- `avg_latency`: average latency for this user's events
- `favorite_event_type`: most common event type for user

**Hints:**
- Use `.groupby('user_id')` to aggregate per user
- Use `.transform()` to add group statistics back to each row
- For favorite type: use `.mode()` or value_counts

**Example pattern:**
```
df['total_events'] = df.groupby('user_id')['event_id'].transform('count')
```

**What to create:**
- Engagement metrics
- Quality metrics (error rate)
- Performance metrics (latency)

### Step 10: Create User Segmentation Features

Categorize users based on their behavior.

**Your task:**
Create categorical features:
- `engagement_level`: "low" (< 10 events), "medium" (10-100), "high" (> 100)
- `reliability_score`: "poor" (>50% errors), "fair" (20-50%), "good" (<20%)
- `performance_tier`: "fast" (avg latency < 300ms), "normal" (300-700ms), "slow" (>700ms)
- `user_value`: Combine engagement + reliability (high engagement + good reliability = valuable)

**Hints:**
- Use `.apply()` or `.cut()` for binning continuous variables
- Use `.apply()` with lambda for conditional logic
- Consider what makes a "valuable" user

**What to think about:**
- What thresholds make sense?
- How do you define "valuable"?
- Could these segments drive business decisions?

### Step 11: Create Time-Based Features

Extract features from timestamps.

**Your task:**
Create time-based columns:
- `days_since_signup`: how long has user been active?
- `signup_cohort`: which month did user sign up? ("2025-01", "2025-02", etc.)
- `event_hour`: what hour of day did event occur?
- `event_dayofweek`: which day of week? (0=Monday, 6=Sunday)
- `is_peak_hours`: is event during peak times (9-17)? (boolean)

**Hints:**
- Use `.dt.` accessor on datetime columns
- Signup cohort: `df['signup_date'].dt.strftime('%Y-%m')`
- Days: `(df['event_timestamp'] - df['signup_date']).dt.days`
- Hour: `df['timestamp'].dt.hour`

**What to create:**
- Temporal patterns
- User lifecycle features
- Usage timing features

### Step 12: Create Interaction Features

Combine multiple features to create new insights.

**Your task:**
Create derived features:
- `events_per_day_active`: events / days_since_signup (velocity)
- `recent_reliability`: error rate in last 7 days
- `latency_variability`: standard deviation of latency (consistency)
- `high_latency_ratio`: % of events with latency > 1000ms

**Hints:**
- Some require groupby + filtering
- Use rolling windows for recent trends
- Think about what would predict customer satisfaction

**What to think about:**
- Which features would be most predictive?
- What do these features tell you about each user?

---

## Part 5: Complex Aggregations

### Step 13: User Segmentation Analysis

Analyze user segments and their metrics.

**Your task:**
Group by user segmentation features and calculate:
- Segment size (how many users?)
- Average error rate per segment
- Average latency per segment
- Retention or engagement by segment

**Hints:**
- Use `.groupby('engagement_level').agg(...)`
- Calculate multiple metrics at once with `.agg()`
- Sort results for clarity

**What to find:**
- Which segments have highest error rates?
- Which are slowest?
- Are there clear patterns?

### Step 14: Geographic Analysis

Analyze patterns by region.

**Your task:**
For each region:
- Number of users
- Total events
- Average events per user
- Error rate by region
- Average latency by region
- Most common event type

**Hints:**
- `.groupby('region')` to group
- Use `.agg()` for multiple metrics
- Sort by interesting metric (e.g., error rate)

**What to find:**
- Do regions have different characteristics?
- Which regions perform best/worst?
- Are there geographic patterns?

### Step 15: Temporal Analysis

Analyze patterns over time.

**Your task:**
Create time-based analysis:
- Peak hours: when are most events?
- Error rate by hour of day
- Error rate by day of week
- Trends over time (by signup cohort or date range)

**Hints:**
- `.groupby('event_hour')['event_id'].count()`
- `.groupby('event_dayofweek')` for day patterns
- `.groupby('signup_cohort')` for cohort analysis
- Use `.sort_index()` for time ordering

**What to find:**
- When is system busiest?
- When do errors happen?
- Are there weekly patterns?

---

## Part 6: Building Insights

### Step 16: Identify Key Insights

Find the most interesting patterns in your data.

**Your task:**
Answer these questions:
1. What percentage of users are "high value"?
2. Which segment has the highest error rate? (and why?)
3. Do high-engagement users have better reliability?
4. What's the most valuable user cohort? (by signup date)
5. Is there a correlation between system metrics and user experience?

**Hints:**
- Use the features and aggregations you created
- Look for counterintuitive patterns
- Think about business implications

**What to present:**
- Top 5 insights
- Why each matters
- What action it suggests

### Step 17: Create a Summary Report

Synthesize your findings.

**Your task:**
Create a comprehensive summary:
- Total users and events analyzed
- Key metrics (error rate, avg latency, etc.)
- Top insights (3-5 key findings)
- Recommendations for action

**Hints:**
- Use formatted print statements
- Create a clear, scannable report
- Include numbers/percentages
- Include context for each metric

**What to include:**
- Executive summary
- Key metrics by segment
- Top findings
- Recommended actions

---

## Part 7: Export and Verify

### Step 18: Save Analysis Results

Export your merged and featured dataset.

**Your task:**
- Save the full merged dataset with all features to CSV
- Save segment summary to CSV
- Save regional summary to CSV
- Verify files were created

**Hints:**
- Name files clearly: `users_analysis.csv`, `regional_analysis.csv`, etc.

### Step 19: Create Final Summary

Document what you discovered.

**Your task:**
Print a final summary showing:
- Data processing pipeline (input → output)
- Rows processed at each step
- Key findings
- Output files created
- Next steps for using this analysis

---

## Summary Checklist

Before comparing with solution:

- ✅ Loaded all three CSV files
- ✅ Explored each dataset separately
- ✅ Understood join relationships
- ✅ Merged events with users
- ✅ Connected events with system metrics
- ✅ Created engagement features
- ✅ Created segmentation features
- ✅ Created time-based features
- ✅ Created interaction features
- ✅ Analyzed user segments
- ✅ Analyzed by region
- ✅ Analyzed temporal patterns
- ✅ Identified 5+ key insights
- ✅ Created summary report
- ✅ Exported results

If you've done all this, you've completed the capstone! 🎉

---

## Hints for Common Issues

**Problem: "Column not found" after merge**
- Check column names are exactly the same
- Use `df.columns` to see actual names
- Look for leading/trailing spaces

**Problem: Many NaN values after merge**
- User IDs don't match perfectly?
- Check `.isin()` results
- Look for data type mismatches

**Problem: Merge creates too many rows**
- Many-to-many join created all combinations
- Use inner join to debug
- Check uniqueness of keys

**Problem: Can't merge events with metrics by timestamp**
- Events and metrics have different granularity
- Use `.merge_asof()` for nearest-neighbor
- Or round timestamps to common interval

**Problem: Feature creation is slow**
- Use `.groupby().transform()` instead of loops
- Avoid `.apply()` when vectorized operations work
- Consider data size—is it too large?

---

## You've got this! This is real data engineering! 🚀