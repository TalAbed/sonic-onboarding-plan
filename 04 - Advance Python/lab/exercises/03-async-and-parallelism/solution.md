# Exercise 3: Concurrency & Parallelism - Solution

**Goal:** Understand when to use threading, multiprocessing, and async/await by implementing each approach on two workload types (I/O-bound and CPU-bound).

---

## Part 1: Sequential Baseline (Steps 1-6)

### Step 1: Create a function that downloads a single URL

```python
import requests

def download_url(url):
    """
    Download a single URL and return status code.
    
    This is the basic building block for all other approaches.
    """
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None
```

**Explanation:**
- Uses `requests.get()` to download the URL
- Sets 5-second timeout to prevent hanging
- Returns HTTP status code (200, 404, etc.)
- Catches exceptions if download fails

---

### Step 2: Process a list of URLs sequentially

```python
def download_sequential(urls):
    """
    Download all URLs one at a time (sequentially).
    
    This is slow: each URL blocks until it completes.
    10 URLs × 1 second each = 10 seconds total
    """
    results = []
    for url in urls:
        status = download_url(url)
        results.append(status)
    return results
```

**Explanation:**
- Loops through each URL in sequence
- Waits for each download to complete before starting next
- Collects all status codes in results list
- No parallelism at all—this is our baseline

---

### Step 3: Measure sequential I/O time

```python
import time

def measure_sequential_io():
    """
    Time how long sequential downloads take.
    
    Using httpbin.org/delay/1 to simulate 1-second network latency.
    """
    urls = ["https://httpbin.org/delay/1"] * 10  # 10 URLs with 1s delay each
    
    start = time.perf_counter()
    results = download_sequential(urls)
    io_time = time.perf_counter() - start
    
    print(f"Sequential I/O: {len(results)} URLs downloaded in {io_time:.2f}s")
    return io_time, results
```

**Explanation:**
- `time.perf_counter()` gives high-resolution timing
- httpbin.org/delay/1 adds 1-second artificial delay to simulate network latency
- 10 URLs × 1 second = ~10 seconds expected
- Returns timing and results for comparison

---

### Step 4: Compute checksum of large data (CPU-bound)

```python
import hashlib

def compute_checksum(data_id):
    """
    Compute SHA256 checksum of large data (simulates CPU work).
    
    Each call takes ~1 second of pure CPU computation.
    """
    # Simulate a 100MB file by hashing a large string repeatedly
    data = b"x" * 10_000_000  # 10MB of data
    hasher = hashlib.sha256()
    
    for _ in range(10):  # Hash it 10 times to simulate heavy work
        hasher.update(data)
    
    return hasher.hexdigest()
```

**Explanation:**
- Creates large 10MB block of data
- Hashes it 10 times to simulate heavy computation
- Returns hexadecimal checksum
- Each call takes ~1 second (adjust multiplier for your system)

---

### Step 5: Process files sequentially (CPU-bound)

```python
def compute_sequential(num_files=10):
    """
    Compute checksums for all files sequentially.
    
    This blocks on each computation.
    10 files × 1 second each = 10 seconds total
    """
    results = []
    for i in range(num_files):
        checksum = compute_checksum(i)
        results.append(checksum)
    return results
```

**Explanation:**
- Loops through file indices
- Computes checksum for each file sequentially
- Each computation blocks until complete
- No parallelism—pure sequential execution

---

### Step 6: Create baseline summary report

```python
def baseline_summary():
    """
    Establish baseline measurements.
    
    Measure I/O and CPU separately to understand what we're optimizing.
    These times will be compared against threaded/async/multiprocess versions.
    """
    print("\n" + "=" * 60)
    print("PART 1: SEQUENTIAL BASELINE")
    print("=" * 60)
    
    # Measure I/O time
    io_time, _ = measure_sequential_io()
    
    # Measure CPU time
    print("\nSequential CPU: Computing checksums...")
    start = time.perf_counter()
    results = compute_sequential(10)
    cpu_time = time.perf_counter() - start
    print(f"Sequential CPU: 10 files processed in {cpu_time:.2f}s")
    
    baseline = {
        'io_time': io_time,
        'cpu_time': cpu_time,
        'total': io_time + cpu_time
    }
    
    print(f"\nBaseline Summary:")
    print(f"  I/O:    {baseline['io_time']:.2f}s")
    print(f"  CPU:    {baseline['cpu_time']:.2f}s")
    print(f"  Total:  {baseline['total']:.2f}s")
    
    return baseline
```

**Explanation:**
- Measures I/O and CPU times separately
- Stores results in dictionary for easy comparison
- This is the BASELINE that other approaches will try to beat
- Expected: ~10 seconds I/O + ~10 seconds CPU = ~20 seconds total

---

## Part 2: Threading Approach (Steps 7-12)

### Step 7: Create a thread pool with worker threads

```python
from concurrent.futures import ThreadPoolExecutor

def create_thread_pool(max_workers=5):
    """
    Set up a thread pool with worker threads.
    
    ThreadPoolExecutor manages a pool of 5 worker threads.
    Tasks are distributed to available workers.
    """
    return ThreadPoolExecutor(max_workers=max_workers)
```

**Explanation:**
- `ThreadPoolExecutor` creates a pool of reusable threads
- `max_workers=5` means 5 threads handling tasks simultaneously
- Using context manager (`with` statement) automatically cleans up
- Threads can handle ~5 concurrent operations

---

### Step 8: Download URLs in parallel using threads

```python
from concurrent.futures import as_completed

def download_threaded(urls, max_workers=5):
    """
    Download all URLs in parallel using threads.
    
    Submit all tasks first, then collect results as they complete.
    While one thread waits for network, others can run.
    """
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks at once (non-blocking)
        futures = [executor.submit(download_url, url) for url in urls]
        
        # Collect results as they complete (not in order)
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    
    return results
```

**Explanation:**
- `executor.submit()` adds task to queue without waiting
- Returns `Future` object that will eventually have result
- `as_completed()` yields futures as their tasks finish
- Results can come back in any order (not submission order)
- With 5 workers, 10 URLs complete in ~2 seconds (5x speedup)

---

### Step 9: Ensure thread-safe result collection

```python
# Already handled above with as_completed()
# Each future.result() is thread-safe
# Results are collected in a list (thread-safe append)
```

**Explanation:**
- `as_completed()` provides thread-safe iteration
- Each `future.result()` waits for completion and returns result
- Python's GIL ensures list append is atomic (thread-safe)
- No explicit locks needed for this simple case

---

### Step 10: Measure threading speedup for I/O

```python
def measure_threaded_io():
    """
    Time threaded I/O and compare to baseline.
    
    With 5 worker threads, we download 5 URLs in parallel.
    10 URLs × 1s each, parallel 5: ~2 seconds (5x speedup)
    """
    urls = ["https://httpbin.org/delay/1"] * 10
    
    start = time.perf_counter()
    results = download_threaded(urls, max_workers=5)
    threaded_io = time.perf_counter() - start
    
    print(f"Threaded I/O: {len(results)} URLs downloaded in {threaded_io:.2f}s")
    return threaded_io
```

**Explanation:**
- Same timing approach as sequential
- Threading should be ~5x faster for I/O (5 workers × 10 seconds / 5 = 2 seconds)
- Shows massive speedup for network operations
- This demonstrates threading's strength for I/O-bound work

---

### Step 11: Attempt CPU work with threading

```python
def compute_threaded(num_files=10):
    """
    Try to compute checksums in parallel with threads.
    
    WARNING: This won't provide speedup due to Python's GIL!
    """
    results = []
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(compute_checksum, i) for i in range(num_files)]
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    
    return results
```

**Explanation:**
- Uses same pattern as I/O threading
- Submits CPU tasks to thread pool
- BUT: Python GIL prevents actual parallelism
- Only one thread can execute Python bytecode at a time
- Expect: ~10 seconds (no speedup!)

---

### Step 12: Threading analysis - observe GIL effect

```python
def threading_analysis(baseline):
    """
    Compare threading results and analyze the GIL effect.
    
    Key observations:
    - I/O is fast (5x faster) because threads wait for network
    - CPU is NOT faster because GIL blocks all other threads
    """
    print("\n" + "=" * 60)
    print("PART 2: THREADING APPROACH")
    print("=" * 60)
    
    # Measure I/O with threading
    io_time = measure_threaded_io()
    io_speedup = baseline['io_time'] / io_time
    
    # Measure CPU with threading
    print("\nThreaded CPU: Computing checksums...")
    start = time.perf_counter()
    results = compute_threaded(10)
    cpu_time = time.perf_counter() - start
    print(f"Threaded CPU: 10 files processed in {cpu_time:.2f}s")
    cpu_speedup = baseline['cpu_time'] / cpu_time if cpu_time > 0 else 1.0
    
    threading_results = {
        'io_time': io_time,
        'cpu_time': cpu_time,
        'total': io_time + cpu_time,
        'io_speedup': io_speedup,
        'cpu_speedup': cpu_speedup
    }
    
    print(f"\nThreading Results:")
    print(f"  I/O:    {io_time:.2f}s ({io_speedup:.1f}x faster)")
    print(f"  CPU:    {cpu_time:.2f}s ({cpu_speedup:.1f}x faster)")
    print(f"  Total:  {threading_results['total']:.2f}s")
    print(f"\n⚠️  CPU time didn't improve! This is the GIL (Global Interpreter Lock) effect.")
    print(f"    Python only lets one thread execute bytecode at a time.")
    print(f"    For CPU-bound work, use multiprocessing instead!")
    
    return threading_results
```

**Explanation:**
- Shows I/O gets ~5x faster (excellent!)
- Shows CPU gets no speedup (disappointing!)
- Explains why: GIL prevents parallel CPU execution
- Python release the GIL only during I/O operations
- This demonstrates threading's limitation for CPU work

---

## Part 3: Multiprocessing Approach (Steps 13-18)

### Step 13: Create a process pool with worker processes

```python
from concurrent.futures import ProcessPoolExecutor

def create_process_pool(max_workers=4):
    """
    Set up a process pool with worker processes.
    
    ProcessPoolExecutor creates separate Python processes.
    Each process has its own interpreter = no GIL!
    """
    return ProcessPoolExecutor(max_workers=max_workers)
```

**Explanation:**
- `ProcessPoolExecutor` creates separate Python processes
- Each process has own interpreter (no shared GIL)
- `max_workers=4` matches typical 4-core CPU
- True parallelism possible (unlike threading)
- Higher overhead due to process creation

---

### Step 14: Download URLs using separate processes

```python
def download_multiprocess(urls, max_workers=4):
    """
    Download URLs using separate processes.
    
    This will be SLOWER than threading for I/O.
    Process overhead > thread overhead for simple I/O tasks.
    """
    results = []
    
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(download_url, url) for url in urls]
        
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    
    return results
```

**Explanation:**
- Uses same pattern as threading
- But creates processes instead of threads
- Process creation overhead is significant (~100ms per process)
- For simple I/O, this overhead hurts performance
- 10 URLs with 4 processes: ~11 seconds (vs 2 seconds with threading)

---

### Step 15: Handle inter-process communication

```python
# Already handled above with ProcessPoolExecutor
# Each process is independent
# Results are automatically serialized/deserialized
# No shared memory (unlike threads)
```

**Explanation:**
- Processes don't share memory (unlike threads)
- Results are serialized (pickled) when returned from process
- ProcessPoolExecutor handles this automatically
- No race conditions (separate memory spaces)
- No thread-safety concerns needed

---

### Step 16: Compute checksums with multiprocessing

```python
def compute_multiprocess(num_files=10):
    """
    Compute checksums in parallel using processes.
    
    This is FASTER than threading for CPU work.
    Each process runs on different CPU core without GIL!
    """
    results = []
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(compute_checksum, i) for i in range(num_files)]
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    
    return results
```

**Explanation:**
- Same pattern as threading
- With 4 processes, can use 4 CPU cores simultaneously
- 10 files × 1 second, parallel 4: ~2.5 seconds (3.8x speedup)
- No GIL limitation—true parallelism!
- Each process can run Python bytecode concurrently

---

### Step 17: Compare I/O performance

```python
# Multiprocess I/O timing shown in Step 18 analysis
# Expected: 11-12 seconds (slower than threading due to overhead)
```

**Explanation:**
- Multiprocessing overhead for I/O-bound tasks hurts performance
- Process creation takes ~100ms each
- Context switching between processes adds overhead
- For many simple I/O operations, threading is better

---

### Step 18: Multiprocessing analysis

```python
def multiprocessing_analysis(baseline):
    """
    Multiprocessing excels at CPU-bound, slower for I/O.
    
    Key observations:
    - I/O is slower (process overhead > thread overhead)
    - CPU is fast (true parallelism, no GIL)
    """
    print("\n" + "=" * 60)
    print("PART 3: MULTIPROCESSING APPROACH")
    print("=" * 60)
    
    # Measure I/O with multiprocessing
    print("Multiprocess I/O: Downloading URLs...")
    urls = ["https://httpbin.org/delay/1"] * 10
    start = time.perf_counter()
    results = download_multiprocess(urls, max_workers=4)
    io_time = time.perf_counter() - start
    print(f"Multiprocess I/O: {len(results)} URLs downloaded in {io_time:.2f}s")
    io_speedup = baseline['io_time'] / io_time
    
    # Measure CPU with multiprocessing
    print("\nMultiprocess CPU: Computing checksums...")
    start = time.perf_counter()
    results = compute_multiprocess(10)
    cpu_time = time.perf_counter() - start
    print(f"Multiprocess CPU: 10 files processed in {cpu_time:.2f}s")
    cpu_speedup = baseline['cpu_time'] / cpu_time
    
    multiprocess_results = {
        'io_time': io_time,
        'cpu_time': cpu_time,
        'total': io_time + cpu_time,
        'io_speedup': io_speedup,
        'cpu_speedup': cpu_speedup
    }
    
    print(f"\nMultiprocessing Results:")
    print(f"  I/O:    {io_time:.2f}s ({io_speedup:.1f}x faster)")
    print(f"  CPU:    {cpu_time:.2f}s ({cpu_speedup:.1f}x faster)")
    print(f"  Total:  {multiprocess_results['total']:.2f}s")
    print(f"\n✓ CPU is FAST (no GIL limitation)!")
    print(f"⚠️  I/O is SLOWER (process overhead not worth it for simple I/O).")
    print(f"    Use multiprocessing for CPU-bound work only.")
    
    return multiprocess_results
```

**Explanation:**
- Shows I/O gets ~0.9x slower (process overhead hurts)
- Shows CPU gets ~3.8x faster (true parallelism!)
- Demonstrates multiprocessing's strength for CPU
- Demonstrates multiprocessing's weakness for I/O
- Clear recommendation: CPU work = multiprocessing, I/O work = threading

---

## Part 4: Async/Await Approach (Steps 19-24)

### Step 19: Create async download function

```python
import asyncio
import aiohttp

async def download_url_async(session, url):
    """
    Async function to download a single URL.
    
    The `await` keyword suspends this function until network responds.
    While waiting, event loop can run other tasks.
    """
    try:
        async with session.get(url, timeout=5) as response:
            return response.status
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None
```

**Explanation:**
- `async def` defines asynchronous function
- `await session.get()` suspends until response received
- While suspended, event loop runs other tasks
- `async with` ensures session is properly managed
- Returns status code like synchronous version

---

### Step 20: Download multiple URLs with asyncio.gather()

```python
async def download_async_gather(urls):
    """
    Download all URLs concurrently using async.
    
    asyncio.gather() waits for all tasks to complete.
    All requests run concurrently in single thread's event loop.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [download_url_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    return results
```

**Explanation:**
- Creates list of async tasks (not awaiting them yet)
- `asyncio.gather(*tasks)` runs all tasks concurrently
- Single thread's event loop switches between tasks
- Efficient I/O handling without threading overhead
- 10 URLs downloaded in ~2 seconds (like threading)

---

### Step 21: Use async context managers

```python
# Already shown in Step 20:
# async with aiohttp.ClientSession() as session:
```

**Explanation:**
- `async with` ensures resource cleanup
- Session is properly closed after all requests
- Prevents connection leaks
- Similar to regular context managers but for async

---

### Step 22: Run async downloader with asyncio.run()

```python
def measure_async_io():
    """
    Time async I/O and compare to baseline.
    
    asyncio.run() starts the event loop and runs our async function.
    Performance should be similar to threading (~2s for 10 URLs).
    """
    urls = ["https://httpbin.org/delay/1"] * 10
    
    start = time.perf_counter()
    results = asyncio.run(download_async_gather(urls))
    async_io = time.perf_counter() - start
    
    print(f"Async I/O: {len(results)} URLs downloaded in {async_io:.2f}s")
    return async_io
```

**Explanation:**
- `asyncio.run()` creates event loop and runs async function
- Handles all the event loop machinery
- Should complete in ~2 seconds (single thread, efficient I/O)
- Same throughput as threading, less overhead

---

### Step 23: Async for CPU-bound work (won't help)

```python
async def compute_checksum_async(data_id):
    """
    Try async for CPU-bound work.
    
    Note: Async doesn't help with CPU!
    Event loop still runs on single thread.
    CPU work blocks other tasks.
    """
    return compute_checksum(data_id)


async def compute_async_gather(num_files=10):
    """
    Run CPU tasks asynchronously (but this won't help).
    """
    tasks = [compute_checksum_async(i) for i in range(num_files)]
    results = await asyncio.gather(*tasks)
    return results
```

**Explanation:**
- Converting to async doesn't help CPU
- CPU work doesn't yield to other tasks
- Event loop is still single-threaded
- While task1 computes, tasks 2-10 wait
- Expected: ~10 seconds (no speedup)

---

### Step 24: Async analysis and decision framework

```python
def async_analysis(baseline):
    """
    Compare async results and create decision guide.
    
    Key observations:
    - I/O is fast (efficient single-threaded event loop)
    - CPU is NOT faster (async is only for I/O)
    """
    print("\n" + "=" * 60)
    print("PART 4: ASYNC/AWAIT APPROACH")
    print("=" * 60)
    
    # Measure I/O with async
    io_time = measure_async_io()
    io_speedup = baseline['io_time'] / io_time
    
    # Measure CPU with async (won't help)
    print("\nAsync CPU: Computing checksums...")
    start = time.perf_counter()
    results = asyncio.run(compute_async_gather(10))
    cpu_time = time.perf_counter() - start
    print(f"Async CPU: 10 files processed in {cpu_time:.2f}s")
    cpu_speedup = baseline['cpu_time'] / cpu_time if cpu_time > 0 else 1.0
    
    async_results = {
        'io_time': io_time,
        'cpu_time': cpu_time,
        'total': io_time + cpu_time,
        'io_speedup': io_speedup,
        'cpu_speedup': cpu_speedup
    }
    
    print(f"\nAsync Results:")
    print(f"  I/O:    {io_time:.2f}s ({io_speedup:.1f}x faster)")
    print(f"  CPU:    {cpu_time:.2f}s ({cpu_speedup:.1f}x faster)")
    print(f"  Total:  {async_results['total']:.2f}s")
    print(f"\n✓ I/O is fast and efficient (single thread, event loop).")
    print(f"⚠️  CPU time didn't improve (async not for CPU work).")
    print(f"    Async is for I/O-heavy workloads only!")
    
    return async_results
```

**Explanation:**
- Shows I/O gets ~5x faster (excellent!)
- Shows CPU gets no speedup (expected)
- Demonstrates async's strength for I/O
- Demonstrates async's limitation for CPU
- Clear recommendation: I/O work = async, CPU work = multiprocessing

---

## Final Comparison & Recommendations

### Step 24 (continued): Comprehensive comparison

```python
def final_comparison(baseline, threading_results, multiprocess_results, async_results):
    """
    Create comprehensive comparison table and recommendations.
    """
    print("\n" + "=" * 60)
    print("FINAL COMPARISON & RECOMMENDATIONS")
    print("=" * 60)
    
    print("\nPerformance Table (in seconds):")
    print("-" * 80)
    print(f"{'Approach':<20} {'I/O Time':<15} {'CPU Time':<15} {'Total':<15}")
    print("-" * 80)
    print(f"{'Sequential':<20} {baseline['io_time']:<15.2f} {baseline['cpu_time']:<15.2f} {baseline['total']:<15.2f}")
    print(f"{'Threading':<20} {threading_results['io_time']:<15.2f} {threading_results['cpu_time']:<15.2f} {threading_results['total']:<15.2f}")
    print(f"{'Multiprocessing':<20} {multiprocess_results['io_time']:<15.2f} {multiprocess_results['cpu_time']:<15.2f} {multiprocess_results['total']:<15.2f}")
    print(f"{'Async/Await':<20} {async_results['io_time']:<15.2f} {async_results['cpu_time']:<15.2f} {async_results['total']:<15.2f}")
    print("-" * 80)
    
    print("\nSpeedup Comparison (vs Sequential):")
    print("-" * 80)
    print(f"{'Approach':<20} {'I/O Speedup':<15} {'CPU Speedup':<15} {'Overall':<15}")
    print("-" * 80)
    print(f"{'Sequential':<20} {'1.0x':<15} {'1.0x':<15} {'1.0x':<15}")
    print(f"{'Threading':<20} {f'{threading_results[\"io_speedup\"]:.1f}x':<15} {f'{threading_results[\"cpu_speedup\"]:.1f}x':<15} {f'{baseline[\"total\"] / threading_results[\"total\"]:.1f}x':<15}")
    print(f"{'Multiprocessing':<20} {f'{multiprocess_results[\"io_speedup\"]:.1f}x':<15} {f'{multiprocess_results[\"cpu_speedup\"]:.1f}x':<15} {f'{baseline[\"total\"] / multiprocess_results[\"total\"]:.1f}x':<15}")
    print(f"{'Async/Await':<20} {f'{async_results[\"io_speedup\"]:.1f}x':<15} {f'{async_results[\"cpu_speedup\"]:.1f}x':<15} {f'{baseline[\"total\"] / async_results[\"total\"]:.1f}x':<15}")
    print("-" * 80)
    
    print("\nRecommendations:")
    print("-" * 80)
    print("\n✓ For I/O-bound workloads (network, file I/O):")
    print("  BEST:   Async/Await (lowest overhead, highest throughput)")
    print("  GOOD:   Threading (simpler, works well)")
    print("  AVOID:  Multiprocessing (overhead not worth it)")
    
    print("\n✓ For CPU-bound workloads (heavy computation):")
    print("  BEST:   Multiprocessing (true parallelism, no GIL)")
    print("  AVOID:  Threading (GIL blocks everything)")
    print("  AVOID:  Async (doesn't help CPU work)")
    
    print("\n✓ For mixed workloads (both I/O and CPU):")
    print("  OPTION 1: Async for I/O + Multiprocessing for CPU")
    print("  OPTION 2: Multiprocessing if CPU dominates")
    print("  OPTION 3: Threading if I/O dominates and CPU is light")
    
    print("\n✓ Decision Tree:")
    print("  1. Is it I/O-bound?")
    print("     YES → Is it network-heavy? YES → Use Async")
    print("     YES → Is it mixed I/O? → Use Threading")
    print("     NO  → Is it CPU-bound? YES → Use Multiprocessing")
    print("     NO  → Use Sequential (no concurrency benefit)")
```

**Explanation:**
- Shows all timings side-by-side
- Calculates speedups for each approach
- Clear winner for each workload type
- Explains trade-offs and recommendations
- Provides decision tree for choosing approach

---

### Save Results

```python
import json
from datetime import datetime

def save_results(baseline, threading_results, multiprocess_results, async_results):
    """
    Save results to JSON file for later analysis.
    """
    report = {
        'timestamp': datetime.utcnow().isoformat(),
        'sequential': baseline,
        'threading': threading_results,
        'multiprocessing': multiprocess_results,
        'async': async_results,
        'recommendations': {
            'io_bound': 'Async > Threading > Multiprocessing',
            'cpu_bound': 'Multiprocessing > Threading ≈ Sequential',
            'mixed': 'Async + Multiprocessing or Multiprocessing alone'
        }
    }
    
    with open('exercise3_results.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\n✓ Results saved to exercise3_results.json")
```

**Explanation:**
- Saves all results to JSON for later reference
- Includes timestamp for when test was run
- Stores recommendations for quick lookup
- Can be used by comparison script

---

### Main Execution

```python
def main():
    """Execute all parts of the exercise."""
    print("\n" + "=" * 60)
    print("EXERCISE 3: CONCURRENCY & PARALLELISM")
    print("=" * 60)
    
    # Part 1: Baseline
    baseline = baseline_summary()
    
    # Part 2: Threading
    threading_results = threading_analysis(baseline)
    
    # Part 3: Multiprocessing
    multiprocess_results = multiprocessing_analysis(baseline)
    
    # Part 4: Async
    async_results = async_analysis(baseline)
    
    # Comparison
    final_comparison(baseline, threading_results, multiprocess_results, async_results)
    
    # Save
    save_results(baseline, threading_results, multiprocess_results, async_results)
    
    print("\n✓ Exercise 3 Complete!")


if __name__ == '__main__':
    main()
```

**Explanation:**
- Runs all 4 parts in sequence
- Collects results from each part
- Generates final comparison
- Saves results to file
- Prints completion message

---

## Key Imports

To run this solution, you need:

```python
import time
import hashlib
import requests
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import json
from datetime import datetime
```

Install missing packages:
```bash
pip install requests aiohttp
```

---

## Summary Table

| Part | Approach | I/O Result | CPU Result | Best For |
|------|----------|-----------|-----------|----------|
| 1 | Sequential | 10s | 10s | Baseline only |
| 2 | Threading | 2s ✓ | 10s ✗ | I/O operations |
| 3 | Multiprocessing | 11s ✗ | 2.5s ✓ | CPU operations |
| 4 | Async/Await | 2s ✓ | 10s ✗ | Network-heavy I/O |

