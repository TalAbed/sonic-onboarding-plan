# Exercise 2: Merge Conflict Resolution - Instructions

This is a longer exercise because conflicts require careful attention. Follow each step closely and read all explanations.

---

## Step 1: Go Back to Your Lab Branch

Make sure you're on your main lab branch before creating new branches.

```bash
# Switch to your lab branch
git checkout lab/<your-name>/exercises

# Update it with latest changes
git pull origin lab/<your-name>/exercises

# Verify you're on the right branch
git branch
```

---

## Step 2: Create First Feature Branch

Create the first branch that will make changes to the changelog.

```bash
git checkout -b lab/<your-name>/changelog-v1
```

**Example**:
```bash
git checkout -b lab/alex/changelog-v1
```

**What this does**: Creates a branch where you'll simulate Developer A's work.

---

## Step 3: Edit changelog.md (Branch 1)

Open the changelog file:

```bash
code changelog.md
```

The file should look like:

```markdown
# Sonic Data Pipeline - Changelog

## [Unreleased]

### Added
- Real-time event processing
- Data validation layer

### Fixed
- Memory leak in pipeline connector

## [1.0.0] - 2026-01-07

Initial release
```

**Edit it**: Under `### Added`, modify the first item to add more detail:

**Change this**:
```
- Real-time event processing
```

**To this**:
```
- Real-time event processing with sub-millisecond latency
```

Save the file.

---

## Step 4: Commit Changes in Branch 1

```bash
git add changelog.md
git commit -m "Add latency details to real-time processing feature"
```

**Verify**:
```bash
git log --oneline -1
# Should show your new commit
```

---

## Step 5: Create Second Feature Branch

Now create a second branch that will make conflicting changes. Start from your lab branch again (not from changelog-v1).

```bash
# Go back to your lab branch
git checkout lab/<your-name>/exercises

# Create a new branch from here (this is important!)
git checkout -b lab/<your-name>/changelog-v2
```

**What this does**: Simulates another developer working on the same file independently. Both branches started from the same point (main), so when you try to merge them, Git will find conflicts.

---

## Step 6: Edit changelog.md (Branch 2)

Open the changelog file again:

```bash
code changelog.md
```

**Edit it**: Under `### Added`, modify the first item DIFFERENTLY than in branch 1:

**Change this**:
```
- Real-time event processing
```

**To this**:
```
- Real-time event processing with comprehensive monitoring
```

This is different from what you wrote in branch 1! Now you have two branches with conflicting changes to the same line.

Save the file.

---

## Step 7: Commit Changes in Branch 2

```bash
git add changelog.md
git commit -m "Add monitoring details to real-time processing"
```

**Verify**:
```bash
git log --oneline -1
# Should show your new commit
```

---

## Step 8: Merge Branch 1 into Branch 2

Now you'll attempt to merge the changes from branch 1 into branch 2. This is where the conflict happens.

```bash
# You should be on changelog-v2
git status

# Merge branch 1 into current branch (v2)
git merge lab/<your-name>/changelog-v1
```

**Example**:
```bash
git merge lab/alex/changelog-v1
```

**Expected output**:
```
Auto-merging changelog.md
CONFLICT (content): Merge conflict in changelog.md
Automatic merge failed; fix conflicts and then commit the result.
```

**This is expected!** Git detected the conflict and stopped. Your job is to resolve it.

---

## Step 9: Examine the Conflict

```bash
git status
```

**You should see**:
```
On branch lab/alex/changelog-v2
You have unmerged paths.
  (use "git add/rm <file>..." as appropriate to mark resolution)
  (use "git merge --abort" to abort the merge)

both modified:   changelog.md
```

Open the file to see the conflict markers:

```bash
code changelog.md
```

**You'll see something like**:

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
```

**Understanding the markers**:
- `<<<<<<< HEAD` = Your current branch's version (v2 with "comprehensive monitoring")
- `=======` = Divider between versions
- `>>>>>>> lab/alex/changelog-v1` = Incoming branch's version (v1 with "sub-millisecond latency")

---

## Step 10: Resolve the Conflict

You need to decide: which change do you want? Or do you want both? Or neither?

**For this exercise**, keep BOTH changes in a merged form:

Edit the file to:

```markdown
# Sonic Data Pipeline - Changelog

## [Unreleased]

### Added
- Real-time event processing with sub-millisecond latency and comprehensive monitoring

### Fixed
- Memory leak in pipeline connector

## [1.0.0] - 2026-01-07

Initial release
```

**What you did**:
1. ✅ Removed the conflict markers (`<<<<`, `====`, `>>>>`)
2. ✅ Kept both pieces of useful information
3. ✅ Created a logical, merged result
4. ✅ Left the rest of the file untouched

Save the file.

---

## Step 11: Verify Your Resolution

```bash
git status
```

You should see:
```
both modified:   changelog.md
```

View your resolved file:

```bash
cat changelog.md
# Or
code changelog.md
```

Confirm the conflict markers are gone and your resolution makes sense.

---

## Step 12: Stage the Resolved File

```bash
git add changelog.md
```

**This tells Git**: "I've resolved the conflict in this file, it's ready to go."

**Verify**:
```bash
git status
```

You should see:
```
On branch lab/alex/changelog-v2
All conflicts fixed but you are still merging.
  (use "git commit" to conclude the merge)

Changes to be committed:
  modified:   changelog.md
```

---

## Step 13: Complete the Merge

```bash
git commit -m "Merge changelog-v1 into changelog-v2: combine latency and monitoring details"
```

**What this does**: Completes the merge and creates a merge commit that documents the resolution.

**Verify**:
```bash
git log --oneline -3
```

You should see something like:

```
a1b2c3d Merge changelog-v1 into changelog-v2: combine latency and monitoring details
d4e5f6g Add monitoring details to real-time processing
h7i8j9k Add latency details to real-time processing feature
```

Notice the merge commit at the top, showing both branches were merged.

---

## Step 14: Verify the Merge

```bash
# View the resolved file
cat changelog.md

# See what changed in the merge
git log -p -1
# (This shows the patch/diff of the last commit)

# View the merge commit specifically
git show HEAD
```

Confirm that:
- ✅ Conflict markers are gone
- ✅ Both sets of meaningful changes are present
- ✅ The file makes sense and is valid

---

## Step 15: Push Your Work

```bash
git push origin lab/<your-name>/changelog-v2
```

**What this does**: Sends your resolved merge to GitLab so others can see how you handled the conflict.

---

## You've Completed Exercise 2! 🎉

### What You Did

1. ✅ Created two branches with conflicting changes
2. ✅ Modified the same file differently in each branch
3. ✅ Triggered a real merge conflict
4. ✅ Identified conflict markers in the file
5. ✅ Resolved the conflict thoughtfully
6. ✅ Staged and committed the resolution
7. ✅ Completed the merge

### What This Means

You now know how to:
- Prevent unnecessary conflicts through communication
- Recognize and understand conflict markers
- Resolve conflicts safely without losing code
- Complete merges with clear documentation

---

## Key Insights

### Why Conflicts Happen
When two developers modify the same lines, Git can't automatically decide which version is correct. It stops and asks: "Which changes should I keep?"

### Why Communication Matters
Many conflicts are preventable through communication: "I'm working on the changelog—avoid that file." But when they happen, knowing how to resolve them gracefully is invaluable.

### Safe Resolution
- ✅ Review both versions
- ✅ Understand what each change is trying to do
- ✅ Make an intentional decision
- ✅ Test the resolved file makes sense
- ✅ Document your decision in the merge commit

---

## Troubleshooting

### "I made a mistake and want to abort the merge"
```bash
git merge --abort
# This reverts to before the merge started
```

### "I resolved the conflict wrong"
You can still fix it! Just edit the file again and re-stage it:
```bash
code changelog.md  # Edit the file again
git add changelog.md
git commit  # Use existing merge commit message
```

### "I forgot which branch I'm on"
```bash
git branch
# The asterisk shows which branch is current
```

### "Merge seems stuck"
```bash
git status
# Should tell you what's waiting for you
```

---

## You did it!

Great job handling a real, complex Git scenario! 🚀
