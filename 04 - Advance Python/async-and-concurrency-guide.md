# Async and Concurrency

## Introduction

When your data pipeline has **I/O operations** (network calls, file reads, database queries), your program often sits **idle waiting** for responses. Concurrency lets you use that idle time productively.

There are three main approaches in Python:
1. **Threading** - Multiple threads in one process (I/O-bound)
2. **Multiprocessing** - Multiple processes (CPU-bound)
3. **AsyncIO** - Async/await with event loop (I/O-bound, many operations)

This guide explains when to use each.

---

## The GIL (Global Interpreter Lock)

**Python's GIL** is the biggest thing to understand. It means only **one thread can execute Python code at a time**, even on multi-core machines.

```python
import threading
import time

def cpu_task(n):
    """CPU-intensive task"""
    total = 0
    for i in range(n):
        total += i
    return total

# Sequential execution
start = time.time()
cpu_task(100000000)
cpu_task(100000000)
sequential_time = time.time() - start

# Threading (won't help - GIL prevents true parallelism)
start = time.time()
t1 = threading.Thread(target=cpu_task, args=(100000000,))
t2 = threading.Thread(target=cpu_task, args=(100000000,))
t1.start()
t2.start()
t1.join()
t2.join()
threading_time = time.time() - start

# Result: threading_time ≈ sequential_time or even slower!
# The GIL prevents parallelism for CPU-bound work
```

**Key point:** The GIL doesn't block I/O operations, so threading is great for I/O.

---

## Threading

**Threading** is best for **I/O-bound** operations (network, files, databases).

### Basic Threading

```python
import threading
import requests
from typing import List

def fetch_url(url: str) -> str:
    """Fetch a URL (I/O operation)"""
    response = requests.get(url)
    return response.text

# Sequential approach - slow
urls = ['https://api.sonic.com/events', 'https://api2.sonic.com/metrics']
results = []
for url in urls:
    result = fetch_url(url)
    results.append(result)

# Threaded approach - faster
threads = []
results = [None, None]

def fetch_and_store(index, url):
    results[index] = fetch_url(url)

for i, url in enumerate(urls):
    t = threading.Thread(target=fetch_and_store, args=(i, url))
    threads.append(t)
    t.start()

for t in threads:
    t.join()  # Wait for all threads to complete
```

### Thread Pool (Better)

Instead of creating threads manually, use a pool:

```python
from concurrent.futures import ThreadPoolExecutor
import requests

def fetch_url(url):
    response = requests.get(url)
    return response.text

urls = ['https://api.sonic.com/events', 'https://api2.sonic.com/metrics']

# ThreadPoolExecutor manages threads automatically
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_url, urls))
    # Or: results = [executor.submit(fetch_url, url) for url in urls]
```

### When to Use Threading

- ✅ I/O operations (network, disk, database)
- ✅ Many concurrent operations (10-100)
- ✅ Operations that might block
- ❌ CPU-intensive tasks (GIL prevents parallelism)
- ❌ Shared state (requires locks, complex)

### Example: Processing Event Batches

```python
from concurrent.futures import ThreadPoolExecutor

class EventProcessor:
    def process_event(self, event):
        """Process one event - includes I/O"""
        # Validate (CPU)
        if not self._validate(event):
            return None
        
        # Call external API (I/O)
        enriched = self._enrich_from_api(event)
        
        # Save to database (I/O)
        self._save(enriched)
        
        return enriched
    
    def process_batch_threaded(self, events, max_workers=10):
        """Process multiple events in parallel"""
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(self.process_event, events))
        return [r for r in results if r is not None]
```

---

## Multiprocessing

**Multiprocessing** is best for **CPU-bound** operations. Each process has its own Python interpreter.

### Basic Multiprocessing

```python
import multiprocessing

def calculate(n):
    """CPU-intensive calculation"""
    total = 0
    for i in range(n):
        total += i
    return total

# CPU-bound work - multiprocessing shines
numbers = [100000000, 100000000, 50000000, 75000000]

with multiprocessing.Pool(processes=4) as pool:
    results = pool.map(calculate, numbers)

# This actually runs in parallel (unlike threading for CPU)
```

### Process Pool vs Thread Pool

```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time

def cpu_work(n):
    total = 0
    for i in range(n):
        total += i
    return total

numbers = [50000000] * 4

# Threading - slow for CPU work
start = time.time()
with ThreadPoolExecutor(max_workers=4) as e:
    list(e.map(cpu_work, numbers))
print(f"Threading: {time.time() - start:.2f}s")

# Multiprocessing - faster
start = time.time()
with ProcessPoolExecutor(max_workers=4) as e:
    list(e.map(cpu_work, numbers))
print(f"Multiprocessing: {time.time() - start:.2f}s")

# Multiprocessing is 3-4x faster for CPU work
```

### Sharing Data Between Processes

```python
from multiprocessing import Queue, Process
import time

def worker(queue):
    """Worker processes data from queue"""
    while True:
        item = queue.get()
        if item is None:  # Poison pill - signal to stop
            break
        result = item ** 2
        print(f"Processed: {result}")

# Main process
queue = Queue()

# Start worker processes
processes = [Process(target=worker, args=(queue,)) for _ in range(3)]
for p in processes:
    p.start()

# Send work
for i in range(10):
    queue.put(i)

# Signal completion
for _ in range(3):
    queue.put(None)

for p in processes:
    p.join()
```

### When to Use Multiprocessing

- ✅ CPU-intensive calculations
- ✅ Large data processing
- ✅ Need true parallelism on multi-core systems
- ❌ Quick, lightweight operations (overhead is high)
- ❌ Frequent process creation/destruction
- ⚠️ Complex data sharing between processes

---

## AsyncIO

**AsyncIO** uses `async`/`await` and an event loop. Perfect for **many I/O operations** without process/thread overhead.

### Basic Async

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    """Async version of fetch"""
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        'https://api.sonic.com/events',
        'https://api2.sonic.com/metrics'
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    return results

# Run the async function
results = asyncio.run(main())
```

### Async Syntax

```python
# Define async function with 'async'
async def my_async_function():
    # Use 'await' to wait for async operations
    result = await some_async_operation()
    return result

# Run async code
asyncio.run(my_async_function())

# Or gather multiple async tasks
tasks = [async_task1(), async_task2(), async_task3()]
results = asyncio.gather(*tasks)  # Run concurrently
```

### Event Loop Concept

```python
import asyncio

async def task(name, duration):
    print(f"{name} starting")
    await asyncio.sleep(duration)
    print(f"{name} done")
    return name

async def main():
    # Create tasks
    t1 = task("A", 2)
    t2 = task("B", 1)
    t3 = task("C", 3)
    
    # Run concurrently - event loop switches between them
    results = await asyncio.gather(t1, t2, t3)
    # Output:
    # A starting
    # B starting
    # C starting
    # B done       (after 1 second)
    # A done       (after 2 seconds)
    # C done       (after 3 seconds)
    # Total time: ~3 seconds (not 6)

asyncio.run(main())
```

### When to Use AsyncIO

- ✅ Many I/O operations (100+)
- ✅ Network calls to multiple services
- ✅ Lightweight, minimal overhead
- ✅ Need to interleave operations
- ❌ CPU-bound work (use multiprocessing)
- ❌ Blocking library calls (can't await them)

### Example: Async Event Processing

```python
import asyncio
import aiohttp

class AsyncEventProcessor:
    def __init__(self):
        self.session = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, *args):
        await self.session.close()
    
    async def enrich_event(self, event):
        """Enrich event with data from external API"""
        url = f"https://api.sonic.com/enrich/{event['id']}"
        async with self.session.get(url) as response:
            enrichment = await response.json()
        return {**event, **enrichment}
    
    async def process_batch(self, events):
        """Process multiple events concurrently"""
        tasks = [self.enrich_event(e) for e in events]
        return await asyncio.gather(*tasks)

# Usage
async def main():
    events = [{'id': 1}, {'id': 2}, {'id': 3}]
    
    async with AsyncEventProcessor() as processor:
        enriched = await processor.process_batch(events)
    
    return enriched

results = asyncio.run(main())
```

---

## Decision Tree: Which Concurrency to Use?

```
Is it I/O-bound? (network, files, database)
├─ YES
│  ├─ How many concurrent operations?
│  │  ├─ Few (< 20): Use Threading
│  │  └─ Many (>= 20): Use AsyncIO
│  └─ Can you modify code to use async?
│     ├─ YES: Use AsyncIO (preferred)
│     └─ NO: Use Threading
│
└─ NO (CPU-bound)
   └─ Use Multiprocessing
```

### Quick Decision Table

| Scenario | Use | Why |
|----------|-----|-----|
| Fetch 5 URLs | Threading | Simple, few operations |
| Fetch 1000 URLs | AsyncIO | Lightweight, high concurrency |
| Parallel data processing | Multiprocessing | CPU-bound work |
| File I/O (read/write) | Threading | Straightforward I/O |
| Database queries | AsyncIO | Many concurrent queries |
| Machine learning model training | Multiprocessing | CPU-intensive |

---

## DE Context: Concurrent Event Processing

```python
from concurrent.futures import ThreadPoolExecutor
import asyncio
import logging

class ConcurrentPipeline:
    def __init__(self, num_workers=10):
        self.num_workers = num_workers
        self.logger = logging.getLogger(__name__)
    
    def process_with_threading(self, events):
        """Use threading for I/O-bound operations"""
        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            results = list(executor.map(self._process_one, events))
        return results
    
    async def process_with_asyncio(self, events):
        """Use asyncio for many concurrent I/O operations"""
        tasks = [self._process_one_async(e) for e in events]
        results = await asyncio.gather(*tasks)
        return results
    
    def _process_one(self, event):
        # Validate
        if not self._validate(event):
            self.logger.warning(f"Invalid event: {event['id']}")
            return None
        
        # Call external API (I/O)
        enriched = self._call_api(event)
        
        # Save to database (I/O)
        self._save(enriched)
        
        self.logger.info(f"Processed event {event['id']}")
        return enriched
    
    async def _process_one_async(self, event):
        # Same logic but async-compatible
        if not self._validate(event):
            self.logger.warning(f"Invalid event: {event['id']}")
            return None
        
        # Use async API call
        enriched = await self._call_api_async(event)
        await self._save_async(enriched)
        
        self.logger.info(f"Processed event {event['id']}")
        return enriched
```

---

## Best Practices

### ✅ DO:

1. **Profile before choosing concurrency**
   ```python
   # Find the actual bottleneck
   import cProfile
   cProfile.run('your_function()')
   ```

2. **Use thread/process pools, not manual management**
   ```python
   # Good
   with ThreadPoolExecutor(max_workers=10) as executor:
       results = executor.map(func, items)
   ```

3. **Handle timeouts and failures**
   ```python
   with ThreadPoolExecutor(max_workers=5) as executor:
       futures = [executor.submit(fetch, url) for url in urls]
       for future in concurrent.futures.as_completed(futures, timeout=30):
           try:
               result = future.result()
           except Exception as e:
               logger.error(f"Task failed: {e}")
   ```

4. **Log concurrency issues**
   ```python
   logger.info(f"Starting {len(events)} tasks with {num_workers} workers")
   ```

### ❌ DON'T:

1. **Use threading for CPU-bound work**
   ```python
   # Bad - GIL prevents parallelism
   with ThreadPoolExecutor(max_workers=4) as e:
       e.map(cpu_heavy_task, data)
   ```

2. **Create threads in tight loops**
   ```python
   # Bad - overhead is huge
   for item in huge_list:
       t = threading.Thread(target=process, args=(item,))
       t.start()
   ```

3. **Share mutable state without locks**
   ```python
   # Bad - race conditions
   counter = 0
   def increment():
       global counter
       counter += 1  # Not thread-safe!
   ```

4. **Mix threading and asyncio carelessly**
   ```python
   # Bad - deadlock risk
   async def async_func():
       result = threading_func()  # Wrong!
   ```

---

## Common Mistakes

### Mistake 1: Choosing Wrong Concurrency Type

```python
# Bad - using threading for CPU work
with ThreadPoolExecutor(max_workers=4) as e:
    results = e.map(heavy_calculation, large_dataset)
# Runs slowly due to GIL

# Good - use multiprocessing
with ProcessPoolExecutor(max_workers=4) as e:
    results = e.map(heavy_calculation, large_dataset)
# True parallelism
```

### Mistake 2: Not Handling Failures

```python
# Bad - if one task fails, you don't know
with ThreadPoolExecutor(max_workers=10) as e:
    results = list(e.map(fetch_url, urls))

# Good - handle failures gracefully
with ThreadPoolExecutor(max_workers=10) as e:
    futures = [e.submit(fetch_url, url) for url in urls]
    results = []
    for future in futures:
        try:
            results.append(future.result(timeout=30))
        except Exception as e:
            logger.error(f"Failed: {e}")
            results.append(None)
```

### Mistake 3: Creating Too Many Threads

```python
# Bad - creates 1000 threads (huge overhead)
with ThreadPoolExecutor(max_workers=1000) as e:
    results = e.map(fetch, urls)

# Good - use reasonable worker count
workers = min(len(urls), 50)
with ThreadPoolExecutor(max_workers=workers) as e:
    results = e.map(fetch, urls)
```

---

## Quick Reference

| Tool | I/O-bound | CPU-bound | Concurrency |
|------|-----------|-----------|-------------|
| **Threading** | ✅ Good | ❌ No | 10-100 |
| **Multiprocessing** | ⚠️ Overhead | ✅ Good | 2-8 |
| **AsyncIO** | ✅✅ Best | ❌ No | 100+ |
| **Sequential** | ❌ Slow | ✅ Simple | 1 |

---

Concurrency is powerful but tricky. Profile first, choose wisely, and always handle failures gracefully. 🚀

