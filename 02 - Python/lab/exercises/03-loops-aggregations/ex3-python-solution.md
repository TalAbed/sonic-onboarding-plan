# Exercise 3: Loops and Aggregations - Solution

This is a reference solution. Your approach might differ—as long as it works correctly!

---

## Complete Solution

```python
# =================================================
# PART 1: RANGES AND ACCUMULATORS
# =================================================

print("=== PART 1: RANGES AND ACCUMULATORS ===")

# Print numbers 1 to 10
print("\nNumbers 1 to 10:")
for i in range(1, 11):
    print(i)

# Sum numbers 1 to 10
total = 0
for i in range(1, 11):
    total += i
print(f"\nSum of 1 to 10: {total}")

# Process response times
response_times = [120, 340, 95, 610, 450, 280, 190]

# Calculate count, sum, and average
count = 0
total_time = 0
for time in response_times:
    count += 1
    total_time += time

average_time = total_time / count

print("\nResponse Time Statistics:")
print(f"Number of requests: {count}")
print(f"Total response time: {total_time}")
print(f"Average response time: {average_time:.2f}")

# =================================================
# PART 2: CONDITIONAL PROCESSING IN LOOPS
# =================================================

print("\n=== PART 2: CONDITIONAL PROCESSING ===")

# Count slow requests (> 300ms)
slow_count = 0
for time in response_times:
    if time > 300:
        slow_count += 1

print(f"\nRequests over 300ms: {slow_count}")

# List slow requests with index
print("\nSlow requests (over 300ms):")
for i in range(len(response_times)):
    if response_times[i] > 300:
        print(f"  Index {i}: {response_times[i]}ms")

# =================================================
# PART 3: WHILE LOOPS
# =================================================

print("\n=== PART 3: WHILE LOOPS ===")

# Countdown from 5 to 1
print("\nCountdown:")
countdown = 5
while countdown >= 1:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Blastoff!")
```

---

## Expected Output

```
=== PART 1: RANGES AND ACCUMULATORS ===

Numbers 1 to 10:
1
2
3
4
5
6
7
8
9
10

Sum of 1 to 10: 55

Response Time Statistics:
Number of requests: 7
Total response time: 2085
Average response time: 297.86

=== PART 2: CONDITIONAL PROCESSING ===

Requests over 300ms: 3

Slow requests (over 300ms):
  Index 1: 340ms
  Index 3: 610ms
  Index 4: 450ms

=== PART 3: WHILE LOOPS ===

Countdown:
Countdown: 5
Countdown: 4
Countdown: 3
Countdown: 2
Countdown: 1
Blastoff!
```

---

## Line-by-Line Explanation

### Part 1: Ranges and Accumulators

#### Printing 1 to 10

```python
for i in range(1, 11):
    print(i)
```

**How it works**:
- `range(1, 11)` creates numbers 1 through 10 (note: 11 is excluded)
- Each iteration, `i` gets the next number
- `print(i)` outputs that number

**Why `range(1, 11)` and not `range(10)`?**
- `range(10)` would be 0-9
- `range(1, 11)` is 1-10, which is what we want

#### Summing 1 to 10

```python
total = 0
for i in range(1, 11):
    total += i
print(f"Sum of 1 to 10: {total}")
```

**How it works**:
- `total = 0` initializes the accumulator
- Each iteration: `total += i` adds the current number
- After loop ends, print the result

#### Processing a List

```python
response_times = [120, 340, 95, 610, 450, 280, 190]

count = 0
total_time = 0
for time in response_times:
    count += 1
    total_time += time

average_time = total_time / count
```

**How it works**:
- `for time in response_times:` loops through each item
- `count += 1` counts how many items (7)
- `total_time += time` sums all values (2085)
- `average_time = 2085 / 7 = 297.86`

---

### Part 2: Conditional Processing in Loops

#### Count Slow Requests

```python
slow_count = 0
for time in response_times:
    if time > 300:
        slow_count += 1

print(f"Requests over 300ms: {slow_count}")
```

**How it works**:
- `slow_count = 0` initializes counter
- For each time in the list, check if it's > 300
- If true, increment the counter
- Result: 3 (values 340, 610, 450 are > 300)

#### List Slow Requests with Index

```python
print("Slow requests (over 300ms):")
for i in range(len(response_times)):
    if response_times[i] > 300:
        print(f"  Index {i}: {response_times[i]}ms")
```

**How it works**:
- `range(len(response_times))` creates indices (0-6 for a 7-item list)
- `response_times[i]` accesses the item at index `i`
- Only print if the value is > 300
- Shows both the index and the value

---

### Part 3: While Loops

#### Countdown from 5 to 1

```python
countdown = 5
while countdown >= 1:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Blastoff!")
```

**How it works**:
- `countdown = 5` initializes the variable
- `while countdown >= 1:` checks the condition
- If true, execute the block and update `countdown -= 1`
- When `countdown` becomes 0, the condition is false and loop stops

**Execution**:
```
countdown = 5, print "Countdown: 5", countdown = 4
countdown = 4, print "Countdown: 4", countdown = 3
countdown = 3, print "Countdown: 3", countdown = 2
countdown = 2, print "Countdown: 2", countdown = 1
countdown = 1, print "Countdown: 1", countdown = 0
countdown = 0, condition false, exit loop
```

---

## Key Patterns

### Pattern 1: Accumulating a Sum

```python
total = 0
for item in items:
    total += item  # Add each item
```

### Pattern 2: Counting Items

```python
count = 0
for item in items:
    count += 1  # Increment for each item
```

### Pattern 3: Counting Matching Items

```python
count = 0
for item in items:
    if condition(item):
        count += 1  # Only increment if condition is true
```

### Pattern 4: Computing Average

```python
total = 0
count = 0
for item in items:
    total += item
    count += 1
average = total / count
```

### Pattern 5: Looping with Index

```python
for i in range(len(items)):
    item = items[i]
    print(f"Index {i}: {item}")
```

---

## For vs While Loops

### Use `for` when:
- You know how many times to loop (range)
- You're iterating through a list
- The number of iterations is predetermined

```python
for i in range(10):  # Know it's 10 iterations
for item in items:   # Know we have a list
```

### Use `while` when:
- You loop until a condition changes
- The number of iterations is unknown
- You need flexible control

```python
while user_input != "quit":  # Loop until user quits
while countdown > 0:          # Loop until countdown reaches 0
```

---

## Common Variations

### Alternative: Using len() to Count

```python
# Instead of:
count = 0
for item in response_times:
    count += 1

# You could use:
count = len(response_times)  # Directly get the length
```

### Alternative: Using sum() for Total

```python
# Instead of:
total = 0
for time in response_times:
    total += time

# You could use:
total = sum(response_times)  # Python's built-in function
```

### Alternative: Processing Lists Differently

```python
# Method 1: Loop through items
for time in response_times:
    print(time)

# Method 2: Loop through indices
for i in range(len(response_times)):
    print(response_times[i])

# Method 3: Loop with both index and item
for i, time in enumerate(response_times):
    print(f"Index {i}: {time}")
```

---

## Reflection Questions

1. **What happens if the list is empty?**
   - Sum would be 0 (correct)
   - Count would be 0 (correct)
   - Average would fail (division by zero!)

2. **When should you use `for` vs `while`?**
   - `for`: when you know how many iterations
   - `while`: when you loop until a condition changes

3. **Why does `range(1, 11)` give 1-10?**
   - First number is inclusive
   - Last number is exclusive
   - This is a Python convention

---

## Next Steps

1. ✅ Compare your code to this solution
2. ✅ Run both with the same values
3. ✅ Make sure you understand each loop pattern
4. ✅ Try modifying the response times list and testing again
5. ✅ Move on to Exercise 4: Functions and Data Structures