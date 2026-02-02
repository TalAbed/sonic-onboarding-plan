# Exercise 3: Solution

Here's a comprehensive solution for Exercise 3. Your approach may differ significantly—that's expected and fine!

## Complete Solution

```python
import pandas as pd
import numpy as np
from datetime import datetime

# ============================================================
# PART 1: LOAD AND EXPLORE
# ============================================================

print("=" * 60)
print("PART 1: LOAD AND EXPLORE ALL DATASETS")
print("=" * 60)

# Step 1: Load all three datasets
df_events = pd.read_csv('events_cleaned.csv')
df_users = pd.read_csv('users.csv')
df_metrics = pd.read_csv('system_metrics.csv')

# Store original counts
events_count = len(df_events)
users_count = len(df_users)
metrics_count = len(df_metrics)

print(f"\nDatasets loaded:")
print(f"  Events: {events_count} rows, {len(df_events.columns)} columns")
print(f"  Users: {users_count} rows, {len(df_users.columns)} columns")
print(f"  Metrics: {metrics_count} rows, {len(df_metrics.columns)} columns")

# Step 2: Explore events
print("\n\nEvents Dataset:")
print(f"  Shape: {df_events.shape}")
print(f"  Unique users: {df_events['user_id'].nunique()}")
print(f"  Unique event types: {df_events['event_type'].nunique()}")
print(f"  Event types: {df_events['event_type'].unique()}")
print(f"  Missing values:\n{df_events.isnull().sum()}")

# Step 3: Explore users
print("\n\nUsers Dataset:")
print(f"  Shape: {df_users.shape}")
print(f"  Regions: {df_users['region'].unique()}")
print(f"  Account types: {df_users['account_type'].unique()}")
print(f"  Missing values:\n{df_users.isnull().sum()}")

# Step 4: Explore metrics
print("\n\nMetrics Dataset:")
print(f"  Shape: {df_metrics.shape}")
print(f"  Time range: {df_metrics['timestamp'].min()} to {df_metrics['timestamp'].max()}")
print(f"  CPU range: {df_metrics['cpu_usage'].min():.1f} to {df_metrics['cpu_usage'].max():.1f}%")
print(f"  Missing values:\n{df_metrics.isnull().sum()}")


# ============================================================
# PART 2: UNDERSTAND JOIN RELATIONSHIPS
# ============================================================

print("\n\n" + "=" * 60)
print("PART 2: UNDERSTAND JOIN RELATIONSHIPS")
print("=" * 60)

# Step 5: Check join key integrity
print("\nEvents-Users Relationship:")
print(f"  Unique user_ids in events: {df_events['user_id'].nunique()}")
print(f"  Unique user_ids in users: {df_users['user_id'].nunique()}")

# Check if all event users exist in users
events_users = set(df_events['user_id'].unique())
user_ids = set(df_users['user_id'].unique())
missing_users = events_users - user_ids
print(f"  Users in events but not in users: {len(missing_users)}")

# Events per user
events_per_user = df_events.groupby('user_id').size()
print(f"  Events per user: {events_per_user.min()} to {events_per_user.max()}")
print(f"  Average: {events_per_user.mean():.1f}")

# Step 6: Check timestamp relationship
print("\n\nEvents-Metrics Relationship:")
df_events['timestamp'] = pd.to_datetime(df_events['timestamp'])
df_metrics['timestamp'] = pd.to_datetime(df_metrics['timestamp'])

print(f"  Events timestamp range: {df_events['timestamp'].min()} to {df_events['timestamp'].max()}")
print(f"  Metrics timestamp range: {df_metrics['timestamp'].min()} to {df_metrics['timestamp'].max()}")
print(f"  Events granularity: per-event")
print(f"  Metrics granularity: {(df_metrics['timestamp'].iloc[1] - df_metrics['timestamp'].iloc[0]).total_seconds() / 3600:.0f} hours")


# ============================================================
# PART 3: MERGE DATASETS
# ============================================================

print("\n\n" + "=" * 60)
print("PART 3: MERGE DATASETS")
print("=" * 60)

# Step 7: Merge events with users
print("\nStep 7: Merging events with users...")
df_merged = df_events.merge(df_users, on='user_id', how='left')

print(f"  Events before merge: {len(df_events)}")
print(f"  Merged rows: {len(df_merged)}")
print(f"  Lost rows: {len(df_events) - len(df_merged)}")
print(f"  New columns: {list(df_users.columns[1:])}")

# Step 8: Merge with system metrics (nearest neighbor)
print("\nStep 8: Merging events with system metrics...")

# Convert user dates to datetime
df_merged['signup_date'] = pd.to_datetime(df_merged['signup_date'])

# Round event timestamps to nearest metric time for joining
# Each metric is hourly, so we'll match events to their hourly bucket
df_merged['metric_hour'] = df_merged['timestamp'].dt.floor('H')
df_metrics['metric_hour'] = df_metrics['timestamp'].dt.floor('H')

# Merge on hour
df_merged = df_merged.merge(
    df_metrics[['metric_hour', 'cpu_usage', 'memory_usage', 'error_rate', 'events_per_second']],
    left_on='metric_hour',
    right_on='metric_hour',
    how='left'
)

print(f"  After metrics merge: {len(df_merged)} rows")
print(f"  Rows with system metrics: {df_merged['cpu_usage'].notna().sum()}")


# ============================================================
# PART 4: FEATURE ENGINEERING
# ============================================================

print("\n\n" + "=" * 60)
print("PART 4: FEATURE ENGINEERING")
print("=" * 60)

# Step 9: Create user engagement features
print("\nStep 9: Creating engagement features...")

# Total events per user
df_merged['total_events_by_user'] = df_merged.groupby('user_id')['event_id'].transform('count')

# Error count per user
df_merged['error_count_by_user'] = df_merged.groupby('user_id').apply(
    lambda x: (x['status'] == 'error').sum()
).reset_index(drop=True)

# Error rate per user
df_merged['error_rate_by_user'] = df_merged['error_count_by_user'] / df_merged['total_events_by_user']

# Average latency per user
df_merged['avg_latency_by_user'] = df_merged.groupby('user_id')['latency_ms'].transform('mean')

# Favorite event type (most common for each user)
df_merged['favorite_event_type'] = df_merged.groupby('user_id')['event_type'].transform(
    lambda x: x.value_counts().index[0] if len(x.value_counts()) > 0 else 'unknown'
)

print("  ✓ total_events_by_user")
print("  ✓ error_count_by_user")
print("  ✓ error_rate_by_user")
print("  ✓ avg_latency_by_user")
print("  ✓ favorite_event_type")

# Step 10: Create user segmentation features
print("\nStep 10: Creating segmentation features...")

# Engagement level
def engagement_level(total):
    if total < 10:
        return 'low'
    elif total < 100:
        return 'medium'
    else:
        return 'high'

df_merged['engagement_level'] = df_merged['total_events_by_user'].apply(engagement_level)

# Reliability score
def reliability_score(error_rate):
    if error_rate > 0.5:
        return 'poor'
    elif error_rate > 0.2:
        return 'fair'
    else:
        return 'good'

df_merged['reliability_score'] = df_merged['error_rate_by_user'].apply(reliability_score)

# Performance tier
def performance_tier(avg_latency):
    if avg_latency < 300:
        return 'fast'
    elif avg_latency < 700:
        return 'normal'
    else:
        return 'slow'

df_merged['performance_tier'] = df_merged['avg_latency_by_user'].apply(performance_tier)

# User value (combination of engagement and reliability)
def user_value(row):
    engagement = row['engagement_level']
    reliability = row['reliability_score']
    
    if engagement == 'high' and reliability in ['good', 'fair']:
        return 'high'
    elif engagement in ['medium', 'high'] and reliability == 'good':
        return 'high'
    elif engagement == 'low':
        return 'low'
    else:
        return 'medium'

df_merged['user_value'] = df_merged.apply(user_value, axis=1)

print("  ✓ engagement_level")
print("  ✓ reliability_score")
print("  ✓ performance_tier")
print("  ✓ user_value")

# Step 11: Create time-based features
print("\nStep 11: Creating time-based features...")

# Days since signup
df_merged['days_since_signup'] = (df_merged['timestamp'] - df_merged['signup_date']).dt.days

# Signup cohort (month of signup)
df_merged['signup_cohort'] = df_merged['signup_date'].dt.strftime('%Y-%m')

# Event hour and day of week
df_merged['event_hour'] = df_merged['timestamp'].dt.hour
df_merged['event_dayofweek'] = df_merged['timestamp'].dt.dayofweek

# Peak hours (9-17)
df_merged['is_peak_hours'] = (df_merged['event_hour'] >= 9) & (df_merged['event_hour'] <= 17)

print("  ✓ days_since_signup")
print("  ✓ signup_cohort")
print("  ✓ event_hour")
print("  ✓ event_dayofweek")
print("  ✓ is_peak_hours")

# Step 12: Create interaction features
print("\nStep 12: Creating interaction features...")

# Events per day active (velocity)
df_merged['events_per_day_active'] = (
    df_merged['total_events_by_user'] / (df_merged['days_since_signup'] + 1)
).fillna(0)

# High latency ratio
df_merged['high_latency_ratio'] = df_merged.groupby('user_id').apply(
    lambda x: (x['latency_ms'] > 1000).sum() / len(x)
).reset_index(drop=True)

print("  ✓ events_per_day_active")
print("  ✓ high_latency_ratio")


# ============================================================
# PART 5: COMPLEX AGGREGATIONS
# ============================================================

print("\n\n" + "=" * 60)
print("PART 5: COMPLEX AGGREGATIONS & ANALYSIS")
print("=" * 60)

# Step 13: User segmentation analysis
print("\nStep 13: Analyzing user segments...")

# Get unique users for segment analysis
df_users_analysis = df_merged[['user_id', 'engagement_level', 'reliability_score', 
                               'performance_tier', 'user_value', 'total_events_by_user',
                               'error_rate_by_user', 'avg_latency_by_user']].drop_duplicates('user_id')

segment_analysis = df_users_analysis.groupby('user_value').agg({
    'user_id': 'count',
    'total_events_by_user': 'mean',
    'error_rate_by_user': 'mean',
    'avg_latency_by_user': 'mean'
}).rename(columns={'user_id': 'user_count'})

print("\nUser Value Segmentation:")
print(segment_analysis.round(2))

# By engagement level
engagement_analysis = df_users_analysis.groupby('engagement_level').agg({
    'user_id': 'count',
    'error_rate_by_user': 'mean',
    'avg_latency_by_user': 'mean'
}).rename(columns={'user_id': 'user_count'})

print("\nEngagement Level Analysis:")
print(engagement_analysis.round(2))

# Step 14: Geographic analysis
print("\nStep 14: Analyzing by region...")

regional_analysis = df_merged.groupby('region').agg({
    'user_id': 'nunique',
    'event_id': 'count',
    'status': lambda x: (x == 'error').sum() / len(x) * 100,
    'latency_ms': 'mean',
    'event_type': lambda x: x.value_counts().index[0] if len(x.value_counts()) > 0 else 'unknown'
}).rename(columns={'user_id': 'unique_users', 'event_id': 'total_events', 'status': 'error_rate_pct'})

print("\nRegional Analysis:")
print(regional_analysis.round(2))

# Step 15: Temporal analysis
print("\nStep 15: Analyzing temporal patterns...")

# Peak hours analysis
peak_analysis = df_merged.groupby('is_peak_hours').agg({
    'event_id': 'count',
    'status': lambda x: (x == 'error').sum() / len(x) * 100
}).rename(columns={'event_id': 'events', 'status': 'error_rate_pct'})

peak_analysis.index = ['Off-peak (0-8, 18-23)', 'Peak Hours (9-17)']
print("\nPeak Hours Analysis:")
print(peak_analysis.round(2))

# By hour of day
hourly_analysis = df_merged.groupby('event_hour').agg({
    'event_id': 'count',
    'status': lambda x: (x == 'error').sum() / len(x) * 100
}).rename(columns={'event_id': 'events', 'status': 'error_rate_pct'})

print("\nError Rate by Hour of Day:")
print(hourly_analysis.round(2))


# ============================================================
# PART 6: KEY INSIGHTS
# ============================================================

print("\n\n" + "=" * 60)
print("PART 6: KEY INSIGHTS")
print("=" * 60)

# Insight 1: High-value users
high_value_users = (df_users_analysis['user_value'] == 'high').sum()
high_value_pct = high_value_users / len(df_users_analysis) * 100

print(f"\n1. HIGH-VALUE USERS")
print(f"   {high_value_users} users ({high_value_pct:.1f}%) are high-value")
print(f"   These users have high engagement AND good/fair reliability")

# Insight 2: Most reliable segment
best_reliability = df_users_analysis.groupby('reliability_score')['user_id'].count()
print(f"\n2. RELIABILITY DISTRIBUTION")
for reliability, count in best_reliability.items():
    print(f"   {reliability}: {count} users ({count/len(df_users_analysis)*100:.1f}%)")

# Insight 3: Geographic patterns
fastest_region = regional_analysis['latency_ms'].idxmin()
slowest_region = regional_analysis['latency_ms'].idxmax()
print(f"\n3. GEOGRAPHIC PATTERNS")
print(f"   Fastest region: {fastest_region} ({regional_analysis.loc[fastest_region, 'latency_ms']:.0f}ms avg)")
print(f"   Slowest region: {slowest_region} ({regional_analysis.loc[slowest_region, 'latency_ms']:.0f}ms avg)")

# Insight 4: Peak hour impact
peak_errors = peak_analysis.loc['Peak Hours (9-17)', 'error_rate_pct']
offpeak_errors = peak_analysis.loc['Off-peak (0-8, 18-23)', 'error_rate_pct']
print(f"\n4. PEAK HOUR IMPACT ON ERRORS")
print(f"   Peak hours error rate: {peak_errors:.2f}%")
print(f"   Off-peak error rate: {offpeak_errors:.2f}%")
print(f"   Difference: {abs(peak_errors - offpeak_errors):.2f}%")

# Insight 5: User value distribution
value_events = df_merged.groupby('user_value')['event_id'].agg(['count', 'size']).rename(columns={'count': 'unique_events', 'size': 'total_events'})
print(f"\n5. USER VALUE CONCENTRATION")
for value in ['high', 'medium', 'low']:
    if value in value_events.index:
        pct = value_events.loc[value, 'total_events'] / len(df_merged) * 100
        print(f"   {value}: {pct:.1f}% of all events")


# ============================================================
# PART 7: EXPORT AND REPORT
# ============================================================

print("\n\n" + "=" * 60)
print("PART 7: EXPORT AND FINAL REPORT")
print("=" * 60)

# Step 18: Save analysis results
print("\nStep 18: Saving analysis results...")

df_merged.to_csv('events_analysis_full.csv', index=False)
print("  ✓ Saved full analysis to events_analysis_full.csv")

segment_analysis.to_csv('segment_analysis.csv')
print("  ✓ Saved segment analysis to segment_analysis.csv")

regional_analysis.to_csv('regional_analysis.csv')
print("  ✓ Saved regional analysis to regional_analysis.csv")

# Step 19: Final summary
print("\nStep 19: Final Summary Report")
print("=" * 60)

print(f"\nData Processing Pipeline:")
print(f"  Input:")
print(f"    - Events: {events_count:,} rows")
print(f"    - Users: {users_count:,} rows")
print(f"    - Metrics: {metrics_count:,} rows")
print(f"  Output:")
print(f"    - Merged analysis: {len(df_merged):,} rows with {len(df_merged.columns)} features")
print(f"    - Unique users analyzed: {df_merged['user_id'].nunique()}")

print(f"\nKey Metrics:")
print(f"  Overall error rate: {(df_merged['status'] == 'error').sum() / len(df_merged) * 100:.2f}%")
print(f"  Average latency: {df_merged['latency_ms'].mean():.0f}ms")
print(f"  p95 latency: {df_merged['latency_ms'].quantile(0.95):.0f}ms")
print(f"  p99 latency: {df_merged['latency_ms'].quantile(0.99):.0f}ms")

print(f"\nUser Segmentation:")
print(f"  High-value: {high_value_pct:.1f}% of users")
print(f"  Event distribution: {df_merged.groupby('user_value')['event_id'].count().to_dict()}")

print(f"\nRegional Distribution:")
for region in df_merged['region'].unique():
    count = len(df_merged[df_merged['region'] == region])
    pct = count / len(df_merged) * 100
    print(f"  {region}: {pct:.1f}%")

print(f"\nFiles Generated:")
print(f"  - events_analysis_full.csv")
print(f"  - segment_analysis.csv")
print(f"  - regional_analysis.csv")

print("\n✓ Exercise 3 Complete!")
```

---

## Key Patterns Used

### Pattern 1: Merging DataFrames
```python
df_merged = df_events.merge(df_users, on='user_id', how='left')
```

### Pattern 2: Transform for Group Features
```python
df['total_per_user'] = df.groupby('user_id')['event_id'].transform('count')
```

### Pattern 3: Feature Engineering
```python
df['engagement_level'] = df['total_events'].apply(
    lambda x: 'high' if x > 100 else 'low'
)
```

### Pattern 4: Group Aggregation
```python
df.groupby('segment').agg({
    'user_id': 'count',
    'latency_ms': 'mean',
    'status': lambda x: (x == 'error').sum() / len(x)
})
```

---

## What This Teaches

✅ **Multiple data sources** - Real systems have data everywhere  
✅ **Join strategies** - Different approaches for different relationships  
✅ **Feature engineering** - Creating value from raw data  
✅ **Analysis pipelines** - Chaining operations logically  
✅ **Business insights** - Turning data into decisions  

---

## Next Steps

1. ✅ Compare your output with this solution
2. ✅ Understand different approaches to the same problem
3. ✅ Notice patterns you can reuse in your work
4. ✅ Build on this foundation

**Congratulations—you've completed the NumPy/Pandas section!** 🎉🚀