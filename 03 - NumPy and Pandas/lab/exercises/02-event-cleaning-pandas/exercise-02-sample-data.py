"""
Sample data generator for Exercise 2.

This script generates a messy CSV file with intentional data quality issues.
It simulates real event data from the Sonic pipeline.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def generate_messy_events(n_events=1000, seed=42):
    """
    Generate a DataFrame with intentional data quality issues.
    
    Parameters:
        n_events: Number of events to generate
        seed: Random seed for reproducibility
    
    Returns:
        DataFrame with messy event data
    
    Issues included:
    - Missing values in various columns
    - Wrong data types (latency as string "N/A")
    - Duplicate rows
    - Invalid status values
    - Future/suspicious timestamps
    """
    
    random.seed(seed)
    np.random.seed(seed)
    
    # Base data
    base_timestamp = datetime(2026, 1, 15, 0, 0, 0)
    
    event_ids = list(range(1, n_events + 1))
    
    # Generate timestamps
    timestamps = [
        (base_timestamp + timedelta(seconds=random.randint(0, 86400))).strftime("%Y-%m-%d %H:%M:%S")
        for _ in range(n_events)
    ]
    
    # Add some future dates (invalid)
    for i in random.sample(range(n_events), int(n_events * 0.02)):
        timestamps[i] = (datetime(2050, 1, 15) + timedelta(seconds=random.randint(0, 86400))).strftime("%Y-%m-%d %H:%M:%S")
    
    # Event types (with some missing)
    event_types = []
    valid_types = ["purchase", "login", "checkout", "view"]
    for i in range(n_events):
        if random.random() < 0.05:  # 5% missing
            event_types.append(np.nan)
        elif random.random() < 0.03:  # 3% invalid
            event_types.append("invalid_type")
        else:
            event_types.append(random.choice(valid_types))
    
    # User IDs (with some missing)
    user_ids = []
    for i in range(n_events):
        if random.random() < 0.02:  # 2% missing
            user_ids.append(np.nan)
        else:
            user_ids.append(f"user_{random.randint(100, 999)}")
    
    # Status values (with some missing and invalid)
    statuses = []
    valid_statuses = ["ok", "error", "timeout"]
    for i in range(n_events):
        if random.random() < 0.03:  # 3% missing
            statuses.append(np.nan)
        elif random.random() < 0.02:  # 2% invalid
            statuses.append("failed")  # Invalid status
        else:
            statuses.append(random.choice(valid_statuses))
    
    # Latency values (with some as strings "N/A", some missing)
    latencies = []
    for i in range(n_events):
        if random.random() < 0.05:  # 5% N/A strings
            latencies.append("N/A")
        elif random.random() < 0.02:  # 2% missing
            latencies.append(np.nan)
        elif random.random() < 0.01:  # 1% invalid text
            latencies.append("timeout")
        else:
            latencies.append(random.randint(50, 2000))
    
    # Create DataFrame
    df = pd.DataFrame({
        'event_id': event_ids,
        'timestamp': timestamps,
        'event_type': event_types,
        'user_id': user_ids,
        'status': statuses,
        'latency_ms': latencies
    })
    
    # Add some exact duplicates (rows 10-15 are duplicates of 5-10)
    duplicates = df.iloc[5:11].copy()
    df = pd.concat([df, duplicates], ignore_index=True)
    
    # Shuffle
    df = df.sample(frac=1.0, random_state=seed).reset_index(drop=True)
    
    return df


def save_messy_events(filename='events_raw.csv', n_events=1000):
    """Generate and save messy event data to CSV."""
    df = generate_messy_events(n_events)
    df.to_csv(filename, index=False)
    print(f"Generated {filename} with {len(df)} events")
    print(f"Columns: {', '.join(df.columns)}")
    return df


if __name__ == "__main__":
    # Generate and show sample
    df = generate_messy_events(1000)
    
    print("Messy Event Data Sample")
    print("=" * 60)
    print(f"Total rows: {len(df)}")
    print(f"\nFirst 10 rows:")
    print(df.head(10))
    
    print(f"\n\nData Info:")
    print(df.info())
    
    print(f"\n\nMissing Values:")
    print(df.isnull().sum())
    
    print(f"\n\nUnique Event Types:")
    print(df['event_type'].value_counts(dropna=False))
    
    print(f"\n\nUnique Statuses:")
    print(df['status'].value_counts(dropna=False))
    
    # Save it
    df.to_csv('events_raw.csv', index=False)
    print("\n\nSaved to events_raw.csv")
