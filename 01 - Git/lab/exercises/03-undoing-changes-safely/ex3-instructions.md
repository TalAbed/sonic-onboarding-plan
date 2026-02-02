# Exercise 3: Undoing Changes Safely - Instructions

Follow these steps to learn safe undo practices.

---

## Step 1: Create Exercise Branch

Create a branch for this exercise.

```bash
# Go to your lab branch first
git checkout lab/<your-name>/exercises

# Create exercise branch
git checkout -b lab/<your-name>/undo-practice
```

**Example**:
```bash
git checkout -b lab/alex/undo-practice
```

---

## Step 2: Create a Good Commit

First, make a legitimate commit so you have something good to reference later.

```bash
# Create a simple file
echo "# Production Configuration" > config.md

# Stage and commit
git add config.md
git commit -m "Add production configuration template"
```

**Verify**:
```bash
git log --oneline -1
# Should show: abc1234 Add production configuration template
```

---

## Step 3: Create the "Mistake" Commit

Now create a commit that we'll later undo (simulating a real mistake).

```bash
# Add a debug line to the config
echo "DEBUG: Admin password is Sonic2024!" >> config.md

# Stage and commit
git add config.md
git commit -m "Add admin credentials for testing"
```

**Verify**:
```bash
git log --oneline -2
# Should show your two commits, newest first
```

---

## Step 4: Realize the Mistake

Let's look at what you committed:

```bash
cat config.md
```

**You'll see**:
```
# Production Configuration
DEBUG: Admin password is Sonic2024!
```

Oh no! You accidentally committed a password to a shared repository! This is a security disaster. You need to undo it.

---

## Step 5: View Your Commit History

```bash
git log --oneline -3
```

**Output example**:
```
a1b2c3d Add admin credentials for testing  ← The one to undo
e2f3g4h Add production configuration template
initial Initial commit
```

Note the hash of the "bad" commit (`a1b2c3d` in the example). You'll use this in the next step.

---

## Step 6: Understand git revert vs git reset

Before undoing, understand your options:

### Option A: `git reset --hard` (Dangerous on shared branches)
```bash
git reset --hard e2f3g4h  # Deletes the bad commit from history
# Result: Commit a1b2c3d is gone like it never existed
# Problem: If others pulled it, their history conflicts with yours!
```

### Option B: `git revert` (Safe on shared branches)
```bash
git revert a1b2c3d  # Creates a NEW commit that undoes it
# Result: Commit a1b2c3d stays, plus new undo commit
# Benefit: History stays clean, others see what happened
```

**For this exercise** (and real shared work): Use `git revert`

---

## Step 7: Use git revert

Revert the bad commit:

```bash
git revert a1b2c3d
```

Replace `a1b2c3d` with your actual bad commit hash.

**What happens**: Git opens your editor to create a revert commit message.

**You'll see a message like**:
```
Revert "Add admin credentials for testing"

This reverts commit a1b2c3d7e8f9g0h1i2j3k4l5m6n7o8p9.
```

**Press Enter** or save to accept the message (Git provides a good default).

---

## Step 8: Verify the Revert

After the revert completes:

```bash
git status
```

**You should see**:
```
On branch lab/alex/undo-practice
nothing to commit, working tree clean
```

---

## Step 9: Check the File Contents

```bash
cat config.md
```

**Expected output**:
```
# Production Configuration
```

✅ The password line is gone!

---

## Step 10: Review Your History

```bash
git log --oneline -3
```

**Output example**:
```
b1c2d3e Revert "Add admin credentials for testing"
a1b2c3d Add admin credentials for testing
e2f3g4h Add production configuration template
```

**Notice**:
- ✅ The bad commit (`a1b2c3d`) is still in history
- ✅ A new revert commit (`b1c2d3e`) documents the fix
- ✅ Anyone reading history sees: "Here's what happened and how we fixed it"

**See what the revert commit changed**:

```bash
git show b1c2d3e
```

You'll see the revert removed the password line.

---

## Step 11: View the Revert Commit in Detail

```bash
git show HEAD
```

This shows you exactly what the revert commit did:

```
commit b1c2d3e...
Author: You <you@company.com>
Date: ...

    Revert "Add admin credentials for testing"
    
    This reverts commit a1b2c3d...

diff --git a/config.md b/config.md
index abc123...def456... 100644
--- a/config.md
+++ b/config.md
@@ -1,2 +1,1 @@
 # Production Configuration
-DEBUG: Admin password is Sonic2024!
```

The `-` line shows what was removed.

---

## Step 12: Push Your Work

```bash
git push origin lab/alex/undo-practice
```

**What this demonstrates**: You've safely shared the mistake AND the fix with your team.

---

## Step 13: Bonus - Understand git reset (for local work only)

To understand why `reset` is dangerous, let's try it on a local copy (don't push this):

```bash
# View your current commit
git log --oneline -1
# Shows the revert commit

# If you wanted to go back (locally only!) you could do:
git reset --hard HEAD~2
# This would go back 2 commits to before the mistake

# But DON'T push this! It rewrites shared history.
# Instead, use the push below to undo the reset:
git reset --hard b1c2d3e
# Go back to where you had the revert
```

**Key learning**: `reset --hard` changes history. On shared branches, this breaks other developers' repositories.

---

## Step 14: Understand git reflog (Emergency Recovery)

If you ever make a terrible mistake and want to recover:

```bash
git reflog
```

**Output shows every action**:
```
b1c2d3e HEAD@{0}: commit: Revert "Add admin credentials"
a1b2c3d HEAD@{1}: commit: Add admin credentials for testing
e2f3g4h HEAD@{2}: commit: Add production configuration
```

Even if you delete commits with `reset`, `reflog` remembers them for 30 days!

```bash
# Recover a deleted commit
git reset --hard HEAD@{1}
```

---

## You've Completed Exercise 3! 🎉

### What You Did

1. ✅ Created a "mistake" commit (simulating real error)
2. ✅ Identified the problematic commit using `git log`
3. ✅ Used `git revert` to safely undo it
4. ✅ Preserved history while fixing the problem
5. ✅ Understood why `reset --hard` is dangerous on shared branches
6. ✅ Learned `git reflog` for emergency recovery

### What This Means

You now know:
- **The safe way** to undo commits on shared branches (`git revert`)
- **When it's safe** to use `git reset --hard` (local work only)
- **How to protect your team** from history rewrites
- **How to recover** from almost any mistake

---

## Safety Rules to Remember

### ✅ SAFE - Use on shared branches:
```bash
git revert <hash>           # Safe, creates new commit
git push origin <branch>    # Normal push
```

### 🚨 DANGEROUS - Only on unpushed local commits:
```bash
git reset --hard <hash>     # Only before pushing!
git push --force            # Never do this to shared branches!
```

### 🆘 EMERGENCY:
```bash
git reflog                  # See all actions (30-day recovery window)
git reset --hard HEAD@{n}   # Recover from any mistake
```

---

## Real-World Scenarios

### Scenario 1: Oops, I committed a password!
```bash
git log --oneline
# Find the bad commit
git revert <bad-commit-hash>
git push origin <branch>
# Tell your team: "Found a security issue, check your configs"
```

### Scenario 2: I messed up locally before pushing
```bash
git reset --hard HEAD~1     # Go back 1 commit
# No push needed - no one has it yet
```

### Scenario 3: I deleted something accidentally 30 minutes ago
```bash
git reflog
# Find the commit you want
git reset --hard <commit-hash>
# You're recovered! 🎉
```

---

## Troubleshooting

### "I reverted but I'm not sure it worked"
```bash
git log --oneline -5  # View history
cat <filename>        # Check file contents
git show HEAD         # See exactly what last commit changed
```

### "I used reset --hard by accident on a shared branch"
```bash
# Tell your team immediately
# They need to update their local repositories
# Help them with: git pull origin <branch>
```

### "I can't find the commit I want to revert"
```bash
git log --all --oneline  # See all commits
git log -S "search-text" # Find commits containing text
git log --grep="keyword" # Find commits by message
```

---

## Summary

You've now completed all three Git Lab exercises! 🎉

**Exercise 1**: Basic workflow (branch → commit → push → MR)  
**Exercise 2**: Merge conflicts (resolve conflicts safely)  
**Exercise 3**: Undoing changes (safe practices for shared work)  

You're one step closer to be ready to work on real projects!

---

Great job! You've learned the core Git skills every professional needs. 🚀  
Time to move on to the next section - [Python]()
