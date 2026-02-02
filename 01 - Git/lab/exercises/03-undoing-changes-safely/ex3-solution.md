# Exercise 3: Undoing Changes Safely - Solution

This solution demonstrates the professional, safe way to undo commits on shared branches.

---

## Solution Overview

The workflow:

1. Create a "mistake" commit to simulate real scenarios
2. Identify the problematic commit using `git log`
3. Use `git revert` to safely undo it
4. Verify that history shows both the mistake and the fix
5. Understand when `reset` vs. `revert` is appropriate

---

## Step-by-Step Solution

### Steps 1-3: Create Test Commits

```bash
# Step 1: Create exercise branch
git checkout lab/alex/exercises
git checkout -b lab/alex/undo-practice

# Step 2: Create a good commit
echo "# Production Configuration" > config.md
git add config.md
git commit -m "Add production configuration template"

# Step 3: Create the "mistake" commit
echo "DEBUG: Admin password is Sonic2024!" >> config.md
git add config.md
git commit -m "Add admin credentials for testing"
```

**History now looks like**:
```
[Good Commit] → [Bad Commit with password]
```

---

### Step 4: Realize the Mistake

```bash
cat config.md
```

**Content**:
```
# Production Configuration
DEBUG: Admin password is Sonic2024!
```

**This is a security disaster**:
- ❌ Password is in version control
- ❌ All team members can see it
- ❌ It's in Git history permanently (unless we revert)
- ❌ It might be in backups too

---

### Step 5: Identify the Bad Commit

```bash
git log --oneline -3
```

**Output**:
```
a1b2c3d Add admin credentials for testing  ← This needs to be reverted
e2f3g4h Add production configuration template
initial Initial commit
```

**Key**: Note the hash of the bad commit (`a1b2c3d`).

---

### Step 6: Why NOT to Use git reset

**Dangerous approach** (don't do this on shared branches):

```bash
# This would "work" locally but break for others:
git reset --hard e2f3g4h
# History becomes: [Good Commit] only
# The bad commit is deleted from your local history
```

**Why this is bad**:
```
Your history:        [Good] → end
Others' history:     [Good] → [Bad] → continues...
Result: Massive merge conflicts when others push!
```

---

### Step 7: Use git revert (Safe)

```bash
git revert a1b2c3d
```

**What happens**:

1. Git opens your editor with a default message
2. The message shows what you're reverting
3. You confirm or edit, then save

**Default message**:
```
Revert "Add admin credentials for testing"

This reverts commit a1b2c3d7e8f9g0h1i2j3k4l5m6n7o8p9.
```

**Press Enter** to accept (or Ctrl+X, then Y to save if in vim).

---

### Step 8: Verify the Revert

```bash
git status
```

**Output**:
```
On branch lab/alex/undo-practice
nothing to commit, working tree clean
```

---

### Step 9: Check File Contents

```bash
cat config.md
```

**Output**:
```
# Production Configuration
```

✅ The password is gone!

---

### Step 10: Review the Safe History

```bash
git log --oneline -3
```

**Output**:
```
b1c2d3e Revert "Add admin credentials for testing"
a1b2c3d Add admin credentials for testing
e2f3g4h Add production configuration template
```

**Notice the benefits**:

```
Your history:        [Good] → [Bad] → [Revert] ✅
Others' history:     [Good] → [Bad] → [Revert] ✅
Result: Everyone syncs correctly, no conflicts!
```

---

### Step 11: See What the Revert Changed

```bash
git show HEAD
```

**Output** (simplified):
```
commit b1c2d3e...
Author: You <you@company.com>

    Revert "Add admin credentials for testing"
    
    This reverts commit a1b2c3d.

diff --git a/config.md b/config.md
index abc123..def456 100644
--- a/config.md
+++ b/config.md
@@ -1,2 +1,1 @@
 # Production Configuration
-DEBUG: Admin password is Sonic2024!
```

The `-` line shows what was removed.

---

### Step 12: Push Your Work

```bash
git push origin lab/alex/undo-practice
```

**Output**:
```
To https://gitlab.company.com/sonic/onboarding.git
 * [new branch]      lab/alex/undo-practice -> lab/alex/undo-practice
```

**What this shows**:
- ✅ Your team can see the mistake
- ✅ Your team can see how you fixed it
- ✅ No secret deletions or history rewrites
- ✅ Professional and transparent

---

## Deep Dive: Reset vs. Revert

### Scenario A: Local-Only Work

```bash
git log --oneline -3
# abc1234 Bad commit (not pushed yet)
# def5678 Good commit
# ghi9012 Initial

# Safe to use reset (no one has abc1234 yet)
git reset --hard def5678
# History: [Initial] → [Good] only
```

✅ This is safe because no one pulled the bad commit yet.

### Scenario B: Shared Branch (This Exercise)

```bash
git log --oneline -3
# a1b2c3d Bad commit (already pushed)
# e2f3g4h Good commit
# initial Initial

# MUST use revert (others already have a1b2c3d)
git revert a1b2c3d
# Creates commit b1c2d3e that undoes it
# History: [Initial] → [Good] → [Bad] → [Undo]
```

✅ Everyone can `pull` and get the fix without confusion.

---

## Understanding git reflog

If you ever accidentally delete something:

```bash
git reflog
```

**Output**:
```
b1c2d3e HEAD@{0}: commit: Revert "Add admin credentials"
a1b2c3d HEAD@{1}: commit: Add admin credentials for testing
e2f3g4h HEAD@{2}: commit: Add production configuration
```

**What this shows**: Every action Git has taken.

**Recover from a mistake**:
```bash
# If you accidentally deleted important work
git reset --hard HEAD@{n}  # Where n is the entry number
```

**Example**:
```bash
# If you did reset --hard and want to undo it:
git reset --hard HEAD@{1}
# Gets you back to the commit before the reset
```

---

## Real-World Examples

### Example 1: Accidentally Committed Secrets

```bash
# Current state: You pushed a commit with API keys
git log --oneline -3
# abc1234 Add database credentials  ← BAD
# def5678 Add database setup
# ghi9012 Initial

# Safe fix on shared branch
git revert abc1234
# Creates new commit that removes the credentials
# Team can pull safely

# Also do this:
git push origin <branch>  # Normal push, no force!
# Tell the team: "Rotate all database credentials"
```

### Example 2: Logic Error Before Pushing

```bash
# Commits not yet pushed
git log --oneline -3
# abc1234 Fixed bug (but made logic error)
# def5678 Previous work
# ghi9012 Initial

# Safe fix (not on shared branch yet)
git reset --hard def5678
# Delete the bad commit locally
# Re-do the fix correctly
# Then push when ready
```

### Example 3: Merge Mistake

```bash
# You merged a bad branch into main
git log --oneline -3
# abc1234 Merge feature-x (broke production!)
# def5678 Good commit
# ghi9012 Initial

# Safe fix
git revert abc1234 -m 1
# -m 1 says "keep the first parent" (the main branch)
# Creates commit that undoes the merge
git push origin main
```

---

## Safety Checklist

### Before Using `git reset --hard`:

- [ ] Is this a local-only commit (not yet pushed)?
- [ ] Have you confirmed no one else has this commit?
- [ ] Have you backed up important work elsewhere?

### Before Pushing Any Changes to Shared Branches:

- [ ] Is the fix appropriate for a shared branch?
- [ ] Have you tested the fix works?
- [ ] Have you told your team about the issue?

---

## Key Learnings

### 1. History is Sacred

Once you push commits, don't delete them with `reset`. Your teammates depend on that history being stable.

### 2. Revert is Professional

Using `git revert` shows:
- ✅ You made a mistake (human, normal, fine)
- ✅ You fixed it thoughtfully (professional)
- ✅ You documented it (transparent)

### 3. Reset is Dangerous

Using `git reset --hard` on shared work shows:
- ❌ You deleted history (broke teammates)
- ❌ You hid the mistake (deceptive)
- ❌ You caused merge conflicts (harmful)

### 4. There's Always Recovery

Even if you make a terrible mistake:
- `git reflog` keeps records for 30 days
- You can always recover
- Git is designed to be safe

---

## Summary

You successfully:

1. ✅ Created a realistic "mistake" scenario
2. ✅ Identified the problematic commit
3. ✅ Used `git revert` to safely undo it
4. ✅ Preserved full history (everyone sees what happened)
5. ✅ Pushed the fix safely
6. ✅ Learned when to use `reset` vs. `revert`
7. ✅ Learned emergency recovery with `reflog`

---

## All Three Exercises Complete! 🎉

**Exercise 1**: Basic workflow ✅  
**Exercise 2**: Conflict resolution ✅  
**Exercise 3**: Safe undo practices ✅  

You now have professional-level Git knowledge!

---

## Next Steps

1. ✅ Review this solution
2. ✅ Make sure all concepts are clear
3. ✅ Update `../PROGRESS.md` as fully complete
4. ✅ Share your completion with your team lead
5. ✅ You're ready for real Sonic projects!

---

## Questions?

These concepts are deep and important. If anything is unclear:
- Ask your team lead
- Share this scenario with teammates
- Discuss real mistakes you've all encountered

Great job mastering Git safety practices! 🚀
