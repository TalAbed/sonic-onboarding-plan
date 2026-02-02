# Exercise 3: Instructions

Welcome to the final exercise! You'll combine data from multiple sources and create insights through feature engineering.
Follow these steps to complete Exercise 3. This is the capstone exercise—combine everything you've learned!

## Part 1: Load and Explore All Datasets

### Step 1: Load All Three CSV Files

Load the three datasets into DataFrames.

**Your task:**
- Load `events_cleaned.csv` (from the previous) into `df_events`
- Load `users.csv` into `df_users`
- Load `system_metrics.csv` into `df_metrics`

---

## Part 3: Merging Datasets

### Step 7: Merge Events with Users

Join the cleaned events with user information.

**Your task:**
1. Merge df_events with df_users on user_id
2. Use a left join (keep all events, add user info when available)
3. Store result in df_merged


### Step 8: Add System Metrics to Events

Connect events with system performance data by timestamp.

**Your task:**
1. Convert system_metrics timestamp to datetime
2. For each event, find the nearest system metrics snapshot
3. Merge events with metrics based on timestamp
4. Store in df_merged

**Complexity note:**
- Simple approach: round event timestamps to nearest metric time
- Advanced: use `.merge_asof()` for nearest-neighbor join

---

## Part 4: Feature Engineering

### Step 9: Create User Engagement Features

Calculate engagement metrics for each user.
**Your task:**
Create new columns (per user):
- `total_events`: how many events did this user generate?
- `error_rate`: what percentage of events were errors?
- `avg_latency`: average latency for this user's events


### Step 10: Create User Segmentation Features

Categorize users based on their behavior.

**Your task:**
Create categorical features:
- `engagement_level`: "low" (< 10 events), "medium" (10-100), "high" (> 100)
- `reliability_score`: "poor" (>50% errors), "fair" (20-50%), "good" (<20%)
- `performance_tier`: "fast" (avg latency < 300ms), "normal" (300-700ms), "slow" (>700ms)
- `user_value`: Combine engagement + reliability (high engagement + good reliability = valuable)

### Step 11: Create Time-Based Features

Extract features from timestamps.

**Your task:**
Create time-based columns:
- `days_since_signup`: how long has user been active?
- `event_hour`: what hour of day did event occur?

---

## Part 5: Complex Aggregations

### Step 14: Geographic Analysis

Analyze patterns by region.

**Your task:**
For each region:
- Number of users
- Error rate by region
- Average latency by region

Show the data in a nice visualization using matplotlib.

### Step 15: Temporal Analysis

Analyze patterns over time.

**Your task:**
Create time-based analysis:
- Peak hours: when are most events?
- Error rate by hour of day

Show the data in a nice visualization using matplotlib.