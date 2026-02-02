"""
Sample data generator for Exercise 3.

This script generates three CSV files for the capstone exercise:
1. users.csv - User profile information
2. system_metrics.csv - System-wide performance data
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generate_users(n_users=200, seed=42):
    """
    Generate user profile data.
    
    Parameters:
        n_users: Number of users to generate
        seed: Random seed
    
    Returns:
        DataFrame with user information
    """
    random.seed(seed)
    np.random.seed(seed)
    
    regions = ["US-East", "US-West", "EU", "APAC", "LATAM"]
    account_types = ["free", "standard", "premium"]
    
    base_date = datetime(2025, 6, 1)
    
    user_ids = [f"user_{i:03d}" for i in range(100, 100 + n_users)]
    
    names = [
        f"User {random.randint(1000, 9999)}"
        for _ in range(n_users)
    ]
    
    regions_list = [random.choice(regions) for _ in range(n_users)]
    
    signup_dates = [
        (base_date + timedelta(days=random.randint(0, 250))).strftime("%Y-%m-%d")
        for _ in range(n_users)
    ]
    
    account_types_list = [
        random.choice(account_types) if random.random() < 0.8 else "free"
        for _ in range(n_users)
    ]
    
    emails = [
        f"user{i}@example.com"
        for i in range(n_users)
    ]
    
    df = pd.DataFrame({
        'user_id': user_ids,
        'name': names,
        'region': regions_list,
        'signup_date': signup_dates,
        'account_type': account_types_list,
        'email': emails
    })
    
    return df


def generate_system_metrics(n_samples=100, seed=42):
    """
    Generate system performance metrics.
    
    Parameters:
        n_samples: Number of metric samples
        seed: Random seed
    
    Returns:
        DataFrame with system metrics
    """
    random.seed(seed)
    np.random.seed(seed)
    
    base_timestamp = datetime(2026, 1, 15, 0, 0, 0)
    
    # Generate hourly metrics
    timestamps = [
        (base_timestamp + timedelta(hours=i)).strftime("%Y-%m-%d %H:%M:%S")
        for i in range(n_samples)
    ]
    
    # CPU usage (realistic ranges)
    cpu_usage = [random.uniform(20, 85) for _ in range(n_samples)]
    
    # Memory usage
    memory_usage = [random.uniform(30, 80) for _ in range(n_samples)]
    
    # Error rate (increases with system load)
    error_rates = [
        min(0.5, cpu/100 * 0.3 + random.uniform(0, 0.1))
        for cpu in cpu_usage
    ]
    
    # Events per second
    events_per_sec = [
        int(1000 + cpu * 10 + random.randint(-200, 200))
        for cpu in cpu_usage
    ]
    
    df = pd.DataFrame({
        'timestamp': timestamps,
        'cpu_usage': [round(c, 2) for c in cpu_usage],
        'memory_usage': [round(m, 2) for m in memory_usage],
        'error_rate': [round(e, 4) for e in error_rates],
        'events_per_second': events_per_sec
    })
    
    return df


def save_exercise3_data(events_csv='events_cleaned.csv'):
    """
    Generate and save all Exercise 3 data files.
    
    Assumes events_cleaned.csv already exists from Exercise 2.
    Creates users.csv and system_metrics.csv
    """
    
    # Generate users and metrics
    df_users = generate_users(200)
    df_metrics = generate_system_metrics(100)
    
    # Save
    df_users.to_csv('users.csv', index=False)
    print("✓ Generated users.csv with 200 users")
    
    df_metrics.to_csv('system_metrics.csv', index=False)
    print("✓ Generated system_metrics.csv with 100 metrics")
    
    # Show samples
    print("\n\nUsers Sample:")
    print(df_users.head())
    
    print("\n\nSystem Metrics Sample:")
    print(df_metrics.head())
    
    return df_users, df_metrics


if __name__ == "__main__":
    print("Exercise 3: Data Generation")
    print("=" * 60)
    
    # Generate the data
    df_users, df_metrics = save_exercise3_data()
    
    print("\n\nGeneration Summary:")
    print("=" * 60)
    print(f"Users: {len(df_users)}")
    print(f"  Regions: {df_users['region'].nunique()}")
    print(f"  Account types: {df_users['account_type'].nunique()}")
    
    print(f"\nSystem Metrics: {len(df_metrics)}")
    print(f"  Time range: {df_metrics['timestamp'].min()} to {df_metrics['timestamp'].max()}")
    
    print("\n✓ Ready for Exercise 3!")
