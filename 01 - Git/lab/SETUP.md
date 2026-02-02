# Git Lab - Setup Guide

Before you start any exercises, follow this setup guide to prepare your environment. This should take about 10 minutes.

## Prerequisites

Make sure you have:
- ✅ Git installed on your machine (`git --version` should show version 2.20+)
- ✅ Access to the Sonic onboarding GitLab repository
- ✅ A text editor or IDE (VS Code or Pycharm)

---

## Step 1: Clone the Onboarding Repository

The Git Lab lives in the team's onboarding repository. Clone it to your local machine:

```bash
git clone https://gitlab.com/sonic2791202/sonic-onboarding.git
```

**What this does**: Downloads a complete copy of the Sonic onboarding materials, including the Git lab exercises.

---

## Step 2: Create Your Lab Branch

Before starting any exercises, create a personal branch for your lab work. This keeps your exercises separate from the main branch and lets you practice branching and pushing.

```bash
# Make sure you're on the main branch
git checkout main

# Update to latest version
git pull origin main

# Create your personal lab branch
git checkout -b lab/<your-name>/exercises
```

**Branch naming convention**: `lab/<your-name>/<exercise-name>`

**What this does**: Creates a new branch where you'll do all your lab work without affecting the main branch.

---

## Step 3: Navigate to the Lab Directory

```bash
cd 01 - Git/lab
```

You should now see:
- `README.md` – Overview and exercise descriptions
- `SETUP.md` – This file
- `PROGRESS.md` – Checklist for tracking your progress
- `exercises/` – Folder containing all three exercises

---

## Step 4: Verify Your Setup

Run this command to confirm everything is ready:

```bash
git status
```

You should see output like:
```
On branch lab/alex/exercises
nothing to commit, working tree clean
```

**What this means**: Your branch is created and ready, and you have a clean working directory with no uncommitted changes.

---

## Step 5: Understand the Exercise Structure

Each exercise folder is organized like this:

```
exercises/
└── 01-first-merge-request/
    ├── README.md (what you're learning & why)
    ├── instructions.md (step-by-step walkthrough)
    ├── solution.md (reference solution)
    └── [starter files if needed]
```

---

## Step 6: Ready to Start!

You're all set! Here's your workflow for each exercise:

1. **Read** the exercise `README.md` to understand the learning objectives
2. **Follow** the `instructions.md` step-by-step
3. **Check** your work against `solution.md`
4. **Commit** your work with a meaningful message
5. **Track** your progress in `PROGRESS.md`

---

## Important: How to Commit Your Lab Work

After each exercise, commit your progress:

```bash
# Stage your changes
git add .

# Commit with a clear message
git commit -m "Complete exercise 1: First Merge Request"

# Push to your lab branch
git push origin lab/<your-name>/exercises
```

**Why this matters**: You're practicing the Git workflow you'll use every day on Sonic. Meaningful commit messages and clean branches are part of our team culture.

---

## If You Need to Reset an Exercise

If you make a mistake during an exercise and want to start over:

```bash
# See your recent commits
git log --oneline -5

# If you haven't pushed yet, you can reset (local only!)
git reset --hard HEAD~1

# If you already pushed, use revert instead (safer)
git revert HEAD
git push origin lab/<your-name>/exercises
```

**Remember**: `git reset --hard` erases commits. Only use it on your personal branch before pushing. Once pushed, use `git revert` instead.

---

## Troubleshooting Setup Issues

### "fatal: destination path 'onboarding' already exists"
You already have the repo cloned. Navigate to it:
```bash
cd ~/path/to/onboarding/git
```

### "error: Your local changes would be overwritten by checkout"
You have uncommitted changes. Either:
```bash
# Commit them
git add .
git commit -m "WIP: lab setup"

# Or discard them (careful!)
git checkout -- .
```

### "Not a git repository"
Make sure you're in the right directory and the `.git` folder exists:
```bash
pwd  # See where you are
ls -la  # Check for .git folder
```

---

## Setup Checklist

Use this checklist to verify you're ready:

- [ ] Git is installed and version 2.20+
- [ ] Git is configured with your name and email
- [ ] You have access to the Sonic onboarding GitLab repository
- [ ] You've cloned the onboarding repo locally
- [ ] You've created your `lab/<your-name>/exercises` branch
- [ ] You're in the `sonic-git-lab/` directory
- [ ] `git status` shows your branch is clean
- [ ] You can see the `exercises/` folder and understand its structure

If all boxes are checked, you're ready to start! 🎉

---

## Next Steps

1. Complete this setup
2. If needed open [README.md](./README.md) once again to understand the lab structure
3. Start with [Exercise 1](./exercises/01-first-merge-request/)

Good luck, and enjoy the learning process! 🚀
