# Sonic Git Lab

Welcome to the Git Lab! This is where theory meets practice. You've learned what Git is and reviewed the commands - now it's time to apply your knowledge in a real-world workflow.

## What is the Git Lab?

The Git Lab is a series of hands-on exercises designed to bridge the gap between understanding Git concepts and using Git effectively. Each exercise simulates real scenarios you'll encounter while working on our real-time data processing pipelines.

All exercises take place in this safe sandbox environment so there is no risk to production code, only learning and growth.

## Exercises Overview

| # | Exercise | Difficulty | Time | Skills Tested |
|---|----------|-----------|------|---------------|
| 1 | [First Merge Request](#exercise-1-first-merge-request) | Beginner | ~15 min | Basic workflow, branching, pushing, merge requests |
| 2 | [Merge Conflict Resolution](#exercise-2-merge-conflict-resolution) | Intermediate | ~20 min | Conflict resolution, rebasing, collaborative workflows |
| 3 | [Undoing Changes Safely](#exercise-3-undoing-changes-safely) | Intermediate | ~15 min | Reverting commits, safe undo practices, commit history |

**Total Lab Time**: ~50 minutes  
**Recommended**: Complete in order, one exercise per session

---

## Before You Start

Make sure you've completed:
- ✅ Watched the [Git Tutorial for Beginners video](../README.md)
- ✅ Reviewed the [Basic Git Commands guide](../basic-git-commands.md)
- ✅ Have Git installed and configured on your machine

Then, follow the [SETUP.md](./SETUP.md) guide to prepare your environment.

---

## Exercise 1: First Merge Request

**Difficulty**: Beginner  
**Time**: ~15 minutes  
**Location**: [01-first-merge-request/](./exercises/01-first-merge-request/)

**What You'll Learn**:
- How to use Git for collaboration
- The complete workflow: branch → commit → push → merge request
- Best practices for branch naming
- How to submit code via GitLab merge requests

**Skills Tested**:
- `git clone`
- `git checkout -b` / `git switch -c`
- `git add` and `git commit`
- `git push`
- GitLab merge request creation and approval

---

## Exercise 2: Merge Conflict Resolution

**Difficulty**: Intermediate  
**Time**: ~20 minutes  
**Location**: [02-merge-conflict-resolution/](./exercises/02-merge-conflict-resolution/)

**What You'll Learn**:
- What causes merge conflicts and why they happen
- How to safely resolve conflicts without losing code
- Strategies for preventing conflicts through communication
- How to handle conflicts on shared branches

**Skills Tested**:
- `git fetch`
- `git merge` and `git rebase`
- Understanding and resolving conflicts
- `git add` during merge resolution
- `git log` to understand history

**Note**: This exercise is more challenging because it simulates real team scenarios. Take your time and ask questions if needed.

---

## Exercise 3: Undoing Changes Safely

**Difficulty**: Intermediate  
**Time**: ~15 minutes  
**Location**: [03-undoing-changes-safely/](./exercises/03-undoing-changes-safely/)

**What You'll Learn**:
- The difference between `git revert` and `git reset`
- Why `git reset --hard` is dangerous on shared branches
- Safe ways to undo commits without breaking team collaboration
- When to use each undo strategy

**Skills Tested**:
- `git log` and commit navigation
- `git revert` (safe, creates new commit)
- `git reset` (destructive, for local work only)
- `git reflog` for emergency recovery
- Understanding commit history

**Critical**: This exercise teaches safety practices that protect your team's code. Pay special attention to when each command is appropriate.

---

## How to Complete Each Exercise

### Step 1: Read the Exercise README
Each exercise folder has a README file that explains:
- Learning objectives
- What you'll be practicing
- Any special setup needed

### Step 2: Follow the Instructions
Open `instructions.md` and work through each step carefully. The instructions are written to be clear and step-by-step.

### Step 3: Check Your Work
After completing, compare your work against `solution.md`. This is a reference solution showing one way to complete the exercise. Your approach might differ slightly—that's okay! What matters is understanding the concepts.

### Step 4: Reflect
Ask yourself:
- Do I understand why each command worked?
- Could I explain this exercise to a teammate?
- Where did I get stuck, and what helped me understand?

---

## Submission & Progress Tracking

### Optional: Submit as Merge Request
If you want feedback from your buddy:
1. Complete an exercise
2. Create a merge request from your lab branch to `main` with the label `lab-exercise`
3. Your buddy will review and provide feedback
4. You can iterate and learn from their comments

This is especially useful for exercises 2 and 3, where getting feedback on your approach is valuable.

---

## Getting Unstuck

**If you're stuck**:
1. Re-read the instructions and the related section in `basic-git-commands.md`
2. Check the solution file to see how it should look
3. Use `git status` and `git log` to understand your current state
4. Ask your buddy or any other team member - we are all here for you!

**If you made a mistake**:
- Don't panic! Git is designed to be recoverable
- Check `git reflog` to see your command history
- Your buddy can help you recover
- Use this as a learning opportunity

---

## Questions or Feedback?

Found a typo in the exercises? Think an exercise could be clearer? Have a suggestion for a new exercise?

Please let us know. Continuous improvement of our onboarding is a team effort!

---

**Ready to start?** Go to [SETUP.md](./SETUP.md) and follow the environment setup steps.

**Good Luck!**
