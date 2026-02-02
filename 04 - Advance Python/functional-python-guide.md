# Functional Python

## Introduction

**Functional programming** is a way of thinking about code where:
- Functions are **first-class citizens** (can be passed around like data)
- Data is **immutable** (doesn't change)
- **Computation is composition** of functions (chaining operations)

For data engineering, functional programming shines when you need to:
- Transform sequences of data (filter out bad records, map to new format)
- Chain multiple operations together clearly
- Write concise, expressive code that's easy to test
- Avoid side effects (functions that modify global state)

**Python isn't purely functional**, but it has excellent functional tools. This guide shows you how to use them.

---

## Core Concepts

### 1. Lambda Functions (Anonymous Functions)

A **lambda** is a small, nameless function. Use it for simple operations.

```python
# Regular function
def double(x):
    return x * 2

# Lambda equivalent
double = lambda x: x * 2

# Most useful: lambda as argument to another function
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10]
```

**When to use lambdas:**
- ✅ Simple, one-line operations
- ✅ Passed as arguments (callbacks)
- ❌ Complex logic (use regular functions instead)
- ❌ Anything with multiple lines

**Lambda syntax:**
```python
lambda arguments: expression

# Examples
lambda x: x + 1
lambda x, y: x + y
lambda event: event['status'] == 'error'
lambda x: x * 2 if x > 0 else 0
```

### 2. Map Function

**Map** applies a function to every item in a sequence.

```python
# Without map - explicit loop
results = []
for event in events:
    results.append({'id': event['id'], 'status': event['status'].upper()})

# With map - functional
results = list(map(lambda e: {'id': e['id'], 'status': e['status'].upper()}, events))

# Or better - define a function
def normalize_event(event):
    return {'id': event['id'], 'status': event['status'].upper()}

results = list(map(normalize_event, events))
```

**Key point:** Map returns an iterator, so convert to list if you need it all at once.

```python
# Better - use list comprehension (more Pythonic)
results = [normalize_event(e) for e in events]
```

### 3. Filter Function

**Filter** keeps only items that match a condition.

```python
# Without filter
valid_events = []
for event in events:
    if event['status'] == 'ok':
        valid_events.append(event)

# With filter
valid_events = list(filter(lambda e: e['status'] == 'ok', events))

# Better - list comprehension
valid_events = [e for e in events if e['status'] == 'ok']
```

**Key point:** Filter also returns an iterator.

### 4. Reduce Function

**Reduce** combines all items into a single result.

```python
from functools import reduce

# Sum all latencies
events = [
    {'latency_ms': 100},
    {'latency_ms': 200},
    {'latency_ms': 150}
]

total = reduce(lambda acc, e: acc + e['latency_ms'], events, 0)
# 450

# Find maximum latency
max_latency = reduce(
    lambda acc, e: e['latency_ms'] if e['latency_ms'] > acc else acc,
    events,
    0
)
# 200
```

**Reduce syntax:**
```
reduce(function, sequence, initial_value)
```

The function receives:
- `acc` (accumulator) - the accumulated result so far
- `item` - the current item being processed

**Note:** Python's `sum()`, `max()`, `min()` are better for simple cases. Use reduce for custom aggregations.

### 5. List Comprehensions

**List comprehensions** are Python's elegant way to create lists from existing lists.

```python
# Simple transformation
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
# [1, 4, 9, 16, 25]

# With filtering
even = [x for x in numbers if x % 2 == 0]
# [2, 4]

# Nested (multiple loops)
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [item for row in matrix for item in row]
# [1, 2, 3, 4, 5, 6]

# Complex transformation
events = [
    {'id': 1, 'latency': 100},
    {'id': 2, 'latency': 300},
    {'id': 3, 'latency': 150}
]
slow_ids = [e['id'] for e in events if e['latency'] > 200]
# [2]
```

**List comprehension syntax:**
```
[expression for item in list if condition]
```

### 6. Dictionary Comprehensions

Create dictionaries from sequences.

```python
# Simple transformation
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x ** 2 for x in numbers}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# From existing dict, filtering
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
even_values = {k: v for k, v in data.items() if v % 2 == 0}
# {'b': 2, 'd': 4}

# Group events by status
events = [
    {'id': 1, 'status': 'ok'},
    {'id': 2, 'status': 'error'},
    {'id': 3, 'status': 'ok'}
]
by_status = {}
for event in events:
    status = event['status']
    if status not in by_status:
        by_status[status] = []
    by_status[status].append(event)

# Same thing with comprehension
by_status = {
    status: [e for e in events if e['status'] == status]
    for status in set(e['status'] for e in events)
}
# {'ok': [...], 'error': [...]}
```

### 7. Generator Expressions

Like list comprehensions, but return items **one at a time** instead of creating the whole list.

```python
# List comprehension - creates entire list in memory
squares = [x ** 2 for x in range(1000000)]  # Big!

# Generator expression - creates items on demand
squares = (x ** 2 for x in range(1000000))  # Lazy!

# Generators are perfect for processing large datasets
for square in squares:
    process(square)  # Process one at a time, memory efficient
```

**When to use generators:**
- ✅ Large datasets that don't fit in memory
- ✅ Processing that stops early (don't need all items)
- ✅ Chaining operations (pipeline-style)

---

## DE Context: Transforming Event Data

Let's apply functional patterns to event processing:

### Example 1: Simple Event Filtering

```python
# Imperative approach (step-by-step instructions)
def get_error_events(events):
    result = []
    for event in events:
        if event['status'] == 'error':
            result.append(event)
    return result

# Functional approach (what you want, not how)
def get_error_events(events):
    return list(filter(lambda e: e['status'] == 'error', events))

# Pythonic approach (list comprehension)
def get_error_events(events):
    return [e for e in events if e['status'] == 'error']
```

All three work. The list comprehension is most readable.

### Example 2: Multi-Step Transformation

```python
events = [
    {'id': 1, 'latency_ms': 100, 'status': 'ok'},
    {'id': 2, 'latency_ms': 500, 'status': 'ok'},
    {'id': 3, 'latency_ms': 1200, 'status': 'error'},
]

# Step 1: Filter valid events
# Step 2: Extract just id and latency
# Step 3: Mark slow events

# Imperative
valid = []
for e in events:
    if e['status'] == 'ok':
        valid.append({'id': e['id'], 'latency': e['latency_ms']})

result = []
for e in valid:
    if e['latency'] > 1000:
        e['slow'] = True
    else:
        e['slow'] = False
    result.append(e)

# Functional pipeline
def extract_fields(event):
    return {
        'id': event['id'],
        'latency': event['latency_ms'],
        'slow': event['latency_ms'] > 1000
    }

result = list(
    filter(lambda e: e['status'] == 'ok', events)
    | map(extract_fields)  # Wait, doesn't work...
)

# Need to use composition properly
result = [
    extract_fields(e)
    for e in events
    if e['status'] == 'ok'
]

# Or chain functions
valid_events = filter(lambda e: e['status'] == 'ok', events)
enhanced_events = map(extract_fields, valid_events)
result = list(enhanced_events)
```

### Example 3: Aggregation with Reduce

```python
from functools import reduce

events = [
    {'latency_ms': 100, 'error': False},
    {'latency_ms': 200, 'error': False},
    {'latency_ms': 1500, 'error': True},
]

# Calculate multiple metrics in one pass
def aggregate_metrics(acc, event):
    return {
        'total_latency': acc['total_latency'] + event['latency_ms'],
        'count': acc['count'] + 1,
        'error_count': acc['error_count'] + (1 if event['error'] else 0),
        'max_latency': max(acc['max_latency'], event['latency_ms'])
    }

initial = {'total_latency': 0, 'count': 0, 'error_count': 0, 'max_latency': 0}
result = reduce(aggregate_metrics, events, initial)

# Result:
# {
#   'total_latency': 1800,
#   'count': 3,
#   'error_count': 1,
#   'max_latency': 1500
# }
```

---

## Decorators (Functional Wrappers)

**Decorators** wrap functions to add behavior without changing the original function.

```python
import time
import logging

# Simple decorator
def log_execution(func):
    """Decorator that logs function calls."""
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Completed {func.__name__}")
        return result
    return wrapper

@log_execution
def process_events(events):
    return [e for e in events if e['status'] == 'ok']

# Equivalent to:
process_events = log_execution(process_events)

# Usage
events = [{'status': 'ok'}, {'status': 'error'}]
result = process_events(events)
# Logs: "Calling process_events"
# Logs: "Completed process_events"

# Another decorator: timing
def time_it(func):
    """Decorator that measures execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"{func.__name__} took {duration:.4f} seconds")
        return result
    return wrapper

@time_it
@log_execution
def slow_process(events):
    time.sleep(1)
    return events

# Multiple decorators stack (bottom-up execution)
slow_process(events)
# Logs: "Calling slow_process"
# Logs: "Completed slow_process"
# Prints: "slow_process took 1.0001 seconds"
```

**Key decorator patterns:**
- `@log_execution` - log function calls
- `@time_it` - measure performance
- `@retry` - retry on failure
- `@cache` - memorize results
- `@validate` - check inputs before processing

---

## Best Practices

### ✅ DO:

1. **Use list comprehensions for simple transformations**
   ```python
   # Good
   doubled = [x * 2 for x in numbers]
   ```

2. **Use filter/map when logic is complex**
   ```python
   # Good - complex lambda
   errors = list(filter(lambda e: e['status'] == 'error' and e['retry_count'] > 0, events))
   ```

3. **Chain functions logically**
   ```python
   # Good - clear pipeline
   valid = [e for e in events if e['status'] == 'ok']
   slow = [e for e in valid if e['latency'] > 1000]
   ```

4. **Use decorators for cross-cutting concerns**
   ```python
   # Good - logging happens everywhere
   @log_execution
   def process(data): pass
   ```

5. **Document complex comprehensions**
   ```python
   # Good - explains what's happening
   # Group events by status, keeping count for each
   status_counts = {
       status: len([e for e in events if e['status'] == status])
       for status in set(e['status'] for e in events)
   }
   ```

### ❌ DON'T:

1. **Use lambdas for complex logic**
   ```python
   # Bad - too complex
   bad = lambda e: e['latency'] if e['status'] == 'ok' and e['retry_count'] < 3 else None
   
   # Good - use a function
   def get_valid_latency(event):
       if event['status'] == 'ok' and event['retry_count'] < 3:
           return event['latency']
       return None
   ```

2. **Nest comprehensions too deeply**
   ```python
   # Bad - hard to read
   result = [[y * 2 for y in x] for x in [[1, 2], [3, 4]]]
   
   # Better
   result = []
   for row in [[1, 2], [3, 4]]:
       result.append([y * 2 for y in row])
   ```

3. **Chain map/filter excessively**
   ```python
   # Bad - hard to follow
   result = map(f3, filter(condition2, map(f1, filter(condition1, data))))
   
   # Better - combine into one comprehension
   result = [f3(f1(x)) for x in data if condition1(x) and condition2(f1(x))]
   ```

---

## Common Mistakes

### Mistake 1: Forgetting to Convert Iterators to Lists

```python
# Problem: map() and filter() return iterators
result = map(lambda x: x * 2, numbers)
# You can iterate once, then it's empty
for x in result:
    print(x)  # Works
for x in result:
    print(x)  # Empty - already consumed!

# Solution: Convert to list
result = list(map(lambda x: x * 2, numbers))
```

### Mistake 2: Over-Using Comprehensions

```python
# Bad - comprehension trying to do too much
[e['id'] for e in [e for e in events if e['status'] == 'ok'] if e['latency'] > 100]

# Better - clearer
valid_events = [e for e in events if e['status'] == 'ok']
slow_events = [e for e in valid_events if e['latency'] > 100]
ids = [e['id'] for e in slow_events]
```

### Mistake 3: Lambda Capturing Wrong Variables

```python
# Problem: lambda captures variable reference, not value
functions = []
for i in range(3):
    functions.append(lambda x: x + i)

# All functions add 2 (the final value of i)
print(functions[0](10))  # 12, not 10!
print(functions[1](10))  # 12, not 11!

# Solution: use default argument
functions = []
for i in range(3):
    functions.append(lambda x, i=i: x + i)

print(functions[0](10))  # 10
print(functions[1](10))  # 11
```

---

## OOP vs Functional: When to Use Each

| Scenario | Use | Example |
|----------|-----|---------|
| **Stateful operation** | OOP | EventProcessor class that maintains processed_count |
| **Simple transformation** | Functional | `[e * 2 for e in events]` |
| **Multiple related methods** | OOP | Pipeline class with run(), validate(), aggregate() |
| **Transform sequences** | Functional | `filter()`, `map()`, comprehensions |
| **Complex logic flow** | OOP | Inheritance hierarchies for different processor types |
| **Reusable utility** | Functional | Decorators for timing, logging, retry logic |

**Best practice:** Use **both together**. OOP for architecture, functional for data transformation.

```python
class EventPipeline:  # OOP architecture
    def __init__(self, source, sink):
        self.source = source
        self.sink = sink
    
    def run(self, events):  # Functional inside
        valid = [e for e in events if self._validate(e)]
        transformed = [self._transform(e) for e in valid]
        return transformed
    
    @staticmethod
    def _validate(event):
        return event['id'] > 0
    
    @staticmethod
    def _transform(event):
        return {**event, 'processed': True}
```

---

## Quick Reference

| Tool | Use Case | Example |
|------|----------|---------|
| **lambda** | Simple anonymous function | `lambda x: x * 2` |
| **map()** | Apply function to each item | `map(double, numbers)` |
| **filter()** | Keep matching items | `filter(lambda x: x > 0, numbers)` |
| **reduce()** | Combine to single result | `reduce(add, numbers)` |
| **List comprehension** | Transform list | `[x * 2 for x in numbers]` |
| **Dict comprehension** | Transform dict | `{k: v*2 for k, v in d.items()}` |
| **Generator expression** | Lazy list | `(x * 2 for x in huge_list)` |
| **@decorator** | Wrap function | `@log_execution` |

---

Functional programming makes data transformation **clear, concise, and testable**. Master these patterns and your pipelines will be a joy to maintain. 🚀

