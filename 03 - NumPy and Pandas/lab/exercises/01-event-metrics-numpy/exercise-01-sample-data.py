"""
Sample data generator for Exercise 1.

This module generates realistic event latency data
simulating what you'd see in the Sonic pipeline.
"""

import numpy as np


def generate_latencies(n_events=1000, seed=42):
    """
    Generate realistic latency measurements for Sonic events.
    
    Parameters:
        n_events: Number of latency measurements to generate
        seed: Random seed for reproducibility (same data each time)
    
    Returns:
        NumPy array of latencies in milliseconds
    
    Distribution:
        - Most events: 100-400ms (normal operation)
        - Some events: 400-800ms (occasional slowness)
        - Few events: 800-2000ms (rare, very slow)
    """
    
    # Set seed for reproducibility
    np.random.seed(seed)
    
    # Generate from normal distribution
    # Mean around 350ms, std dev around 200ms
    latencies = np.random.normal(loc=350, scale=180, size=n_events)
    
    # Add some outliers (very slow events, rare)
    # ~5% of events should be very slow
    n_outliers = int(n_events * 0.05)
    outlier_indices = np.random.choice(n_events, n_outliers, replace=False)
    latencies[outlier_indices] = np.random.uniform(1000, 2000, n_outliers)
    
    # Ensure all values are positive and convert to integers
    latencies = np.maximum(latencies, 50)  # Minimum 50ms
    latencies = latencies.astype(int)
    
    return latencies


if __name__ == "__main__":
    # Test: Generate and display sample data
    latencies = generate_latencies(1000)
    
    print("Sample Latency Data Generated")
    print(f"Total events: {len(latencies)}")
    print(f"First 10 latencies: {latencies[:10]}")
    print(f"Mean: {latencies.mean():.2f} ms")
    print(f"Median: {np.median(latencies):.2f} ms")
    print(f"Min: {latencies.min()} ms")
    print(f"Max: {latencies.max()} ms")
