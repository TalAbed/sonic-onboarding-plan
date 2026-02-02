# Sonic Python Lab - Setup Guide

Before you start the exercises, follow this setup guide to prepare your local environment. This should take about 5-10 minutes.

## Prerequisites

Make sure you have:
- ✅ Python 3.8+ installed on your machine
- ✅ A text editor or IDE (Pycharm recommended)
- ✅ Terminal/command prompt access
- ✅ Completed the Python video tutorial and fundamentals guide

If Python isn't installed, download it from [python.org](https://www.python.org/downloads/).

---

## Step 1: Verify Python Installation

Check that Python is installed and working:

```bash
# Check Python version
python --version
# or
python3 --version
```

**Expected output**: Python 3.8 or higher

Example:
```
Python 3.10.12
```

If you get "command not found," Python isn't installed. Install it before proceeding.

---

## Step 2: Create a Working Directory

Create a folder where you'll store your lab exercises:

```bash
# Create directory
mkdir sonic-python-lab-work
cd sonic-python-lab-work

# Verify you're in the directory
pwd
```

This is your workspace for all four exercises.

---

## Step 3: Understand the Exercise Structure

Each exercise folder contains:

```
01-variables-types-input/
├── README.md          (exercise overview & objectives)
├── instructions.md    (step-by-step walkthrough)
└── solution.md        (reference solution with explanation)
```

You'll create your own `solution.py` file in each exercise directory as you work.

---

## Step 4: Understand How to Run Exercises

For each exercise, you'll:

1. Read the instructions in `instructions.md`
2. Create a file called `solution.py` (or as specified)
3. Write your code
4. Run it to test:

```bash
# In the exercise directory
python solution.py
```

5. Compare your output with what's expected
6. Check the reference solution in `solution.md`

---

## Step 5: File Organization

Organize your work like this:

```
sonic-python-lab-work/
├── 01-variables-types-input/
│   ├── README.md               (from lab repo)
│   ├── instructions.md         (from lab repo)
│   ├── solution.md             (from lab repo)
│   └── solution.py             (YOU create this)
├── 02-conditionals-logic/
│   ├── README.md
│   ├── instructions.md
│   ├── solution.md
│   └── solution.py             (YOU create this)
├── 03-loops-aggregations/
│   ├── README.md
│   ├── instructions.md
│   ├── solution.md
│   └── solution.py             (YOU create this)
└── 04-functions-data-structures/
    ├── README.md
    ├── instructions.md
    ├── solution.md
    └── solution.py             (YOU create this)
```

---

## Step 6: Copy Lab Files

Copy the lab exercise files to your working directory:

**Clone from Git**
```bash
git clone https://gitlab.com/sonic2791202/sonic-onboarding.git
cd sonic-onboarding/02 - Python/lab
```

---

## Quick Reference Commands

| Command | Purpose |
|---------|---------|
| `python --version` | Check Python version |
| `python filename.py` | Run a Python file |
| `python` | Open interactive Python shell |
| `exit()` | Exit Python shell |
| `pwd` | Show current directory |
| `cd dirname` | Change directory |
| `mkdir dirname` | Create directory |
| `ls` or `dir` | List files |

---

## Troubleshooting Setup

### "python: command not found"
Python isn't installed or not in your PATH. Download and install from [python.org](https://www.python.org/).

### "No such file or directory"
Make sure you're in the correct directory:
```bash
pwd  # See where you are
ls   # List files in current directory
```

### "Permission denied" when running Python file
Make the file executable:
```bash
chmod +x solution.py
./solution.py
```

Or just use:
```bash
python solution.py
```

### Python shell opens instead of running file
You're typing `python` without a filename. To run a file:
```bash
python solution.py  # Correct
python              # Wrong - opens interactive shell
```

Exit with `exit()` if you accidentally opened the shell.

---

## Next Steps

Once setup is complete:

1. ✅ Go back to [README.md](./README.md)
2. ✅ Start with [Exercise 1](./exercises/01-variables-types-input/)
3. ✅ Follow the instructions carefully
4. ✅ Write your code and test it
5. ✅ Compare with the reference solution

---

**Ready?** Move to Exercise 1 and start coding! 🚀
