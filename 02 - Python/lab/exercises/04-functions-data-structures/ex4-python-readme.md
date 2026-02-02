# Exercise 4: Functions and Data Structures

## Overview

In this exercise, you'll bring everything together: functions, lists, and dictionaries. You'll create reusable functions that process complex data (events as dictionaries in lists). This mirrors real data engineering work where you transform batches of events through pipeline stages.

Functions let you organize code, make it reusable, and handle increasing complexity. Combined with data structures, they're the foundation of professional Python code.

---

## Learning Objectives

By the end of this exercise, you will be able to:

✅ Define functions with `def`  
✅ Create functions with parameters  
✅ Return values from functions  
✅ Work with lists of dictionaries  
✅ Loop through complex data structures  
✅ Build functions that process batches of data  
✅ Call functions and use their results  

---

## What You'll Practice

| Concept | Used For |
|---------|----------|
| Function definition | Creating reusable code blocks |
| Parameters | Passing data to functions |
| Return values | Getting results from functions |
| Dictionaries | Storing related data together |
| Lists of dictionaries | Representing batches of events |
| Looping through complex structures | Processing event data |
| Function composition | Using functions together |

---

## The Scenario

You're building utility functions for the Sonic data pipeline. You receive a batch of events (each event is a dictionary with id, status, and latency). You need to:

**Function 1**: Count how many events have errors  
**Function 2**: Calculate the average latency across all events  
**Main program**: Call both functions and display results

This teaches the pattern you'll use constantly: write functions to process data batches, call them in sequence, and combine results.

---

## Difficulty & Time

**Difficulty**: Beginner  
**Estimated Time**: ~20 minutes  
**Prerequisites**: Completed Exercises 1-3, understand variables, loops, conditionals

---

## Getting Started

1. Create a file called `solution.py` in this directory
2. Follow the instructions in [instructions.md](./ex4-python-instructions.md)
3. Write your code and test it
4. Compare your solution against [solution.md](./ex4-python-solution.md)
5. Make sure your functions work correctly with different data

---

## Success Criteria

Your solution is complete when:

✅ Functions are defined with appropriate parameters  
✅ Functions return correct values  
✅ You can loop through a list of dictionaries  
✅ You correctly access dictionary values  
✅ Both functions produce correct results  
✅ Code is readable with clear names  
✅ Comments explain function purpose  

---

## Important Notes

- **Functions organize code**: Break complex work into small, focused functions
- **Dictionaries store related data**: `event = {"id": 1, "status": "ok"}`
- **Lists hold multiple items**: `events = [event1, event2, event3]`

---

## Hints (If You Get Stuck)

- Review Functions section in basic-python-fundamentals.md
- Review Data Structures section for dictionaries and lists
- Remember: `return` exits the function immediately
- Access dict values with `event["key"]` or `event.get("key")`
- Loop through list of dicts with `for event in events:`

---

## Next Steps

1. Open [instructions.md](./ex4-python-instructions.md) and follow each step
2. Write your code in `solution.py`
3. Test it by running `python solution.py`
4. When done, compare against [solution.md](./ex4-python-solution.md)
5. Make sure you understand how functions and data structures work together

Good luck! You're almost there! 🐍
