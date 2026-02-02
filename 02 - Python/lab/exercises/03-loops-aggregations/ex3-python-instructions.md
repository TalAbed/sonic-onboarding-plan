# Exercise 3: Loops and Aggregations - Instructions

Follow these instructions carefully. Work through each part and think about how loops help you process data.

---

## Part 1: Working with Ranges and Accumulators

### Step 1: Create Your Solution File

Create a new file called `solution.py` in this directory.

Open it in your text editor.

---

### Step 2: Print Numbers 1 to 10

Write a `for` loop that prints the numbers 1 through 10.

**Think about**:
- How do you create a sequence of numbers?
- What should the range be? (Should it be 0-9 or 1-10?)
- How do you iterate over the range?

Run your program and verify all 10 numbers print.

---

### Step 3: Sum Numbers 1 to 10

Write a loop that adds all numbers from 1 to 10 and prints the sum.

**Example output**:
```
Sum: 55
```

---

### Step 4: Process a List of Response Times

You're given a list of response times from the pipeline. Define this list:

```python
response_times = [120, 340, 95, 610, 450, 280, 190]
```

**Write code that**:
- Counts how many response times are in the list
- Sums all the response times
- Calculates the average

**Example output** (with the list above):
```
Number of requests: 7
Total response time: 2085
Average response time: 297.86
```

---

## Part 2: Conditional Processing in Loops

### Step 5: Count Slow Requests

Using the same list, count how many requests took more than 300 milliseconds.

**Example output** (with the list above):
```
Requests over 300ms: 3
```

---

### Step 6: List Slow Requests

Modify your code to not just count, but also display which response times were slow.

**Example output** (with the list above):
```
Slow requests (over 300ms):
  Index 1: 340ms
  Index 3: 610ms
  Index 4: 450ms
```

---

## Part 3: While Loops

### Step 7: Simple Countdown

Write a `while` loop that counts down from 5 to 1, then prints "Blastoff!".

**Think about**:
- You need a variable to track the count
- What should it start at?
- What's the condition? (When should the loop stop?)
- How do you update the variable each iteration?

**Example output**:
```
Countdown: 5
Countdown: 4
Countdown: 3
Countdown: 2
Countdown: 1
Blastoff!
```

---

## Step 8: Organize Your Code

Now that you have multiple parts working, organize your code with comments and section headers.

**Think about**:
- Add a comment before each section
- Add a comment explaining each tricky part
- Make the output clear and separated

---

## Step 10: Test Everything

Run your complete program and verify all parts work.

**Checklist**:
- ✅ Numbers 1-10 print correctly
- ✅ Sum of 1-10 is 55
- ✅ Response time statistics are calculated correctly
- ✅ Slow requests are counted and listed properly
- ✅ Countdown works (5 down to 1, then Blastoff!)
- ✅ Code has helpful comments
- ✅ Output is clear and organized

**Example of successful output for response times**:

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

## You've Completed Exercise 3! 🎉

### Next: Compare to Reference Solution

Once you're satisfied:

1. Verify all parts run correctly
2. Check that output matches expected format
3. Open [solution.md](./ex3-python-solution.md) to see a reference solution

Compare your loops and see how the reference handles each part. Great work on mastering loops! 🐍
