# NumPy & Pandas Lab - Setup Guide

This guide will walk you through setting up your environment to run the lab exercises. Follow these steps carefully.

## System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows
- **Disk Space**: ~500 MB for dependencies
- **Internet**: For pip package downloads

Check your Python version:

```bash
python --version
# Should show Python 3.8.x or higher
```

## Step 1: Install Required Packages

### Using pip (Recommended)

```bash
# Upgrade pip first
pip install --upgrade pip

# Install required packages
pip install numpy pandas jupyter

# Optional: useful additions
pip install matplotlib ipykernel
```

### Verify Installation

```bash
# Check installed packages
pip list

# You should see:
# numpy (version 1.x or higher)
# pandas (version 2.x or higher)
# jupyter (for notebook support)
```

### Check Versions

```bash
python -c "import numpy as np; import pandas as pd; print(f'NumPy: {np.__version__}'); print(f'pandas: {pd.__version__}')"
```

Expected output:
```
NumPy: 1.26.x (or higher)
pandas: 2.x.x (or higher)
```

## Step 2: Verify Your Setup

Run this verification script to ensure everything works:

```bash
python -c "
import numpy as np
import pandas as pd
import sys

print('=== Environment Setup Verification ===')
print(f'Python Version: {sys.version}')
print(f'NumPy Version: {np.__version__}')
print(f'pandas Version: {pd.__version__}')

# Test NumPy
arr = np.array([1, 2, 3, 4, 5])
print(f'✓ NumPy works: {arr.mean()}')

# Test pandas
df = pd.DataFrame({'col': [1, 2, 3]})
print(f'✓ pandas works: {df.shape[0]} rows')

print('=== Setup Complete ===')
"
```

You should see all checks pass with ✓ marks.

## Step 3: Clone the Lab

If you haven't already, get the lab files using the clone command.

## File Structure

Once set up, you should see:

```
sonic-numpy-pandas-lab/
├── README.md                          (Main lab overview)
├── SETUP.md                           (This file)
│
└── exercises/
    │
    ├── 01-event-metrics-numpy/
    │   ├── README.md
    │   ├── instructions.md
    │   ├── solution.md
    │   └── sample_data.py
    │
    ├── 02-event-cleaning-pandas/
    │   ├── README.md
    │   ├── instructions.md
    │   ├── solution.md
    │   └── events_raw.csv
    │
    └── 03-dashboard-analysis/
        ├── README.md
        ├── instructions.md
        ├── solution.md
        ├── events_data.csv
        └── users_data.csv
```

## Tips for Success

### Use Reference Guides

While working, keep these open:
- NumPy Fundamentals Guide
- pandas Fundamentals Guide
- Official NumPy/pandas documentation

### Work in Order

Do exercises in this order:
1. Exercise 1 (NumPy focus)
2. Exercise 2 (pandas focus)
3. Exercise 3 (Integration)

### Save Your Work

Keep your solution files with unique names:

```bash
# Instead of modifying instructions
# Create your own file:
cp exercises/01-event-metrics-numpy/instructions.md my_solution_01.py
```

### Use Version Control

Commit your work:

```bash
git add .
git commit -m "Exercise 1: Completed event metrics analysis"
```

## Getting Help

If you're stuck:

1. **Check this guide again** - Most issues covered above
2. **Review official docs**:
   - NumPy: https://numpy.org/doc/
   - pandas: https://pandas.pydata.org/docs/
3. **Ask your team** - They are here for you!
4. **Google the error message** - Likely someone solved it

## Ready?

Once you see "✓ All checks passed - you are ready!" you can start:

1. Read the main **README.md** for lab overview
2. Navigate to **exercises/01-event-metrics-numpy/**
3. Follow the exercise README and instructions
4. Build something amazing!

**Happy learning!** 🚀📊

Questions? Your team is here to help!
