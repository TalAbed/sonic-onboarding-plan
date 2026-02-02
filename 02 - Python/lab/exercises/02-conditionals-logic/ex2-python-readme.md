# Exercise 2: Conditionals and Logic

## Overview

In this exercise, you'll practice making decisions in code. You'll work with conditional statements (`if/elif/else`), comparison operators, and logical operators to evaluate conditions and determine appropriate actions.

This mirrors real data engineering work where you constantly evaluate: "Is this event valid? Should I alert? What priority level?"

---

## Learning Objectives

By the end of this exercise, you will be able to:

✅ Write `if/elif/else` statements correctly  
✅ Use comparison operators (`>`, `<`, `>=`, `<=`, `==`, `!=`)  
✅ Combine conditions with logical operators (`and`, `or`, `not`)  
✅ Understand how Python evaluates boolean expressions  
✅ Make decisions based on multiple conditions  
✅ Write clean, readable conditional logic  

---

## What You'll Practice

| Concept | Used For |
|---------|----------|
| Comparison operators | Evaluating if one value is greater, less, equal to another |
| Logical operators | Combining multiple conditions |
| `if` statement | Execute code when condition is true |
| `elif` statement | Test another condition if the first was false |
| `else` statement | Execute code when all conditions are false |
| Indentation | Defining what code belongs to each condition |
| Boolean logic | Understanding how conditions are evaluated |

---

## The Scenario

You're monitoring system health metrics for the Sonic data pipeline. Three key metrics come in:

- **Latency** (response time in milliseconds)
- **Throughput** (requests per second)
- **Health Status** (True if healthy, False if unhealthy)

Your job is to evaluate these metrics and assign a status:
- `CRITICAL` - Something is seriously wrong
- `WARN` - There's a problem, but not critical
- `OK` - Everything is running smoothly

This teaches you how to write the kind of decision-making logic that determines system behavior in real pipelines.

---

## Difficulty & Time

**Difficulty**: Beginner  
**Estimated Time**: ~15 minutes

---

## Getting Started

1. Create a file called `solution.py` in this directory
2. Follow the instructions in [instructions.md](./ex2-python-instructions.md)
3. Write your code and test it with different values
4. Compare your solution against [solution.md](./ex2-python-solution.md)
5. Make sure your conditional logic is clear and correct

---

## Success Criteria

Your solution is complete when:

✅ The program runs without errors  
✅ It correctly evaluates system metrics  
✅ It assigns the right status (CRITICAL, WARN, OK)  
✅ It handles multiple conditions properly  
✅ Your code is readable with clear variable names  
✅ You have comments explaining the logic  

---

## Important Notes

- **Order matters**: Put your `if` conditions in a logical order
- **Indentation**: All code inside an `if/elif/else` must be indented
- **Boolean values**: `True` and `False` (capitalized) are Python keywords
- **Operators**: Know the difference between `=` (assignment) and `==` (comparison)

---

## Next Steps

1. Open [instructions.md](./ex2-python-instructions.md) and follow each step carefully
2. Write your code in `solution.py`
3. Test it by running `python solution.py`
4. When done, compare against [solution.md](./ex2-python-solution.md)
5. Make sure you understand why each condition works the way it does

Good luck! Mastering conditionals is essential for any programmer. 🐍
