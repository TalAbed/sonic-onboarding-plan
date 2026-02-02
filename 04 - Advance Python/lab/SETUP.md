# Advanced Python Lab - SETUP

Follow this guide to set up your environment for the Advanced Python lab.

---

## Prerequisites

Before starting, make sure you have:

✅ **Python 3.8+** installed  
✅ **pip** (Python package manager)  
✅ Completed Sections 1-3 (Git, Basic Python, NumPy/Pandas)  
✅ Read the 4 reference guides:
- oop-for-data-engineering.md
- functional-python.md
- async-and-concurrency.md
- error-handling-and-logging.md

---

## Step 1: Create Project Structure

Create a folder for your lab work:

```bash
# Create main directory
mkdir section4-advanced-python
cd section4-advanced-python

# Create subdirectories
mkdir exercises
mkdir data
mkdir results
```

Your structure should look like:
```
section4-advanced-python/
├── exercises/
│   ├── exercise-1-oop/
│   ├── exercise-2-functional/
│   └── exercise-3-concurrency/
├── data/
│   ├── events_raw.csv (will be generated)
│   └── events_large.csv (will be generated)
├── results/
│   ├── exercise-1-output.json
│   ├── exercise-2-output.json
│   └── exercise-3-output.json
├── section4-lab-readme.md
└── SETUP.md (this file)
```

---

## Step 2: Install Required Packages

The exercises use these standard Python packages:

```bash
# Core packages (usually already installed)
# - logging (built-in)
# - json (built-in)
# - csv (built-in)
# - time (built-in)
# - threading (built-in)
# - concurrent.futures (built-in)
# - asyncio (built-in)
# - abc (built-in)

# Optional but recommended for exercises
pip install requests         # For API calls in examples
pip install pandas          # For CSV reading (Exercise 1 setup)
pip install aiohttp         # For async HTTP (Exercise 3 optional)
```

**If you want a fresh environment:**

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install packages
pip install pandas requests aiohttp
```

---

## Step 3: Verify Your Setup

Create a test file `test_setup.py`:

```python
#!/usr/bin/env python3
"""Verify Section 4 lab setup."""

import sys
import json
import logging
from concurrent.futures import ThreadPoolExecutor
import asyncio

print("=" * 60)
print("SECTION 4 SETUP VERIFICATION")
print("=" * 60)

# Check Python version
print(f"\n✓ Python version: {sys.version}")
assert sys.version_info >= (3, 8), "Python 3.8+ required"

# Check built-in modules
modules = [
    'json', 'csv', 'logging', 'time', 'threading',
    'concurrent.futures', 'asyncio', 'abc'
]

print("\n✓ Built-in modules:")
for module in modules:
    try:
        __import__(module)
        print(f"  ✓ {module}")
    except ImportError:
        print(f"  ✗ {module} - FAILED")
        sys.exit(1)

# Check optional packages
print("\n✓ Optional packages:")
optional = ['pandas', 'requests', 'aiohttp']
for package in optional:
    try:
        __import__(package)
        print(f"  ✓ {package}")
    except ImportError:
        print(f"  ⚠ {package} - not installed (optional)")

# Test basic OOP
print("\n✓ Testing OOP:")
class TestClass:
    def __init__(self):
        self.value = 42
    
    def method(self):
        return self.value

obj = TestClass()
assert obj.method() == 42
print("  ✓ Classes and methods work")

# Test decorators
print("\n✓ Testing decorators:")
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def test_func():
    return "works"

assert test_func() == "works"
print("  ✓ Decorators work")

# Test comprehensions
print("\n✓ Testing comprehensions:")
result = [x*2 for x in range(5)]
assert result == [0, 2, 4, 6, 8]
print("  ✓ List comprehensions work")

# Test threading
print("\n✓ Testing threading:")
def thread_task():
    return "done"

with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(thread_task)
    assert future.result() == "done"
print("  ✓ Threading works")

# Test async
print("\n✓ Testing async:")
async def async_task():
    return "async works"

result = asyncio.run(async_task())
assert result == "async works"
print("  ✓ Async/await works")

print("\n" + "=" * 60)
print("✓ ALL CHECKS PASSED!")
print("=" * 60)
print("\nYou're ready to start Section 4! 🚀")
```

Run it:
```bash
python test_setup.py
```

Expected output:
```
============================================================
SECTION 4 SETUP VERIFICATION
============================================================

✓ Python version: 3.9.x ...
✓ Built-in modules:
  ✓ json
  ✓ csv
  ... (all modules)

✓ Optional packages:
  ✓ pandas
  ✓ requests
  ⚠ aiohttp - not installed (optional)

✓ Testing OOP:
  ✓ Classes and methods work
✓ Testing decorators:
  ✓ Decorators work
✓ Testing comprehensions:
  ✓ List comprehensions work
✓ Testing threading:
  ✓ Threading works
✓ Testing async:
  ✓ Async/await works

============================================================
✓ ALL CHECKS PASSED!
============================================================

You're ready to start Section 4! 🚀
```

---

## Step 4: Set Up Each Exercise Directory

For each exercise, create the working directory:

### Exercise 1: OOP

```bash
# Create directory
mkdir -p exercises/exercise-1-oop
cd exercises/exercise-1-oop

# You'll put your code here:
# - exercise-1-solution.py (your implementation)
# - events_raw.csv (generated data)
# - events_processed.json (your output)
```

### Exercise 2: Functional

```bash
# Create directory
mkdir -p exercises/exercise-2-functional
cd exercises/exercise-2-functional

# You'll refactor Exercise 1 solution here:
# - exercise-2-solution.py (refactored version)
# - performance_comparison.json (benchmarks)
```

### Exercise 3: Concurrency

```bash
# Create directory
mkdir -p exercises/exercise-3-concurrency
cd exercises/exercise-3-concurrency

# You'll add concurrency here:
# - exercise-3-solution.py (concurrent version)
# - events_large.csv (large sample data)
# - errors_report.json (error analysis)
# - performance_metrics.json (timing results)
```

---

## Step 5: Generate Sample Data

### For Exercises 1 & 2 (Small Dataset)

Create `generate_data.py` in your `exercises/exercise-1-oop/` directory:

```python
#!/usr/bin/env python3
"""Generate sample event data for Exercise 1."""

import csv
import json
from datetime import datetime, timedelta
import random

# Configuration
NUM_EVENTS = 100
OUTPUT_FILE = 'events_raw.csv'

# Sample data
EVENT_TYPES = ['purchase', 'login', 'checkout', 'view']
STATUSES = ['ok', 'error', 'timeout']
USER_IDS = [f'user_{i}' for i in range(1, 20)]

def generate_events(num_events):
    """Generate sample events."""
    events = []
    base_time = datetime(2026, 1, 15, 0, 0, 0)
    
    for i in range(num_events):
        event = {
            'event_id': i + 1,
            'timestamp': (base_time + timedelta(seconds=i*10)).isoformat(),
            'event_type': random.choice(EVENT_TYPES),
            'user_id': random.choice(USER_IDS),
            'status': random.choice(STATUSES),
            'latency_ms': random.randint(50, 2000)
        }
        events.append(event)
    
    return events

def write_csv(events, filename):
    """Write events to CSV."""
    fieldnames = ['event_id', 'timestamp', 'event_type', 'user_id', 'status', 'latency_ms']
    
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)
    
    print(f"✓ Generated {len(events)} events in {filename}")

if __name__ == '__main__':
    events = generate_events(NUM_EVENTS)
    write_csv(events, OUTPUT_FILE)
    print(f"✓ Sample data ready for Exercise 1!")
```

Run it:
```bash
cd exercises/exercise-1-oop/
python generate_data.py
# Output: ✓ Generated 100 events in events_raw.csv
```

### For Exercise 3 (Large Dataset)

Create `generate_large_data.py` in `exercises/exercise-3-concurrency/`:

```python
#!/usr/bin/env python3
"""Generate large event data for Exercise 3 (concurrency)."""

import csv
from datetime import datetime, timedelta
import random

NUM_EVENTS = 10000
OUTPUT_FILE = 'events_large.csv'

EVENT_TYPES = ['purchase', 'login', 'checkout', 'view']
STATUSES = ['ok', 'error', 'timeout']
USER_IDS = [f'user_{i}' for i in range(1, 100)]

def generate_events(num_events):
    """Generate sample events."""
    base_time = datetime(2026, 1, 15, 0, 0, 0)
    
    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=['event_id', 'timestamp', 'event_type', 'user_id', 'status', 'latency_ms']
        )
        writer.writeheader()
        
        for i in range(num_events):
            if i % 1000 == 0:
                print(f"  Generated {i}/{num_events}...")
            
            event = {
                'event_id': i + 1,
                'timestamp': (base_time + timedelta(seconds=i*2)).isoformat(),
                'event_type': random.choice(EVENT_TYPES),
                'user_id': random.choice(USER_IDS),
                'status': random.choice(STATUSES),
                'latency_ms': random.randint(50, 2000)
            }
            writer.writerow(event)
    
    print(f"✓ Generated {NUM_EVENTS} events in {OUTPUT_FILE}")

if __name__ == '__main__':
    generate_events(NUM_EVENTS)
```

Run it:
```bash
cd exercises/exercise-3-concurrency/
python generate_large_data.py
# Output: ✓ Generated 10000 events in events_large.csv
```

---

## Step 6: Verify Everything Is Ready

Checklist before starting exercises:

```
✓ Python 3.8+ installed
✓ Required packages installed (pip install pandas requests)
✓ test_setup.py passed all checks
✓ Directory structure created:
  - exercises/exercise-1-oop/
  - exercises/exercise-2-functional/
  - exercises/exercise-3-concurrency/
✓ Sample data generated:
  - exercises/exercise-1-oop/events_raw.csv (100 events)
  - exercises/exercise-3-concurrency/events_large.csv (10,000 events)
✓ Read the Lab README
✓ Read all 4 reference guides
```

---

## Ready to Start?

You're all set! Here's what to do next:

1. **Start with Exercise 1:**
   ```bash
   cd exercises/exercise-1-oop/
   # Read exercise-1-instructions.md
   # Start coding!
   ```

2. **After completing Exercise 1:** Move to Exercise 2
3. **After completing Exercise 2:** Move to Exercise 3

---

## Troubleshooting

### "Module not found" errors

```bash
# Reinstall packages
pip install --upgrade pandas requests aiohttp

# Or use virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install pandas requests aiohttp
```

### "Python version too old"

```bash
# Check your Python version
python --version

# Install Python 3.8+ from python.org
```

### "Can't generate sample data"

```bash
# Make sure you're in the right directory
cd exercises/exercise-1-oop/
python generate_data.py

# Check if events_raw.csv was created
ls events_raw.csv
```

### "test_setup.py fails"

Review the error message and:
1. Check Python version: `python --version` (need 3.8+)
2. Check imports: `python -c "import asyncio"` (should work)
3. Reinstall packages: `pip install --upgrade pandas requests`

---

## Tips for Success

✅ **Work in the right directory** - Each exercise has its own folder  
✅ **Generate data first** - Run the data generation scripts before starting  
✅ **Read instructions carefully** - They provide important context  
✅ **Reference the guides** - When confused, check the relevant guide  
✅ **Write clean code** - Use comments, proper naming, structure  
✅ **Test as you go** - Don't wait until the end  
✅ **Debug patiently** - Use print statements and logging  

---

## Environment Variables (Optional)

For Exercise 3, you might want to set environment variables:

```bash
# Set log level
export LOG_LEVEL=INFO

# Set number of workers
export NUM_WORKERS=10

# Set timeout
export TIMEOUT=30
```

Or in Python:
```python
import os

log_level = os.environ.get('LOG_LEVEL', 'INFO')
num_workers = int(os.environ.get('NUM_WORKERS', 10))
timeout = int(os.environ.get('TIMEOUT', 30))
```

---

## You're Ready! 🚀

Your environment is set up. Your data is ready. Your reference guides are available.

**Time to build something amazing!**

Start with Exercise 1:
```bash
cd exercises/exercise-1-oop/
# Read exercise-1-instructions.md
# Follow the steps
# Write awesome code!
```

Good luck! 💪

