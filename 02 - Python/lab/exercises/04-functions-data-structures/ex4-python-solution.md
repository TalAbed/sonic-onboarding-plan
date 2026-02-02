# Exercise 4: Functions and Data Structures - Solution

This is a reference solution. Your approach might differ—as long as it works correctly!

---

## Complete Solution

```python
# =================================================
# EVENT DATA
# =================================================

# Sample events from the pipeline
events = [
    {"id": 1, "status": "ok", "latency_ms": 120},
    {"id": 2, "status": "error", "latency_ms": 900},
    {"id": 3, "status": "ok", "latency_ms": 450},
    {"id": 4, "status": "ok", "latency_ms": 200},
    {"id": 5, "status": "error", "latency_ms": 1100},
]

# =================================================
# FUNCTION DEFINITIONS
# =================================================

def count_errors(events):
    """
    Count how many events have status 'error'.
    
    Parameters:
        events: list of event dictionaries
    
    Returns:
        int: number of events with errors
    """
    error_count = 0
    for event in events:
        if event["status"] == "error":
            error_count += 1
    return error_count


def average_latency(events):
    """
    Calculate average latency across all events.
    
    Parameters:
        events: list of event dictionaries
    
    Returns:
        float: average latency in milliseconds
    """
    if len(events) == 0:
        return 0.0
    
    total_latency = 0
    for event in events:
        total_latency += event["latency_ms"]
    
    average = total_latency / len(events)
    return average


def get_slow_events(events, threshold):
    """
    Filter events with latency above threshold.
    
    Parameters:
        events: list of event dictionaries
        threshold: latency threshold in milliseconds
    
    Returns:
        list: events with latency > threshold
    """
    slow_events = []
    for event in events:
        if event["latency_ms"] > threshold:
            slow_events.append(event)
    return slow_events


# =================================================
# MAIN PROGRAM - CALL FUNCTIONS AND DISPLAY
# =================================================

print("=== EVENT PROCESSING ===\n")

# Call count_errors function
errors = count_errors(events)
print(f"Number of errors: {errors}")

# Call average_latency function
avg_latency = average_latency(events)
print(f"Average latency: {avg_latency:.1f}ms")

# Call get_slow_events function
slow_threshold = 500
slow_events = get_slow_events(events, slow_threshold)
print(f"\nSlow events (over {slow_threshold}ms):")
for event in slow_events:
    print(f"  Event ID {event['id']}: {event['latency_ms']}ms")
```

---

## Expected Output

```
=== EVENT PROCESSING ===

Number of errors: 2
Average latency: 554.0ms

Slow events (over 500ms):
  Event ID 2: 900ms
  Event ID 5: 1100ms
```

---

## Line-by-Line Explanation

### Event Data Structure

```python
events = [
    {"id": 1, "status": "ok", "latency_ms": 120},
    {"id": 2, "status": "error", "latency_ms": 900},
    ...
]
```

**How it works**:
- `events` is a list `[]`
- Each item in the list is a dictionary `{}`
- Each dictionary has three key-value pairs:
  - `"id"`: unique identifier
  - `"status"`: "ok" or "error"
  - `"latency_ms"`: response time

**Accessing data**:
```python
first_event = events[0]           # Get first event
status = first_event["status"]    # Get status from event
latency = events[1]["latency_ms"] # Get latency directly
```

---

### Function 1: count_errors

```python
def count_errors(events):
    error_count = 0
    for event in events:
        if event["status"] == "error":
            error_count += 1
    return error_count
```

**How it works**:
1. `def count_errors(events):` defines the function with one parameter
2. `error_count = 0` initializes a counter
3. Loop through each event in the list
4. Check if the event's status is "error"
5. If true, increment the counter
6. `return error_count` sends the count back

**Execution with example data**:
```
Event 1: status = "ok" → skip
Event 2: status = "error" → count = 1
Event 3: status = "ok" → skip
Event 4: status = "ok" → skip
Event 5: status = "error" → count = 2
Return: 2
```

---

### Function 2: average_latency

```python
def average_latency(events):
    if len(events) == 0:
        return 0.0
    
    total_latency = 0
    for event in events:
        total_latency += event["latency_ms"]
    
    average = total_latency / len(events)
    return average
```

**How it works**:
1. First, check if list is empty (avoid division by zero)
2. Initialize `total_latency` to 0
3. Loop through each event, summing the latency values
4. Calculate average: total ÷ count
5. Return the average

**Execution with example data**:
```
Sum: 120 + 900 + 450 + 200 + 1100 = 2770
Count: 5
Average: 2770 / 5 = 554.0
Return: 554.0
```

---

### Function 3: get_slow_events

```python
def get_slow_events(events, threshold):
    slow_events = []
    for event in events:
        if event["latency_ms"] > threshold:
            slow_events.append(event)
    return slow_events
```

**How it works**:
1. Create an empty list to hold filtered results
2. Loop through each event
3. Check if latency exceeds threshold
4. If true, add the entire event to the new list using `append()`
5. Return the filtered list

**Execution with threshold = 500**:
```
Event 1 (120ms): < 500 → skip
Event 2 (900ms): > 500 → add to list
Event 3 (450ms): < 500 → skip
Event 4 (200ms): < 500 → skip
Event 5 (1100ms): > 500 → add to list
Return: [Event 2, Event 5]
```

---

### Calling Functions and Using Results

```python
errors = count_errors(events)
print(f"Number of errors: {errors}")
```

**How it works**:
1. Call the function with `events` as argument
2. Function processes and returns a value
3. Store the returned value in `errors`
4. Print the result

```python
avg_latency = average_latency(events)
print(f"Average latency: {avg_latency:.1f}ms")
```

Same pattern, but stores a float and formats it with `.1f` (1 decimal place).

```python
slow_events = get_slow_events(events, slow_threshold)
for event in slow_events:
    print(f"  Event ID {event['id']}: {event['latency_ms']}ms")
```

This time:
1. Call function with two arguments
2. Function returns a list
3. Loop through the returned list
4. Access dictionary values from each event

---

## Key Patterns

### Pattern 1: Simple Function with Counter

```python
def count_items(items, condition):
    count = 0
    for item in items:
        if condition(item):
            count += 1
    return count
```

### Pattern 2: Calculating Aggregate

```python
def calculate_average(values):
    if len(values) == 0:
        return 0
    total = sum(values)
    return total / len(values)
```

### Pattern 3: Filtering a List

```python
def filter_items(items, predicate):
    result = []
    for item in items:
        if predicate(item):
            result.append(item)
    return result
```

### Pattern 4: Processing Dictionary in List

```python
def process_events(events):
    for event in events:
        # Access dictionary values
        event_id = event["id"]
        status = event["status"]
        # Process...
```

---

## Working with Dictionaries in Functions

### Accessing Values

```python
# Using bracket notation
status = event["status"]

# Using get() with default
status = event.get("status", "unknown")  # Returns "unknown" if key missing
```

### Checking Keys

```python
if "status" in event:
    print(event["status"])
```

### Adding to Dictionary

```python
event["processed"] = True
event["timestamp"] = "2026-01-12"
```

### Common Dictionary Operations

```python
# Get all keys
keys = event.keys()  # dict_keys(['id', 'status', 'latency_ms'])

# Get all values
values = event.values()  # dict_values([1, 'ok', 120])

# Get both key and value
for key, value in event.items():
    print(f"{key}: {value}")
```

---

## Function Design Principles

### Single Responsibility

Each function should do ONE thing:
- ✅ `count_errors()` - just counts
- ✅ `average_latency()` - just calculates average
- ❌ `process_and_count_and_average()` - too much!

### Clear Names

Function names should describe what they do:
- ✅ `count_errors()`
- ✅ `get_slow_events()`
- ❌ `process()` - too vague

### Parameters vs Globals

Pass data as parameters, don't use global variables:
- ✅ `count_errors(events)` - parameter passed in
- ❌ `count_errors()` - relies on global `events`

---

## Testing Your Functions

### Manual Testing

```python
# Test count_errors
test_events = [
    {"id": 1, "status": "error", "latency_ms": 100},
    {"id": 2, "status": "ok", "latency_ms": 200},
]
assert count_errors(test_events) == 1, "Should count 1 error"

# Test average_latency
assert average_latency(test_events) == 150, "Average should be 150"

# Test get_slow_events
slow = get_slow_events(test_events, 150)
assert len(slow) == 0, "No events > 150"
```

### Edge Cases

```python
# Empty list
empty_events = []
count_errors(empty_events)  # Should return 0
average_latency(empty_events)  # Should return 0.0

# All errors
all_errors = [
    {"id": 1, "status": "error", "latency_ms": 100},
    {"id": 2, "status": "error", "latency_ms": 200},
]
count_errors(all_errors)  # Should return 2

# No matches
no_slow = [
    {"id": 1, "status": "ok", "latency_ms": 100},
    {"id": 2, "status": "ok", "latency_ms": 200},
]
get_slow_events(no_slow, 300)  # Should return empty list
```

---

## Common Variations

### Using List Comprehension (Advanced)

```python
# Instead of:
def get_slow_events(events, threshold):
    slow = []
    for event in events:
        if event["latency_ms"] > threshold:
            slow.append(event)
    return slow

# You could write:
def get_slow_events(events, threshold):
    return [e for e in events if e["latency_ms"] > threshold]
```

### Using Built-in Functions

```python
# Instead of manual sum:
total = 0
for event in events:
    total += event["latency_ms"]
average = total / len(events)

# You could use:
latencies = [e["latency_ms"] for e in events]
average = sum(latencies) / len(latencies)
```

### Function with Docstring

```python
def my_function(param1, param2):
    """
    One-line description of what this does.
    
    Longer description if needed.
    
    Args:
        param1: description of first parameter
        param2: description of second parameter
    
    Returns:
        description of return value
    """
    # implementation
```

---

## Next Steps

1. ✅ Compare your code to this solution
2. ✅ Run both with the same data
3. ✅ Make sure you understand each function
4. ✅ Try modifying the events list and testing again
5. ✅ Try writing new functions (e.g., count_ok, max_latency, etc.)

---

## Congratulations! 🎉

You've completed all four exercises! You now understand:

✅ **Exercise 1**: Variables, types, and input/output  
✅ **Exercise 2**: Conditionals and making decisions  
✅ **Exercise 3**: Loops and processing data  
✅ **Exercise 4**: Functions and organizing code  

**You've mastered Python fundamentals!** 

These skills form the foundation for data engineering work. From here, you're ready to:
- Learn libraries (pandas, requests, etc.)
- Build real data pipelines
- Work with databases and APIs
- Contribute to Sonic projects

You've done excellent work! 🐍🚀
