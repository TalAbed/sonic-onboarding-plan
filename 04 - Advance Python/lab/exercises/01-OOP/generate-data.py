#!/usr/bin/env python3
"""Generate sample event data for Exercise 1."""

import csv
import random
from datetime import datetime, timedelta

# Configuration
NUM_EVENTS = 100
OUTPUT_FILE = 'events_raw.csv'

# Sample data
EVENT_TYPES = ['purchase', 'login', 'checkout', 'view']
STATUSES = ['ok', 'error', 'timeout']
USER_IDS = [f'user_{i}' for i in range(1, 20)]

def generate_events(num_events):
    """Generate sample events.
    
    Args:
        num_events: Number of events to generate
        
    Returns:
        List of event dictionaries
    """
    events = []
    base_time = datetime(2026, 1, 15, 0, 0, 0)
    
    for i in range(num_events):
        event = {
            'event_id': i + 1,
            'timestamp': (base_time + timedelta(seconds=i*10)).isoformat(),
            'event_type': random.choice(EVENT_TYPES),
            'user_id': random.choice(USER_IDS),
            'status': random.choice(STATUSES),
            'latency_ms': random.randint(50, 2000)
        }
        events.append(event)
    
    return events

def write_csv(events, filename):
    """Write events to CSV file.
    
    Args:
        events: List of event dictionaries
        filename: Output CSV filename
    """
    fieldnames = ['event_id', 'timestamp', 'event_type', 'user_id', 'status', 'latency_ms']
    
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)
    
    print(f"✓ Generated {len(events)} events in {filename}")

if __name__ == '__main__':
    print("=" * 60)
    print("EXERCISE 1: DATA GENERATION")
    print("=" * 60)
    
    events = generate_events(NUM_EVENTS)
    write_csv(events, OUTPUT_FILE)
    
    print("\n✓ Sample data ready for Exercise 1!")
    print(f"  File: {OUTPUT_FILE}")
    print(f"  Events: {NUM_EVENTS}")
    print(f"  Columns: event_id, timestamp, event_type, user_id, status, latency_ms")
    print("\nYou can now run: python exercise-1-solution.py")

