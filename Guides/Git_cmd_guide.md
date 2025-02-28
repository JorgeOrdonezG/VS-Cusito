# Complete Guide to Git and Windows Command-Line Navigation Commands

## **1. Git Command Guide by Experience Level**

### **Beginner Git Commands**
- `git init` → Initialize a new Git repository.
- `git clone <repository-url>` → Clone an existing repository.
- `git status` → Show the working tree status.
- `git add <file>` → Stage a file for the next commit.
- `git add .` → Stage all changes in the current directory.
- `git commit -m "message"` → Commit changes with a message.
- `git log` → View the commit history.
- `git diff` → Show differences between the working directory and the last commit.
- `git checkout <branch>` → Switch to an existing branch.
- `git branch <branch-name>` → Create a new branch.
- `git merge <branch>` → Merge a branch into the current branch.
- `git remote add origin <repository-url>` → Link a local repository to a remote repository.
- `git push origin <branch>` → Push changes to a remote repository.
- `git pull origin <branch>` → Fetch and merge changes from a remote repository.

### **Intermediate Git Commands**
- `git reset <file>` → Unstage a file.
- `git reset --hard <commit>` → Reset to a specific commit, discarding changes.
- `git revert <commit>` → Create a new commit that undoes a previous commit.
- `git stash` → Temporarily store changes without committing.
- `git stash pop` → Restore stashed changes.
- `git cherry-pick <commit>` → Apply a specific commit from another branch.
- `git rebase <branch>` → Reapply commits on top of another branch.
- `git log --oneline --graph` → Show a compact commit history with a graph.
- `git tag <tag-name>` → Create a tag for a specific commit.

### **Advanced Git Commands**
- `git reflog` → Show a history of all references and actions.
- `git bisect start` → Start a binary search to find a bad commit.
- `git blame <file>` → Show who last modified each line of a file.
- `git filter-branch` → Rewrite commit history (use with caution).
- `git worktree add <path> <branch>` → Work with multiple branches in different directories.
- `git submodule add <repository-url>` → Add a submodule to a repository.
- `git sparse-checkout set <directory>` → Fetch only specific parts of a repository.
- `git config --global user.name "Your Name"` → Set global Git username.
- `git config --global user.email "your@email.com"` → Set global Git email.

---

## **2. Windows Command-Line Navigation Commands**

### **Basic Navigation Commands**
- `cd <directory>` → Change to the specified directory.
- `cd ..` → Move up one level in the directory structure.
- `cd ../..` → Move up two levels.
- `cd \` → Go to the root directory.
- `cd %USERPROFILE%` → Go to the user’s home directory.
- `cd /d <drive>:` → Switch to a different drive (e.g., `cd /d D:`).
- `cd -` → (PowerShell only) Switch to the previous directory.

### **Listing and Viewing Files**
- `dir` → List files and folders in the current directory.
- `dir /a` → Show all files, including hidden ones.
- `dir /s` → Show files in all subdirectories.
- `dir /b` → Show a simple list of file names without details.
- `tree` → Display directory structure as a tree.

### **File and Directory Operations**
- `mkdir <directory>` → Create a new directory.
- `rmdir <directory>` → Remove an empty directory.
- `rmdir /s <directory>` → Remove a directory and all its contents.
- `del <file>` → Delete a file.
- `del /f <file>` → Force delete a read-only file.
- `copy <source> <destination>` → Copy a file to a new location.
- `move <source> <destination>` → Move a file or directory.
- `ren <old_name> <new_name>` → Rename a file or directory.

### **Drive and Disk Navigation**
- `<drive>:` → Change to a specific drive (e.g., `D:`).
- `cd /d <drive>:` → Change drive and directory in one command.
- `vol` → Display the volume label and serial number of a drive.

### **Viewing File Content**
- `type <file>` → Display the content of a text file.
- `more <file>` → View a text file one page at a time.
- `notepad <file>` → Open a file in Notepad.

### **Advanced Navigation and Information**
- `echo %CD%` → Print the current directory.
- `path` → Show or set the system path.
- `where <command>` → Locate the executable file of a command.
- `cls` → Clear the screen.
- `exit` → Close the command prompt.

---

This guide provides a structured overview of essential **Git** and **Windows command-line** navigation commands. Let me know if you need more details or explanations! 🚀

