# Error Handling and Logging

## Introduction

Data pipelines fail. Your API goes down. A file is corrupted. The database is full. A user provides invalid data.

**How you handle these failures determines whether you:**
- 🟢 Detect issues quickly and fix them
- 🔴 Let silent failures corrupt data or mislead users

This guide covers two essentials:
1. **Exceptions** - Making failures explicit and actionable
2. **Logging** - Recording what happened so you can debug later

---

## Exception Handling Fundamentals

### Try/Except/Else/Finally

```python
try:
    # Code that might fail
    result = risky_operation()
except SpecificError as e:
    # Handle this error
    print(f"Specific error occurred: {e}")
except (Error1, Error2):
    # Handle multiple error types
    print("One of these errors happened")
except Exception as e:
    # Catch-all (use sparingly!)
    print(f"Unexpected error: {e}")
else:
    # Runs if no exception occurred
    print(f"Success! Result: {result}")
finally:
    # Always runs (cleanup)
    cleanup()
```

### Built-in Exceptions (Python's Hierarchy)

```python
# Most common built-in exceptions
ValueError        # Invalid value (e.g., int("abc"))
TypeError         # Wrong type (e.g., len(5))
KeyError          # Missing dict key
IndexError        # Out of range list index
FileNotFoundError # File doesn't exist
IOError           # Input/output failure
AttributeError    # Attribute doesn't exist
RuntimeError      # Generic runtime error

# Exception hierarchy (simplified)
BaseException
├─ SystemExit
├─ KeyboardInterrupt
└─ Exception
   ├─ StopIteration
   ├─ ArithmeticError
   ├─ AssertionError
   ├─ AttributeError
   ├─ ImportError
   ├─ OSError (FileNotFoundError, IOError, etc.)
   ├─ ValueError
   ├─ TypeError
   └─ ... many more
```

### When to Catch What

```python
def safe_int_conversion(value):
    """Convert to int, handling errors gracefully."""
    try:
        return int(value)
    except ValueError:
        # Handle the specific case of invalid format
        return 0
    except TypeError:
        # Handle the case of wrong type
        raise TypeError(f"Expected string or number, got {type(value)}")

# Usage
safe_int_conversion("123")    # 123
safe_int_conversion("abc")    # 0
safe_int_conversion(None)     # Raises TypeError
```

**Rule: Catch specific exceptions. Avoid bare `except:` or `except Exception:`**

---

## Custom Exceptions for Data Pipelines

Create your own exception hierarchy to make failures explicit:

### Basic Custom Exception

```python
class EventProcessingError(Exception):
    """Base class for all event processing errors."""
    pass

class ValidationError(EventProcessingError):
    """Data failed validation."""
    pass

class EnrichmentError(EventProcessingError):
    """Failed to enrich event from external source."""
    pass

class StorageError(EventProcessingError):
    """Failed to save event to storage."""
    pass

# Usage
def validate_event(event):
    if 'id' not in event:
        raise ValidationError(f"Event missing 'id' field: {event}")
    if event['id'] <= 0:
        raise ValidationError(f"Invalid event ID: {event['id']}")

def save_event(event):
    try:
        database.insert(event)
    except DatabaseError as e:
        raise StorageError(f"Failed to save event {event['id']}: {e}")
```

### Exception with Additional Context

```python
class PipelineError(Exception):
    """Base pipeline error with context."""
    
    def __init__(self, message, event=None, stage=None):
        self.message = message
        self.event = event
        self.stage = stage
        super().__init__(self.message)
    
    def __str__(self):
        parts = [self.message]
        if self.stage:
            parts.append(f"Stage: {self.stage}")
        if self.event:
            parts.append(f"Event ID: {self.event.get('id')}")
        return " | ".join(parts)

class DataValidationError(PipelineError):
    """Data validation failed."""
    pass

# Usage
try:
    if not event['status'] in valid_statuses:
        raise DataValidationError(
            f"Invalid status: {event['status']}",
            event=event,
            stage="validation"
        )
except DataValidationError as e:
    logger.error(str(e))
    # Later: "Invalid status: unknown | Stage: validation | Event ID: 123"
```

### Exception Chaining (Preserve Context)

```python
def process_event(event):
    try:
        result = external_api_call(event)
    except requests.RequestException as e:
        # Chain exceptions - preserve original error
        raise StorageError(
            f"Failed to enrich event from API"
        ) from e  # 'from e' shows the original cause

# Error shows both the new and original exception
# Much more useful for debugging!

try:
    process_event({'id': 1})
except StorageError as e:
    print(f"Error: {e}")
    print(f"Caused by: {e.__cause__}")  # Original RequestException
```

---

## Error Handling Patterns

### Pattern 1: Retry on Failure

```python
import time
from typing import Callable, Any

def retry(max_attempts=3, delay=1, backoff=2):
    """Decorator to retry a function with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            attempt = 1
            current_delay = delay
            
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise  # Give up
                    
                    logger.warning(
                        f"{func.__name__} attempt {attempt} failed: {e}. "
                        f"Retrying in {current_delay}s..."
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff
                    attempt += 1
        
        return wrapper
    return decorator

# Usage
@retry(max_attempts=3, delay=1)
def call_external_api(event):
    """Call API with automatic retry."""
    return requests.get('https://api.sonic.com/enrich', json=event)
```

### Pattern 2: Fail-Safe Defaults

```python
def get_user_preference(user_id, preference_key, default=None):
    """Get user preference, return default if not found."""
    try:
        user = database.get_user(user_id)
        return user.preferences[preference_key]
    except (KeyError, AttributeError, DatabaseError):
        # Safe to return default instead of crashing
        return default

# Usage
color = get_user_preference(123, 'theme_color', default='light')
```

### Pattern 3: Graceful Degradation

```python
class EnrichedEventProcessor:
    def process(self, event):
        try:
            enrichment = self._fetch_enrichment(event)
        except EnrichmentError as e:
            # Log the failure but continue with partial data
            logger.warning(f"Enrichment failed: {e}. Processing without.")
            enrichment = {}
        
        return {**event, **enrichment}
    
    def _fetch_enrichment(self, event):
        """Might fail if external API is down."""
        response = requests.get('https://api.sonic.com/enrich')
        if response.status_code != 200:
            raise EnrichmentError(f"API returned {response.status_code}")
        return response.json()
```

---

## Logging Fundamentals

### Basic Logging Setup

```python
import logging

# Get a logger for this module
logger = logging.getLogger(__name__)

# Configure it (usually done once at app startup)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),      # Write to file
        logging.StreamHandler()               # Also write to console
    ]
)

# Use it
logger.info("Application started")
logger.warning("This is a warning")
logger.error("Something went wrong")
```

### Log Levels

```python
logger.debug("Detailed diagnostic info (lots of these)")
logger.info("General informational messages")
logger.warning("Warning: something unexpected (watch this)")
logger.error("Error: something failed (fix this)")
logger.critical("Critical: system is broken (immediate action)")
```

**Rule: Use the right level**
- `DEBUG` - Details for developers (variable values, loop iterations)
- `INFO` - Important events (pipeline started, 1000 events processed)
- `WARNING` - Potentially problematic (retry attempt, missing optional data)
- `ERROR` - Something failed (failed to save, API error, exception)
- `CRITICAL` - System broken (can't proceed, fatal error)

### Structured Logging

Instead of string messages, use structured key/value pairs for better analysis:

```python
# Bad - unstructured, hard to parse
logger.info(f"Processing event {event_id} from user {user_id} with status {status}")

# Good - structured, easy to search/filter
logger.info("event_processed", extra={
    'event_id': event_id,
    'user_id': user_id,
    'status': status
})

# Or JSON format
import json
logger.info(json.dumps({
    'action': 'event_processed',
    'event_id': event_id,
    'user_id': user_id,
    'status': status
}))
```

### Contextual Information

```python
import logging

class ContextualLogger:
    def __init__(self, logger):
        self.logger = logger
        self.context = {}
    
    def add_context(self, key, value):
        """Add information to all log messages."""
        self.context[key] = value
    
    def log(self, level, message):
        """Log with context."""
        full_message = f"{message} | {json.dumps(self.context)}"
        self.logger.log(level, full_message)

# Usage
logger = ContextualLogger(logging.getLogger(__name__))
logger.add_context('pipeline_id', 'pipeline-123')
logger.add_context('batch_id', 'batch-456')
logger.log(logging.INFO, "Processing events")
# "Processing events | {'pipeline_id': 'pipeline-123', 'batch_id': 'batch-456'}"
```

---

## Best Practices

### ✅ DO:

1. **Create custom exception hierarchy**
   ```python
   class EventError(Exception): pass
   class ValidationError(EventError): pass
   class EnrichmentError(EventError): pass
   ```

2. **Log errors with context**
   ```python
   logger.error(f"Failed to process event {event_id}", extra={
       'event_id': event_id,
       'stage': 'enrichment',
       'error': str(e)
   })
   ```

3. **Log at appropriate levels**
   ```python
   logger.info("Pipeline started")        # Important event
   logger.debug(f"Processing: {event}")   # Detailed diagnostic
   logger.warning("Retrying after failure")  # Needs attention
   logger.error("Failed permanently")     # Fix this
   ```

4. **Include stack traces for exceptions**
   ```python
   try:
       risky_operation()
   except Exception:
       logger.exception("Operation failed")  # Includes stack trace
   ```

### ❌ DON'T:

1. **Use bare except or except Exception**
   ```python
   # Bad - catches everything, including KeyboardInterrupt
   try:
       something()
   except:
       pass
   
   # Better - catch specific exceptions
   try:
       something()
   except ValueError as e:
       handle(e)
   ```

2. **Log sensitive data**
   ```python
   # Bad - logs passwords
   logger.info(f"User {user} logged in with password {pwd}")
   
   # Good
   logger.info(f"User {user} logged in")
   ```

3. **Create loggers inside functions**
   ```python
   # Bad - creates logger every time
   def process():
       logger = logging.getLogger(__name__)
       logger.info("Processing")
   
   # Good - create once at module level
   logger = logging.getLogger(__name__)
   def process():
       logger.info("Processing")
   ```

4. **Swallow exceptions silently**
   ```python
   # Bad - hides the error
   try:
       save(event)
   except:
       pass
   
   # Good - at least log it
   try:
       save(event)
   except Exception as e:
       logger.error(f"Failed to save: {e}")
       raise  # Re-raise if critical
   ```

---

## Common Mistakes

### Mistake 1: Too Generic Exceptions

```python
# Bad - catches too much, masks real problems
try:
    events = process_events()
except Exception:
    events = []  # Silence the error

# Good - specific handling
try:
    events = validate_and_process(events)
except ValidationError:
    logger.warning("Invalid events, processing valid ones")
    events = [e for e in events if is_valid(e)]
except DatabaseError:
    logger.error("Database error, giving up")
    raise
```

### Mistake 2: Not Including Enough Context

```python
# Bad - which event failed?
logger.error("Event failed")

# Good - full context for debugging
logger.error(f"Failed to process event {event['id']}: {error}")
```

### Mistake 3: Logging Too Much

```python
# Bad - spam in logs, can't find important messages
for event in events:
    logger.info(f"Processing event {event['id']}")
    logger.info(f"Validating {event}")
    logger.info(f"Done")

# Good - log summaries, errors, important events
logger.info(f"Processing {len(events)} events")
if errors:
    for error in errors:
        logger.error(f"Failed: {error}")
logger.info(f"Processed {success_count} events, {error_count} errors")
```

### Mistake 4: Wrong Log Levels

```python
# Bad - logs warnings for expected situations
if user_not_found:
    logger.warning("User not found")

# Good - log at appropriate level
if user_not_found:
    logger.info("User lookup returned no results")

# Or warning if truly unexpected
if database_connection_lost:
    logger.warning("Database connection lost, retrying...")
```

---

## Quick Reference

| Topic | Do This | Why |
|-------|---------|-----|
| **Custom exceptions** | Create hierarchy | Clear failure modes |
| **Catch exceptions** | Catch specific types | Explicit error handling |
| **Re-raise** | Use `raise` or `raise from e` | Preserve context |
| **Log levels** | Use appropriate level | Easier to filter |
| **Context** | Include event ID, stage | Easier to debug |
| **Structure** | Use JSON format | Easier to parse/search |
| **Sensitive data** | Don't log it | Security |

---

Proper error handling and logging transform debugging from a nightmare into a science. Invest in both. 🚀

