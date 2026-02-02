# Exercise 1: Variables, Types, and Input - Solution

This is a reference solution. Your approach might differ slightly, and that's okay as long as your code works correctly!

---

## Complete Solution

```python
# Get user information
name = input("What is your name? ")
age = int(input("How old are you? "))
salary_monthly = float(input("What is your monthly salary? "))

# Calculate annual salary
salary_annual = salary_monthly * 12

# Display formatted summary
print("===== EMPLOYEE SUMMARY =====")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Monthly Salary: ${salary_monthly:.2f}")
print(f"Annual Salary: ${salary_annual:.2f}")
```

---

## Expected Output

When you run this with test input:

**Input**:
```
What is your name? Alex
How old are you? 28
What is your monthly salary? 5000.50
```

**Output**:
```
===== EMPLOYEE SUMMARY =====
Name: Alex
Age: 28 years old
Monthly Salary: $5000.50
Annual Salary: $60006.00
```

---

## Line-by-Line Explanation

### Getting Input

```python
name = input("What is your name? ")
```

- `input()` displays the prompt and waits for user to type
- Everything the user types is stored as a **string**
- Example: User types `Alex` → stored as `"Alex"`

```python
age = int(input("How old are you? "))
```

- `input()` returns the user's input as a string
- `int()` converts that string to an integer
- Example: User types `28` → returned as `"28"` → converted to `28`

```python
salary_monthly = float(input("What is your monthly salary? "))
```

- `input()` returns the string
- `float()` converts to a decimal number
- Example: User types `5000.50` → returned as `"5000.50"` → converted to `5000.50`

### Calculation

```python
salary_annual = salary_monthly * 12
```

- Multiplies monthly salary by 12 months
- Result is automatically a float because `salary_monthly` is a float
- Example: `5000.50 * 12 = 60006.0`

### Displaying Results

```python
print("===== EMPLOYEE SUMMARY =====")
```

- Prints a header line as-is (no variables, just text)

```python
print(f"Name: {name}")
```

- F-string: `f"text {variable} text"`
- Replaces `{name}` with the actual value of `name`
- Example: If `name = "Alex"`, prints `"Name: Alex"`

```python
print(f"Age: {age} years old")
```

- Inserts the integer value
- Example: If `age = 28`, prints `"Age: 28 years old"`

```python
print(f"Monthly Salary: {salary_monthly:.2f}$")
```

- F-string with formatting: `{variable:.2f}`
- `:.2f` means: show 2 decimal places
- Example: `5000.5` displays as `5000.50`
- The `$` is just text to indicate currency

```python
print(f"Annual Salary: {salary_annual:.2f}$")
```

- Same formatting with annual salary
- Example: `60006.0` displays as `60006.00`

---

## Key Concepts Demonstrated

### 1. Type Conversion

```python
# String to Integer
age_str = "28"
age = int(age_str)  # Now it's 28, not "28"

# String to Float
salary_str = "5000.50"
salary = float(salary_str)  # Now it's 5000.50, not "5000.50"

# Integer to Float (automatic)
monthly = 5000
annual = monthly * 12.0  # Result is float, not int
```

### 2. F-Strings

```python
# Basic f-string
name = "Alex"
print(f"Hello, {name}")  # Output: Hello, Alex

# With formatting (2 decimal places)
price = 19.5
print(f"Price: ${price:.2f}")  # Output: Price: $19.50

# Multiple variables
age = 28
city = "San Francisco"
print(f"{name} is {age} and lives in {city}")
# Output: Alex is 28 and lives in San Francisco
```

### 3. Arithmetic with Variables

```python
monthly = 5000
annual = monthly * 12  # Simple multiplication

# More complex
base_salary = 5000
bonus = base_salary * 0.10  # 10% bonus
total = base_salary + bonus  # Add them together
```

---

## Common Variations

### Alternative 1: Separate Input and Conversion

Instead of:
```python
age = int(input("How old are you? "))
```

You could write:
```python
age_str = input("How old are you? ")
age = int(age_str)
```

Both are equivalent. The first is more concise; the second is more explicit.

### Alternative 2: Different Formatting

Instead of:
```python
print(f"Monthly Salary: ${salary_monthly:.2f}")
```

You could write:
```python
print(f"Monthly Salary: ${round(salary_monthly, 2)}")
```

Or even:
```python
print("Monthly Salary: $" + str(round(salary_monthly, 2)))
```

F-strings are recommended as they're most readable.

### Alternative 3: Using Variables in Prompts

```python
name = "Alex"
age = input(f"What age are you, {name}? ")
```

You can use f-strings in prompts too!

---

## What to Look For in Your Solution

✅ **Does it run without errors?**
- If you get a `NameError`, you used a variable before defining it
- If you get a `TypeError`, you tried to do math with wrong types

✅ **Does it produce correct output?**
- Annual salary should be monthly × 12
- Currency should show 2 decimal places

✅ **Are variable names meaningful?**
- `age` is better than `a`
- `salary_monthly` is better than `sm`

✅ **Does it have comments?**
- Comments help you (and others) understand the code
- Use `#` to start a comment

✅ **Is the output formatted nicely?**
- Users prefer pretty output
- The formatting makes code more professional

---

### Great job on Exercise 1!

🎉 You've covered the fundamentals of variables, types, and I/O. Ready for Exercise 2?
