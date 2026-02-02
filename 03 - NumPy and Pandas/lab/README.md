# NumPy & Pandas Lab

Welcome to the NumPy and pandas hands-on lab! This is where you apply everything you've learned from the reference guides and videos to solve real data engineering problems.

## What You'll Build

This lab contains **3 practical exercises** that simulate real work you'll do at Sonic:

1. **Exercise 1: Event Metrics Processing with NumPy**
   - Process 1,000 event latencies from the pipeline
   - Calculate statistics and identify performance issues
   - Detect anomalies using statistical methods
   - Compare NumPy performance vs Python loops

2. **Exercise 2: Event Data Cleaning with Pandas**
   - Load messy, real-world event data from CSV
   - Clean and validate the dataset
   - Handle missing values and duplicates
   - Answer business questions about event patterns

3. **Exercise 3: Building an Event Performance Dashboard**
   - Load and merge two datasets (events + users)
   - Engineer meaningful features
   - Perform complex analysis by user tier, event type, and time
   - Export results for dashboarding

## Prerequisites

✅ **Completed Python Fundamentals Lab** (Exercises 1-4)  
✅ **Watched NumPy video** (~1 hour)  
✅ **Watched pandas video** (~1.5 hours)   
✅ **Python 3.8+** with NumPy and pandas installed  

## Why These Exercises Matter

Real data engineering is about moving and transforming data efficiently. These exercises teach you:

- **NumPy**: How to process numerical data at scale
- **pandas**: How to handle real-world, messy data
- **Integration**: How to combine these tools in workflows
- **Business Value**: How your code solves actual problems

**80% of data engineering is data cleaning and aggregation.** These exercises teach production-grade patterns you'll use constantly.

## Learning Path

Follow this order:

```
Read reference guides
         ↓
Exercise 1: NumPy focus (arrays, filtering, stats)
         ↓
Exercise 2: pandas focus (loading, cleaning, groupby)
         ↓
Exercise 3: Integration (merging, analysis, dashboards)
```

## How to Work Through Each Exercise

### For Each Exercise:

1. **Read the Exercise README** - Understand the scenario and business context
2. **Review Instructions** - Follow step-by-step guidance without looking at solutions
3. **Try the Implementation** - Write your own code and test it
4. **Check Your Work** - Compare with the reference solution
5. **Reflect** - Understand why the solution works that way
6. **Experiment** - Try variations and edge cases

### Tips for Success

✅ **Don't skip the instructions** - They teach you the right approach  
✅ **Try before looking at solutions** - The struggle builds understanding  
✅ **Use reference guides frequently** - That's what they're for  
✅ **Ask questions** - Your team can help you   
✅ **Experiment with the data** - See what breaks and why  

## Time Commitment

| Exercise | Duration | Effort |
|----------|----------|--------|
| **Exercise 1** | 30-40 min | Medium |
| **Exercise 2** | 50-60 min | Medium-High |
| **Exercise 3** | 50-60 min | High |
| **Total** | 2-3 hours | Substantial |

This is a serious time investment, but the skills pay off for years.

## Lab Structure

```
sonic-numpy-pandas-lab/
├── README.md                          (this file)
├── SETUP.md                           (installation & setup)
│
└── exercises/
    │
    ├── 01-event-metrics-numpy/
    │   ├── README.md                  (exercise overview)
    │   ├── instructions.md            (step-by-step guide)
    │   ├── solution.md                (reference solution)
    │   └── sample_data.py             (data generator)
    │
    ├── 02-event-cleaning-pandas/
    │   ├── README.md                  (exercise overview)
    │   ├── instructions.md            (step-by-step guide)
    │   ├── solution.md                (reference solution)
    │   └── events_raw.csv             (messy sample data)
    │
    └── 03-dashboard-analysis/
        ├── README.md                  (exercise overview)
        ├── instructions.md            (step-by-step guide)
        ├── solution.md                (reference solution)
        ├── events_data.csv            (clean event data)
        └── users_data.csv             (user metadata)
```

## What Success Looks Like

After completing this lab:

✅ **Exercise 1**: You can process arrays, filter data, calculate statistics, and find anomalies  
✅ **Exercise 2**: You can load, clean, and explore real datasets  
✅ **Exercise 3**: You can merge datasets, engineer features, and create comprehensive analyses  

More importantly:
- ✅ You understand NumPy and pandas deeply
- ✅ You can solve real data problems
- ✅ You're ready to work on actual Sonic pipelines
- ✅ You have code patterns you'll reuse constantly

## Important Notes

### On Solutions

- Multiple valid solutions exist for each exercise
- Your approach may differ from the reference solution
- As long as your code works and is understandable, it's valid
- Read the reference solution to learn different approaches

### On Data

- Exercise 1 uses generated data (realistic but synthetic)
- Exercise 2 uses messy CSV with intentional problems
- Exercise 3 uses real multi-table scenario
- **Don't modify raw data files** - copy them if you need to experiment

### On Code Quality

- Write comments explaining your logic
- Use descriptive variable names
- Follow pandas naming conventions (`df` for DataFrames, `s` for Series)
- Make your code readable for future you

### On Performance

- Don't worry about optimization
- Correctness > Speed for learning
- After mastery, then optimize
- NumPy/pandas often beat hand-written code anyway

## Key Principle

**Real data engineering is about solving problems with data.** NumPy and pandas are just tools. What matters is:

1. Understanding your data
2. Asking the right questions
3. Using the right tools efficiently
4. Delivering useful answers

These exercises teach all four.

---

## Ready?

When you're ready to start:

1. ✅ Review [SETUP.md](./SETUP.md) to ensure your environment is ready
2. ✅ Navigate to [Exercise 1](./exercises/01-event-metrics-numpy) to start practice
3. ✅ Read that exercise's README
4. ✅ Follow the instructions
5. ✅ Build something amazing!

**Good luck, and welcome to real data engineering!** 🚀📊

Questions? Ask your team. We're all learning together.
