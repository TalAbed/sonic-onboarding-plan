# Exercise 3: Undoing Changes Safely

## Overview

We all make mistakes. You commit something you shouldn't have. You push the wrong branch. You realize a commit was wrong after merging to main.

Git offers several ways to undo changes, but **choosing the right method is critical**. Using the wrong command can accidentally delete code or break your team's history.

This exercise teaches you the safe, professional way to undo changes. This is essential knowledge because:

1. **You will make mistakes** (everyone does)
2. **Your safety practices protect the team**
3. **Using the right command is the difference between "oops, fixed!" and "we lost production code"**

---

## Learning Objectives

By the end of this exercise, you will be able to:

✅ Understand the difference between `git revert` and `git reset`  
✅ Know when to use each command  
✅ Safely undo commits on shared branches using `git revert`  
✅ Use `git revert` for shared work  
✅ Use `git reset` safely for local-only work  
✅ Navigate commit history using `git log` and commit hashes  
✅ Recover from mistakes using `git reflog`  

---

## What You'll Practice

| Skill | Command(s) |
|-------|-----------|
| Viewing history | `git log --oneline` |
| Finding commits | `git show <hash>` |
| Safe undo (shared) | `git revert <hash>` |
| Unsafe undo (local) | `git reset --hard <hash>` |
| Emergency recovery | `git reflog` |

---

## The Scenario

Imagine you commit something to a shared branch that you later realize was wrong:

- You added a debug line that you shouldn't have pushed
- You accidentally committed a config file with secrets
- You made a logic error that breaks other features
- You realize your change was based on misunderstanding

**The wrong approach**: `git reset --hard` to delete the commit from history
- ❌ Breaks other developers' work
- ❌ Rewrites shared history
- ❌ Causes confusion and merge conflicts
- ❌ Never use on shared branches!

**The right approach**: `git revert` to create a new commit that undoes the changes
- ✅ Preserves history (everyone can see what happened)
- ✅ Doesn't break others' work
- ✅ Safe on shared branches
- ✅ Professional and transparent

In this exercise, you'll practice `git revert` on a shared scenario.

---

## The Comparison: Reset vs. Revert

### `git reset --hard` (Destructive)

```
History: [Commit A] → [Commit B] → [Commit C] ← wrong!
         [Commit A] → [Commit B]  (C is deleted!)
```

- ❌ Deletes commits from history
- ❌ Breaks other developers' work
- ❌ Only use for **unpushed, local work**
- ❌ Never use on shared branches

### `git revert` (Safe)

```
History: [Commit A] → [Commit B] → [Commit C] ← wrong!
         [Commit A] → [Commit B] → [Commit C] → [Commit D] ← undoes C
```

- ✅ Preserves all history
- ✅ Creates new commit that undoes changes
- ✅ Safe on shared branches
- ✅ Professional and traceable

---

## Difficulty & Time

**Difficulty**: Intermediate  
**Estimated Time**: ~15 minutes  
**Prerequisites**: Completed Exercises 1 & 2, understands commits and history  

---

## Getting Started

Ready? Open [instructions](./ex3-instructions.md) and follow the steps.

After completing, check your work against [solution](./ex3-solution.md).

---

## Key Concepts Reinforced

1. **Git History is Sacred**: Once pushed, don't rewrite it
2. **Transparency Over Deletion**: Show what happened, don't hide it
3. **Professional Practices**: Use safe commands on shared work
4. **Recovery Options**: Git offers ways to fix almost any mistake

---

## Success Criteria

You'll know you've completed this exercise successfully when:

✅ You've created a commit with a mistake  
✅ You've used `git log` to find the problematic commit  
✅ You've used `git revert` to safely undo it  
✅ History shows both the mistake and the fix  
✅ You understand when to use `revert` vs. `reset`  

---

## Reflection Questions

After completing this exercise, ask yourself:

1. What's the difference between `git revert` and `git reset --hard`?
2. When would each be appropriate?
3. Why is `git reset` dangerous on shared branches?
4. How would you explain this safety practice to a new team member?
5. What would you do if you accidentally pushed bad code?

---

## Critical Safety Rules

### 🚨 NEVER do this on shared branches:
```bash
git reset --hard  # Only for unpushed local work!
git push --force  # Rewrites team history!
```

### ✅ DO this on shared branches:
```bash
git revert <commit>  # Safe, creates new commit
git push origin      # Normal push, no force
```

---

## Next Steps

1. Read [instructions](./ex3-instructions.md)
2. Complete all steps carefully
3. Review [solution](./ex3-solution.md) to compare 
4. You'll have completed all three exercises! 🎉

### Good luck! 🚀