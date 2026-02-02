# Exercise 3: Concurrency & Parallelism - Instructions

**Goal:** Learn when to use threading, multiprocessing, and async/await by implementing each approach on two different workload types (I/O-bound and CPU-bound).

---

## Part 1: Sequential Baseline (Steps 1-6)

**Step 1:** Create a function that downloads a single URL and returns the status code.

*Hints:*
- Use `requests` library
- Handle timeouts (5 seconds)
- Return just the status code

**Step 2:** Create a function that processes a list of 10 URLs sequentially (one after another) and returns all status codes.

*Hints:*
- Loop through each URL
- Call your Step 1 function for each
- Collect results in a list

**Step 3:** Measure how long it takes to download all 10 URLs sequentially.

*Hints:*
- Use `time.time()` or `time.perf_counter()`
- Calculate: end_time - start_time
- Print the total seconds

**Step 4:** Create a function that computes the SHA256 checksum of a single file (simulate with large data computation).

*Hints:*
- Use `hashlib.sha256()`
- Simulate a large file by hashing a large string multiple times
- Return the checksum as hexadecimal

**Step 5:** Create a function that processes 10 files sequentially, computing checksums for each and measuring the total time.

*Hints:*
- Loop through file list
- Call Step 4 function for each
- Measure total time
- How does CPU time compare to I/O time?

**Step 6:** Create a summary report comparing I/O time, CPU time, and total time to establish the baseline for comparison.

*Hints:*
- Store results in a dictionary: `{'io_time': X, 'cpu_time': Y, 'total': Z}`
- This baseline is what we'll try to beat with concurrency

---

## Part 2: Threading Approach (Steps 7-12)

**Step 7:** Import ThreadPoolExecutor from concurrent.futures and create a function that sets up a thread pool with 5 worker threads.

*Hints:*
- `from concurrent.futures import ThreadPoolExecutor`
- Use `with ThreadPoolExecutor(max_workers=5) as executor:`
- Return the executor or use it within context manager

**Step 8:** Implement a threaded downloader that uses the thread pool to fetch all 10 URLs in parallel instead of sequentially.

*Hints:*
- Use `executor.submit(function, url)` to submit tasks
- Store the returned Future objects
- Don't wait yet—submit all tasks first

**Step 9:** Ensure thread-safe result collection by using proper synchronization.

*Hints:*
- Use `as_completed(futures)` to get results as they complete
- Or use `map()` method on executor
- Collect results in a list

**Step 10:** Measure the time taken to download all 10 URLs with threading and calculate the speedup compared to sequential.

*Hints:*
- Use same timing approach as Step 3
- Calculate speedup: `sequential_time / threaded_time`
- Should be approximately 5x faster

**Step 11:** Attempt to process the 10 files using threads with the same thread pool and measure the CPU computation time.

*Hints:*
- Use same thread pool approach as Steps 7-9
- Submit checksum computation tasks
- Measure time and calculate speedup

**Step 12:** Compare threading results: observe that I/O is fast but CPU-bound tasks show no improvement.

*Hints:*
- Why is CPU slower or same speed with threading?
- Research: Python's Global Interpreter Lock (GIL)
- Note: GIL only lets one thread execute Python bytecode at a time
- This is the limitation of threading for CPU-bound work!

---

## Part 3: Multiprocessing Approach (Steps 13-18)

**Step 13:** Import ProcessPoolExecutor and create a function that sets up a process pool with 4 worker processes.

*Hints:*
- `from concurrent.futures import ProcessPoolExecutor`
- Use `with ProcessPoolExecutor(max_workers=4) as executor:`
- Each process has its own Python interpreter (no GIL!)

**Step 14:** Implement a multiprocessing downloader to fetch all 10 URLs using separate processes.

*Hints:*
- Use same `executor.submit()` approach
- Submit all URL download tasks
- Note: Multiprocessing has overhead, so I/O might be slower

**Step 15:** Handle inter-process communication by collecting results from each process.

*Hints:*
- Use `as_completed()` to collect results as they finish
- Each process returns results independently
- No thread-safety issues—processes don't share memory

**Step 16:** Measure the time taken to compute checksums for all 10 files using multiprocessing.

*Hints:*
- Use ProcessPoolExecutor again
- Submit checksum tasks
- Measure time and calculate speedup compared to sequential
- Should be 3-4x faster for CPU-bound work

**Step 17:** Measure I/O time with multiprocessing and compare it to threading.

*Hints:*
- Compare multiprocessing I/O time with threading I/O time
- Why might multiprocessing be slower for I/O?
- Hint: Process creation overhead is higher than thread creation

**Step 18:** Create a summary showing multiprocessing excels at CPU-bound tasks but is slower for I/O.

*Hints:*
- Store results: `{'io_time': X, 'cpu_time': Y, 'total': Z}`
- Compare all three approaches so far
- Create a comparison showing strengths and weaknesses

---

## Part 4: Async/Await Approach (Steps 19-24)

**Step 19:** Import asyncio and aiohttp, then create an async function that downloads a single URL without blocking.

*Hints:*
- `import asyncio`
- `import aiohttp`
- Use `async def download_url(url):`
- Use `await session.get(url)` inside the async function

**Step 20:** Implement an async downloader using asyncio.gather() to download all 10 URLs concurrently.

*Hints:*
- Create an async session: `async with aiohttp.ClientSession() as session:`
- Create list of tasks: `tasks = [download_url(url) for url in urls]`
- Use `await asyncio.gather(*tasks)` to run all concurrently

**Step 21:** Use async context managers to properly manage the HTTP session and ensure resources are cleaned up.

*Hints:*
- Use `async with` keyword for session management
- This ensures session is closed properly
- Research: Why is context manager important?

**Step 22:** Run the async downloader using asyncio.run() and measure the time.

*Hints:*
- Use `asyncio.run(your_async_function())`
- Measure time using same approach as before
- Should be similar to threading, around 2 seconds

**Step 23:** Attempt to use async for CPU-bound checksum computation and observe the results.

*Hints:*
- Convert checksum function to async (or call it from async)
- Measure the time
- Does async help with CPU-bound work?
- Why or why not? (Hint: Async is for I/O, not CPU)

**Step 24:** Create a comprehensive comparison table showing which approach wins for each workload type.

*Hints:*
- Create table with approaches (Sequential, Threading, Multiprocessing, Async)
- Columns: I/O Time, CPU Time, Total Time, Speedup
- Add recommendations: When to use each approach
- Decision tree: How to choose the right one

---

## Comparison & Recommendations

After completing all steps, create a decision guide:

```
When I/O-bound (lots of network/file I/O):
  - Best: Async/Await (lowest overhead, best throughput)
  - Good: Threading (simpler, good enough)
  - Bad: Sequential (too slow)

When CPU-bound (heavy computation):
  - Best: Multiprocessing (true parallelism)
  - Bad: Threading (GIL blocks it)
  - Bad: Async (doesn't help CPU)

When mixed (both I/O and CPU):
  - Consider: Async for I/O + Multiprocessing for CPU
  - Or: Multiprocessing for both if CPU dominates
  - Or: Threading if I/O dominates and CPU is light
```

---

## Key Concepts to Understand

1. **GIL (Global Interpreter Lock):** Only one thread can run Python bytecode at a time
2. **Threading:** Good for I/O (thread waits for I/O, others run), bad for CPU (GIL blocks)
3. **Multiprocessing:** Each process has own interpreter, true parallelism, but higher overhead
4. **Async/Await:** Single thread, very efficient I/O handling, not suitable for CPU
5. **Trade-offs:** Speedup vs Complexity vs Resource usage

---

## Testing Tips

- Use httpbin.org for simulated delays (`/delay/1` adds 1 second)
- Use loops or library to simulate CPU-intensive work
- Measure everything with `time.perf_counter()`
- Start with 10 tasks (URLs or files) for reasonable timing
- Compare your results to the expected speedups
- Try different worker pool sizes and observe effects

