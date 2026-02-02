# Exercise 1: Instructions

Follow these steps to complete Exercise 1. Don't look at the solution.md until you've tried these on your own.

## Part 1: Data Setup

### Step 1: Generate the Data

You'll use a helper script to generate realistic latency data.

**What to do:**
- Open the file `sample_data.py`
- This file generates 1,000 realistic latency measurements
- Import it and generate your data

**Your code should:**
```python
# Import NumPy
import numpy as np

# Import the data generator
from sample_data import generate_latencies

# Generate 1,000 latency measurements
latencies = generate_latencies(1000)

# Print first few values to see what you're working with
print("First 10 latencies:")
print(latencies[:10])
print(f"\nTotal events: {len(latencies)}")
print(f"Data type: {latencies.dtype}")
```

**What to expect:**
- An array of 1,000 integer values
- Values in range roughly 50ms to 2000ms
- Array shape should be `(1000,)`

### Step 2: Explore the Array

**Your code should:**
```python
# Check array properties
print(f"Shape: {latencies.shape}")
print(f"Size: {latencies.size}")
print(f"Data type: {latencies.dtype}")
print(f"Min value: {latencies.min()}")
print(f"Max value: {latencies.max()}")
```

**What to expect:**
- Min around 50-100ms
- Max around 1500-2000ms
- All integers, all positive

---

## Part 2: Basic Statistics

### Step 3: Calculate Central Tendency

Calculate where most latencies fall.

**Your code should calculate:**
1. **Mean (average)** - Sum all values, divide by count
2. **Median (middle value)** - 50th percentile
3. **Standard Deviation** - How spread out the values are

**Hint:** NumPy has built-in functions for all of these.

**What to expect:**
- Mean probably around 400-600ms
- Median might be lower (some very slow events pull mean up)
- Std dev tells you how much variation exists

### Step 4: Calculate Percentiles

Percentiles tell you: "X% of events are faster than this value"

**Your code should calculate:**
1. **p50** - 50th percentile (median, already calculated)
2. **p95** - 95th percentile (SLA target)
3. **p99** - 99th percentile (worst case)

**What to expect:**
- p50 < p95 < p99 (percentiles should increase)
- p95 probably around 500-800ms
- p99 probably around 1000-1500ms

---

## Part 3: Filtering and Categorization

### Step 5: Find Slow Events

Events exceeding SLA thresholds need investigation.

**Your code should:**
1. Find all events slower than 500ms
2. Find all events slower than 1000ms
3. Count how many fall into each category

**What to expect:**
- ~5% of events > 500ms (roughly matches "95% < 500ms")
- ~1% of events > 1000ms (roughly matches "99% < 1000ms")

### Step 6: Categorize All Events

Create buckets: Fast, Normal, Slow, Very Slow

**Your code should:**
- Count events in ranges: 0-200ms, 200-500ms, 500-1000ms, 1000+ms
- Use boolean indexing for each range

**What to expect:**
- Most events in "Normal" or "Slow" range
- Very few in "Very Slow"
- Total should equal 1,000

---

## Part 4: Anomaly Detection

### Step 7: Calculate Z-Scores

Z-score measures how far a value is from the mean (in standard deviations).

**Formula:** `z = (value - mean) / std_dev`

**Your code should:**
1. Calculate z-score for every latency
2. Find outliers (|z-score| > 2)
3. Return the original latency values of these outliers

**What to expect:**
- Roughly 5% of events are anomalies (statistical expectation)
- Anomalies are in the extreme ranges (very fast or very slow)
- Most will be very slow (>1000ms)

### Step 8: Get Indices of Anomalies

Sometimes you need to know WHERE in the data anomalies occurred (for time-series analysis).

**Your code should:**
1. Find the indices (positions) of anomalous events
2. Print a few examples

**What to expect:**
- Indices scattered throughout the array

---

## Part 5: Performance Comparison

### Step 9: NumPy vs Python Loops

Show why NumPy is faster for this work.

**Your code should:**
1. Use a Python loop to calculate Mean
2. Use NumPy (already done above)
3. Compare execution time
4. Print the speedup factor

**What to expect:**
- NumPy probably completes in microseconds
- Python takes milliseconds
- NumPy is 100-1000x faster!

## Summary

You've now completed Exercise 1! You:

✅ Created and explored NumPy arrays  
✅ Calculated statistical summaries  
✅ Filtered data with boolean indexing  
✅ Detected anomalies  
✅ Compared NumPy performance vs Python  

**Key Takeaways:**
- NumPy arrays are much faster than Python lists
- Vectorization (operating on entire arrays) is powerful
- Boolean indexing lets you filter elegantly
- Statistical functions are built-in and fast

---

## Next Steps

1. Compare your code with [exercise-01-solution.md](./exercise-01-solution.md)
2. Understand any differences
3. Notice patterns you'll reuse
4. Move to **Exercise 2** when ready

**Great work!** 🎉
