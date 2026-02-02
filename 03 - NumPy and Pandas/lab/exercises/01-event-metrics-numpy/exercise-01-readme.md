# Exercise 1: Event Metrics Processing with NumPy

Welcome to your first Sonic NumPy exercise! In this exercise, you'll process demo event data using NumPy arrays.

## What You'll Do

You have **1,000 event latency measurements** (in milliseconds) from a pipeline collected over one hour. Your job is to:

1. Load the latency data into a NumPy array
2. Calculate key statistics (mean, median, standard deviation, percentiles)
3. Filter and categorize events by latency
4. Detect performance anomalies
5. Compare NumPy performance vs Python loops

## Why This Matters

Our pipelines may process thousands of events per hour. Understanding latency distribution helps us:
- Identify performance bottlenecks
- Detect when the system is degrading
- Validate that optimizations actually work
- Alert when something goes wrong

NumPy's vectorization makes this analysis **100x faster** than Python loops.

## Difficulty: Beginner-Intermediate
## Time Estimate: 30-40 minutes
## Concepts Covered:
- ✅ NumPy array creation
- ✅ Array indexing and slicing
- ✅ Vectorized operations
- ✅ Boolean indexing and filtering
- ✅ Aggregate functions (mean, median, std, percentiles)
- ✅ Statistical analysis (z-scores)
- ✅ Performance comparison (NumPy vs Python loops)

## How to Approach This

1. **Read this file completely** - Understand the task ahead of you
2. **Follow the [instruction file](./exercise-01-instructions.md)** - Step by step guidance
3. **Write your own code** - Don't look at the solution yet
4. **Test as you go** - Print intermediate results
5. **Compare with the [solution file](./exercise-01-solution.md)** - See how it was done professionally

## Learning Objectives

By the end of this exercise, you will:

✅ Understand NumPy array operations deeply  
✅ Know how to filter arrays with boolean indexing  
✅ Calculate statistics on large datasets  
✅ Appreciate NumPy's performance advantages  
✅ Write code that production engineers would use  

## Data Structure

You'll work with latency data:

```python
# Sample of what the data looks like (1,000 values total)
latencies = [120, 450, 95, 610, 280, 190, 1100, 150, 340, ...]

# In milliseconds (ms)
# Range: typically 50ms to 2000ms
```

## Key Patterns You'll Learn

### Pattern 1: Vectorized Operations
```python
# SLOW (Python loop)
results = []
for latency in latencies:
    results.append(latency * 1.5)

# FAST (NumPy - what you'll use)
results = latencies * 1.5  # Entire array at once!
```

### Pattern 2: Boolean Indexing
```python
# Find slow events (> 500ms)
slow_events = latencies[latencies > 500]  # NumPy magic!
```

### Pattern 3: Statistics
```python
# Get percentile 95
p95 = np.percentile(latencies, 95)  # One line!
```

## Real-World Application

After this exercise, you'll use these exact patterns to:
- Monitor pipeline performance
- Generate SLA reports
- Detect anomalies automatically
- Debug performance issues
- Build dashboards

This isn't a toy problem—it's how real data engineers work.

## Before You Start

Make sure you have:
- ✅ Completed Python Fundamentals Lab
- ✅ Watched NumPy video (Bro Code - 1 hour)
- ✅ Read NumPy Fundamentals Reference Guide
- ✅ NumPy installed (`pip install numpy`)
- ✅ PyCharm or Jupyter running

## Tips for Success

✅ **Understand the goal first** - Why are we calculating each statistic?  
✅ **Test frequently** - Print results after each step  
✅ **Use the reference guide** - Don't memorize, look things up  
✅ **Ask questions** - If something doesn't make sense, ask  
✅ **Experiment** - Try variations on the code  

## Ready?

1. Open [exercise-01-instructions.md](./exercise-01-instructions.md) - Follow the step-by-step guide
2. Write your code in PyCharm or Jupyter
3. Test and validate each step
4. When done, compare with [exercise-01-solution.md](./exercise-01-solution.md)
5. Learn from any differences

**You've got this!** Let's process some data! 🚀📊

