# Exercise 2: Merge Conflict Resolution

## Overview

This is where Git gets "real." In Exercise 1, you had a linear, conflict-free workflow. But on a real team, multiple developers work on the same files simultaneously. When those changes intersect, Git can't automatically merge them—you get a **merge conflict**.

This exercise teaches you how to handle conflicts gracefully and safely. It's intermediate-level because conflicts require you to think critically about what code should be kept.

**This is essential knowledge.** Every developer faces conflicts regularly, and knowing how to resolve them safely is a core professional skill.

---

## Learning Objectives

By the end of this exercise, you will be able to:

✅ Understand what causes merge conflicts  
✅ Recognize conflict markers in files  
✅ Resolve conflicts using Git commands (not manual file editing)  
✅ Handle merge conflicts safely on shared branches  
✅ Use `git fetch`, `git merge`, and `git rebase` effectively  
✅ Know when to ask for help resolving conflicts  

---

## What You'll Practice

| Skill | Command(s) |
|-------|-----------|
| Fetching updates | `git fetch` |
| Merging branches | `git merge` |
| Handling conflicts | Manual conflict resolution |
| Adding resolved files | `git add` |
| Completing merge | `git commit` |
| Viewing differences | `git diff` |

---

## The Scenario

Imagine two Sonic developers are working on the same documentation file (a `changelog.md`) at the same time:

- **Developer A** adds a change on branch `lab/alex/changelog-v1`
- **Developer B** adds a different change to the same lines on branch `lab/jamie/changelog-v2`

When one of them tries to merge their work into `main`, Git finds the conflict: "I can't decide whose change to keep—you tell me!"

You'll simulate this scenario by:
1. Creating two branches from main
2. Having each branch modify the same file differently
3. Attempting to merge one branch (triggering conflict)
4. Resolving the conflict by choosing which changes to keep
5. Completing the merge successfully

---

## What You'll Modify

**File**: `changelog.md`

This is a fictional changelog tracking Sonic project updates. You'll modify it on two different branches to create a real conflict.

---

## Difficulty & Time

**Difficulty**: Intermediate  
**Estimated Time**: ~20 minutes  
**Prerequisites**: Completed Exercise 1, understands branching and commits  

---

## Important Concepts

### What Causes Conflicts?

Conflicts happen when:
1. Two branches modify the **same lines** in the **same file**
2. Git can't automatically merge (unlike when you modify different files or different sections)

### Conflict Markers

When Git detects a conflict, it marks the problem area in the file:

```
<<<<<<< HEAD
Your current changes here
=======
Incoming changes here
>>>>>>> branch-name
```

- `<<<<<<< HEAD` = start of your current branch's changes
- `=======` = divider between the two versions
- `>>>>>>> branch-name` = end of incoming branch's changes

### Safe Conflict Resolution

✅ **Safe approach**: Use Git commands to understand conflicts, then edit the file intentionally  
❌ **Unsafe approach**: Blindly delete conflict markers without understanding  

---

## Getting Started

Ready? Open [ex2-instructions.md](./ex2-instructions.md) and follow the steps carefully.

After completing the exercise, check your work against [ex2-solution.md](./ex2-solution.md).

---

## Key Concepts Reinforced

1. **Collaboration challenges**: Real teams face these constantly
2. **Conflict investigation**: Using `git diff` and `git status` to understand conflicts
3. **Thoughtful resolution**: Deciding which changes to keep
4. **Safe practices**: Ensuring merges don't lose important code

---

## Success Criteria

You'll know you've completed this exercise successfully when:

✅ You've created two branches with conflicting changes  
✅ You've triggered a real merge conflict  
✅ You've resolved the conflict by editing the file  
✅ You've completed the merge with a clear commit message  
✅ The resolved version contains the changes you intended  
✅ You understand why the conflict happened  

---

## Reflection Questions

After completing this exercise, ask yourself:

1. What caused the conflict?
2. How did Git mark the conflicting sections?
3. Could you resolve this conflict on a real team project?
4. When would you ask a teammate for help resolving a conflict?
5. Why is communication important during merge conflicts?

---

Good luck! This is challenging exercise but essential one 🚀