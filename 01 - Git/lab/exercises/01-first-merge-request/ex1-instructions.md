# Exercise 1: First Merge Request - Instructions

Follow these steps carefully. Read each step fully before executing the command.

---

## Step 1: Verify Your Setup

First, make sure you're in the right place and on the right branch.

```bash
# Check your current location
pwd
# You should be in: .../01-Git/lab/01-first-merge-request

# Check your current branch
git branch
# You should see your lab branch highlighted, like: lab/tal/exercises

# Verify clean working directory
git status
# You should see: "nothing to commit, working tree clean"
```

**What this does**: Confirms you're ready to start.

---

## Step 2: Create an Exercise-Specific Branch

While you're on your lab branch, create a sub-branch specifically for this exercise. This is how real feature work happens—each feature gets its own branch.

```bash
# Create a new branch from your current lab branch
git checkout -b lab/<your-name>/introduce-yourself
```

**Example**: 
```bash
git checkout -b lab/tal/introduce-yourself
```

**What this does**: Creates a new branch where you'll do this exercise work. Branch naming: `lab/<your-name>/introduce-yourself`.

**Verify it worked**:
```bash
git branch
# Should show: * lab/tal/introduce-yourself (with asterisk = current branch)
```

---

## Step 3: View the DEVELOPERS.md File

Open and read the file you'll be editing.

```bash
# View the file
cat DEVELOPERS.md
# Or open it in your editor
code DEVELOPERS.md
```

---

## Step 4: Edit the File

Open `DEVELOPERS.md` in your editor and add your information.



**What to add**:

Add a new section for yourself following this format:

```markdown
### Your Name
- **Name**: Your Full Name
- **Role**: Data Engineer / Software Engineer / Your Role
- **Focus**: What area are you interested in?
- **Fun Fact**: Something fun or interesting about you!
```

**Example**:
```markdown
### Tal
- **Name**: Tal Abed
- **Role**: Data Engineer Team Leader
- **Focus**: Real-time pipeline optimization
- **Fun Fact**: I completed 70% of the Grizzler archive (but it got deleted 😢)
```

Don't forget to **Save the file** when done.

---

## Step 5: Check Your Changes

Verify that your changes are what you expect.

```bash
# See what you've modified
git status
```

You should see:
```
On branch lab/tal/introduce-yourself
Changes not staged for commit:
  modified:   DEVELOPERS.md
```

**View the exact changes**:
```bash
git diff DEVELOPERS.md
```

This shows lines you added (green with `+`) and removed (red with `-`). You should only see additions.

---

## Step 6: Stage Your Changes

Prepare your changes for committing.

```bash
# Stage the file
git add DEVELOPERS.md

# Or stage everything
git add .
```

**What this does**: Moves your changes from working directory to staging area.

**Verify staging**:
```bash
git status
```

You should see:
```
On branch lab/tal/introduce-yourself
Changes to be committed:
  modified:   DEVELOPERS.md
```

Notice the color changed from red to green (if using a colored terminal).

---

## Step 7: Commit Your Changes

Save your changes to Git history with a meaningful message.

```bash
git commit -m "Add Tal to developers list"
```

**Message format**: Use clear, imperative language. Examples:
- ✅ "Add Tal to developers list"
- ✅ "Introduce Tal to Sonic team"
- ❌ "Added Tal"
- ❌ "Update"

**Verify the commit**:
```bash
git log --oneline
# Should show your new commit at the top
```

Output example:
```
a1b2c3d Add Tal to developers list
x9y8z7w Initial commit
```

---

## Step 8: Push Your Branch

Send your committed changes to GitLab.

```bash
# Push your branch to the remote repository
git push origin lab/<your-name>/introduce-yourself
```

**Example**:
```bash
git push origin lab/tal/introduce-yourself
```

**What this does**: Uploads your branch and commits to GitLab so others can see your work.

**Verify the push** (you should see output like):
```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
...
 * [new branch]      lab/tal/introduce-yourself -> lab/tal/introduce-yourself
```

---

## Step 9: Verify Your Work in GitLab

Now let's verify everything is in GitLab.

1. **Open GitLab** in your browser
2. **Navigate** to the Sonic onboarding repository
3. **Look for your branch** in the branches list (it should appear near the top)
4. **Click on your branch** and verify:
   - Your commit is there
   - Your changes to DEVELOPERS.md are visible
   - The commit message is clear and meaningful

---

## Step 10: Check Your Final Status

Verify your local repository is clean and ready.

```bash
# Check status
git status
# Should show: "nothing to commit, working tree clean"

# View your commit history
git log --oneline -3
# Should show your new commit at the top

# Verify you're on the right branch
git branch
# Should show your exercise branch is current
```

---

## You've Completed Exercise 1! 🎉

### What You Did

1. ✅ Created a feature branch following Sonic conventions
2. ✅ Modified a file to add your information
3. ✅ Staged changes using `git add`
4. ✅ Committed changes with a meaningful message
5. ✅ Pushed your branch to GitLab
6. ✅ Verified your work is visible in GitLab

### What This Means

You've now practiced the core Git workflow that you'll use every single day on Sonic:
- **Branch** for isolated work
- **Edit** files
- **Add** changes to staging
- **Commit** snapshots
- **Push** to share with the team