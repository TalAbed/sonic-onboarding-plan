# OOP for Data Engineering

## Introduction

Object-Oriented Programming (OOP) is the backbone of scalable, maintainable data systems. While scripts and functional code can work for one-off analysis, **real data engineering** requires structured, extensible systems.

Think about your data pipeline:
- Multiple data sources (APIs, databases, files)
- Multiple processing stages (validation, transformation, aggregation)
- Multiple output destinations (databases, files, dashboards)
- Error handling at each stage
- Monitoring and logging throughout

OOP gives you a way to **model these components as reusable, testable objects** rather than tangled spaghetti code.

### Why OOP Matters for Data Engineering

**Without OOP:**
```python
# Messy approach - copy-paste everywhere
def process_events_from_api():
    events = fetch_from_api()
    validated = validate(events)
    cleaned = clean(validated)
    aggregated = aggregate(cleaned)
    save_to_db(aggregated)

def process_events_from_file():
    events = read_from_file()
    validated = validate(events)  # Duplicate!
    cleaned = clean(validated)    # Duplicate!
    aggregated = aggregate(cleaned)
    save_to_db(aggregated)
```

**With OOP:**
```python
class EventPipeline:
    def __init__(self, source, transformer, sink):
        self.source = source
        self.transformer = transformer
        self.sink = sink
    
    def run(self):
        events = self.source.fetch()
        processed = self.transformer.process(events)
        self.sink.save(processed)

# Reusable for any source, transformer, sink combination
pipeline = EventPipeline(
    source=APISource(),
    transformer=EventTransformer(),
    sink=DatabaseSink()
)
pipeline.run()
```

The OOP approach is **DRY** (Don't Repeat Yourself), **testable** (mock each component), and **extensible** (add new sources/sinks without modifying core logic).

---

## Core Concepts

### 1. Classes and Objects

A **class** is a blueprint. An **object** is an instance of that blueprint.

```python
class EventProcessor:
    """A class to process event data."""
    
    def __init__(self, name):
        """Initialize the processor."""
        self.name = name
        self.processed_count = 0
    
    def process(self, event):
        """Process a single event."""
        self.processed_count += 1
        return {'processed': True, 'event': event}

# Create objects (instances)
processor1 = EventProcessor("processor-1")
processor2 = EventProcessor("processor-2")

# Each object has its own state
processor1.process({'id': 1})
processor2.process({'id': 2})
print(processor1.processed_count)  # 1
print(processor2.processed_count)  # 1
```

**Key points:**
- `__init__` is the constructor (called when you create an object)
- `self` refers to the specific object instance
- Each object maintains its own state (processed_count)

### 2. Attributes and Methods

**Attributes** are data (variables). **Methods** are functions.

```python
class DataValidator:
    def __init__(self):
        self.rules = []  # Attribute: data
        self.errors = 0  # Attribute: state
    
    def add_rule(self, rule):
        """Method: adds a rule"""
        self.rules.append(rule)
    
    def validate(self, data):
        """Method: validates data"""
        for rule in self.rules:
            if not rule(data):
                self.errors += 1
                return False
        return True

validator = DataValidator()
validator.add_rule(lambda x: x['id'] > 0)
validator.add_rule(lambda x: x['status'] in ['ok', 'error'])

is_valid = validator.validate({'id': 1, 'status': 'ok'})
```

### 3. Inheritance

**Inheritance** lets you create a hierarchy of classes. Child classes **inherit** attributes and methods from parent classes.

```python
class DataSource:
    """Base class for all data sources."""
    
    def __init__(self, name):
        self.name = name
    
    def fetch(self):
        """Override this in subclasses."""
        raise NotImplementedError("Subclasses must implement fetch()")

class APISource(DataSource):
    """Fetch data from an API."""
    
    def __init__(self, name, url):
        super().__init__(name)  # Call parent constructor
        self.url = url
    
    def fetch(self):
        # Implementation specific to API
        return requests.get(self.url).json()

class FileSource(DataSource):
    """Fetch data from a file."""
    
    def __init__(self, name, filepath):
        super().__init__(name)
        self.filepath = filepath
    
    def fetch(self):
        # Implementation specific to file
        with open(self.filepath) as f:
            return json.load(f)

# Both are DataSource subclasses
api_source = APISource("api", "https://api.example.com/events")
file_source = FileSource("file", "data/events.json")

# Can be used interchangeably
sources = [api_source, file_source]
for source in sources:
    data = source.fetch()  # Polymorphism!
```

**Key concepts:**
- `super().__init__()` calls the parent class constructor
- Subclasses override parent methods (like `fetch()`)
- Different implementations, same interface

### 4. Polymorphism

**Polymorphism** = "many forms". The same method name behaves differently depending on the object.

```python
class EventTransformer:
    def transform(self, event):
        raise NotImplementedError()

class JSONTransformer(EventTransformer):
    def transform(self, event):
        return json.dumps(event)

class CSVTransformer(EventTransformer):
    def transform(self, event):
        return f"{event['id']},{event['status']}"

# Same method name, different behavior
transformers = [JSONTransformer(), CSVTransformer()]
event = {'id': 1, 'status': 'ok'}

for transformer in transformers:
    result = transformer.transform(event)
    # JSON: '{"id": 1, "status": "ok"}'
    # CSV: '1,ok'
```

This is powerful because you can write code that works with **any** transformer without knowing its specific type.

### 5. Encapsulation

**Encapsulation** = hiding internal details, exposing only what's needed.

```python
class SecureProcessor:
    def __init__(self):
        self._internal_state = {}  # Private (convention: underscore prefix)
        self.status = "ready"       # Public
    
    def _validate_internal(self, data):
        """Private method - not meant to be called externally."""
        return len(data) > 0
    
    def process(self, data):
        """Public method - the intended interface."""
        if self._validate_internal(data):
            self._internal_state = data
            self.status = "processed"
            return True
        return False

processor = SecureProcessor()
processor.process({'id': 1})
processor.status  # OK to access
processor._internal_state  # Works but shouldn't - it's private!
```

**Why it matters:**
- Users of your class don't need to know internals
- You can change internals without breaking user code
- Prevents accidental misuse

### 6. Properties (Getters/Setters)

Python's `@property` decorator lets you add logic to attribute access.

```python
class EventCounter:
    def __init__(self):
        self._count = 0
    
    @property
    def count(self):
        """Getter - access with obj.count"""
        return self._count
    
    @count.setter
    def count(self, value):
        """Setter - set with obj.count = value"""
        if value < 0:
            raise ValueError("Count cannot be negative")
        self._count = value
    
    def increment(self):
        self._count += 1

counter = EventCounter()
counter.increment()
counter.count = 10  # Uses setter - validates
# counter.count = -5  # Raises ValueError
```

This prevents invalid states and adds validation.

---

## Practical Patterns

### Pattern 1: Factory Pattern

Create objects without specifying their exact classes.

```python
class SourceFactory:
    @staticmethod
    def create(source_type, **kwargs):
        if source_type == 'api':
            return APIEventSource(kwargs['url'], kwargs['api_key'])
        elif source_type == 'database':
            return DatabaseEventSource(kwargs['connection_string'])
        elif source_type == 'file':
            return FileEventSource(kwargs['filepath'])
        else:
            raise ValueError(f"Unknown source type: {source_type}")

# Usage - no need to import specific classes
source = SourceFactory.create(
    'api',
    url='https://api.sonic.com/events',
    api_key='key123'
)
```

### Pattern 2: Strategy Pattern

Switch between different algorithms/implementations.

```python
class EventAggregator:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def aggregate(self, events):
        return self.strategy.aggregate(events)

class HourlyAggregation:
    def aggregate(self, events):
        # Group by hour
        pass

class DailyAggregation:
    def aggregate(self, events):
        # Group by day
        pass

class RegionalAggregation:
    def aggregate(self, events):
        # Group by region
        pass

# Switch strategies easily
aggregator = EventAggregator(HourlyAggregation())
# Later: aggregator.strategy = DailyAggregation()
```

### Pattern 3: Observer Pattern

Objects notify others when something happens.

```python
class EventPipeline:
    def __init__(self):
        self.listeners = []
    
    def add_listener(self, listener):
        self.listeners.append(listener)
    
    def notify_listeners(self, event):
        for listener in self.listeners:
            listener.on_event(event)

class LoggerListener:
    def on_event(self, event):
        logging.info(f"Event: {event}")

class MetricsListener:
    def on_event(self, event):
        self.count += 1

# Usage
pipeline = EventPipeline()
pipeline.add_listener(LoggerListener())
pipeline.add_listener(MetricsListener())
```

---

## Best Practices

### ✅ DO:

1. **Use inheritance for "is-a" relationships**
   ```python
   class APISource(EventSource):  # APISource IS-A EventSource
       pass
   ```

2. **Use composition for "has-a" relationships**
   ```python
   class Pipeline:
       def __init__(self, source, processor):  # Pipeline HAS-A source
           self.source = source
   ```

3. **Keep classes focused (Single Responsibility)**
   ```python
   class EventValidator:  # Only validates
       def validate(self, event): pass
   
   class EventLogger:  # Only logs
       def log(self, event): pass
   ```

4. **Use meaningful names**
   ```python
   # Good
   class EventDataValidator: pass
   
   # Bad
   class EDV: pass
   class Processor: pass
   ```

5. **Document with docstrings**
   ```python
   class Pipeline:
       """Coordinates data flow from source through processor to sink."""
       
       def run(self):
           """Execute the pipeline, handling errors gracefully."""
   ```

### ❌ DON'T:

1. **Create god objects** - classes that do everything
   ```python
   # Bad - too many responsibilities
   class MegaProcessor:
       def fetch(self): pass
       def validate(self): pass
       def transform(self): pass
       def aggregate(self): pass
       def save(self): pass
   ```

2. **Use inheritance when composition is better**
   ```python
   # Bad - inheritance for "has-a"
   class LoggingPipeline(Pipeline):
       # Pipeline IS-A LoggingPipeline? No!
       pass
   
   # Good - composition
   class Pipeline:
       def __init__(self, logger):
           self.logger = logger
   ```

3. **Expose implementation details**
   ```python
   # Bad - users shouldn't care about internal queue
   pipeline._internal_queue.append(event)
   
   # Good - hidden behind a method
   pipeline.add_event(event)
   ```

---

## Common Mistakes

### Mistake 1: Over-Engineering

Don't create classes for everything. Sometimes a function is enough.

```python
# Too much
class AddNumbers:
    def add(self, a, b):
        return a + b

# Better
def add(a, b):
    return a + b
```

**Rule:** Use OOP when you need **state** (attributes) or **multiple related behaviors** (methods).

### Mistake 2: Tight Coupling

Classes shouldn't depend on concrete implementations.

```python
# Bad - tight coupling
class Pipeline:
    def __init__(self):
        self.source = APIEventSource()  # Hard-coded dependency
    
    def run(self):
        self.source.fetch()

# Good - loose coupling via dependency injection
class Pipeline:
    def __init__(self, source):
        self.source = source  # Accept any source
    
    def run(self):
        self.source.fetch()
```

### Mistake 3: Deep Inheritance Hierarchies

Keep inheritance shallow (usually 2-3 levels max).

```python
# Bad - deep hierarchy
class DataProcessor: pass
class EventProcessor(DataProcessor): pass
class ValidationProcessor(EventProcessor): pass
class AsyncValidationProcessor(ValidationProcessor): pass

# Better - compose instead
class ValidationProcessor:
    def __init__(self, validator, executor):
        self.validator = validator
        self.executor = executor  # Can be sync or async
```

---

## Quick Reference

| Concept | When to Use | Example |
|---------|-------------|---------|
| **Class** | Model a thing with state and behavior | EventProcessor |
| **Inheritance** | Share code, express "is-a" relationship | APISource extends EventSource |
| **Composition** | Build complex objects from simpler ones | Pipeline contains source, processor, sink |
| **Polymorphism** | Different implementations, same interface | Multiple EventSource types |
| **Encapsulation** | Hide internal details | Private _internal_state, public process() |
| **Properties** | Add logic to attribute access | @property, @setter |

---

OOP is a foundation. Combined with functional patterns and proper error handling, it enables you to build **production-grade data systems**. 🚀

