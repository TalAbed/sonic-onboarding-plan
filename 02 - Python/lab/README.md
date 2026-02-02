# Python Lab

Welcome to the Python Lab! This is where theory meets practice. You've watched the video, reviewed the fundamentals guide, and practiced on Pychallenger—now it's time to write real Python code.

This lab contains four focused exercises that drill down on core Python syntax and concepts. Each exercise is designed to build your confidence with the language before moving to more complex data engineering patterns.

## What is the Python Lab?

This Python Lab is a series of hands-on exercises designed to solidify your understanding of Python fundamentals through direct practice.

All exercises run locally on your machine. No fancy online platforms here—just you, Python, and your text editor.

## Exercises Overview

| # | Exercise | Difficulty | Time    | Skills Tested |
|---|----------|-----------|---------|---------------|
| 1 | [Variables, Types, and Input](#exercise-1-variables-types-and-input) | Beginner | ~15 min | Variable assignment, type conversion, formatted output |
| 2 | [Conditionals and Logic](#exercise-2-conditionals-and-logic) | Beginner | ~15 min | If/elif/else, comparison operators, logical operators |
| 3 | [Loops and Aggregations](#exercise-3-loops-and-aggregations) | Beginner | ~15 min | For loops, ranges, accumulators, while loops |
| 4 | [Functions and Data Structures](#exercise-4-functions-and-data-structures) | Beginner | ~15 min | Function definitions, parameters, lists, dictionaries |

**Total Lab Time**: ~60 minutes  
**Recommended**: Complete in order, one exercise per session

---

## Before You Start

Make sure you've completed:
- ✅ Watched the [Programming with Mosh Python video](../README.md)
- ✅ Reviewed the [Basic Python Fundamentals guide](../basic-python-fundamentals.md)
- ✅ Completed exercises on [Pychallenger](https://pychallenger.com/)
- ✅ Have Python 3.8+ installed on your machine

Then, follow the [SETUP.md](./SETUP.md) guide to prepare your environment.

---

## Exercise 1: Variables, Types, and Input

**Difficulty**: Beginner  
**Time**: ~15 minutes  
**Location**: [01-variables-types-input/](./exercises/01-variables-types-input/)

**What You'll Learn**:
- How to create variables with meaningful names
- Understanding Python's data types (string, int, float, bool)
- Converting between types using int(), float(), str()
- Getting input from users with input()
- Formatting and printing output using f-strings

**Skills Tested**:
- Variable naming conventions
- `input()` function
- Type conversion functions
- f-string formatting
- `print()` with formatted strings

**Real-World Context**: When you build data pipelines, you'll often need to read user input or configuration, validate types, and display results clearly. This exercise practices that flow.

**Next Steps**: Read the [exercise README](./exercises/01-variables-types-input/README.md) for full details.

---

## Exercise 2: Conditionals and Logic

**Difficulty**: Beginner  
**Time**: ~15 minutes  
**Location**: [02-conditionals-logic/](./exercises/02-conditionals-logic/)

**What You'll Learn**:
- Writing if/elif/else statements correctly
- Using comparison operators (>, <, >=, <=, ==, !=)
- Combining conditions with logical operators (and, or, not)
- Understanding how Python evaluates boolean expressions
- Making decisions based on multiple conditions

**Skills Tested**:
- `if`, `elif`, `else` syntax
- Comparison operators
- Logical operators (and, or, not)
- Nested and compound conditions
- Correct indentation and code structure

**Real-World Context**: Data pipelines need to make decisions: "Is this event valid? Should I alert? What priority level?" This exercise teaches the syntax for expressing those decisions clearly.

**Next Steps**: Read the [exercise README](./exercises/02-conditionals-logic/README.md) for full details.

---

## Exercise 3: Loops and Aggregations

**Difficulty**: Beginner  
**Time**: ~15 minutes  
**Location**: [03-loops-aggregations/](./exercises/03-loops-aggregations/)

**What You'll Learn**:
- Writing for loops with range()
- Iterating over lists
- Using accumulators to compute totals and counts
- Understanding loop flow and iteration
- Writing simple while loops
- The difference between for and while loops

**Skills Tested**:
- `for` loops with `range()`
- `for` loops over lists
- Accumulator patterns (total += x, count += 1)
- `while` loop syntax
- Loop control and iteration counting

**Real-World Context**: Processing streams of events, computing statistics (sum, average, count), and aggregating data are core to data engineering. This exercise teaches the fundamental looping patterns you'll use constantly.

**Next Steps**: Read the [exercise README](./exercises/03-loops-aggregations/README.md) for full details.

---

## Exercise 4: Functions and Data Structures

**Difficulty**: Beginner  
**Time**: ~15 minutes  
**Location**: [04-functions-data-structures/](./exercises/04-functions-data-structures/)

**What You'll Learn**:
- Defining functions with def keyword
- Function parameters and arguments
- Return values and the return statement
- Working with lists and dictionaries
- Passing data structures to functions
- Iterating over lists of dictionaries
- Returning computed results

**Skills Tested**:
- `def` function definition
- Parameters and function calls
- `return` statement
- Working with lists
- Working with dictionaries
- Looping over complex data structures
- Function documentation

**Real-World Context**: Every piece of reusable code is a function. Every event in a pipeline is a dictionary. Every batch of events is a list of dictionaries. This exercise brings it all together.

**Next Steps**: Read the [exercise README](./exercises/04-functions-data-structures/README.md) for full details.

---

## How to Complete Each Exercise

### Step 1: Read the Exercise README
Each exercise folder has a README.md that explains:
- Learning objectives
- What you'll be practicing
- Any special setup needed

### Step 2: Follow the Instructions
Open `instructions.md` and work through each step. The instructions are written to be clear and achievable - don't skip reading them carefully.

### Step 3: Write Your Code
Create a Python file (usually named `solution.py` or as specified) and write the code to solve the exercise. Test it by running it:

```bash
python solution.py
```

### Step 4: Compare Against Reference Solution
After completing, compare your work against `solution.md`. This shows one way to solve the problem. Your approach might differ—that's fine! What matters is:
- Does your code run without errors?
- Does it produce the correct output?
- Is it readable and well-structured?

### Step 5: Reflect
Ask yourself:
- Do I understand why each line works?
- Could I explain this exercise to a teammate?
- What syntax do I still need to practice?

---

## Running Your Code

### Basic Execution

```bash
# Run a Python file
python solution.py

# Or with python3 (on some systems)
python3 solution.py

# See output
python solution.py > output.txt  # Save output to file
```

### Interactive Testing

Test small pieces of code without creating a file:

```bash
python
>>> name = "Alex"
>>> age = 28
>>> print(f"Name: {name}, Age: {age}")
Name: Alex, Age: 28
>>> exit()
```

---

## Troubleshooting

### "SyntaxError: invalid syntax"
You have a typo or incorrect syntax. Check:
- Indentation (must be 4 spaces, not tabs)
- Closing parentheses and brackets
- Colons after if/for/def/while
- Quotes matched (single/double)

### "NameError: name 'x' is not defined"
You're using a variable that doesn't exist or hasn't been assigned yet. Check spelling and make sure you assigned it before using it.

### "TypeError: expected string, got int"
You tried to use the wrong type. Check:
- Did you convert input() to int()?
- Are you passing the right type to a function?

### "IndentationError: expected an indented block"
After `if:`, `for:`, `def:`, the next lines must be indented. Use 4 spaces.

### My code runs but produces wrong output
Compare:
1. Your output against the expected output
2. Your logic against the instructions
3. Your implementation against the reference solution

Debug by adding `print()` statements to see what's happening at each step.

---

## Code Quality Tips

### Use Meaningful Variable Names
```python
# Good
user_name = "Alex"
response_time_ms = 120

# Bad
u = "Alex"
rt = 120
```

### Add Comments for Complex Logic
```python
# Calculate average latency, excluding errors
valid_latencies = [x for x in latencies if x > 0]
average = sum(valid_latencies) / len(valid_latencies)
```

### Test Edge Cases
```python
# What if the list is empty?
# What if the user enters 0?
# What if the string is empty?
```

---

## Success Indicators

You've successfully completed this lab when:

✅ All four exercises run without errors  
✅ You understand each line of code you wrote  
✅ You could explain the exercises to a teammate  
✅ You feel comfortable with Python syntax  
✅ You're ready to move to the next onboarding section  

---

## Questions or Issues?

If something doesn't make sense:
1. Re-read the instructions carefully
2. Check the reference solution and the explanation
3. Review the relevant section in [basic-python-fundamentals.md](../basic-python-fundamentals.md)
4. Ask your team members for help :)

Remember: **Struggling with syntax is part of learning.** Everyone, including expert programmers, looks things up constantly. Use these exercises to build your confidence and fluency.

---

**Ready to start?** Go to [SETUP.md](./SETUP.md) and then dive into Exercise 1!

### Good luck!
