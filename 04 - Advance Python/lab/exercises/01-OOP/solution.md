# Exercise 1: Solution

Here's a comprehensive solution for Exercise 1. Your approach may differ—that's expected and fine!

## Complete Solution

```python
#!/usr/bin/env python3
"""
Exercise 1: Building Data Pipeline Classes (OOP)

A modular, extensible event processing pipeline using OOP design patterns.
"""

import csv
import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Any

# ============================================================
# STEP 1: SETUP AND LOGGING
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================
# STEP 2: CUSTOM EXCEPTIONS
# ============================================================

class PipelineError(Exception):
    """Base exception for all pipeline errors."""
    pass

class ValidationError(PipelineError):
    """Event failed validation."""
    pass

class EnrichmentError(PipelineError):
    """Event enrichment failed."""
    pass

class StorageError(PipelineError):
    """Event storage failed."""
    pass

# ============================================================
# STEPS 3 - 5: EventSource, EventProcessor, EventSink
# ============================================================

class EventSource(ABC):
    """Abstract base class for event sources."""
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
    
    @abstractmethod
    def fetch(self) -> List[Dict[str, Any]]:
        """Fetch events from source."""
        pass
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

class EventProcessor(ABC):
    """Abstract base class for event processors."""
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
    
    @abstractmethod
    def process(self, events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process a batch of events."""
        pass
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

class EventSink(ABC):
    """Abstract base class for event sinks (outputs)."""
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
    
    @abstractmethod
    def save(self, events: List[Dict[str, Any]]) -> None:
        """Save events to destination."""
        pass
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

# ============================================================
# STEPS 7 - 9: CSVEventSource, DatabaseEventSource, APIEventSource
# ============================================================

class CSVEventSource(EventSource):
    """Read events from a CSV file."""
    
    def __init__(self, filepath: str):
        super().__init__(name=f"CSV({filepath})")
        self.filepath = filepath
    
    def fetch(self) -> List[Dict[str, Any]]:
        try:
            self.logger.info(f"Fetching events from {self.filepath}")
            events = []
            
            with open(self.filepath, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    event = {
                        'event_id': int(row['event_id']),
                        'timestamp': row['timestamp'],
                        'event_type': row['event_type'],
                        'user_id': row['user_id'],
                        'status': row['status'],
                        'latency_ms': int(row['latency_ms'])
                    }
                    events.append(event)
            
            self.logger.info(f"Fetched {len(events)} events from CSV")
            return events
        
        except FileNotFoundError as e:
            raise PipelineError(f"CSV file not found: {self.filepath}") from e
        except Exception as e:
            raise PipelineError(f"Error reading CSV: {e}") from e

class DatabaseEventSource(EventSource):
    """Read events from a database (STUB)."""
    
    def __init__(self, connection_string: str):
        super().__init__(name=f"Database({connection_string[:20]}...)")
        self.connection_string = connection_string
    
    def fetch(self) -> List[Dict[str, Any]]:
        self.logger.info("Fetching events from database (STUB)")
        return []

class APIEventSource(EventSource):
    """Read events from an API endpoint (STUB)."""
    
    def __init__(self, api_url: str, api_key: str = ""):
        super().__init__(name=f"API({api_url})")
        self.api_url = api_url
        self.api_key = api_key
    
    def fetch(self) -> List[Dict[str, Any]]:
        self.logger.info(f"Fetching events from API (STUB)")
        return []

# ============================================================
# STEPS 11 - 13: EventValidator, EventEnricher, EventAggregator
# ============================================================

class EventValidator(EventProcessor):
    """Validate events meet required standards."""
    
    def __init__(self):
        super().__init__(name="EventValidator")
        self.valid_event_types = {'purchase', 'login', 'checkout', 'view'}
        self.valid_statuses = {'ok', 'error', 'timeout'}
    
    def process(self, events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        self.logger.info(f"Validating {len(events)} events")
        
        valid_events = []
        invalid_count = 0
        
        for event in events:
            if self._is_valid(event):
                valid_events.append(event)
            else:
                invalid_count += 1
                self.logger.warning(f"Invalid event: {event}")
        
        self.logger.info(f"Validation complete: {len(valid_events)} valid, {invalid_count} invalid")
        return valid_events
    
    def _is_valid(self, event: Dict[str, Any]) -> bool:
        required = {'event_id', 'timestamp', 'event_type', 'user_id', 'status', 'latency_ms'}
        if not all(k in event for k in required):
            return False
        if event['event_type'] not in self.valid_event_types:
            return False
        if event['status'] not in self.valid_statuses:
            return False
        if event['latency_ms'] < 0:
            return False
        return True

class EventEnricher(EventProcessor):
    """Add additional data to events."""
    
    def __init__(self):
        super().__init__(name="EventEnricher")
        self.user_data = {
            'user_1': {'country': 'US', 'premium': True},
            'user_2': {'country': 'UK', 'premium': False},
            'user_3': {'country': 'CA', 'premium': True},
        }
    
    def process(self, events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        self.logger.info(f"Enriching {len(events)} events")
        
        enriched = []
        for event in events:
            try:
                enriched_event = self._enrich(event)
                enriched.append(enriched_event)
            except Exception as e:
                self.logger.error(f"Failed to enrich event {event['event_id']}: {e}")
                raise EnrichmentError(f"Enrichment failed for event {event['event_id']}") from e
        
        self.logger.info(f"Enriched {len(enriched)} events")
        return enriched
    
    def _enrich(self, event: Dict[str, Any]) -> Dict[str, Any]:
        enriched = event.copy()
        
        user_id = event['user_id']
        if user_id in self.user_data:
            enriched['user_country'] = self.user_data[user_id]['country']
            enriched['is_premium'] = self.user_data[user_id]['premium']
        else:
            enriched['user_country'] = 'UNKNOWN'
            enriched['is_premium'] = False
        
        enriched['enriched_at'] = datetime.utcnow().isoformat()
        return enriched

class EventAggregator(EventProcessor):
    """Aggregate events by type and add statistics."""
    
    def __init__(self):
        super().__init__(name="EventAggregator")
    
    def process(self, events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        self.logger.info(f"Aggregating {len(events)} events")
        
        aggregates = self._calculate_aggregates(events)
        
        processed = []
        for event in events:
            event_with_agg = event.copy()
            event_type = event['event_type']
            event_with_agg['type_stats'] = aggregates[event_type]
            processed.append(event_with_agg)
        
        self.logger.info(f"Added aggregation stats to {len(processed)} events")
        return processed
    
    def _calculate_aggregates(self, events: List[Dict]) -> Dict[str, Dict]:
        stats = {}
        
        for event in events:
            event_type = event['event_type']
            
            if event_type not in stats:
                stats[event_type] = {
                    'count': 0,
                    'total_latency': 0,
                    'error_count': 0
                }
            
            stats[event_type]['count'] += 1
            stats[event_type]['total_latency'] += event['latency_ms']
            if event['status'] == 'error':
                stats[event_type]['error_count'] += 1
        
        for event_type in stats:
            count = stats[event_type]['count']
            stats[event_type]['avg_latency'] = stats[event_type]['total_latency'] / count
            del stats[event_type]['total_latency']
        
        return stats

# ============================================================
# STEPS 15 - 17: JSONSink, DatabaseSink, WebhookSink
# ============================================================

class JSONSink(EventSink):
    """Write events to a JSON file."""
    
    def __init__(self, filepath: str):
        super().__init__(name=f"JSON({filepath})")
        self.filepath = filepath
    
    def save(self, events: List[Dict[str, Any]]) -> None:
        try:
            self.logger.info(f"Saving {len(events)} events to {self.filepath}")
            
            output = {
                'events': events,
                'metadata': {
                    'total_events': len(events),
                    'saved_at': datetime.utcnow().isoformat()
                }
            }
            
            with open(self.filepath, 'w') as f:
                json.dump(output, f, indent=2)
            
            self.logger.info(f"Saved {len(events)} events to JSON")
        
        except Exception as e:
            raise StorageError(f"Failed to save JSON: {e}") from e

class DatabaseSink(EventSink):
    """Write events to a database (STUB)."""
    
    def __init__(self, connection_string: str):
        super().__init__(name=f"Database({connection_string[:20]}...)")
        self.connection_string = connection_string
    
    def save(self, events: List[Dict[str, Any]]) -> None:
        self.logger.info(f"Saving {len(events)} events to database (STUB)")

class WebhookSink(EventSink):
    """Send events to a webhook endpoint (STUB)."""
    
    def __init__(self, webhook_url: str):
        super().__init__(name=f"Webhook({webhook_url})")
        self.webhook_url = webhook_url
    
    def save(self, events: List[Dict[str, Any]]) -> None:
        self.logger.info(f"Sending {len(events)} events to webhook (STUB)")

# ============================================================
# STEP 19: PIPELINE ORCHESTRATOR
# ============================================================

class EventPipeline:
    """Orchestrates the flow from source to sink through processors."""
    
    def __init__(self, 
                 source: EventSource,
                 processors: List[EventProcessor],
                 sink: EventSink):
        self.source = source
        self.processors = processors
        self.sink = sink
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.metrics = {
            'events_fetched': 0,
            'events_processed': 0,
            'events_saved': 0,
            'errors': 0
        }
    
    def run(self) -> Dict[str, Any]:
        self.logger.info("=" * 60)
        self.logger.info("PIPELINE STARTED")
        self.logger.info(f"Source: {self.source}")
        self.logger.info(f"Processors: {[str(p) for p in self.processors]}")
        self.logger.info(f"Sink: {self.sink}")
        self.logger.info("=" * 60)
        
        try:
            self.logger.info("\nStep 1: Fetching events...")
            events = self.source.fetch()
            self.metrics['events_fetched'] = len(events)
            self.logger.info(f"✓ Fetched {len(events)} events")
            
            self.logger.info(f"\nStep 2: Processing events through {len(self.processors)} processor(s)...")
            for processor in self.processors:
                self.logger.info(f"  Applying {processor}")
                events = processor.process(events)
                self.logger.info(f"  ✓ {len(events)} events after {processor.name}")
            
            self.metrics['events_processed'] = len(events)
            
            self.logger.info(f"\nStep 3: Saving events...")
            self.sink.save(events)
            self.metrics['events_saved'] = len(events)
            self.logger.info(f"✓ Saved {len(events)} events")
            
            self.logger.info("\n" + "=" * 60)
            self.logger.info("PIPELINE COMPLETED SUCCESSFULLY")
            self.logger.info("=" * 60)
            self.logger.info(f"Events fetched:   {self.metrics['events_fetched']}")
            self.logger.info(f"Events processed: {self.metrics['events_processed']}")
            self.logger.info(f"Events saved:     {self.metrics['events_saved']}")
            self.logger.info("=" * 60)
            
            return self.metrics
        
        except Exception as e:
            self.metrics['errors'] = 1
            self.logger.error("=" * 60)
            self.logger.error("PIPELINE FAILED")
            self.logger.error(f"Error: {e}")
            self.logger.error("=" * 60)
            raise

# ============================================================
# STEPS 20 - 22: FACTORIES
# ============================================================

class SourceFactory:
    """Factory for creating event sources."""
    
    @staticmethod
    def create(source_type: str, **kwargs) -> EventSource:
        if source_type == 'csv':
            return CSVEventSource(kwargs['filepath'])
        elif source_type == 'database':
            return DatabaseEventSource(kwargs['connection_string'])
        elif source_type == 'api':
            return APIEventSource(kwargs['api_url'], kwargs.get('api_key', ''))
        else:
            raise ValueError(f"Unknown source type: {source_type}")

class SinkFactory:
    """Factory for creating event sinks."""
    
    @staticmethod
    def create(sink_type: str, **kwargs) -> EventSink:
        if sink_type == 'json':
            return JSONSink(kwargs['filepath'])
        elif sink_type == 'database':
            return DatabaseSink(kwargs['connection_string'])
        elif sink_type == 'webhook':
            return WebhookSink(kwargs['webhook_url'])
        else:
            raise ValueError(f"Unknown sink type: {sink_type}")

class ProcessorFactory:
    """Factory for creating processors."""
    
    @staticmethod
    def create_default_chain() -> List[EventProcessor]:
        return [
            EventValidator(),
            EventEnricher(),
            EventAggregator()
        ]

# ============================================================
# STEPS 23 - 24: MAIN EXECUTION
# ============================================================

def main():
    """Execute the pipeline with sample data."""
    
    print("\n" + "=" * 60)
    print("SECTION 4 - EXERCISE 1: OOP DATA PIPELINE")
    print("=" * 60)
    
    import os
    if not os.path.exists('events_raw.csv'):
        print("\n❌ Error: events_raw.csv not found!")
        print("Please run: python generate-data.py")
        return
    
    print("\nCreating pipeline components...")
    source = SourceFactory.create('csv', filepath='events_raw.csv')
    processors = ProcessorFactory.create_default_chain()
    sink = SinkFactory.create('json', filepath='events_processed.json')
    
    pipeline = EventPipeline(source, processors, sink)
    metrics = pipeline.run()
    
    print("\n✓ Pipeline execution complete!")
    print(f"  - Fetched: {metrics['events_fetched']} events")
    print(f"  - Processed: {metrics['events_processed']} events")
    print(f"  - Saved to: events_processed.json")
    print("=" * 60 + "\n")

if __name__ == '__main__':
    main()
```

---

## Key Design Decisions Explained

### 1. Abstract Base Classes Pattern

We use `ABC` (Abstract Base Class) to define interfaces:

```python
class EventSource(ABC):
    @abstractmethod
    def fetch(self) -> List[Dict[str, Any]]:
        pass
```

**Why?**
- Forces all subclasses to implement the required method
- Creates a contract: "All sources must have a `fetch()` method"
- Enables polymorphism: code can work with any source

**Without ABC**, nothing prevents a broken implementation. Python wouldn't complain until runtime.

### 2. Inheritance with `super()`

Each concrete class calls `super().__init__()`:

```python
class CSVEventSource(EventSource):
    def __init__(self, filepath: str):
        super().__init__(name=f"CSV({filepath})")
        self.filepath = filepath
```

**Why?**
- Ensures parent class initialization runs
- Reuses parent constructor logic (name, logger setup)
- DRY principle: don't repeat base class setup code

**Without it**, `self.logger` wouldn't exist in subclasses.

### 3. Custom Exceptions with Inheritance

```python
class PipelineError(Exception):
    pass

class ValidationError(PipelineError):
    pass
```

**Why?**
- Can catch specific errors: `except ValidationError:`
- Can catch all pipeline errors: `except PipelineError:`
- More informative than generic `Exception`

**Exception chaining** (`from e`) preserves the original error:
```python
raise PipelineError(f"CSV file not found") from e
```
This shows what originally caused the error—helpful for debugging!

### 4. Factory Pattern

Instead of:
```python
# Tightly coupled—knows about all source types
if user_type == 'csv':
    source = CSVEventSource(filepath)
```

We use:
```python
# Loose coupling—factory handles creation
source = SourceFactory.create('csv', filepath=filepath)
```

**Why?**
- Pipeline code doesn't change when adding new sources
- New sources just need a factory method added
- Separation of concerns: creation logic centralized

### 5. Composition Over Inheritance

`EventPipeline` composes components:

```python
class EventPipeline:
    def __init__(self, source: EventSource, processors: List[EventProcessor], sink: EventSink):
        self.source = source
        self.processors = processors
        self.sink = sink
```

**Why?**
- Flexible: can swap any source/processor/sink
- Reusable: same pipeline works with different configs
- Testable: can test with mock sources

**Without composition**, pipeline would be tightly coupled to specific implementations.

### 6. Logging at Multiple Levels

We create loggers per class:

```python
class EventSource(ABC):
    def __init__(self, name: str):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
```

**Why?**
- Can filter logs by component
- Helps debug which processor/source had issues
- Better than one global logger

### 7. Metrics Tracking

Pipeline tracks execution:

```python
self.metrics = {
    'events_fetched': 0,
    'events_processed': 0,
    'events_saved': 0,
    'errors': 0
}
```

**Why?**
- Know what happened during execution
- Useful for monitoring and optimization
- Helps detect issues (e.g., validation filtered most events)

### 8. Helper Methods for Complex Logic

Processors use helper methods:

```python
class EventValidator(EventProcessor):
    def process(self, events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for event in events:
            if self._is_valid(event):  # Delegate to helper
                valid_events.append(event)
    
    def _is_valid(self, event: Dict[str, Any]) -> bool:
        # Complex logic isolated here
        pass
```

**Why?**
- Makes code readable: `if self._is_valid(event)` is clear
- Isolates complexity: validation logic in one place
- Easier to test and modify

---

## Understanding the Flow

When you run this pipeline:

```
Input: events_raw.csv (100 events)
    ↓
[CSVEventSource] reads CSV
    ↓ 100 events
[EventValidator] checks validity
    ↓ ~95 events (5 filtered as invalid)
[EventEnricher] adds user country/premium status
    ↓ ~95 events (enriched)
[EventAggregator] calculates stats by event_type
    ↓ ~95 events (with statistics)
[JSONSink] writes to events_processed.json
    ↓
Output: events_processed.json
```

Each processor transforms the data for the next one. The pipeline orchestrator coordinates this flow.

---

## Testing Your Implementation

Try these variations:

```python
# Different processor chain
processors = [EventValidator()]  # Just validation

# Different sink
sink = SinkFactory.create('database', connection_string='postgresql://...')

# Different source + sink
source = SourceFactory.create('api', api_url='https://api.example.com')
sink = SinkFactory.create('webhook', webhook_url='https://webhook.example.com')
```

The beauty of this design: everything still works! No code changes needed.

---

## Next: Exercise 2

In Exercise 2, you'll refactor this using **functional programming patterns**:
- Replace classes with functions where simpler
- Use decorators for cross-cutting concerns (logging, timing)
- Apply map/filter/reduce for data processing
- Compare performance with OOP approach

This exercise teaches why OOP shines for large systems—and when functional programming is cleaner!

