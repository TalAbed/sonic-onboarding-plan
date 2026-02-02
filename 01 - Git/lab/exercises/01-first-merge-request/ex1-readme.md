# Exercise 1: First Merge Request

## Overview

Welcome to your first Git exercise! In this exercise, you'll complete the entire Git workflow that you'll use every day on the team: create a branch, make changes, commit, push, and submit a merge request.

This is a beginner-level exercise that focuses on getting comfortable with the foundational workflow. There are no tricks or gotchas—just straightforward practice of the commands you learned.

---

## Learning Objectives

By the end of this exercise, you will be able to:

✅ Create a feature branch  
✅ Make changes to files and stage them  
✅ Commit changes with a meaningful message  
✅ Push your branch to GitLab  
✅ Understand the complete cycle: branch → commit → push → merge request  

---

## What You'll Practice

| Skill | Command(s) |
|-------|-----------|
| Creating branches | `git checkout -b` or `git switch -c` |
| Checking status | `git status` |
| Staging changes | `git add` |
| Committing changes | `git commit -m` |
| Pushing to remote | `git push origin` |
| Viewing history | `git log --oneline` |

---

## The Scenario

Imagine you're joining the Sonic team. Part of the onboarding process is to introduce yourself to the team by adding your information to a shared developer list. You'll:

1. Create a feature branch
2. Edit a file to add your information
3. Commit your changes
4. Push to GitLab
5. Submit a merge request so the team can review and approve your work

This is exactly how real work flows on Sonic - every feature, bug fix, or documentation update follows this same path.

---

## File You'll Modify

**File**: `DEVELOPERS.md` (can be found in the exercise directory)

This file contains a list of team members. You'll add your name and a brief introduction.

**Current state**: The file exists with a few team members already listed.

---

## Difficulty & Time

**Difficulty**: Beginner  
**Estimated Time**: ~10 minutes  
**Prerequisites**: Git installed, configured, and cloned onboarding repo

---

## Getting Started

Ready? Open [instructions.md](./instructions.md) and follow each step carefully.

After completing the instructions, check your work against [solution.md](./solution.md).

---

## Key Concepts Reinforced

1. **Branching**: Isolating your work from the main branch
2. **Staging & Committing**: Taking snapshots of your changes
3. **Pushing**: Sharing your work with the team
4. **Merge Requests**: The formal process for code review and approval

---

## Success Criteria

You'll know you've completed this exercise successfully when:

✅ You've created a branch named `lab/<your-name>/introduce-yourself`  
✅ You've added your name to `DEVELOPERS.md`  
✅ You've committed with a clear message  
✅ You've pushed to your branch  
✅ Your branch is visible in GitLab  

---

## Reflection Questions

After completing this exercise, ask yourself:

1. What does each command do and why is it needed?
2. Could you explain this workflow to a teammate?
3. How would you use this workflow on a real feature?
4. What's the purpose of having a branch instead of working on `main` directly?

---

## Next Steps

1. Read [instructions.md](./ex1-instructions.md)
2. Complete all steps
3. Review [solution.md](./ex1-solution.md) to compare approaches
4. Update your progress in `../PROGRESS.md`
5. Move on to Exercise 2

Good luck! 🚀
