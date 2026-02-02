# Basic Python Fundamentals Guide

## Overview

This comprehensive guide covers the essential Python concepts that every Python developer needs to know. Use this as a reference while learning and building data pipelines. Examples are practical and relevant to data engineering work.

## Table of Contents

1. [Installation and Setup](#installation-and-setup)
2. [Python Basics](#python-basics)
3. [Variables and Data Types](#variables-and-data-types)
4. [Operators](#operators)
5. [Control Flow](#control-flow)
6. [Functions](#functions)
7. [Data Structures](#data-structures)
8. [String Operations](#string-operations)
9. [File Operations](#file-operations)
10. [Common Patterns](#common-patterns)
11. [Best Practices for Sonic](#best-practices-for-sonic)

---

## Installation and Setup

### Check Python Installation

```bash
# Check if Python is installed
python --version
# or
python3 --version
```

**Expected output**: Python 3.8 or higher (preferably 3.10+)

### Using Python Interactively

The **Python REPL** (Read-Eval-Print Loop) lets you test code instantly:

```bash
# Start interactive Python
python
# or
python3
```

You'll see:
```
Python 3.10.0 (main, Oct  4 2021, 14:55:26) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Now you can type Python code and see results immediately:

```python
>>> 2 + 2
4
>>> print("Hello, Sonic!")
Hello, Sonic!
```

Exit the REPL with `exit()` or `Ctrl+D`

### Running Python Files

Create a file with `.py` extension and run it:

```bash
# Create a file
echo 'print("Hello from Sonic!")' > hello.py

# Run it
python hello.py
```

---

## Python Basics

### Your First Program

```python
# This is a comment (lines starting with # are ignored)
print("Hello, Sonic!")  # You can comment at the end of lines too
```

**Output**:
```
Hello, Sonic!
```

### Multiple Statements

```python
print("First line")
print("Second line")
print("Third line")
```

**Output**:
```
First line
Second line
Third line
```

### Indentation Matters

Python uses indentation (spaces) to define code blocks:

```python
if True:
    print("This is indented")
    print("Also indented")
print("This is not indented")
```

---

## Variables and Data Types

In Python, you don't have to declare the variable type:

```python
# Create variables
name = "Alex"
age = 28
salary = 75000.50
is_active = True

# Use them
print(name)      # Output: Alex
print(age)       # Output: 28
```

### Naming Conventions

Follow these rules for variable names:

✅ **Good**:
```python
user_name = "alex"           # snake_case (preferred in Python)
firstName = "alex"           # camelCase (acceptable)
MAX_RETRIES = 3             # UPPER_CASE (for constants)
```

❌ **Bad**:
```python
1name = "alex"              # Can't start with number
user-name = "alex"          # Can't use hyphens
user name = "alex"          # Can't use spaces
```

### Data Types

#### 1. Strings (Text)

```python
# Create strings with single, double, or triple quotes
name = "Sonic"
greeting = 'Hello, world!'
message = """This is a
multi-line string"""

# Check type
print(type(name))           # Output: <class 'str'>
```

#### 2. Integers (Whole Numbers)

```python
age = 28
count = -5
distance = 0

print(type(age))            # Output: <class 'int'>
```

#### 3. Floats (Decimal Numbers)

```python
price = 19.99
temperature = -5.5
pi = 3.14159

print(type(price))          # Output: <class 'float'>
```

#### 4. Booleans (True/False)

```python
is_active = True
is_closed = False
has_access = True

print(type(is_active))      # Output: <class 'bool'>
```

#### 5. None (No Value)

```python
result = None               # Represents "no value"
print(type(result))         # Output: <class 'NoneType'>
```

### Type Conversion

Convert between types:

```python
# String to Integer
age_str = "28"
age_int = int(age_str)      # Result: 28

# Integer to String
count = 5
count_str = str(count)      # Result: "5"

# String to Float
price_str = "19.99"
price_float = float(price_str)  # Result: 19.99

# Integer to Float
total = int(100)
total_float = float(total)  # Result: 100.0

# String to Boolean (any non-empty string is True)
value = bool("hello")       # Result: True
empty = bool("")            # Result: False

# Common pattern: Convert user input
user_input = input("Enter a number: ")  # Always returns string
number = int(user_input)    # Convert to integer
```

---

## Operators

### Arithmetic Operators

```python
# Addition
result = 10 + 5             # Result: 15

# Subtraction
result = 10 - 5             # Result: 5

# Multiplication
result = 10 * 5             # Result: 50

# Division (always returns float)
result = 10 / 3             # Result: 3.3333...

# Floor Division (rounds down)
result = 10 // 3            # Result: 3

# Modulo (remainder)
result = 10 % 3             # Result: 1

# Exponentiation
result = 2 ** 3             # Result: 8
```

### Comparison Operators

These return True or False:

```python
# Equal
10 == 10                    # True
10 == 5                     # False

# Not Equal
10 != 5                     # True
10 != 10                    # False

# Greater Than
10 > 5                      # True
5 > 10                      # False

# Less Than
5 < 10                      # True
10 < 5                      # False

# Greater Than or Equal
10 >= 10                    # True
5 >= 10                     # False

# Less Than or Equal
5 <= 10                     # True
10 <= 5                     # False
```

### Logical Operators

Combine conditions:

```python
# AND (both must be True)
age = 25
has_license = True
can_drive = age >= 18 and has_license  # True

# OR (at least one must be True)
is_weekend = True
is_holiday = False
is_off = is_weekend or is_holiday  # True

# NOT (reverses the value)
is_raining = False
go_outside = not is_raining         # True
```

### Assignment Operators

```python
x = 10              # Simple assignment

x += 5              # Same as: x = x + 5 (x is now 15)
x -= 3              # Same as: x = x - 3
x *= 2              # Same as: x = x * 2
x /= 4              # Same as: x = x / 4

# String concatenation
greeting = "Hello"
greeting += " Sonic"    # Result: "Hello Sonic"
```

---

## Control Flow

### If/Elif/Else Statements

Make decisions based on conditions:

```python
age = 25

if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")
```

**Output**: "You are an adult"

### Multiple Conditions

```python
score = 85
is_absent = False

if score >= 80 and not is_absent:
    print("Excellent performance!")
elif score >= 70:
    print("Good performance")
else:
    print("Needs improvement")
```

### Nested Conditions

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You must get a license")
else:
    print("You are too young to drive")
```

---

## Loops

### For Loops

Repeat actions a specific number of times or over a sequence:

```python
# Loop through range of numbers
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with custom range
for i in range(1, 6):       # Start at 1, end before 6
    print(i)                # 1, 2, 3, 4, 5

# Loop with step
for i in range(0, 10, 2):   # Start 0, end before 10, step by 2
    print(i)                # 0, 2, 4, 6, 8
```

### While Loops

Repeat while a condition is True:

```python
count = 0
while count < 5:
    print(count)
    count += 1              # Must change count or loop forever!

# Output: 0, 1, 2, 3, 4
```

### Loop Control

```python
# Break: Exit the loop immediately
for i in range(10):
    if i == 5:
        break               # Exit loop
    print(i)                # Prints: 0, 1, 2, 3, 4

# Continue: Skip to next iteration
for i in range(5):
    if i == 2:
        continue            # Skip this iteration
    print(i)                # Prints: 0, 1, 3, 4
```

---

## Functions

Functions are reusable blocks of code:

### Basic Function

```python
def greet():
    print("Hello, Sonic!")

greet()                     # Call the function
greet()                     # Call it again
```

### Function with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alex")               # Output: Hello, Alex!
greet("Jamie")              # Output: Hello, Jamie!
```

### Function with Return Value

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)               # Output: 8
```

### Multiple Parameters and Return Values

```python
def process_data(value, multiplier):
    result = value * multiplier
    return result

output = process_data(10, 3)
print(output)               # Output: 30
```

### Default Parameters

```python
def greet(name="User"):
    print(f"Hello, {name}!")

greet()                     # Output: Hello, User!
greet("Alex")               # Output: Hello, Alex!
```

### Multiple Return Values

```python
def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average

min_val, max_val, avg_val = get_stats([10, 20, 30, 40])
print(f"Min: {min_val}, Max: {max_val}, Avg: {avg_val}")
```

### Docstrings (Document Your Functions)

```python
def calculate_total(price, tax_rate=0.1):
    """
    Calculate total price including tax.
    
    Args:
        price (float): The base price
        tax_rate (float): Tax rate as decimal (default 0.1 for 10%)
    
    Returns:
        float: Total price including tax
    """
    return price + (price * tax_rate)

# Use the docstring
help(calculate_total)
```

---

## Data Structures

### Lists (Ordered, Mutable)

Lists store multiple values and can be changed:

```python
# Create a list
colors = ["red", "green", "blue"]

# Access elements
print(colors[0])            # Output: red
print(colors[1])            # Output: green

# List methods
colors.append("yellow")     # Add to end
colors.insert(1, "orange")  # Insert at position
colors.remove("red")        # Remove by value
popped = colors.pop()       # Remove and return last item

# List operations
length = len(colors)        # Get length
reversed_list = colors[::-1] # Reverse
sorted_list = sorted(colors) # Sort

# Loop through list
for color in colors:
    print(color)

# List slicing
first_three = colors[0:3]   # Items 0, 1, 2
last_two = colors[-2:]      # Last 2 items
```

### Tuples (Ordered, Immutable)

Tuples are like lists but cannot be changed:

```python
# Create a tuple
coordinates = (10, 20, 30)

# Access elements (same as lists)
print(coordinates[0])       # Output: 10

# Cannot modify (this raises error)
# coordinates[0] = 15        # Error!

# Useful for returning multiple values
def get_location():
    return (40.7128, 74.0060)  # Latitude, longitude

lat, lon = get_location()
```

### Dictionaries (Key-Value Pairs)

Store data with labels:

```python
# Create a dictionary
person = {
    "name": "Alex",
    "age": 28,
    "role": "Data Engineer",
    "active": True
}

# Access values
print(person["name"])       # Output: Alex
print(person.get("age"))    # Output: 28

# Modify values
person["age"] = 29
person["salary"] = 75000    # Add new key

# Remove items
del person["active"]        # Delete a key

# Loop through dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Get all keys or values
all_keys = person.keys()
all_values = person.values()

# Check if key exists
if "name" in person:
    print("Name exists")
```

### Sets (Unordered, Unique)

Store unique values without duplicates:

```python
# Create a set
colors = {"red", "green", "blue"}

# Add and remove
colors.add("yellow")
colors.remove("red")

# Set operations
colors1 = {1, 2, 3}
colors2 = {2, 3, 4}

union = colors1 | colors2           # {1, 2, 3, 4}
intersection = colors1 & colors2    # {2, 3}
difference = colors1 - colors2      # {1}
```

---

## String Operations

### Creating Strings

```python
# Different quote styles (all equivalent)
name = "Alex"
greeting = 'Hello'
message = """Multi-line
string works
here"""
```

### String Methods

```python
text = "Hello Sonic"

# Case conversion
upper = text.upper()        # "HELLO SONIC"
lower = text.lower()        # "hello sonic"
title = text.title()        # "Hello Sonic"

# Search
position = text.find("Sonic")       # 6 (index where "Sonic" starts)
count = text.count("o")             # 2 (number of "o"s)
contains = "Sonic" in text          # True

# Replace
new_text = text.replace("Sonic", "Team")  # "Hello Team"

# Strip whitespace
padded = "  hello  "
clean = padded.strip()              # "hello"
left = padded.lstrip()              # "hello  "
right = padded.rstrip()             # "  hello"

# Split and join
words = text.split()                # ["Hello", "Sonic"]
rejoined = "-".join(words)          # "Hello-Sonic"
```

### String Formatting

```python
# f-strings (modern, preferred)
name = "Alex"
age = 28
message = f"My name is {name} and I'm {age} years old"
print(message)  # My name is Alex and I'm 28 years old

# Format method
message = "My name is {} and I'm {} years old".format(name, age)

# Old-style formatting (don't use)
message = "My name is %s" % name  # Avoid this style
```

---

## File Operations

### Reading Files

```python
# Read entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline

# Read all lines into a list
with open("data.txt", "r") as file:
    lines = file.readlines()
```

### Writing Files

```python
# Write to file
with open("output.txt", "w") as file:
    file.write("Hello, Sonic!\n")
    file.write("This is a new file")

# Append to file
with open("output.txt", "a") as file:
    file.write("Adding more content\n")
```

### Working with CSV Files

```python
import csv

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)  # Reads with headers
    for row in reader:
        print(row["name"], row["age"])

# Write CSV
import csv
data = [
    {"name": "Alex", "age": 28},
    {"name": "Jamie", "age": 32}
]

with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)
```

---

## Common Patterns

### Checking if Value Exists in List

```python
names = ["Alex", "Jamie", "Morgan"]

if "Alex" in names:
    print("Alex is in the list")
```

### Filtering Lists

```python
numbers = [1, 2, 3, 4, 5, 6]

# Get only even numbers
even = [n for n in numbers if n % 2 == 0]
print(even)  # [2, 4, 6]

# More examples
greater_than_3 = [n for n in numbers if n > 3]
doubled = [n * 2 for n in numbers]
```

### Counting Occurrences

```python
data = ["a", "b", "a", "c", "a"]
count = data.count("a")  # 3
```

### Finding Maximum/Minimum

```python
numbers = [10, 20, 5, 30, 15]
max_num = max(numbers)  # 30
min_num = min(numbers)  # 5
total = sum(numbers)    # 80
```

### Checking if All/Any Conditions are True

```python
scores = [85, 90, 78, 95]

# All scores >= 70?
all_passing = all(score >= 70 for score in scores)  # True

# Any score >= 90?
has_excellent = any(score >= 90 for score in scores)  # True
```

---

## Best Practices

### 1. Write Clean, Readable Code

✅ **Good**:
```python
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
```

❌ **Bad**:
```python
def avg(n):
    return sum(n)/len(n) if n else 0
```

### 2. Use Meaningful Variable Names

✅ **Good**:
```python
user_id = 12345
event_timestamp = "2026-01-08T10:30:00"
processed_records = 1000
```

❌ **Bad**:
```python
u = 12345
t = "2026-01-08T10:30:00"
p = 1000
```

### 3. Add Comments for Complex Logic

```python
def process_pipeline(events):
    """
    Process incoming events and filter valid ones.
    
    Args:
        events: List of event dictionaries
    
    Returns:
        List of processed events
    """
    # Filter events that occurred in the last 24 hours
    valid_events = [
        e for e in events 
        if is_recent(e['timestamp'])
    ]
    
    # Sort by timestamp for consistent processing
    return sorted(valid_events, key=lambda x: x['timestamp'])
```

### 4. Handle Errors Gracefully

```python
try:
    result = int(user_input)
    print(f"You entered: {result}")
except ValueError:
    print("Please enter a valid number")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### 5. Use Constants for Magic Numbers

```python
# Bad: Magic number
if events_count > 1000000:
    trigger_alert()

# Good: Named constant
MAX_EVENTS_BEFORE_ALERT = 1000000
if events_count > MAX_EVENTS_BEFORE_ALERT:
    trigger_alert()
```

### 6. Keep Functions Small and Focused

```python
# Good: Each function does one thing
def validate_event(event):
    """Check if event has required fields."""
    return "id" in event and "timestamp" in event

def process_event(event):
    """Transform event for pipeline."""
    return {
        "event_id": event["id"],
        "processed_at": datetime.now()
    }

# Bad: Function does too much
def do_everything(event):
    # Validates, processes, stores, etc.
    pass
```

### 7. Use Type Hints (Optional but Recommended)

```python
def calculate_total(price: float, tax_rate: float) -> float:
    """Calculate total with tax."""
    return price + (price * tax_rate)

# Helps catch errors early and improves code clarity
```

---

## Next Steps

Once you're comfortable with these fundamentals:

1. **Practice on Pychallenger** - Solidify your understanding
2. **Start the Sonic Python Lab** - Apply skills to exercises

---

## Resources

- **Official Docs**: https://docs.python.org/
- **Real Python**: https://realpython.com/ (excellent tutorials)
---

## Questions?

This guide covers fundamentals. As you use Python, you'll discover new patterns and libraries. That's normal and part of growth!

Ready to practice? Head to [Pychallenger](https://pychallenger.com/) and start building Python fluency! 🐍
