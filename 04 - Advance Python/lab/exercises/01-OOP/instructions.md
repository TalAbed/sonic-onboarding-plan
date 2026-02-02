# Exercise 1: Building Data Pipeline Classes (OOP)

## Overview

In this exercise, you'll build a **modular event processing pipeline** using Object-Oriented Programming. You'll design classes that are **reusable, composable, and extensible** without copy-pasting code.

### What You'll Build

A complete event processing system with:
- **Sources** - Multiple ways to read events (CSV, database, API)
- **Processors** - Multiple ways to transform events (validate, enrich, aggregate)
- **Sinks** - Multiple ways to output events (JSON, database, webhooks)
- **Pipeline** - Orchestrator that ties everything together

### Key Concepts

- Abstract base classes (interfaces)
- Inheritance hierarchies
- Polymorphism
- Factory pattern
- Custom exceptions
- Composition

### Time Estimate

**60-75 minutes** for thorough completion

### Learning Outcomes

By the end of this exercise, you will:
- ✅ Understand abstract base classes and interfaces
- ✅ Use inheritance to eliminate code duplication
- ✅ Apply polymorphism for flexible implementations
- ✅ Create extensible systems using composition
- ✅ Handle errors with custom exceptions
- ✅ Use factory pattern for object creation

---

## Part 1: Design Base Classes (Steps 1-6)

Your task: Create abstract base classes that define interfaces for sources, processors, and sinks.

### Step 1: Create Project File and Imports

Create `exercise-1-solution.py` with the necessary imports and logging configuration.

**Hints:**
- Import `ABC` and `abstractmethod` from the `abc` module
- Import `csv`, `json`, `logging`, and `datetime`
- Set up basic logging with `basicConfig()`
- Use type hints (`List`, `Dict`, `Any`)

**Key decision:** Where should you place logging configuration? Should it be at module level?

### Step 2: Define Custom Exceptions

You need exceptions for different error scenarios (validation, enrichment, storage).

**Hints:**
- Create a base `PipelineError` exception class
- Create specific exception classes that inherit from it
- Think: When would you raise each exception?

**Key decision:** Why is a base exception class better than just one generic exception?

### Step 3: Define EventSource Base Class

Create an abstract base class for event sources.

**Hints:**
- the event sorces are: EventSource, EventProcessor and EventSink
- Use `ABC` and `@abstractmethod` decorator
- Include `name` attribute and logger for each instance
- Define abstract method `fetch()` that returns `List[Dict[str, Any]]`
- Add `__repr__()` method for debugging

**Key decision:** Why should `name` and `logger` be instance attributes?

### Step 4: Define EventProcessor Base Class

Create an abstract base class for processors.

**Hints:**
- Follow the same pattern as EventSource
- Define abstract method `process()` that takes and returns `List[Dict[str, Any]]`
- Think: Why does processor need both input and output?

### Step 5: Define EventSink Base Class

Create an abstract base class for sinks.

**Hints:**
- Follow the same pattern
- Define abstract method `save()` that takes events but returns `None`
- Difference from others: sinks don't transform, they store/send

### Step 6: Understand the Pattern

Before moving on, think about these questions:
- What do all three base classes have in common?
- Why can't you instantiate `EventSource` directly?
- What happens if a subclass doesn't implement the abstract method?

---

## Part 2: Implement Concrete Sources (Steps 7-12)

Your task: Create specific implementations of `EventSource`.

### Step 7: Implement CSVEventSource

Read events from a CSV file.

**Hints:**
- Use `csv.DictReader` to read the file
- Convert string fields to appropriate types (event_id, latency_ms → int)
- Handle `FileNotFoundError` and convert to `PipelineError`
- Log progress at each stage

**Key decision:** Should numeric conversion happen during reading or processing?

### Step 8: Implement DatabaseEventSource

Read events from a database (stub for now).

**Hints:**
- Create the class with a `connection_string` parameter
- For now, just log and return empty list
- This demonstrates the pattern—you can implement it fully later

**Key decision:** How should connection string be handled?

### Step 9: Implement APIEventSource

Read events from an API endpoint (stub for now).

**Hints:**
- Parameters: `api_url` and optional `api_key`
- For now, just log and return empty list
- Demonstrates pattern

### Step 10: Understand Polymorphism

All three sources have different implementations but the **same interface**:

```python
# They all work the same way:
events = source.fetch()
```

This is polymorphism—different implementations, same interface. Your pipeline code can work with any source without knowing which one it is.

---

## Part 3: Implement Concrete Processors (Steps 11-14)

Your task: Create three useful processors.

### Step 11: Implement EventValidator

Validate events meet required standards.

**Hints:**
- Check for required fields: event_id, timestamp, event_type, user_id, status, latency_ms
- Check valid event types: {purchase, login, checkout, view}
- Check valid statuses: {ok, error, timeout}
- Check latency_ms >= 0
- Filter out invalid events (don't raise exception, just exclude)

**Implementation approach:**
- Create helper method `_is_valid(event)` that returns boolean
- Log warnings for invalid events
- Return list of valid events only

**Key decision:** Should invalid events cause pipeline to fail or just be filtered?

### Step 12: Implement EventEnricher

Add additional data to events.

**Hints:**
- Create mock user data lookup: `{'user_1': {'country': 'US', 'premium': True}, ...}`
- For each event, look up user info and add to event
- If user not found, set defaults: `country: 'UNKNOWN'`, `premium: False`
- Add `enriched_at` timestamp

**Implementation approach:**
- Create helper method `_enrich(event)` for single event
- Use `.copy()` to avoid modifying originals
- Raise `EnrichmentError` if enrichment fails

**Key decision:** When should enrichment fail vs just use defaults?

### Step 13: Implement EventAggregator

Aggregate events by type and add statistics.

**Hints:**
- Group events by `event_type`
- Calculate for each type:
  - `count`: number of events
  - `avg_latency`: average latency
  - `error_count`: how many had status='error'
- Add these stats to each event under `type_stats` field

**Implementation approach:**
- Create helper method `_calculate_aggregates(events)` that returns dict
- Add stats to every event (so all events have context)
- Don't fail if aggregation can't complete, just log

**Key decision:** Should every event get all aggregate stats or just for its type?

### Step 14: Understand Processor Chaining

Processors can be chained:
```python
events = validator.process(events)
events = enricher.process(events)
events = aggregator.process(events)
```

Each processor transforms the output to feed to the next.

---

## Part 4: Implement Concrete Sinks (Steps 15-19)

Your task: Create outlets for processed events.

### Step 15: Implement JSONSink

Write events to a JSON file.

**Hints:**
- Structure output as: `{ 'events': [...], 'metadata': { 'total_events': N, 'saved_at': timestamp } }`
- Use `json.dump()` with `indent=2`
- Raise `StorageError` on failure

**Key decision:** What metadata should be included?

### Step 16: Implement DatabaseSink

Write events to database (stub).

**Hints:**
- Take `connection_string` parameter
- For now, just log that you would save
- Demonstrates pattern

### Step 17: Implement WebhookSink

Send events to webhook (stub).

**Hints:**
- Take `webhook_url` parameter
- For now, just log that you would send
- Demonstrates pattern

### Step 18: Understand Sink Polymorphism

All sinks have the same interface but different implementations:
```python
sink.save(events)  # Works for JSON, Database, Webhook
```

---

## Part 5: Build the Pipeline (Steps 19)

Your task: Create orchestrator and factories.

### Step 19: Create EventPipeline Class

Orchestrates flow from source → processors → sink.

**Hints:**
- Constructor takes: source (EventSource), processors (List[EventProcessor]), sink (EventSink)
- Track metrics: events_fetched, events_processed, events_saved, errors
- Implement `run()` method that:
  1. Calls source.fetch()
  2. Passes events through each processor in order
  3. Calls sink.save() with final result
  4. Returns metrics

**Key decisions:**
- How should errors be handled?
- When should you log?
- What metrics matter?

### Step 20: Create SourceFactory

Flexible source creation.

**Hints:**
- Static method `create(source_type: str, **kwargs)` → EventSource
- Handle types: 'csv', 'database', 'api'
- Return appropriate source instance

**Implementation approach:**
```python
if source_type == 'csv':
    return CSVEventSource(kwargs['filepath'])
# ... etc
```

### Step 21: Create SinkFactory

Flexible sink creation.

**Hints:**
- Similar pattern to SourceFactory
- Handle types: 'json', 'database', 'webhook'

### Step 22: Create ProcessorFactory

Helper to build processor chains.

**Hints:**
- Method `create_default_chain()` → List[EventProcessor]
- Return: [EventValidator(), EventEnricher(), EventAggregator()]

### Step 23: Create Main Function

Execute pipeline with sample data.

**Hints:**
- Check if `events_raw.csv` exists (error if not)
- Use factories to create components
- Create EventPipeline instance
- Call `.run()` and print metrics

### Step 24: Make Module Executable

Add standard Python entry point:
```python
if __name__ == '__main__':
    main()
```

---

## Testing Your Code

Before moving to Exercise 2, verify everything works:

```bash
# Generate sample data
python generate-data.py

# Run pipeline
python exercise-1-solution.py

# Should see:
# - Fetched X events
# - Validated and filtered
# - Enriched with user data
# - Aggregated statistics
# - Saved to events_processed.json
```

---

## Common Challenges & Hints

**Challenge:** "I'm not sure when to use abstract methods"
- **Hint:** Use `@abstractmethod` for anything every subclass MUST implement
- Example: Every source must have `fetch()`, but implementation differs

**Challenge:** "How do I know when to raise an exception vs log an error?"
- **Hint:** 
  - Log for informational messages (progress, debugging)
  - Raise exceptions for things that break the pipeline
  - Example: Invalid event → log & filter; CSV file missing → raise error

**Challenge:** "My EnrichmentError isn't being caught"
- **Hint:** Make sure it inherits from `PipelineError` or you catch the specific type

**Challenge:** "I'm not sure about type hints"
- **Hint:** 
  - `List[Dict[str, Any]]` = list of dictionaries with string keys
  - `Dict[str, Any]` = dictionary with string keys, any value types
  - Use them! They help catch bugs early

**Challenge:** "Factory pattern seems overly complex"
- **Hint:** It's worth it when you have many implementations
- Future: You could add sources/sinks without changing pipeline code

---

## Design Patterns Summary

| Pattern | Used For | Benefit |
|---------|----------|---------|
| **Abstract Base Class** | Define interfaces | Enforce consistency |
| **Inheritance** | Share code | DRY principle |
| **Polymorphism** | Flexible implementations | Loosely coupled |
| **Factory** | Object creation | No hard-coded dependencies |
| **Composition** | Build complex systems | Flexible combinations |
| **Custom Exceptions** | Error handling | Clear error types |

---

## Next Steps

✅ **You've implemented Exercise 1!**

Your code now demonstrates:
- Modular design (each class does one thing)
- Extensibility (add new sources/processors/sinks easily)
- Testability (each component works independently)
- SOLID principles in practice

**Ready for Exercise 2?**
You'll refactor this using **functional programming patterns and decorators** to make it even cleaner!

