# Advanced Python Lab

Welcome to Section 4's hands-on lab! After learning OOP, functional programming, concurrency, and error handling through the reference guides, you'll now **apply these concepts** to build a production-grade data pipeline.

---

## Lab Overview

This lab consists of **3 progressive exercises** that build on each other:

### **Exercise 1: Building Data Pipeline Classes (OOP)**
Learn to design **reusable, composable data pipeline components** using Object-Oriented Programming.

- **Concepts:** Classes, inheritance, polymorphism, factory pattern, custom exceptions
- **Outcome:** A working pipeline with reusable OOP components

### **Exercise 2: Functional Optimization & Decorators**
Refactor Exercise 1 using **functional patterns and custom decorators** while keeping clean architecture.

- **Concepts:** Custom decorators, comprehensions, map/filter, functional refactoring
- **Outcome:** Cleaner, more functional code with decorator patterns

### **Exercise 3: Concurrent Processing Capstone**
Scale your pipeline with **threading or async**, add error handling, and comprehensive logging.

- **Concepts:** Threading/async, error recovery, structured logging, performance monitoring
- **Outcome:** Production-grade concurrent pipeline with error handling

---

## Context: DE Processing Pipeline

Throughout this lab, you'll build a **real (simple) data engineering system** for processing events:

```
Raw Events (CSV)
      ↓
  [SOURCES]  (CSVSource, APISource, DatabaseSource)
      ↓
  [PROCESSORS]  (Validator, Enricher, Aggregator)
      ↓
  [SINKS]  (JSONSink, DatabaseSink, WebhookSink)
      ↓
Processed Events (JSON)
```

Each exercise adds more sophistication:
- **Exercise 1:** Build the architecture (OOP components)
- **Exercise 2:** Refactor internals (functional patterns, decorators)
- **Exercise 3:** Scale it (concurrent processing, error handling, logging)

---

## Lab Structure

```
section4-lab/
├── README.md (this file)
├── SETUP.md (setup instructions)
│
├── exercises/
│   ├── exercise-1-oop/
│   │   ├── exercise-1-instructions.md
│   │   ├── exercise-1-solution.md
│   │   └── sample-data.py
│   │
│   ├── exercise-2-functional/
│   │   ├── exercise-2-instructions.md
│   │   ├── exercise-2-solution.md
│   │   └── (uses Exercise 1 solution)
│   │
│   └── exercise-3-concurrency/
│       ├── exercise-3-instructions.md
│       ├── exercise-3-solution.md
│       └── sample-data-large.py
│
└── reference-guides/
    ├── python-oop.md
    ├── functional-python.md
    ├── async-and-concurrency.md
    └── error-handling-and-logging.md
```

---

## Learning Path

### **Before Starting the Lab**

Make sure you've completed:
- ✅ Went over 4 reference guides (OOP, Functional, Async, Error/Logging)
- ✅ Watched/read the recommended online resources
- ✅ Understand Python classes, functions, and basic I/O

### **During the Lab**

**Suggested approach:**
1. **Read the instructions carefully** - They guide you step-by-step
2. **Code along** - Write the code yourself, don't just read solutions
3. **Reference the guides** - When stuck, check the relevant reference guide
4. **Compare with solutions** - After completing, review the solution
5. **Experiment** - Try variations, break things, learn from failures

---

## Exercise Details

### Exercise 1: Building Data Pipeline Classes (OOP)

**What you'll build:**
A modular event processing pipeline using classes and inheritance.

**Key patterns:**
- Abstract base classes (interfaces)
- Inheritance hierarchies
- Polymorphism (different implementations, same interface)
- Factory pattern (flexible object creation)
- Custom exceptions for error handling

**Sample data:**
- Input: `events_raw.csv` (100 sample events)
- Output: `events_processed.json` (processed and enriched)

**You'll implement:**
- `EventSource` (base) → `CSVEventSource`, `DatabaseEventSource`, `APIEventSource`
- `EventProcessor` (base) → `EventValidator`, `EventEnricher`, `EventAggregator`
- `EventSink` (base) → `JSONSink`, `DatabaseSink`
- `EventPipeline` (orchestrator)
- Custom exceptions: `ValidationError`, `EnrichmentError`, `StorageError`

**Expected time:** 60-75 minutes

---

### Exercise 2: Functional Optimization & Decorators

**What you'll do:**
Refactor Exercise 1 using functional patterns and custom decorators.

**Key patterns:**
- Custom decorators: `@log_execution`, `@time_it`, `@validate_input`, `@handle_errors`, `@retry_on_failure`
- List comprehensions instead of loops
- map/filter for transformations
- reduce for aggregations
- Combining OOP + functional

**Changes from Exercise 1:**
- Keep the class architecture
- Make internals more functional
- Add decorators for logging, timing, error handling
- Reduce code verbosity
- Better separation of concerns

**You'll create:**
- `@log_execution` - Log function calls with context
- `@time_it` - Measure execution time
- `@validate_input` - Validate inputs before processing
- `@handle_errors` - Catch and log exceptions
- `@retry_on_failure` - Retry with exponential backoff

Then refactor:
- Loops → list comprehensions
- Conditionals → filter
- Aggregations → reduce
- Processing chains → composed functions

**Expected time:** 75-90 minutes

---

### Exercise 3: Concurrent Processing Capstone

**What you'll do:**
Add concurrent processing, error handling, and production logging to your pipeline.

**Key patterns:**
- ThreadPoolExecutor for parallel processing
- asyncio for high-concurrency I/O
- Error classification (transient vs permanent)
- Retry logic with exponential backoff
- Structured JSON logging
- Performance metrics and reporting

**Steps:**
1. Profile the sequential pipeline (find bottlenecks)
2. Implement threading version (10-20 workers)
3. Implement async version (if desired)
4. Add retry logic and error handling
5. Add comprehensive structured logging
6. Generate performance metrics and error reports

**You'll generate:**
- `errors_report.json` - Error analysis
- `performance_metrics.json` - Timing and speedup
- `events_processed.json` - Final output

**Expected time:** 90-120 minutes

---

## Important Notes

### ✅ DO:
- **Read instructions carefully** - Each step builds on previous ones
- **Code yourself** - Don't copy-paste from solutions
- **Reference the guides** - They explain concepts in depth
- **Experiment** - Try variations and improvements
- **Handle errors** - Make your code robust

### ❌ DON'T:
- **Skip steps** - They're ordered for a reason
- **Jump to solutions** - Try to solve it first
- **Copy without understanding** - Understand what you're doing
- **Ignore errors** - Debug and fix issues
- **Skip the lab** - Practice is essential

---

## Expected Learning Outcomes

After completing this lab, you should be able to:

✅ **Design OOP architectures** for data systems  
✅ **Implement class hierarchies** with inheritance and polymorphism  
✅ **Use design patterns** (factory, strategy, observer)  
✅ **Write custom decorators** for functions and methods  
✅ **Refactor code** using functional patterns  
✅ **Implement concurrent processing** (threading or async)  
✅ **Handle errors gracefully** with retries and recovery  
✅ **Add production logging** for debugging and monitoring  
✅ **Measure performance** and optimize bottlenecks  
✅ **Build maintainable, scalable systems**  

---

## Quick Start

1. **Follow SETUP.md** to prepare your environment
2. **Read the instructions** in `exercise-X-instructions.md`
3. **Write the code** yourself
4. **Reference the guides** when needed
5. **Compare with solutions** when done
6. **Move to next exercise**

---

## Getting Help

**If you get stuck:**

1. **Re-read the instructions** - Details matter
2. **Check the reference guide** - Concepts are explained there
3. **Look at hints** in the instructions (if provided)
4. **Review the solution** - See how it's done
5. **Experiment** - Try different approaches
6. **Ask questions** - Seek clarification

---

## Common Issues & Solutions

### "I don't understand what to build"
→ Read the instructions more carefully, look at the expected output

### "My code doesn't work"
→ Check error messages, use print/logging to debug, review the reference guide

### "This is too hard"
→ Break it into smaller steps, review the solution, then try again

### "I finished but don't understand the solution"
→ Rewrite the solution from scratch, line by line, understanding each part

### "How do I test my code?"
→ Instructions include test cases and sample data files

---

## Next Steps After Lab

After completing all 3 exercises:
- ✅ You'll have built a production-grade data pipeline
- ✅ You'll understand OOP, functional, and concurrent Python
- ✅ You'll know how to structure maintainable systems
- ✅ You're ready for real-world data engineering projects

Consider:
- Building your own mini-project
- Exploring advanced topics (async frameworks, distributed systems)
- Reading about software design patterns in depth

---

## Lab Philosophy

This lab teaches through **doing, not just reading:**
- Each exercise starts simple and gets progressively harder
- You write real, working code
- You learn patterns by applying them
- You solve real problems (event processing, error handling, scaling)
- You build something you're proud of

**The goal isn't to finish quickly. The goal is to understand deeply.**

Take your time. Experiment. Break things. Learn. 🚀

---

## You've Got This! 💪

These exercises are challenging but rewarding. You'll learn more by doing than by reading. Stick with it, debug patiently, and celebrate your progress.

**Ready? Go to [SETUP.md](SETUP.md) to get started!** 🚀

