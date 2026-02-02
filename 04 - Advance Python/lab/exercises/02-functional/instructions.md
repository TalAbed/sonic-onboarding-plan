# Exercise 2: Functional Optimization & Decorators

## Overview

In this exercise, you'll **refactor Exercise 1** using **functional programming patterns** and **custom decorators**. You'll learn when OOP is overkill and when functional approaches are cleaner.

### What You'll Learn

- Functional programming patterns (map, filter, reduce, comprehensions)
- Custom decorators for cross-cutting concerns (logging, timing, error handling)
- Performance optimization techniques
- Comparing OOP vs Functional approaches
- Data pipelines using composition of pure functions

### Key Concepts

- First-class functions
- Higher-order functions
- Decorators (function and class decorators)
- Pure functions and side effects
- Functional composition
- List comprehensions and generator expressions
- Timing and performance measurement

### Learning Outcomes

By the end of this exercise, you will:
- ✅ Understand when to use functional vs OOP patterns
- ✅ Write custom decorators for reusable logic
- ✅ Optimize data processing with functional patterns
- ✅ Measure and compare performance
- ✅ Use composition to build flexible pipelines
- ✅ Refactor existing OOP code to functional style

---

## Part 1: Understanding the Refactoring Strategy (Steps 1-3)

### Step 1: Load Exercise 1 Solution

Copy your Exercise 1 solution to use as a starting point.

**Key decision:** Where in the code is the most "boilerplate" that decorators could simplify?

### Step 2: Identify Decorator Opportunities

Look at your Exercise 1 code and find repeated patterns:
- Every processor class has: logging at start, logging at end
- Every sink has: try/except with logging
- Every source has: try/except with logging

**Hints:**
- Think about what decorators could abstract these patterns
- Decorators can wrap functions to add behavior
- A decorator wraps the original function and returns a wrapper

**Key decision:** Should decorators handle logging, error handling, or both?

### Step 3: Plan Functional Refactoring

Some processors could be simplified to functions instead of classes.

**Hints:**
- EventValidator is really just filtering - could be a function
- EventEnricher is really just transforming - could be a function
- EventAggregator is really just grouping - could be a function
- Complex orchestration (EventPipeline) still benefits from OOP

**Key decision:** What makes sense as a class vs a function?

---

## Part 2: Create Decorator Utilities (Steps 4-8)

### Step 4: Create `@log_execution` Decorator

This decorator logs before and after function execution.

**Hints:**
- Use `@wraps` from `functools` to preserve function metadata
- Log function name and input size
- Log result size and execution status
- Handle exceptions—should it catch or let them bubble?

**Key decision:** Should decorator re-raise exceptions or catch them?

### Step 5: Create `@measure_time` Decorator

This decorator tracks execution time.

**Hints:**
- Use `time.time()` or `time.perf_counter()`
- Return timing info along with result
- Format as milliseconds for readability
- Could store metrics for later analysis

**Key decision:** Should timing data be returned with result or logged separately?

### Step 6: Create `@handle_errors` Decorator

This decorator wraps error handling logic.

**Hints:**
- Convert specific exceptions to pipeline-specific ones
- Log error details
- Could retry on certain exceptions
- Could have custom error messages

**Key decision:** Should decorator retry automatically or just log?

### Step 7: Create `@validate_input` Decorator

This decorator validates inputs before processing.

**Hints:**
- Check that events list isn't empty
- Check that events have required structure
- Could enforce type checking
- Should fail fast with clear message

**Key decision:** What's the minimal validation needed?

### Step 8: Understand Decorator Stacking

Decorators can be stacked in order:

```python
@log_execution
@measure_time
@handle_errors
def process_events(events):
    return events
```

**Key decision:** Does the order of decorators matter? Why?

---

## Part 3: Refactor Processors as Functions (Steps 9-13)

### Step 9: Implement `validate_events()` Function

Convert EventValidator to a pure function.

**Hints:**
- Input: list of events
- Output: list of valid events
- Use filter() or list comprehension
- Create helper `is_valid_event(event)` function
- Decorate with `@log_execution` and `@handle_errors`

**Key decision:** List comprehension or filter()? Which is more readable?

### Step 10: Implement `enrich_events()` Function

Convert EventEnricher to a pure function.

**Hints:**
- Input: list of events
- Output: enriched events
- Use map() or list comprehension
- Create helper `enrich_single_event(event)` function
- Decorate appropriately

**Key decision:** How to handle user data lookup? Global dict or parameter?

### Step 11: Implement `aggregate_events()` Function

Convert EventAggregator to a pure function.

**Hints:**
- Input: list of events
- Output: events with aggregation stats
- Use groupby from itertools (or manual grouping)
- Calculate stats for each group
- Attach stats to each event

**Key decision:** How to handle missing groups gracefully?

### Step 12: Create Processor Chain Function

Compose processors together.

**Hints:**
- Function `process_pipeline(events, processors)` that chains them
- Apply each processor to output of previous
- Could use `reduce()` from functools
- Could use a simple for loop

**Key decision:** reduce() vs for loop? What's more readable?

### Step 13: Test Processor Refactoring

Verify functional processors work same as Exercise 1.

**Hints:**
- Run same test data through both versions
- Compare output (should be identical)
- Compare execution time (should be similar)
- What if functional version is faster? Why?

**Key decision:** Should you keep both OOP and functional versions or just one?

---

## Part 4: Refactor Sources and Sinks (Steps 14-17)

### Step 14: Create Source Functions

Convert source classes to functions.

**Hints:**
- `fetch_from_csv(filepath)` function
- `fetch_from_database(connection_string)` function
- `fetch_from_api(api_url, api_key)` function
- Each returns list of events
- Decorate with error handling and logging

**Key decision:** Keep factory pattern or just call functions directly?

### Step 15: Create Sink Functions

Convert sink classes to functions.

**Hints:**
- `save_to_json(events, filepath)` function
- `save_to_database(events, connection_string)` function
- `send_to_webhook(events, webhook_url)` function
- Each takes events and destination, returns None or status

**Key decision:** How to return success/failure from side-effect functions?

### Step 16: Create Source/Sink Selection Functions

Simple functions to select implementations.

**Hints:**
- `get_source(source_type, **kwargs)` returns appropriate fetch function
- `get_sink(sink_type, **kwargs)` returns appropriate save function
- Dictionary mapping types to functions (instead of factory classes)
- Could use lambdas for simple cases

**Key decision:** Dict mapping vs if/elif? Pros/cons?

### Step 17: Simplify Pipeline Orchestration

Refactor EventPipeline or replace with simpler function.

**Hints:**
- Could keep EventPipeline class for complex orchestration
- Or create `run_pipeline(source_fn, processors, sink_fn)` function
- Handles fetching, processing, saving
- Tracks metrics
- Logs progress

**Key decision:** Does orchestration still need to be a class?

---

## Common Challenges & Hints

**Challenge:** "I don't understand decorators"
- **Hint:** Decorator is just a function that takes a function and returns a wrapper
- Think: "I want to add behavior to functions without changing them"
- Example: Add logging to any function automatically

**Challenge:** "When should I use @functools.wraps?"
- **Hint:** Always! It preserves function metadata (name, docstring)
- Without it, decorated function loses its identity
- Makes debugging easier

**Challenge:** "Functional vs OOP—which is better?"
- **Hint:** Neither! Use what fits the problem
- OOP: Good for complex state and behavior
- Functional: Good for data transformations
- Many real systems mix both

**Challenge:** "My decorated function breaks type hints"
- **Hint:** Use typing module: `Callable[[int], str]` for function types
- Decorators can specify what types they accept/return
- IDE might not understand wrapped function—that's okay

**Challenge:** "Performance comparison shows no difference"
- **Hint:** Normal! Python abstracts away many differences
- Both styles compile to similar bytecode
- Readability/maintainability matters more than micro-optimizations

**Challenge:** "reduce() confuses me"
- **Hint:** It's accumulator pattern: combine list into single value
- `reduce(lambda x, y: x + y, [1, 2, 3])` = 6
- Useful for combining results, but often a loop is clearer

---

## Implementation Tips

**Tip 1:** Start by refactoring one processor at a time
- Don't try to do everything at once
- Test each functional version matches OOP version
- Build confidence step by step

**Tip 2:** Use type hints throughout
- Even though Python doesn't enforce them
- They document what functions expect
- IDE autocomplete works better

**Tip 3:** Mix styles boldly
- Some things are better as functions (pure transformations)
- Some things are better as classes (stateful operations)
- Some things are better as decorators (cross-cutting concerns)

**Tip 4:** Profile real data
- Performance tests with tiny data sets are misleading
- Use Exercise 1's sample data or create realistic dataset
- Timing needs to be significant to be meaningful

**Tip 5:** Document your hybrid approach
- Show why you chose function vs class for each component
- It helps future maintainers understand design
- Helps you remember your reasoning

---

## File Structure

```
exercises/exercise-2-functional/
├── exercise-2-solution.md      # This solution (code + explanations)
├── exercise-2-instructions.md  # Hints-based instructions
├── exercise-2-refactored.py    # Refactored code (functional version)
├── compare_performance.py       # Benchmark script
├── results/
│   ├── performance_comparison.json
│   ├── memory_analysis.json
│   └── timing_breakdown.json
└── data/
    └── events_raw.csv          # Use same data as Exercise 1
```

---

## Testing Your Code

```bash
# Generate data (if not already done)
python generate-data.py

# Run refactored functional version
python exercise-2-refactored.py

# Run performance comparison
python compare_performance.py

# Should see:
# Functional approach completed successfully
# Performance comparison results
# Detailed timing and memory analysis
```

---

## Next Steps

✅ **You've completed Exercise 2!**

Your code now demonstrates:
- Functional programming patterns
- Custom decorators for reusable logic
- Performance awareness and measurement
- Hybrid OOP/functional design
- Improved readability through composition

**Ready for Exercise 3?**
You'll add **concurrent processing** to handle large datasets efficiently using threading and async!

