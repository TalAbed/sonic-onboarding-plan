# Section 4: Advanced Python

Welcome to Section 4! In this section you'll level up from "comfortable Python user" to someone who can design **robust, extensible, production-grade** Python systems. The focus is on concepts that matter for real data engineering work: OOP design, functional patterns, concurrency, error handling, logging, design patterns, and decorators.

---

## Learning Goals

By the end of this section, you should be able to:

✅ **Design and implement** object-oriented components that model real data workflows  
✅ **Use functional programming** tools (lambda, map, filter, reduce, comprehensions) to write concise, expressive transformations  
✅ **Decide when to use** threading, multiprocessing, or async for concurrency and implement basic patterns  
✅ **Implement reliable error handling** with custom exceptions that clarify failures  
✅ **Apply logging best practices** that are actually useful in production debugging  
✅ **Recognize and apply** basic design patterns (especially factory-style patterns) in data pipelines  
✅ **Use decorators** to add reusable behavior (logging, timing, validation) without cluttering business logic  

You'll combine all of this later in Advanced Python exercises (pipeline classes, functional refactors, concurrent processing).

---

## Why This Matters

You have just built strong **NumPy/Pandas data manipulation skills**. Now it's time to learn how to structure, organize, and scale Python code for **production systems**.

Real data engineering challenges:
- ❌ Spaghetti code that's hard to extend
- ❌ Silent failures with no visibility
- ❌ Bottlenecks from sequential processing
- ❌ Duplicated pipeline logic across projects

This section teaches patterns that solve these problems:
- ✅ Clean, testable OOP architecture
- ✅ Functional transforms for clarity
- ✅ Concurrent processing when needed
- ✅ Proper error handling and logging
- ✅ Reusable design patterns

---

## Recommended Learning Path

### 1. Object-Oriented Programming (OOP)

**Start here.** Everything else builds on a solid understanding of classes, objects, and how to structure logic.

**Watch (video):**

**Object Oriented Programming (OOP) In Python - Beginner Crash Course**
- Channel: Python Engineer
- Duration: 1 hour 19 minutes
- URL: https://www.youtube.com/watch?v=-pEs-Bss8Wc
- Topics: Classes, instances, methods, inheritance, encapsulation, properties
- Perfect for: Getting OOP fundamentals before advanced topics

**How to use it:**
- Watch end-to-end once at normal speed
- Re-watch the sections on inheritance and properties while thinking how to represent:
  - Pipelines as classes
  - Stages / operators as base classes
  - Data sources / sinks as subclasses

**Time:** 1.5 hours

---

### 2. Functional Programming Basics

Once you're comfortable with OOP, learn how to use functional tools to make transformations more **concise and composable**.

Read the following article:

**Python Lambda Functions, Map, Filter, Reduce & Comprehensions**
- Author: Owais
- URL: https://www.owais.io/blog/2025-09-21_python-lambda-functions-map-filter-reduce-comprehensions
- Topics: Anonymous functions (lambda), map(), filter(), reduce(), list/dict comprehensions, when to prefer functional over loops
- Perfect for: Understanding functional patterns in Python

Go over the following interactive practice:

**"Map, Filter, Reduce"**
- Site: learnpython.org
- URL: https://www.learnpython.org/en/Map,_Filter,_Reduce
- Type: Interactive exercises with immediate browser feedback
- Perfect for: Solidifying map/filter/reduce patterns

**How to use it:**
- Read the Owais article and run examples locally
- Then do the learnpython.org exercises to practice
- Think about transforming event lists, filtering bad records, aggregating metrics
- Keep these patterns in mind for later exercises

**Time:** 1.5-2 hours (45 min reading + 45 min practice)

---

### 3. Async & Concurrency (Threads, Processes, AsyncIO)

Now that you can structure code, learn how to make it **run concurrently** when needed.

Watch the following videos:

**Threading vs. multiprocessing in Python**
- Channel: Carberra
- Duration: ~20 minutes
- URL: https://www.youtube.com/watch?v=m70_u0DPK5k
- Topics: GIL explanation, when to use threads vs processes, performance trade-offs
- Perfect for: High-level understanding of concurrency options

**AsyncIO, await, and async – Concurrency in Python**
- Channel: Socratica
- Duration: ~30 minutes
- URL: https://www.youtube.com/watch?v=K56nNuBEd0c
- Topics: Coroutines, event loop, async/await syntax, concurrent task execution
- Perfect for: Understanding async programming fundamentals

**How to use it:**
- After Carberra: be able to answer "threading or multiprocessing?" for a given task
- After Socratica: understand when async is a better fit (I/O-bound workloads, many concurrent external calls)
- Think about which approach suits your event processing pipeline

**Time:** 1 hour

---

### 4. Error Handling & Custom Exceptions

Concurrency and complex pipelines fail in many ways. This section ensures failures are **visible, explicit, and meaningful**.

Watch the following video:

**Python Exception Handling Tutorial for Beginners**
- Channel: Dave Gray
- Duration: ~10-15 minutes
- URL: https://www.youtube.com/watch?v=PHzm_Iox1mE
- Topics: try/except/else/finally, common built-in exceptions, basic custom exceptions
- Perfect for: Getting foundations before diving deeper

Read the following article:

**Python Exceptions: An Introduction**
- Site: Real Python
- URL: https://realpython.com/python-exceptions/
- Topics: Exception semantics and hierarchy, best practices for catching/handling/re-raising, how error handling shapes API design
- Perfect for: Professional exception handling practices

**How to use it:**
- Think about where in a data pipeline you want to catch vs propagate exceptions
- Sketch a small custom exception hierarchy for:
  - Data validation failures
  - Upstream dependency failures
  - Unexpected internal bugs
- Remember: exceptions are part of your API design

**Time:** 1.5 hours

---

### 5. Logging Best Practices

Exceptions are only useful if they're **logged well**. This section focuses on high-signal logging.

Read the following articles:

**10 Best Practices for Logging in Python**
- Site: Better Stack Community
- URL: https://betterstack.com/community/guides/logging/python/python-logging-best-practices/
- Topics: Logger hierarchy, handler and formatter configuration, avoiding noisy/sensitive logs
- Perfect for: Structured logging foundations

**12 Python Logging Best Practices To Debug Apps Faster**
- Site: Middleware.io
- URL: https://middleware.io/blog/python-logging-best-practices/
- Topics: Choosing log levels, structuring log messages, integrating with log analysis tools
- Perfect for: Production-ready logging patterns

**How to use it:**
- Decide a **standard logging pattern** for your exercises:
  - Logger naming conventions
  - Which log levels for which situations
  - What structure to use for messages
- Apply the same pattern in all future exercises:
  - Each module gets its own logger
  - Structured key/value messages where possible
  - Consistent formatting across the codebase

**Time:** 1.5-2 hours

---

### 6. Design Patterns (Factory & Pipeline Patterns)

Next, use **lightweight design patterns** to keep pipeline code maintainable and extendable.

Read the following articles:

**Factory Design Patterns in Python**
- Site: Dagster
- URL: https://dagster.io/blog/python-factory-patterns
- Topics: Factory pattern for assets and components, separating object creation from business logic, data engineering-specific patterns
- Perfect for: Understanding factory patterns in data context

**Python Helpers – Code Patterns for Data Pipelines**
- Site: Start Data Engineering
- URL: https://www.startdataengineering.com/post/code-patterns/
- Topics: Practical patterns for data pipelines, when to use classes vs functions, how to templatize pipeline flows
- Perfect for: Data engineering-specific design patterns

**How to use it:**
- Identify places in your lab exercises where a factory or template class would:
  - Remove copy-paste code
  - Standardize configuration and behavior
  - Make pipelines easier to extend
- Think about how to apply these patterns in the lab

**Time:** 1.5-2 hours

---

### 7. Decorators

Finally, learn decorators as a **clean way to add cross-cutting behavior** (logging, timing, retries) without polluting core logic.

Read the following articles:

**Primer on Python Decorators**
- Site: Real Python
- URL: https://realpython.com/primer-on-python-decorators/
- Topics: How decorators work under the hood, function/method decorators, practical use cases (logging, timing, caching, access control)
- Perfect for: Comprehensive understanding

**Python Decorators (With Examples)**
- Site: Programiz
- URL: https://www.programiz.com/python-programming/decorator
- Topics: Simple visual explanation, step-by-step custom decorator examples
- Perfect for: Visual learners

**How to use it:**
- Implement at least 1-2 decorators you'll reuse later:
  - `@log_execution` - log function calls and results
  - `@time_it` - measure function execution time
  - Maybe `@retry_on_exception` - for external API calls
- Use these decorators in the lab

**Time:** 1 hour

---

## How This Connects to Section 4 Exercises

After completing these resources, you'll be ready for:

### **3 Hands-On Exercises**
1. **Exercise 1: Building Data Pipeline Classes**
   - Create reusable pipeline components using OOP
   - Practice inheritance and polymorphism
   - Apply factory patterns
   - Add proper logging and error handling

2. **Exercise 2: Functional Optimization**
   - Refactor Exercise 1 using functional patterns
   - Implement custom decorators for logging and timing
   - Compare performance of different approaches
   - Understand when to use each pattern

3. **Exercise 3: Concurrent Processing Capstone**
   - Process multiple event streams in parallel
   - Choose between threading, multiprocessing, and async
   - Handle errors and logging gracefully
   - Build production-ready error recovery

---

## Prerequisites

Before starting Section 4, make sure you've completed:
- ✅ Basic Python understanding (variables, functions, loops, if/else)
- ✅ NumPy & Pandas Fundamentals

---

## Tips for Success

✅ **Follow the order** - OOP first, then functional, then concurrency. Each builds on previous concepts

✅ **Write code as you learn** - Don't just watch videos or read articles. Code along with examples

✅ **Apply to Sonic context** - As you learn each concept, think about:
   - How would this apply to our event processing pipeline?
   - How would this improve our current code?
   - Where are we using this pattern already?

✅ **Experiment** - Try decorators on your own functions. Write a simple factory. Build a small async program

✅ **Reference the guides** - use them alongside these resources

✅ **Ask questions** - If something doesn't click, review the video/article again, try a different example or ask your team members :)

---


## Ready to dive in?
Start with the OOP video and let's level up your Python! 🚀

---

## Quick Resource Links

| Concept | Type | Link | Time |
|---------|------|------|------|
| OOP | Video | https://www.youtube.com/watch?v=-pEs-Bss8Wc | 1.5 hrs |
| Functional | Article | https://www.owais.io/blog/2025-09-21_python-lambda-functions-map-filter-reduce-comprehensions | 45 min |
| Functional | Practice | https://www.learnpython.org/en/Map,_Filter,_Reduce | 45 min |
| Concurrency | Video | https://www.youtube.com/watch?v=m70_u0DPK5k | 20 min |
| Async | Video | https://www.youtube.com/watch?v=K56nNuBEd0c | 30 min |
| Exceptions | Video | https://www.youtube.com/watch?v=PHzm_Iox1mE | 15 min |
| Exceptions | Article | https://realpython.com/python-exceptions/ | 1 hr |
| Logging | Article | https://betterstack.com/community/guides/logging/python/python-logging-best-practices/ | 1 hr |
| Logging | Article | https://middleware.io/blog/python-logging-best-practices/ | 1 hr |
| Patterns | Article | https://dagster.io/blog/python-factory-patterns | 1 hr |
| Patterns | Article | https://www.startdataengineering.com/post/code-patterns/ | 1 hr |
| Decorators | Article | https://realpython.com/primer-on-python-decorators/ | 1 hr |
| Decorators | Article | https://www.programiz.com/python-programming/decorator | 30 min |


