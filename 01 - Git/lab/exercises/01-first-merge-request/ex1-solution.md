# Exercise 1: First Merge Request - Solution

This is the reference solution for Exercise 1. Compare your approach with this to see if you missed anything or did something differently.

**Note**: There's often more than one way to accomplish a task in Git. If your approach is different but achieves the same result, that's perfectly fine!

---

## Solution Overview

The complete workflow for this exercise:

1. Create an exercise-specific branch from your lab branch
2. Edit DEVELOPERS.md to add your information
3. Stage the changes
4. Commit with a meaningful message
5. Push to GitLab
6. Verify in GitLab

---

## Step-by-Step Solution

### Step 1: Create Exercise Branch

```bash
git checkout -b lab/tal/introduce-yourself
```

**Why this approach**:
- `git checkout -b` creates AND switches to the new branch in one command
- The branch name follows Sonic conventions: `lab/<name>/<exercise-name>`
- Creating a separate branch for each exercise simulates real feature development

**Alternative (modern syntax)**:
```bash
git switch -c lab/tal/introduce-yourself
```

---

### Step 2: Verify Branch Creation

```bash
git status
```

**Expected output**:
```
On branch lab/tal/introduce-yourself
nothing to commit, working tree clean
```

---

### Step 3: Edit DEVELOPERS.md

Open the file:
```bash
code DEVELOPERS.md
```

**Add your entry** following this format (add it at the end, before the closing of the file):

```markdown
### Tal
- **Name**: Tal Abed
- **Role**: Data Engineer Team Leader
- **Focus**: Real-time pipeline optimization
- **Fun Fact**: I completed 70% of the Grizzler archive (but it got deleted 😢)
```

**Important notes**:
- Keep the format consistent with existing entries
- Use markdown formatting (bold with `**`)
- Don't forget to save the file

---

### Step 4: Verify Changes

```bash
git status
```

**Expected output**:
```
On branch lab/tal/introduce-yourself
Changes not staged for commit:
  (use "git add <file>..." to stage changes)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   DEVELOPERS.md

no changes added to commit but untracked files present (use "git add" to track)
```

**View the exact changes**:
```bash
git diff DEVELOPERS.md
```

**Expected output** (simplified):
```
diff --git a/DEVELOPERS.md b/DEVELOPERS.md
index abc1234..def5678 100644
--- a/DEVELOPERS.md
+++ b/DEVELOPERS.md
@@ -12,3 +12,9 @@ Welcome to the Sonic team! This file lists our amazing developers.
 - **Fun Fact**: Gotta go fast! ⚡
 
+### tal Johnson
+- **Name**: tal Johnson
+- **Role**: Data Engineer
+- **Focus**: Real-time pipeline optimization
+- **Fun Fact**: Coffee enthusiast and basketball fan! 🏀
```

Notice the `+` signs indicating additions.

---

### Step 5: Stage Changes

```bash
git add DEVELOPERS.md
```

**Or stage all changes** (works if only modifying one file):
```bash
git add .
```

**Verify staging**:
```bash
git status
```

**Expected output**:
```
On branch lab/tal/introduce-yourself
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   DEVELOPERS.md
```

Notice the file is now green (if using colored terminal output) and under "Changes to be committed".

---

### Step 6: Commit Changes

```bash
git commit -m "Add tal to developers list"
```

**Why this message**:
- ✅ Imperative mood: "Add" not "Added"
- ✅ Clear and descriptive: Says what and who
- ✅ Concise: Fits in one line
- ✅ Specific: "Add tal" not just "Update file"

**Alternative good messages**:
- "Introduce tal to Sonic team"
- "Add tal to developers documentation"

**Less ideal messages**:
- ❌ "Update" (too vague)
- ❌ "Add user" (not specific about who)
- ❌ "Added tal to developers list" (past tense, not imperative)

**Verify commit**:
```bash
git log --oneline -2
```

**Expected output**:
```
a1b2c3d Add tal to developers list
x9y8z7w Initial commit
```

---

### Step 7: Push to GitLab

```bash
git push origin lab/tal/introduce-yourself
```

**Break this down**:
- `git push` = send commits to remote
- `origin` = the remote repository name (GitLab)
- `lab/tal/introduce-yourself` = your branch name

**Expected output**:
```
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 356 bytes | 356.00 KiB/s, done.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Create a merge request for 'lab/tal/introduce-yourself' on GitLab by visiting:
remote:  https://gitlab.company.com/sonic/onboarding/-/merge_requests/new?merge_request%5Bsource_branch%5D=lab%2Ftal%2Fintroduce-yourself
remote:
To https://gitlab.company.com/sonic/onboarding.git
 * [new branch]      lab/tal/introduce-yourself -> lab/tal/introduce-yourself
```

**What this means**:
- ✅ Your branch was successfully created on GitLab
- ✅ Your commit was uploaded
- ✅ GitLab even provides a link to create a merge request

---

### Step 8: Verify in GitLab

1. Go to GitLab
2. Look for **Branches** section
3. Find `lab/tal/introduce-yourself` in the list
4. Click on it to view:
   - Your commit message
   - The DEVELOPERS.md file with your changes
   - Confirmation that your branch is ahead of main

---

### Step 9: Final Local Verification

```bash
# Check status (should be clean)
git status

# View your commit
git log --oneline -2

# See your branches
git branch -v
```

**Expected output for `git status`**:
```
On branch lab/tal/introduce-yourself
nothing to commit, working tree clean
```

---

## What You Accomplished

✅ **Created a feature branch** using Sonic naming conventions  
✅ **Modified a file** and understood what changed  
✅ **Staged changes** using `git add`  
✅ **Committed with intention** using a meaningful message  
✅ **Pushed to remote** to share with the team  
✅ **Verified in GitLab** that your work is there  

---

## Key Learning Points

### 1. Why Branches Matter
```
main branch (stable, production)
    └── lab/tal/introduce-yourself (your work)
```
This isolation prevents accidents—your work doesn't affect main until explicitly merged.

### 2. The Three-Stage Workflow
```
Working Directory → Staging Area → Commit History
    (git diff)        (git add)      (git commit)
       Files          Proposed        Permanent
                     Snapshot         Record
```

### 3. Branch Naming Convention
- `lab/<your-name>/<what-you-did>`
- Makes history readable for the whole team
- Easy to identify whose work this is
- Easy to find related commits

### 4. Meaningful Commit Messages
Helps your future self and teammates understand:
- What changed
- Why it changed
- When it changed
- Who made the change

---

## Common Variations

### Different commit message format
Some people prefer longer messages:
```bash
git commit -m "Add tal to developers list" -m "This is part of the onboarding process to help new team members introduce themselves."
```

The `-m` can be used multiple times. First is the title, rest are body.

### Using git switch instead of git checkout
```bash
git switch -c lab/tal/introduce-yourself  # Create and switch
git switch main                            # Switch to existing branch
```

This is newer syntax and is equivalent to `checkout`.

### Staging specific files vs. everything
```bash
git add DEVELOPERS.md   # Stage only this file
git add .              # Stage all changes
```

For this exercise, both work. In larger projects with multiple files, you might stage specific files.

---

## Reflection

1. **Why create an exercise branch instead of committing directly to lab/exercises?**
   - Real feature development uses separate branches
   - Keeps exercises organized and trackable
   - Simulates the workflow you'll use on actual projects

2. **Why commit before pushing?**
   - Commits are atomic snapshots
   - You could make multiple commits before pushing
   - Each commit documents a logical step
   - Easy to revert specific commits if needed

3. **What would happen if you pushed to main instead?**
   - Direct changes to main are generally discouraged
   - Code review via merge requests is the standard
   - This prevents mistakes from reaching production

---

## Next Step

✅ Compare this solution with your approach  
✅ Note any differences  
✅ Make sure you understand why each step is needed  
✅ Move on to Exercise 2: Merge Conflict Resolution