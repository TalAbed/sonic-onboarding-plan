# NumPy Fundamentals Reference Guide

## Overview

This comprehensive guide covers essential NumPy concepts every Sonic team member needs to know. Use this as a reference while learning and building data pipelines. Examples are practical and relevant to data engineering work.

NumPy is the foundation for numerical computing in Python. It provides efficient arrays and operations that are orders of magnitude faster than Python lists for numerical work.

## Table of Contents

1. [Installation and Setup](#installation-and-setup)
2. [NumPy Basics](#numpy-basics)
3. [Creating Arrays](#creating-arrays)
4. [Array Attributes](#array-attributes)
5. [Indexing and Slicing](#indexing-and-slicing)
6. [Arithmetic Operations](#arithmetic-operations)
7. [Broadcasting](#broadcasting)
8. [Aggregate Functions](#aggregate-functions)
9. [Boolean Indexing and Filtering](#boolean-indexing-and-filtering)
10. [Reshaping and Reorganizing](#reshaping-and-reorganizing)
11. [Random Numbers](#random-numbers)
12. [Common Patterns for Data Engineering](#common-patterns-for-data-engineering)

---

## Installation and Setup

### Install NumPy

```bash
# Using pip
pip install numpy

# Or using conda
conda install numpy
```

### Import NumPy

```python
import numpy as np  # Standard convention - use 'np' as alias
```

### Check Installation

```python
import numpy as np
print(np.__version__)  # Check version
print(np.show_config())  # Check configuration
```

---

## NumPy Basics

### What is a NumPy Array?

A NumPy array is a multidimensional grid of numbers. Think of it like a list, but more powerful:

```python
# Python list (slow)
python_list = [1, 2, 3, 4, 5]

# NumPy array (fast)
numpy_array = np.array([1, 2, 3, 4, 5])
```

**Why NumPy arrays?**
- ✅ Much faster (optimized C code)
- ✅ Less memory (compact storage)
- ✅ Easier to work with (vectorized operations)
- ✅ Mathematical functions built-in

### Key Concepts

**ndarray**: NumPy's main object - an N-dimensional array (1D, 2D, 3D, etc.)

```python
# 1D array (vector)
arr_1d = np.array([1, 2, 3, 4, 5])

# 2D array (matrix)
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

# 3D array (tensor)
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
```

---

## Creating Arrays

### From Lists

```python
# 1D array from list
arr = np.array([1, 2, 3, 4, 5])

# 2D array from list of lists
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Specify data type
arr = np.array([1, 2, 3], dtype=float)  # [1., 2., 3.]
```

### Using Built-in Functions

```python
# Array of zeros
zeros = np.zeros(5)           # [0. 0. 0. 0. 0.]
zeros_2d = np.zeros((3, 4))   # 3x4 matrix of zeros

# Array of ones
ones = np.ones(5)             # [1. 1. 1. 1. 1.]
ones_2d = np.ones((3, 4))     # 3x4 matrix of ones

# Array of a specific value
filled = np.full(5, 7)        # [7 7 7 7 7]
filled_2d = np.full((3, 4), 5)

# Array of a range
range_arr = np.arange(0, 10, 2)  # [0 2 4 6 8]
# np.arange(start, stop, step) like range()

# Array with evenly spaced values
linspace = np.linspace(0, 10, 5)  # [0. 2.5 5. 7.5 10.]
# 5 values from 0 to 10 (inclusive)

# Identity matrix (diagonal 1s)
identity = np.eye(3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

### Random Arrays

```python
# Random values between 0 and 1
random_vals = np.random.rand(5)        # 1D array
random_2d = np.random.rand(3, 4)       # 3x4 array

# Random integers
random_ints = np.random.randint(0, 10, 5)  # 5 ints from 0-9

# Random from normal distribution
normal = np.random.randn(5)  # Gaussian distribution

# Set seed for reproducibility
np.random.seed(42)
random_vals = np.random.rand(5)  # Same result every time
```

---

## Array Attributes

### Shape, Size, and Dtype

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Shape: dimensions
print(arr.shape)      # (2, 3) - 2 rows, 3 columns

# Size: total number of elements
print(arr.size)       # 6

# Ndim: number of dimensions
print(arr.ndim)       # 2

# Dtype: data type of elements
print(arr.dtype)      # int64

# Itemsize: bytes per element
print(arr.itemsize)   # 8

# Nbytes: total bytes used
print(arr.nbytes)     # 48
```

### Data Types

```python
# Common data types
int_arr = np.array([1, 2, 3], dtype=np.int32)
float_arr = np.array([1.5, 2.5], dtype=np.float64)
bool_arr = np.array([True, False], dtype=bool)
complex_arr = np.array([1+2j, 3+4j], dtype=np.complex128)

# Check dtype
print(arr.dtype)

# Convert dtype
arr_float = arr.astype(float)  # Convert to float
arr_int = arr_float.astype(int)  # Convert to int
```

---

## Indexing and Slicing

### 1D Array Indexing

```python
arr = np.array([10, 20, 30, 40, 50])

# Access by index
print(arr[0])      # 10 (first element)
print(arr[-1])     # 50 (last element)
print(arr[-2])     # 40 (second to last)
```

### 1D Array Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

# Slice: arr[start:stop:step]
print(arr[1:4])      # [20 30 40] (indices 1,2,3)
print(arr[::2])      # [10 30 50] (every 2nd element)
print(arr[::-1])     # [50 40 30 20 10] (reversed)
print(arr[1:])       # [20 30 40 50] (from index 1 to end)
print(arr[:3])       # [10 20 30] (first 3 elements)
```

### 2D Array Indexing

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Access element
print(arr[0, 0])     # 1 (row 0, col 0)
print(arr[1, 2])     # 6 (row 1, col 2)
print(arr[-1, -1])   # 9 (last row, last col)

# Access entire row
print(arr[0])        # [1 2 3] (first row)
print(arr[1, :])     # [4 5 6] (second row, all columns)

# Access entire column
print(arr[:, 0])     # [1 4 7] (all rows, first column)

# Access subarray
print(arr[0:2, 1:3]) # [[2 3]
                     #  [5 6]]
```

### Modify Elements

```python
arr = np.array([1, 2, 3, 4, 5])

# Modify single element
arr[0] = 10         # [10 2 3 4 5]

# Modify slice
arr[1:4] = 0        # [10 0 0 0 5]

# Modify 2D array
arr_2d = np.zeros((3, 3))
arr_2d[0, :] = [1, 2, 3]  # Set first row
arr_2d[:, 1] = [4, 5, 6]  # Set second column
```

---

## Arithmetic Operations

### Element-wise Operations

```python
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Addition
result = arr1 + arr2           # [6 8 10 12]

# Subtraction
result = arr1 - arr2           # [-4 -4 -4 -4]

# Multiplication
result = arr1 * arr2           # [5 12 21 32]

# Division
result = arr1 / arr2           # [0.2  0.333  0.428  0.5]

# Exponentiation
result = arr1 ** 2             # [1 4 9 16]

# Modulo
result = arr1 % 2              # [1 0 1 0]
```

### Operations with Scalars

```python
arr = np.array([1, 2, 3, 4])

# Scalar operations
result = arr + 10              # [11 12 13 14]
result = arr * 2               # [2 4 6 8]
result = 10 / arr              # [10. 5. 3.33 2.5]
```

### Mathematical Functions

```python
arr = np.array([1, 4, 9, 16])

# Square root
result = np.sqrt(arr)          # [1. 2. 3. 4.]

# Exponential
result = np.exp(arr)           # [e^1, e^4, e^9, e^16]

# Logarithm
result = np.log(arr)           # [0. 1.386 2.197 2.773]

# Trigonometric
result = np.sin(arr)
result = np.cos(arr)
result = np.tan(arr)

# Absolute value
arr = np.array([-1, -2, 3, -4])
result = np.abs(arr)           # [1 2 3 4]

# Rounding
arr = np.array([1.2, 1.5, 1.8])
result = np.round(arr)         # [1. 2. 2.]
result = np.floor(arr)         # [1. 1. 1.]
result = np.ceil(arr)          # [2. 2. 2.]
```

---

## Broadcasting

Broadcasting allows NumPy to perform operations on arrays of different shapes. It's one of NumPy's most powerful features.

### Basic Broadcasting

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])   # Shape (2, 3)

scalar = 5
result = arr + scalar          # Add 5 to each element
# [[6 7 8]
#  [9 10 11]]

# The scalar is "broadcasted" to match the array shape
```

### Broadcasting Rules

When operating on two arrays, NumPy compares shapes dimension by dimension:

```python
# Array shape (2, 3)
arr_1 = np.array([[1, 2, 3],
                  [4, 5, 6]])

# Array shape (3,) - broadcasts to (2, 3)
arr_2 = np.array([10, 20, 30])

result = arr_1 + arr_2
# [[11 22 33]
#  [14 25 36]]

# arr_2 is repeated for each row to match arr_1 shape
```

### More Broadcasting Examples

```python
# Column vs row
col = np.array([[1], [2], [3]])    # Shape (3, 1)
row = np.array([1, 2, 3])          # Shape (3,)

result = col + row
# [[2 3 4]
#  [3 4 5]
#  [4 5 6]]
```

---

## Aggregate Functions

### Summary Statistics

```python
arr = np.array([1, 2, 3, 4, 5])

# Sum
total = np.sum(arr)            # 15
print(sum(arr))                # Also works: 15

# Mean (average)
average = np.mean(arr)         # 3.0
print(arr.mean())              # Also works: 3.0

# Median
median = np.median(arr)        # 3.0

# Standard deviation
std = np.std(arr)              # 1.414...

# Variance
var = np.var(arr)              # 2.0

# Minimum and maximum
min_val = np.min(arr)          # 1
max_val = np.max(arr)          # 5

# Min/max indices
min_idx = np.argmin(arr)       # 0
max_idx = np.argmax(arr)       # 4
```

### Operations on 2D Arrays

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Operations on entire array
total = np.sum(arr)            # 21

# Operations along axis 0 (down columns)
col_sum = np.sum(arr, axis=0)  # [5 7 9]
col_mean = np.mean(arr, axis=0) # [2.5 3.5 4.5]

# Operations along axis 1 (across rows)
row_sum = np.sum(arr, axis=1)  # [6 15]
row_mean = np.mean(arr, axis=1) # [2. 5.]
```

### Cumulative Operations

```python
arr = np.array([1, 2, 3, 4, 5])

# Cumulative sum
cumsum = np.cumsum(arr)        # [1 3 6 10 15]

# Cumulative product
cumprod = np.cumprod(arr)      # [1 2 6 24 120]
```

---

## Boolean Indexing and Filtering

### Creating Boolean Arrays

```python
arr = np.array([1, 2, 3, 4, 5])

# Comparison operations return boolean arrays
mask = arr > 2                 # [False False True True True]
print(mask)

mask = arr % 2 == 0            # [False True False True False]
print(mask)
```

### Filtering with Boolean Arrays

```python
arr = np.array([1, 2, 3, 4, 5])

# Use boolean array to filter
mask = arr > 2
filtered = arr[mask]           # [3 4 5]

# Combine with operations
result = arr[arr > 2]          # [3 4 5]
result = arr[arr % 2 == 0]     # [2 4]
```

### Combining Conditions

```python
arr = np.array([1, 2, 3, 4, 5])

# AND condition
mask = (arr > 2) & (arr < 5)   # [False False True True False]
result = arr[mask]             # [3 4]

# OR condition
mask = (arr < 2) | (arr > 4)   # [True False False False True]
result = arr[mask]             # [1 5]

# NOT condition
mask = ~(arr > 2)              # [True True False False False]
result = arr[mask]             # [1 2]
```

### Practical Filtering Example

```python
# Latency data from pipeline
latencies = np.array([120, 450, 95, 610, 280, 190, 1100])

# Find slow requests (> 300ms)
slow = latencies[latencies > 300]
print(slow)                    # [450 610 1100]

# Count slow requests
count = np.sum(latencies > 300)  # 3

# Get indices of slow requests
indices = np.where(latencies > 300)  # (array([1, 3, 6]),)
```

---

## Reshaping and Reorganizing

### Reshape

```python
arr = np.arange(12)            # [0 1 2 3 4 5 6 7 8 9 10 11]

# Reshape to 3x4
reshaped = arr.reshape(3, 4)
# [[0 1 2 3]
#  [4 5 6 7]
#  [8 9 10 11]]

# Reshape to 4x3
reshaped = arr.reshape(4, 3)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]
#  [9 10 11]]

# Reshape to 3D
reshaped = arr.reshape(2, 3, 2)
```

### Flatten and Ravel

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Flatten: returns copy
flat = arr.flatten()           # [1 2 3 4 5 6]

# Ravel: returns view (faster)
raveled = arr.ravel()          # [1 2 3 4 5 6]

# Difference: modifying ravel affects original, flatten doesn't
```

### Transpose

```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Transpose: swap rows and columns
transposed = arr.T
# [[1 4]
#  [2 5]
#  [3 6]]

# Or use np.transpose
transposed = np.transpose(arr)
```

### Stacking Arrays

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Stack vertically (rows)
stacked_v = np.vstack([arr1, arr2])
# [[1 2 3]
#  [4 5 6]]

# Stack horizontally (columns)
stacked_h = np.hstack([arr1, arr2])  # [1 2 3 4 5 6]

# Stack along new axis
stacked_depth = np.dstack([arr1, arr2])
```

---

## Random Numbers

### Generate Random Values

```python
# Random floats [0, 1)
rand = np.random.rand(5)       # [0.37, 0.95, 0.73, ...]

# Random integers
randint = np.random.randint(0, 10, 5)  # [7, 2, 8, 4, 9]
# Random ints from 0-9

# Normal distribution (Gaussian)
normal = np.random.randn(5)    # Centered at 0, std=1

# Uniform distribution
uniform = np.random.uniform(0, 10, 5)  # [0-10]

# Choice (random selection)
choice = np.random.choice([1, 2, 3, 4, 5], 3)  # Pick 3 from list
```

### Reproducibility

```python
# Set seed for reproducible results
np.random.seed(42)
arr1 = np.random.rand(3)       # [0.37, 0.95, 0.73]

# Reset seed to same value
np.random.seed(42)
arr2 = np.random.rand(3)       # Same as arr1: [0.37, 0.95, 0.73]
```

---

## Common Patterns for Data Engineering

### Processing Metrics

```python
# Event latencies from pipeline
latencies = np.array([120, 450, 95, 610, 280, 190, 1100])

# Basic statistics
avg_latency = np.mean(latencies)     # 406.4
p95_latency = np.percentile(latencies, 95)  # Slower approach

# Count by threshold
slow_count = np.sum(latencies > 500)  # 2 events > 500ms
acceptable = np.sum(latencies <= 300)  # 4 events <= 300ms

# Percentiles
p50 = np.percentile(latencies, 50)
p99 = np.percentile(latencies, 99)
```

### Aggregating Event Data

```python
# Response codes (1=success, 0=error)
responses = np.array([1, 0, 1, 1, 0, 1, 1, 0, 1, 1])

# Error rate
error_rate = np.mean(responses == 0)  # 0.3 (30% errors)

# Success rate
success_rate = np.mean(responses == 1)  # 0.7 (70% success)

# Running average
rolling_avg = np.convolve(responses, np.ones(3)/3, mode='valid')
```

### Normalizing Data

```python
# Raw metrics
values = np.array([10, 20, 30, 40, 50])

# Normalize to [0, 1] range
normalized = (values - values.min()) / (values.max() - values.min())
# [0. 0.25 0.5 0.75 1.]

# Standardize (z-score)
standardized = (values - values.mean()) / values.std()
```

### Detecting Anomalies

```python
# Response times with possible outliers
response_times = np.array([100, 110, 95, 105, 500, 98, 102])

# Calculate z-scores
z_scores = np.abs((response_times - np.mean(response_times)) / np.std(response_times))

# Find anomalies (|z| > 2)
anomalies = response_times[z_scores > 2]
print(anomalies)  # [500]
```

---

## Quick Reference

### Most Common Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `np.array()` | Create array | `np.array([1, 2, 3])` |
| `np.zeros()` | Array of zeros | `np.zeros(5)` |
| `np.ones()` | Array of ones | `np.ones((3, 4))` |
| `np.arange()` | Range of values | `np.arange(0, 10, 2)` |
| `np.linspace()` | Evenly spaced values | `np.linspace(0, 1, 10)` |
| `np.shape()` | Array dimensions | `arr.shape` |
| `np.sum()` | Sum all elements | `np.sum(arr)` |
| `np.mean()` | Average | `np.mean(arr)` |
| `np.std()` | Standard deviation | `np.std(arr)` |
| `np.max()` / `np.min()` | Max/min | `np.max(arr)` |
| `np.reshape()` | Change shape | `arr.reshape(3, 4)` |
| `np.flatten()` | To 1D | `arr.flatten()` |
| `np.sort()` | Sort values | `np.sort(arr)` |
| `arr[mask]` | Filter with boolean | `arr[arr > 5]` |

---

## Next Steps

Once you're comfortable with these fundamentals:

1. **Practice** - Work through NumPy exercises
2. **Read Code** - Look at how others use NumPy
3. **Experiment** - Try combining these operations
4. **Move to pandas** - Apply NumPy with tabular data
5. **Real Projects** - Use in actual pipelines

---

## Resources

- **Official Docs**: https://numpy.org/doc/
- **API Reference**: https://numpy.org/doc/stable/reference/
- **Tutorials**: https://numpy.org/learn/

---

## Key Principle

**NumPy is built on one idea: vectorization.** Instead of writing loops, you write operations on entire arrays. This is faster, cleaner, and more Pythonic.

Once you internalize vectorization, NumPy becomes second nature! 🚀

