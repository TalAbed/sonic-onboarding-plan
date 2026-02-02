# Basic Git Commands Guide

## Overview

As you already know, Git is a distributed version control system that allows teams to collaborate on code efficiently. This guide covers the essential Git commands every developer needs to master before working with real-life systems.

## Table of Contents

1. [Initial Setup](#initial-setup)
2. [Creating and Cloning Repositories](#creating-and-cloning-repositories)
3. [Basic Workflow](#basic-workflow)
4. [Viewing Changes](#viewing-changes)
5. [Branching](#branching)
6. [Merging and Rebasing](#merging-and-rebasing)
7. [Undoing Changes](#undoing-changes)
8. [Collaboration](#collaboration)
9. [Common Workflows](#common-workflows)

---

## Initial Setup

Before making your first commit, configure your Git identity.

```bash
# Set your name (used for all commits)
git config --global user.name "Your Name"

# Set your email (used for all commits)
git config --global user.email "your.email@company.com"

# Verify your configuration
git config --global --list
```

**Why it matters:** Every commit includes author information. Correct configuration ensures accountability and proper attribution in your team's repositories.

---

## Creating and Cloning Repositories

### Clone an Existing Repository

```bash
# Clone a remote repository to your local machine
git clone <repository-url>

# Clone into a specific directory
git clone <repository-url> <directory-name>

# Clone a specific branch
git clone --branch <branch-name> <repository-url>
```

**Example:**
```bash
git clone https://gitlab.com/sonic2791202/sonic-onboarding.git
```

### Initialize a New Repository

```bash
# Create a new Git repository in the current directory
git init

# Create a new directory and initialize it as a repository
git init <project-name>
```

---

## Basic Workflow

The core Git workflow involves three stages: **working directory**, **staging area**, and **commit history**.

### Check Repository Status

```bash
# Display the state of the working directory and staging area
git status

# Display in short format
git status --short
# or
git status -s
```

### Stage Changes

```bash
# Stage all changes in a file
git add <filename>

# Stage all modified and new files (but not deletions)
git add .

# Stage all changes including deletions
git add -A

# Stage specific parts of a file (interactive mode)
git add -p <filename>
```

### Commit Changes

```bash
# Commit staged changes with a message
git commit -m "Your commit message"

# Commit with a longer description
git commit -m "Short summary" -m "Detailed explanation of changes"

# Stage and commit all tracked files (skips new files)
git commit -am "Your commit message"
```

**Commit Message Best Practices:**
- Use imperative mood: "Add feature" not "Added feature"
- Keep the subject line under 50 characters
- Separate subject from body with a blank line
- Explain what and why, not how

### View Commit History

```bash
# Display commit history
git log

# Display last N commits
git log -n 5

# Display with one line per commit
git log --oneline

# Display with branch visualization
git log --graph --oneline --all

# Display commits by specific author
git log --author="Author Name"

# Display commits after a specific date
git log --since="2 weeks ago"
```

---

## Viewing Changes

### Compare Changes

```bash
# Show unstaged changes (working directory vs. staging area)
git diff

# Show staged changes (staging area vs. last commit)
git diff --staged

# Compare working directory with last commit
git diff HEAD

# Compare two branches
git diff <branch1> <branch2>

# Compare two commits
git diff <commit1> <commit2>

# Show only file names that changed
git diff --name-only <commit1> <commit2>
```

### View Specific Commits

```bash
# Display details of a specific commit
git show <commit-hash>

# Display a specific file at a given commit
git show <commit-hash>:<filepath>

# Display blame (show who changed each line)
git blame <filename>
```

---

## Branching

Branches allow parallel development without affecting the main codebase.

### Create and Switch Branches

```bash
# Create a new branch
git branch <branch-name>

# Switch to a branch
git checkout <branch-name>

# Create and switch to a new branch (shorthand)
git checkout -b <branch-name>

# Alternative syntax (Git 2.23+)
git switch <branch-name>
git switch -c <branch-name>
```

### List Branches

```bash
# List local branches
git branch

# List all branches (local and remote)
git branch -a

# List remote branches only
git branch -r

# List branches with last commit info
git branch -v
```

### Rename Branches

```bash
# Rename current branch
git branch -m <new-branch-name>

# Rename a specific branch
git branch -m <old-branch-name> <new-branch-name>
```

### Delete Branches

```bash
# Delete a local branch (safe: prevents deletion if not merged)
git branch -d <branch-name>

# Force delete a local branch
git branch -D <branch-name>

# Delete a remote branch
git push origin --delete <branch-name>
```

---

## Merging and Rebasing

### Merge Branches

```bash
# Merge a branch into current branch
git merge <branch-name>

# Merge with a custom commit message
git merge --no-ff <branch-name> -m "Custom merge message"
```

### Rebase Branches

```bash
# Rebase current branch onto another branch
git rebase <target-branch>

# Interactive rebase (rewrite commits)
git rebase -i <commit-hash>
git rebase -i HEAD~3  # Rebase last 3 commits
```

**Merge vs. Rebase:**
- **Merge**: Creates a merge commit, preserves history
- **Rebase**: Linear history, cleaner but rewrites commits (avoid on public branches)

---

## Undoing Changes

### Discard Changes

```bash
# Discard changes in a file (restore from last commit)
git checkout -- <filename>

# Discard all changes in working directory
git checkout -- .

# Discard staged changes (unstage file)
git reset <filename>

# Discard all staged changes
git reset
```

### Undo Commits

```bash
# Undo the last commit but keep changes staged
git reset --soft HEAD~1

# Undo the last commit but keep changes in working directory
git reset --mixed HEAD~1

# Completely undo the last commit (discard changes)
git reset --hard HEAD~1

# Create a new commit that undoes a specific commit
git revert <commit-hash>
```

**Important:** Use `git reset --hard` with caution—it permanently discards changes. Prefer `git revert` for shared branches.

---

## Collaboration

### Fetch and Pull

```bash
# Fetch updates from remote without merging
git fetch

# Fetch from specific remote
git fetch origin

# Fetch all remotes
git fetch --all

# Pull (fetch + merge) from remote
git pull

# Pull with rebase instead of merge
git pull --rebase
```

### Push Changes

```bash
# Push current branch to remote
git push

# Push to specific remote and branch
git push origin <branch-name>

# Push all local branches
git push --all

# Push all tags
git push --tags

# Force push (overwrite remote—use carefully!)
git push --force
```

### Manage Remotes

```bash
# List remote repositories
git remote

# List remotes with URLs
git remote -v

# Add a new remote
git remote add <remote-name> <repository-url>

# Remove a remote
git remote remove <remote-name>

# Rename a remote
git remote rename <old-name> <new-name>

# View remote details
git remote show <remote-name>
```

---

## Common Workflows

### Workflow 1: Create and Submit a Feature

```bash
# 1. Update local dev branch
git checkout develop
git pull origin develop

# 2. Create feature branch
git checkout -b feature/new-data-processor

# 3. Make changes and commit
git add .
git commit -m "Add new data processor for real-time events"

# 4. Push to remote
git push origin feature/new-data-processor

# 5. Create merge request (can be done via commands or UI)
```

### Workflow 2: Sync with Main and Resolve Conflicts

```bash
# 1. Fetch latest from remote
git fetch origin

# 2. Rebase on main (keeps linear history)
git rebase origin/main

# 3. If conflicts occur, resolve them manually
# Then continue the rebase
git add <resolved-files>
git rebase --continue

# 4. Push your changes (may require force push if already pushed)
git push origin <branch-name> --force-with-lease
```

### Workflow 3: Fix a Mistake Before Pushing

```bash
# 1. Amend the last commit (if not yet pushed)
git add .
git commit --amend --no-edit

# 2. Or reset and recommit
git reset --soft HEAD~1
git add .
git commit -m "Corrected commit message"

# 3. Push as normal
git push origin <branch-name>
```

### Workflow 4: Keep Your Branch Updated

```bash
# 1. Fetch latest changes
git fetch origin

# 2. Rebase or merge main into your branch
git rebase origin/main
# or
git merge origin/main

# 3. Resolve any conflicts if they exist
# 4. Push updated branch
git push origin <branch-name>
```

---

## Troubleshooting

### "fatal: destination path already exists"
```bash
# Clone with a different directory name
git clone <repository-url> <new-directory-name>
```

### "error: Your local changes to the following files would be overwritten"
```bash
# Option 1: Stash changes temporarily
git stash
git pull
git stash pop

# Option 2: Commit changes first
git add .
git commit -m "Work in progress"
git pull
```

### "detached HEAD state"
```bash
# You're viewing a specific commit, not a branch
# Switch back to a branch
git checkout <branch-name>

# Or create a new branch from this commit
git checkout -b <new-branch-name>
```

---

## Next Steps

Now that you've learned the basics, explore:
- **Stashing changes** (`git stash`) for temporary work
- **Cherry-picking commits** (`git cherry-pick`) for selective merges
- **Tags** (`git tag`) for marking releases
- **Hooks** for automating tasks on Git events
- **Advanced workflows** like GitFlow or trunk-based development

For your Sonic team's real-time data processing work, these foundations will enable smooth collaboration and code quality maintenance across your pipeline infrastructure.

---

## References

- [Official Git Documentation](https://git-scm.com/doc)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
