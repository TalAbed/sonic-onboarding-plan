# Exercise 1: Variables, Types, and Input - Instructions

Follow these instructions carefully. Each step builds on the previous one. Think through what you need to do before writing code.

---

## Step 1: Create Your Solution File

Create a new file called `solution.py` in this directory.

You can do this by:
- Using your text editor's File → New menu
- Right-clicking in your file explorer and creating a new file
- Using the command line: `touch solution.py`

Open `solution.py` in your text editor and get ready to start coding.

---

## Step 2: Get the User's Name

Write code that asks the user "What is your name?" and stores their response.

**Think about**:
- Which function lets you ask for user input?
- What variable name would be appropriate?

---

## Step 3: Get the User's Age

Ask the user "How old are you?" and store their response.

**Important**: The user will type a number, but `input()` returns text. You need to convert it to the correct type.

**Think about**:
- Which conversion function should you use?
- How do you convert and store in one line?

---

## Step 4: Get the User's Monthly Salary

Ask the user "What is your monthly salary?" and store their response with the correct data type.

**Think about**:
- What type should salary be: integer or float? Why?
- What conversion function handles decimal numbers?
- Should this be similar to Step 3?

---

## Step 5: Calculate Annual Salary

Using the monthly salary, calculate what the annual salary would be.

---

## Step 6: Test Your Input Section

At this point, your program should ask for name, age, and salary. Before moving on, run your program:

```bash
python solution.py
```

**Verify**:
- Does each prompt appear?
- Can you type in responses?
- Does it run without errors?

If you get errors, check:
- Did you type the function names correctly?
- Are your parentheses matched?
- Did you include the quotes in your strings?

---

## Step 7: Display the Information

Print out the information you've collected. Start simple—just display each piece of data.

**Think about**:
- How do you display text with `print()`?
- What should your output look like?
- Try printing each variable



Run your program again and verify the values are correct.

---

## Step 8: Format the Output Professionally

Now make the output look professional and user-friendly.

**Think about**:
- How can you add labels to the output?
- Can you organize it nicely?
- From the fundamentals guide, what tool lets you insert variables into strings?

Review the String Formatting section of the fundamentals guide for options.

**Consider**:
- Should salary values show a dollar sign?
- Should they show a specific number of decimal places?
- How can you make this clear and professional?

---

## Step 9: Add Comments

Go through your code and add comments explaining what each section does.

**Guidelines**:
- Comments start with `#`
- Add a comment before major sections
- Explain the "why" not the obvious "what"

Examples of good comments:
- `# Get user information`
- `# Convert age to integer since input() returns strings`
- `# Calculate what they earn in a year`

---

## Step 10: Final Testing

Test your program thoroughly:

```bash
python solution.py
```

**Test cases to try**:
1. Enter a name, age, and salary
2. Verify the annual salary calculation is correct (multiply by 12)
3. Run it again with different values to make sure it works consistently

**Check**:
- Does the program run without errors?
- Is the output formatted nicely?
- Are all calculations correct?
- Are there appropriate comments?

---

## You've Completed Exercise 1! 🎉

### What to Verify

Before moving on, make sure your code:

✅ Asks for name, age, and monthly salary  
✅ Stores values with appropriate data types  
✅ Calculates annual salary correctly  
✅ Displays output in a professional format  
✅ Includes helpful comments  
✅ Runs without errors  

---

## Hints If You Get Stuck

**If you get a TypeError about adding strings:**
- Remember: `input()` returns strings, not numbers
- Check if you converted to `int()` or `float()`

**If the output looks messy:**
- Review the String Formatting section of the fundamentals guide
- Look at how f-strings work

**If you're unsure about format:**
- Open `solution.md` and look at what the expected output looks like
- But try to code it yourself first!

---

## Next: Compare to Reference Solution

Once you're satisfied with your solution:

1. Check that it runs correctly
2. Verify the output makes sense
3. Then open [solution.md](./ex1-python-solution.md) to see a reference solution

Compare your approach:
- Does it work the same way?
- Are there different ways to solve it?
- What can you learn from the reference?

Great effort on your first Python exercise! 🐍
