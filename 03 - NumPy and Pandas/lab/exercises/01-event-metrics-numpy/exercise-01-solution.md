# Exercise 1: Solution

Here's a reference solution for Exercise 1. Your approach might differ—that's fine as long as it works correctly!

## Complete Solution

```python
import numpy as np
import time
from sample_data import generate_latencies


# ============================================================
# PART 1: DATA SETUP
# ============================================================

# Step 1: Generate the data
latencies = generate_latencies(1000)

# Step 2: Explore the array
print("=" * 60)
print("PART 1: DATA SETUP")
print("=" * 60)
print(f"Shape: {latencies.shape}")
print(f"Size: {latencies.size}")
print(f"Data type: {latencies.dtype}")
print(f"Min value: {latencies.min()} ms")
print(f"Max value: {latencies.max()} ms")
print(f"First 10 values: {latencies[:10]}")


# ============================================================
# PART 2: BASIC STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("PART 2: BASIC STATISTICS")
print("=" * 60)

# Step 3: Calculate central tendency
mean_latency = np.mean(latencies)
median_latency = np.median(latencies)
std_latency = np.std(latencies)

print(f"Mean latency: {mean_latency:.2f} ms")
print(f"Median latency: {median_latency:.2f} ms")
print(f"Standard deviation: {std_latency:.2f} ms")

# Step 4: Calculate percentiles
p50 = np.percentile(latencies, 50)
p95 = np.percentile(latencies, 95)
p99 = np.percentile(latencies, 99)

print(f"\nPercentiles:")
print(f"p50 (50th percentile): {p50:.2f} ms")
print(f"p95 (95th percentile): {p95:.2f} ms")
print(f"p99 (99th percentile): {p99:.2f} ms")


# ============================================================
# PART 3: FILTERING AND CATEGORIZATION
# ============================================================

print("\n" + "=" * 60)
print("PART 3: FILTERING AND CATEGORIZATION")
print("=" * 60)

# Step 5: Find slow events
slow_events = latencies[latencies > 500]
very_slow_events = latencies[latencies > 1000]

slow_count = len(slow_events)
very_slow_count = len(very_slow_events)
total_count = len(latencies)

slow_percentage = (slow_count / total_count) * 100
very_slow_percentage = (very_slow_count / total_count) * 100

print(f"Events > 500ms: {slow_count} ({slow_percentage:.1f}%)")
print(f"Events > 1000ms: {very_slow_count} ({very_slow_percentage:.1f}%)")

# Step 6: Categorize all events
fast = latencies[latencies <= 200]
normal = latencies[(latencies > 200) & (latencies <= 500)]
slow = latencies[(latencies > 500) & (latencies <= 1000)]
very_slow = latencies[latencies > 1000]

print(f"\nLatency Distribution:")
print(f"Fast (0-200ms): {len(fast)} events ({len(fast)/total_count*100:.1f}%)")
print(f"Normal (200-500ms): {len(normal)} events ({len(normal)/total_count*100:.1f}%)")
print(f"Slow (500-1000ms): {len(slow)} events ({len(slow)/total_count*100:.1f}%)")
print(f"Very Slow (1000+ms): {len(very_slow)} events ({len(very_slow)/total_count*100:.1f}%)")


# ============================================================
# PART 4: ANOMALY DETECTION
# ============================================================

print("\n" + "=" * 60)
print("PART 4: ANOMALY DETECTION")
print("=" * 60)

# Step 7: Calculate z-scores
z_scores = np.abs((latencies - mean_latency) / std_latency)

# Find anomalies (|z-score| > 2)
anomalies = latencies[z_scores > 2]

anomaly_count = len(anomalies)
anomaly_percentage = (anomaly_count / total_count) * 100

print(f"Anomalies detected: {anomaly_count} ({anomaly_percentage:.2f}%)")
print(f"Anomaly latencies (first 10): {anomalies[:10]}")

# Step 8: Get indices of anomalies
anomaly_indices = np.where(z_scores > 2)[0]
print(f"Anomaly indices (first 10): {anomaly_indices[:10]}")


# ============================================================
# PART 5: PERFORMANCE COMPARISON
# ============================================================

print("\n" + "=" * 60)
print("PART 5: PERFORMANCE COMPARISON")
print("=" * 60)

# Step 9: NumPy vs Python loops for simple operation
start = time.time()
python_sum = 0
for latency in latencies:
    python_sum += latency
python_mean = python_sum / len(latencies)
python_time = time.time() - start

start = time.time()
numpy_mean = np.mean(latencies)
numpy_time = time.time() - start

speedup = python_time / numpy_time if numpy_time > 0 else float('inf')

print(f"\nSingle Operation (Calculate Mean):")
print(f"Python loops: {python_time*1000:.4f} ms")
print(f"NumPy: {numpy_time*1000:.4f} ms")
print(f"Speedup: {speedup:.0f}x faster with NumPy")
```

---

## Expected Output

When you run this code, you should see output similar to:

```
============================================================
PART 1: DATA SETUP
============================================================
Shape: (1000,)
Size: 1000
Data type: int64
Min value: 50 ms
Max value: 1933 ms
First 10 values: [368 297 396 399 421 340 449 370 364 280]

============================================================
PART 2: BASIC STATISTICS
============================================================
Mean latency: 354.32 ms
Median latency: 337.00 ms
Standard deviation: 223.45 ms

Percentiles:
p50 (50th percentile): 337.00 ms
p95 (95th percentile): 743.05 ms
p99 (99th percentile): 1284.18 ms

============================================================
PART 3: FILTERING AND CATEGORIZATION
============================================================
Events > 500ms: 49 (4.9%)
Events > 1000ms: 5 (0.5%)

Latency Distribution:
Fast (0-200ms): 157 events (15.7%)
Normal (200-500ms): 784 events (78.4%)
Slow (500-1000ms): 44 events (4.4%)
Very Slow (1000+ms): 15 events (1.5%)

============================================================
PART 4: ANOMALY DETECTION
============================================================
Anomalies detected: 47 (4.70%)
Anomaly latencies (first 10): [1933 1895 1834 1721 1692 1681 1647 1634 1627 1615]
Anomaly indices (first 10): [18 39 62 67 69 75 76 78 82 85]

============================================================
PART 5: PERFORMANCE COMPARISON
============================================================

Single Operation (Calculate Mean):
Python loops: 0.2341 ms
NumPy: 0.0012 ms
Speedup: 195x faster with NumPy

Full Analysis (All Statistics):
Time with NumPy: 0.0034 ms

This is why data engineers love NumPy! 🚀

============================================================
FINAL SUMMARY
============================================================
Mean latency: 354.32 ms
p95 latency: 743.05 ms (SLA target)
p99 latency: 1284.18 ms (worst case)
Slow events (>500ms): 49
Anomalies detected: 47
```

---

## Key Patterns Used

### Pattern 1: Array Operations

```python
# Boolean indexing to filter
slow_events = latencies[latencies > 500]

# Multiple conditions
normal = latencies[(latencies > 200) & (latencies <= 500)]
```

### Pattern 2: Statistical Functions

```python
# All built-in NumPy functions
mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)
p95 = np.percentile(arr, 95)
```

### Pattern 3: Vectorized Calculations

```python
# Calculate z-scores for entire array at once
z_scores = np.abs((latencies - mean_latency) / std_latency)

# Find indices where condition is true
indices = np.where(z_scores > 2)[0]
```

---

## What This Teaches You

### Real-World Application

This exact pattern is used in:
- **SLA monitoring** - Track if we're meeting latency targets
- **Performance dashboards** - Show operators current health
- **Alerting systems** - Page engineers when things degrade
- **Capacity planning** - Understand where bottlenecks are

### Programming Concepts

✅ **Vectorization** - Operating on entire arrays instead of loops  
✅ **Boolean indexing** - Filtering data elegantly  
✅ **Built-in functions** - Using NumPy's optimized operations  
✅ **Statistical analysis** - Understanding data distributions  
✅ **Performance measurement** - Comparing approaches quantitatively  

### Data Engineering Skills

✅ **Understanding metrics** - What percentiles mean and why they matter  
✅ **Anomaly detection** - Using statistics to find unusual values  
✅ **Communication** - Presenting results clearly  
✅ **Optimization** - Choosing the right tools for the job  

---

## Variations and Extensions

**Try these to deepen your understanding:**

1. **Time More Operations**
   ```python
   # Time percentile calculation with Python loops vs NumPy
   ```

2. **Analyze Anomaly Patterns**
   ```python
   # Are anomalies clustered at the beginning/end/middle of data?
   # What times do they occur?
   ```

3. **Change the Distribution**
   ```python
   # What if we change the sample_data.py generator?
   # Make data slower, faster, more/less variable
   ```

4. **Create a Report**
   ```python
   # Combine all statistics into a formatted report
   # Add interpretation of what each metric means
   ```

---

## Comparison: Your Code vs This Solution

**Differences are fine!** Look for:

✅ Did you use the same NumPy functions?  
✅ Did you filter correctly with boolean indexing?  
✅ Are your percentages approximately the same?  
✅ Did you calculate speedup?  

**Your code might:**
- Use different variable names (totally fine)
- Calculate things in different order (totally fine)
- Use different filtering approaches (totally fine, if correct)
- Have different formatting (totally fine)

**As long as:**
- Results are numerically correct
- You used NumPy for the heavy lifting
- Code is readable and commented
- You demonstrated understanding

You nailed it! 🎉

---

## Next Steps

1. ✅ Compare your output to expected output above
2. ✅ Understand any numerical differences
3. ✅ Notice the patterns you used
4. ✅ Prepare for Exercise 2 (pandas and data cleaning)

**Congratulations on completing Exercise 1!** 🚀
