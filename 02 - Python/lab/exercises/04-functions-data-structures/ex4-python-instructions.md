# Exercise 4: Functions and Data Structures - Instructions

Follow these instructions carefully. Work through each step and think about how functions make code cleaner and reusable.

---

## Step 1: Create Your Solution File

Create a new file called `solution.py` in this directory.

Open it in your text editor.

---

## Step 2: Define Your Event Data

Create a list of events. Each event is a dictionary with:
- `"id"`: unique identifier
- `"status"`: either "ok" or "error"
- `"latency_ms"`: response time in milliseconds

**Example events**:
```python
events = [
    {"id": 1, "status": "ok", "latency_ms": 120},
    {"id": 2, "status": "error", "latency_ms": 900},
    {"id": 3, "status": "ok", "latency_ms": 450},
    {"id": 4, "status": "ok", "latency_ms": 200},
    {"id": 5, "status": "error", "latency_ms": 1100},
]
```

Define this list in your program.

---

## Step 3: Write a Function to Count Errors

Write a function that:
- Takes a list of events as a parameter
- Counts how many events have `"status": "error"`
- Returns the count

**Function behavior**:
- Input: list of events
- Output: integer (count of errors)
- Example: with the list above, should return 2

---

## Step 4: Write a Function to Calculate Average Latency

Write a function that:
- Takes a list of events as a parameter
- Calculates the average latency across all events
- Returns the average as a float

**Function behavior**:
- Input: list of events
- Output: float (average latency)
- Example: with the list above, average should be 554

---

## Step 5: Test Your Functions

Call each function with your events list and print the results.

**Example output**:
```
Number of errors: 2
Average latency: 554.0ms
```

---

## Step 6: Add a Third Function

Write a function called `get_slow_events` that:
- Takes a list of events and a threshold (in milliseconds) as parameters
- Returns a list of only the events that are slower than the threshold
- Example: `get_slow_events(events, 500)` should return events with latency > 500

**Function behavior**:
- Input: list of events, integer threshold
- Output: list of slow events
- Example: with threshold 500, should return 3 events

---

## Step 7: Call Your Third Function and Display Results

Call the third function you wrote and display the results.

**Example output**:
```
Slow events (over 500ms):
  Event ID 2: 900ms
  Event ID 5: 1100ms
```

---

## Step 8: Organize Your Code with Sections

Reorganize your code into clear sections:
1. Define the event data
2. Define all functions
3. Call the functions and display results

Add comments to separate each section.

---

## Step 9: Add Helpful Comments and Docstrings

Add comments explaining:
- What each function does
- What parameters it expects
- What it returns

**Example comment structure**:
```python
def count_errors(events):
    # Count how many events have errors
    # Returns: integer count of errors
    # ...
```

---

## Step 10: Final Testing

Test your complete program with the sample data.

**Example of successful output**:

```
=== EVENT PROCESSING ===

Number of errors: 2
Average latency: 554.0ms

Slow events (over 500ms):
  Event ID 2: 900ms
  Event ID 5: 1100ms
```

**Try with different data**:
- Create a new events list with different values
- Call your functions with this new data
- Verify results are correct

---

## You've Completed Exercise 4! 🎉

### What to Verify

Before moving on, make sure your code:

✅ Defines functions with clear parameters  
✅ Functions return appropriate values  
✅ You can work with lists of dictionaries  
✅ You can access dictionary values correctly  
✅ ALl functions work correctly  
✅ Code is organized into clear sections  
✅ Code is readable with meaningful names  
✅ Comments explain the purpose of functions  

---

## Next: Compare to Reference Solution

Once you're satisfied:

1. Verify all functions work correctly
2. Check that output format matches expected
3. Open [solution.md](./ex4-python-solution.md) to see a reference solution

Compare your approach and see how the reference handles function definitions and data processing. Excellent work completing all four exercises! 🐍
