# Exercise 2: Conditionals and Logic - Instructions

Follow these instructions carefully. Work through each step and think about the conditions you need to write.

---

## Step 1: Create Your Solution File

Create a new file called `solution.py` in this directory.

Open it in your text editor and get ready to code.

---

## Step 2: Define Your System Metrics

Create three variables that represent system health metrics:

1. A variable for **latency** (response time in milliseconds) - use a number like 450
2. A variable for **throughput** (requests per second) - use a number like 2500
3. A variable for **health status** - use True or False

**Think about**:
- What would be good variable names for these?
- Should latency be int or float?
- How do you store a True/False value in Python?

Start with reasonable test values (not too high, not too low).

---

## Step 3: Create Basic If/Else Logic

Write a basic conditional that checks one metric and prints a status.

**Requirements**:
- If latency is greater than 500 milliseconds, print `"Status: CRITICAL"`
- Otherwise, print `"Status: OK"`

**Think about**:
- Which comparison operator do you need (>, <, >=, etc.)?
- How do you write an if/else block?
- Remember: code inside the if/else must be indented

Run your program and test with different latency values.

---

## Step 4: Add Another Condition with elif

Expand your logic to have three status levels:

**Requirements**:
- If latency > 500: `"Status: CRITICAL"`
- If latency > 300 (but not > 500): `"Status: WARN"`
- Otherwise: `"Status: OK"`

**Think about**:
- Should you use `if/elif/else` or multiple `if` statements?
- When you use `elif`, does Python still check previous conditions?
- What order should your conditions be in?

Test with different latency values: 100, 350, 450, 600

---

## Step 5: Combine Conditions with `and`

Add another condition to your logic. The system should go CRITICAL if latency is high **OR** if it's unhealthy.

**Requirements**:
- If latency > 500 **OR** health status is False: `"Status: CRITICAL"`
- If latency > 300 (and healthy): `"Status: WARN"`
- Otherwise: `"Status: OK"`

**Think about**:
- Which logical operator combines conditions? `and` or `or`?
- Do you need parentheses around your conditions?
- How do you check if a boolean variable is False?

Test cases:
- Healthy system, low latency → OK
- Healthy system, high latency → CRITICAL
- Unhealthy system, any latency → CRITICAL
- Unhealthy system, low latency → CRITICAL

---

## Step 6: Add Throughput Check

Add one more condition involving throughput. The system should warn if throughput is below a threshold.

**Requirements**:
- If latency > 500 **OR** health is False: `"Status: CRITICAL"`
- If latency > 300 **AND** throughput is low (< 1000): `"Status: WARN"`
- If latency > 300 (but good throughput): `"Status: WARN"`
- Otherwise: `"Status: OK"`

**Think about**:
- You now have multiple conditions to combine
- Order matters—put your most critical check first
- How many conditions need to be true with `and`?

---

## Step 7: Test Multiple Scenarios

Run your program with different combinations of values.

**Create at least these test cases**:

Test Case 1:
- Latency: 100, Throughput: 3000, Healthy: True
- Expected: OK

Test Case 2:
- Latency: 450, Throughput: 500, Healthy: True
- Expected: WARN

Test Case 3:
- Latency: 600, Throughput: 2000, Healthy: True
- Expected: CRITICAL

Test Case 4:
- Latency: 100, Throughput: 2000, Healthy: False
- Expected: CRITICAL

**Verify**: Does your code produce the expected result for each test case?

---

## Step 8: Add Comments to Your Logic

Go through your code and add comments explaining:
- What each variable represents
- What each condition is checking
- Why you used `and` vs `or`

Good comments help others (and future you) understand the logic.

---

## Step 9: Make Output Clear

Enhance your output to be more informative.

**Think about**:
- Should you also display the metrics alongside the status?
- Can you make the output formatted nicely?
- From Exercise 1, what tool can you use for formatted output?

**Example of better output** (your format may differ):

```
System Metrics:
  Latency: 450ms
  Throughput: 2500 req/s
  Health: Healthy
Status: WARN
```

---

## You've Completed Exercise 2! 🎉

### What to Verify

Before moving on, make sure your code:

✅ Handles all three status levels (CRITICAL, WARN, OK)  
✅ Uses comparison operators correctly (>, <, >=, etc.)  
✅ Combines conditions with logical operators (and, or)  
✅ Has proper if/elif/else structure  
✅ Is properly indented  
✅ Includes helpful comments  
✅ Produces correct output for various inputs  

---

## Next: Compare to Reference Solution

Once you're satisfied:

1. Verify it runs correctly
2. Check that output makes sense
3. Open [solution.md](./ex2-python-solution.md) to see a reference solution

Compare your approach and reasoning with the reference. Great work tackling conditionals! 🐍
