# Exercise 3: Loops and Aggregations

## Overview

In this exercise, you'll practice loops - one of the most essential concepts in programming. You'll learn how to repeat actions, process multiple items, and aggregate data (sum, count, average). These skills are fundamental to data engineering where you constantly process large amounts of data.

This exercise teaches the patterns you'll use in nearly every data pipeline: read items one by one, process each, and accumulate results.

---

## Learning Objectives

By the end of this exercise, you will be able to:

✅ Write `for` loops with `range()`  
✅ Iterate over lists  
✅ Use accumulators to compute totals and counts  
✅ Understand how loops iterate and variables persist  
✅ Write `while` loops for different use cases   
✅ Process multiple items and aggregate results  

---

## What You'll Practice

| Concept | Used For |
|---------|----------|
| `range()` function | Creating sequences of numbers |
| `for` loops | Iterating a specific number of times |
| Loop iterations | Understanding how loops progress |
| Accumulators | Collecting totals or counts |
| Lists | Storing multiple values |
| `while` loops | Repeating until a condition changes |
| Loop flow | Understanding when code runs |

---

## The Scenario

You're working with data from the Sonic pipeline:

**Part 1**: You have a list of response times from recent requests. You need to:
- Count how many requests there were
- Sum all the response times
- Find the average

**Part 2**: You need to count slow requests (those over a threshold).

**Part 3**: You need to implement a simple countdown timer.

This teaches practical patterns: process a batch of data, aggregate statistics, and handle sequential operations.

---

## Difficulty & Time

**Difficulty**: Beginner  
**Estimated Time**: ~15 minutes  
**Prerequisites**: Completed Exercises 1-2, understand variables and conditionals

---

## Getting Started

1. Create a file called `solution.py` in this directory
2. Follow the instructions in [instructions.md](./ex3-python-instructions.md)
3. Write your code and test it
4. Compare your solution against [solution.md](./ex3-python-solution.md)
5. Make sure your loops work correctly with different data

---

## Success Criteria

Your solution is complete when:

✅ `for` loops work with `range()`  
✅ You can loop through a list  
✅ Accumulators correctly sum and count  
✅ You correctly count items matching a condition  
✅ `while` loop counts down correctly  
✅ Code is readable with clear variable names  
✅ Comments explain the loop logic  

---

## Important Notes

- **Loops iterate**: Each time through the loop, the variable updates
- **Accumulators work by adding**: `total = total + item` or `total += item`
- **Lists can be looped**: Use `for item in list:`
- **Range is flexible**: `range(5)`, `range(1, 6)`, `range(0, 10, 2)`
- **While loops need exit conditions**: Or they loop forever!

---

## Next Steps

1. Open [instructions.md](./ex3-python-instructions.md) and follow each step
2. Write your code in `solution.py`
3. Test it by running `python solution.py`
4. When done, compare against [solution.md](./ex3-python-solution.md)
5. Make sure you understand why each loop works the way it does

Good luck! Loops are powerful and fun once you master them. 🐍
