# Exercise 2: Merge Conflict Resolution - Solution

This solution shows how to handle merge conflicts gracefully and safely.

---

## Solution Overview

The workflow for this exercise:

1. Create two branches that will have conflicting changes
2. Modify the same file differently in each branch
3. Merge one branch into the other to trigger a conflict
4. Identify the conflict using Git tools
5. Resolve the conflict by editing the file
6. Complete the merge with clear documentation

---

## Step-by-Step Solution

### Steps 1-7: Setup and Create Conflicts

```bash
# Step 1: Go to lab branch
git checkout lab/alex/exercises
git pull origin lab/alex/exercises

# Step 2: Create first feature branch
git checkout -b lab/alex/changelog-v1

# Step 3: Edit file (add latency detail)
# Open changelog.md and change:
# From: - Real-time event processing
# To:   - Real-time event processing with sub-millisecond latency

# Step 4: Commit in branch 1
git add changelog.md
git commit -m "Add latency details to real-time processing feature"

# Step 5: Create second feature branch (from lab branch, not v1!)
git checkout lab/alex/exercises
git checkout -b lab/alex/changelog-v2

# Step 6: Edit file differently (add monitoring detail)
# Open changelog.md and change:
# From: - Real-time event processing
# To:   - Real-time event processing with comprehensive monitoring

# Step 7: Commit in branch 2
git add changelog.md
git commit -m "Add monitoring details to real-time processing"
```

**Why this setup**:
- Both branches started from the same point (your lab branch)
- Both modified the same line differently
- This creates an intentional conflict for learning

### Step 8: Trigger the Conflict

```bash
# You're on changelog-v2
git merge lab/alex/changelog-v1
```

**Expected output**:
```
Auto-merging changelog.md
CONFLICT (content): Merge conflict in changelog.md
Automatic merge failed; fix conflicts and then commit the result.
```

This is the moment Git says: "I found a conflict. You decide how to resolve it."

---

### Step 9: Examine the Conflict

```bash
git status
```

**Output**:
```
On branch lab/alex/changelog-v2
You have unmerged paths.
  (use "git add/rm <file>..." as appropriate to mark resolution)
  (use "git merge --abort" to abort the merge)

both modified:   changelog.md
```

**View the conflicted file**:

```bash
cat changelog.md
```

**What you see**:

```markdown
# Sonic Data Pipeline - Changelog

## [Unreleased]

### Added
<<<<<<< HEAD
- Real-time event processing with comprehensive monitoring
=======
- Real-time event processing with sub-millisecond latency
>>>>>>> lab/alex/changelog-v1

### Fixed
- Memory leak in pipeline connector

## [1.0.0] - 2026-01-07

Initial release
```

**Breaking down the conflict markers**:

```
<<<<<<< HEAD
  ↓
- Real-time event processing with comprehensive monitoring
  ↓ Your current branch (v2) - "comprehensive monitoring"
  
=======
  ↓
  DIVIDER - both versions shown above and below
  
>>>>>>> lab/alex/changelog-v1
  ↓
- Real-time event processing with sub-millisecond latency
  ↓ Incoming branch (v1) - "sub-millisecond latency"
```

---

### Step 10: Resolve the Conflict (Strategy)

You have options:

**Option A**: Keep only HEAD (current branch)
```markdown
- Real-time event processing with comprehensive monitoring
```

**Option B**: Keep only incoming (v1)
```markdown
- Real-time event processing with sub-millisecond latency
```

**Option C**: Keep both (merge-friendly approach)
```markdown
- Real-time event processing with sub-millisecond latency and comprehensive monitoring
```

**Why Option C is best here**:
- Both changes are valuable and don't contradict each other
- A merged version is more complete than either alone
- Shows you understand the intent of both changes

### Step 11: Resolve the Conflict (Action)

```bash
# Open the file
code changelog.md
```

**Edit to resolve**:

```markdown
# Sonic Data Pipeline - Changelog

## [Unreleased]

### Added
- Real-time event processing with sub-millisecond latency and comprehensive monitoring
- Data validation layer

### Fixed
- Memory leak in pipeline connector

## [1.0.0] - 2026-01-07

Initial release
```

**What you removed**:
- ✅ `<<<<<<< HEAD` marker
- ✅ `=======` divider
- ✅ `>>>>>>> lab/alex/changelog-v1` marker

**What you kept**:
- ✅ Best parts of both changes
- ✅ All other file content unchanged
- ✅ Logical, sensible result

**Save the file**.

---

### Step 12: Verify Resolution

```bash
# Check the current state
git status
```

**Output**:
```
On branch lab/alex/changelog-v2
You have unmerged paths.
  (use "git add/rm <file>..." as appropriate to mark resolution)
  (use "git merge --abort" to abort the merge)

both modified:   changelog.md
```

**View what you resolved**:

```bash
cat changelog.md
# Verify it looks right and makes sense
```

---

### Step 13: Stage the Resolution

```bash
# Tell Git you've resolved the conflict
git add changelog.md
```

**Verify**:

```bash
git status
```

**Output** (note the change):
```
On branch lab/alex/changelog-v2
All conflicts fixed but you are still merging.
  (use "git commit" to conclude the merge)

Changes to be committed:
  modified:   changelog.md
```

**Key phrase**: "All conflicts fixed"—Git recognized you resolved them.

---

### Step 14: Complete the Merge

```bash
# Commit the merge with a descriptive message
git commit -m "Merge changelog-v1 into changelog-v2: combine latency and monitoring details"
```

**Why this message**:
- ✅ Explains which branches were merged
- ✅ Describes the resolution decision
- ✅ Helps future readers understand the merge

**Output**:
```
[lab/alex/changelog-v2 a1b2c3d] Merge changelog-v1 into changelog-v2: combine latency and monitoring details
```

---

### Step 15: Verify the Completed Merge

```bash
# View recent commits
git log --oneline -4
```

**Output**:
```
a1b2c3d Merge changelog-v1 into changelog-v2: combine latency and monitoring details
d4e5f6g Add monitoring details to real-time processing
h7i8j9k Add latency details to real-time processing feature
i0j1k2l Initial commit
```

**See merge details**:

```bash
git show a1b2c3d
# Shows exactly what the merge commit changed
```

**Verify the final file**:

```bash
cat changelog.md
# Should look clean, no conflict markers
```

---

### Step 16: Push Your Work

```bash
git push origin lab/alex/changelog-v2
```

**Output**:
```
To https://gitlab.company.com/sonic/onboarding.git
 * [new branch]      lab/alex/changelog-v2 -> lab/alex/changelog-v2
```

---

## Key Learning: Conflict Prevention vs. Resolution

### Preventing Conflicts (Ideal)
```
Developer A: Works on feature-a
Developer B: Works on feature-b (different files)
→ No conflict! ✅
```

### Handling Conflicts (Reality)
```
Developer A: Modifies same lines as Developer B
→ Conflict! But you know how to resolve it safely ✅
```

---

## Conflict Resolution Strategies

### Strategy 1: Keep Current (HEAD)
Use when your changes are more recent or correct:
```bash
# Keep only your version (remove incoming section)
```

### Strategy 2: Keep Incoming
Use when the other branch has the better approach:
```bash
# Keep only their version
```

### Strategy 3: Merge Both (Smart Conflict Resolution)
Use when both changes are valuable:
```bash
# Combine the best of both (what we did in this exercise)
```

### Strategy 4: Ask For Help
Use when you're unsure what the changes mean:
```bash
# Reach out to the developer who made the change
# Ask: "What was the intent of this change?"
```

---

## When to Ask For Help

❓ **Ask your team lead if**:
- You don't understand what a change is trying to do
- The conflict seems to require domain knowledge
- Both changes are important but seem contradictory
- You're not sure which change is more recent

✅ **You can handle alone if**:
- Both changes are clearly valuable
- The conflict is in formatting or documentation
- You understand the intent of both branches
- The merged result makes logical sense

---

## Common Mistakes to Avoid

❌ **Mistake 1**: Deleting one entire section without understanding it
```
This loses code—avoid!
```

✅ **Solution**: Understand both changes first

---

❌ **Mistake 2**: Leaving conflict markers in the file
```
<<<<<<< HEAD
Code here
>>>>>>> branch
```

✅ **Solution**: Always remove all markers

---

❌ **Mistake 3**: Committing before resolving all conflicts
```
Git won't let you, but if you try:
```

✅ **Solution**: Git prevents this—it requires you to stage resolved files

---

## Real-World Scenario

On a real team, this conversation might happen:

```
Person A: "I merged your branch and got a conflict"
Person B: "In what file?"
Person A: "changelog.md"
Person B: "Oh! I was adding monitoring, you were adding latency?"
Person A: "Yeah. Both are useful. I merged them."
Person B: "Perfect! Let me verify it looks right."
```

This is professional collaboration in action! 🚀

---

## Summary

You successfully:

1. ✅ Created two branches with intentional conflicts
2. ✅ Triggered a real merge conflict
3. ✅ Recognized conflict markers
4. ✅ Made an informed resolution decision
5. ✅ Completed the merge with clear documentation
6. ✅ Pushed your work

You're now equipped to handle real conflicts on a real team!

---

## Next Step

✅ Review this solution and your approach  
✅ Make sure you understand each decision  
✅ Note any questions to discuss with your team lead  
✅ Update your progress in `../PROGRESS.md`  
✅ Move on to Exercise 3: Undoing Changes Safely

---

## Questions?

Conflict resolution is subtle and important. If anything is unclear, ask your team lead. They've resolved conflicts hundreds of times and can share real-world examples!

Great job tackling one of Git's toughest scenarios! 🎉
