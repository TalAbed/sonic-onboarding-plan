# Exercise 2: Conditionals and Logic - Solution

This is a reference solution showing one way to solve this exercise. Your approach might differ, and that's fine!

---

## Complete Solution

```python
# Define system health metrics
latency = 350  # Response time in milliseconds
throughput = 1500  # Requests per second
is_healthy = True  # True if healthy, False if unhealthy

# Evaluate system status based on metrics
if latency > 500 or not is_healthy:
    status = "CRITICAL"
elif latency > 300 and throughput < 1000:
    status = "WARN"
elif latency > 300:
    status = "WARN"
else:
    status = "OK"

# Display results
print("System Metrics:")
print(f"  Latency: {latency}ms")
print(f"  Throughput: {throughput} req/s")
print(f"  Health: {'Healthy' if is_healthy else 'Unhealthy'}")
print(f"Status: {status}")
```

---

## Expected Output

With the values shown above:

```
System Metrics:
  Latency: 350ms
  Throughput: 1500 req/s
  Health: Healthy
Status: WARN
```

---

## Detailed Explanation

### Setting Up Metrics

```python
latency = 350
throughput = 1500
is_healthy = True
```

These represent:
- **Latency**: 350 milliseconds (how long responses take)
- **Throughput**: 1500 requests per second
- **Health**: True (system is functioning)

These are intentionally set to test the WARN condition.

### The Conditional Logic

```python
if latency > 500 or not is_healthy:
    status = "CRITICAL"
```

**Reads as**: "If latency exceeds 500 milliseconds OR the system is not healthy, it's critical"

Key points:
- `latency > 500` checks if latency is high
- `not is_healthy` checks if the boolean is False
- `or` means either one condition being true is enough

This catches the most urgent situations first.

```python
elif latency > 300 and throughput < 1000:
    status = "WARN"
```

**Reads as**: "Otherwise, if latency is above 300 AND throughput is low, it's a warning"

Key points:
- `latency > 300` checks if moderate-to-high latency
- `throughput < 1000` checks if throughput is below threshold
- `and` means BOTH conditions must be true
- This situation suggests degraded performance

```python
elif latency > 300:
    status = "WARN"
```

**Reads as**: "Otherwise, if latency is still above 300, it's still a warning"

This catches high latency even if throughput is good.

```python
else:
    status = "OK"
```

If none of the above conditions were true, the system is running normally.

### Displaying Results

```python
print("System Metrics:")
print(f"  Latency: {latency}ms")
print(f"  Throughput: {throughput} req/s")
print(f"  Health: {'Healthy' if is_healthy else 'Unhealthy'}")
print(f"Status: {status}")
```

This displays:
1. A header
2. Each metric with a label
3. The calculated status

The line `'Healthy' if is_healthy else 'Unhealthy'` uses a ternary operator to display text based on the boolean value.

---

## Testing Different Scenarios

### Test 1: System is OK

```python
latency = 100
throughput = 5000
is_healthy = True
```

**Expected status**: OK

**Why**: Latency is low, throughput is high, system is healthy. No conditions trigger warnings.

### Test 2: High Latency Only

```python
latency = 550
throughput = 3000
is_healthy = True
```

**Expected status**: CRITICAL

**Why**: First condition triggers (`latency > 500`)

### Test 3: Unhealthy System

```python
latency = 100
throughput = 2000
is_healthy = False
```

**Expected status**: CRITICAL

**Why**: First condition triggers (`not is_healthy`)

### Test 4: Moderate Latency with Low Throughput

```python
latency = 400
throughput = 800
is_healthy = True
```

**Expected status**: WARN

**Why**: Second condition triggers (`latency > 300 and throughput < 1000`)

### Test 5: Moderate Latency, Good Throughput

```python
latency = 400
throughput = 3000
is_healthy = True
```

**Expected status**: WARN

**Why**: Third condition triggers (`latency > 300`)

---

## Understanding the Logic Flow

The conditions are checked in order:

```
1. Is it CRITICAL? (highest priority)
   └─ If YES, stop and assign CRITICAL
   
2. Is it a WARN with low throughput?
   └─ If YES, stop and assign WARN
   
3. Is it a WARN with just high latency?
   └─ If YES, stop and assign WARN
   
4. Otherwise, everything is OK
   └─ Assign OK
```

This structure is important: you check critical conditions first, and less severe ones later.

---

## Common Variations

### Using Variables for Thresholds

```python
CRITICAL_LATENCY = 500
WARN_LATENCY = 300
LOW_THROUGHPUT = 1000

if latency > CRITICAL_LATENCY or not is_healthy:
    status = "CRITICAL"
elif latency > WARN_LATENCY and throughput < LOW_THROUGHPUT:
    status = "WARN"
# ... etc
```

This makes the code more maintainable and easier to adjust thresholds.

### Simplifying Conditions

```python
# Instead of this:
if latency > 300 and throughput < 1000:
    status = "WARN"
elif latency > 300:
    status = "WARN"

# You could write:
elif latency > 300 and (throughput < 1000 or True):
    status = "WARN"

# Or even simpler - just check latency:
elif latency > 300:
    status = "WARN"
```

The second `elif` is redundant if you just care about latency > 300.

---

## Reflection Questions

1. **What happens if you reverse the order of conditions?**
   - The logic might still work, but less efficient
   - Critical checks should come first

2. **Why use `elif` instead of multiple `if` statements?**
   - `elif` stops checking once one condition matches
   - Multiple `if` statements check all conditions (slower)

3. **How would you add another metric?**
   - Add another variable
   - Add another condition with `and`/`or`
   - Adjust thresholds as needed

---

## Next Steps

1. ✅ Compare your code to this solution
2. ✅ Run both with the same test values
3. ✅ Make sure you understand each operator
4. ✅ Try modifying the thresholds and testing again
5. ✅ Move on to Exercise 3: Loops and Aggregations

---

**Great job mastering conditionals!** 🎉 You now understand how to make complex decisions in Python, which is essential for data engineering. Next up: loops!
