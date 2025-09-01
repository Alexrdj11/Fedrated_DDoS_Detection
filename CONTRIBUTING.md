# Contributing to Federated DDoS Detection

This guide explains how to contribute to the Federated DDoS Detection project, including how to work with forks and submit pull requests.

## Fork-to-Upstream Workflow

### Understanding the Repository Structure

This repository follows the standard GitHub fork contribution model:

- **Upstream Repository**: The original repository owned by the maintainer (e.g., `HemanthKumar-CS/Fedrated_DDoS_Detection`)
- **Fork**: Your personal copy of the repository (e.g., `YourUsername/Fedrated_DDoS_Detection`)
- **Local Clone**: Your local working copy of your fork

### Step-by-Step Guide: Contributing from Your Fork

#### 1. Initial Setup (One-time only)

If you haven't already forked and cloned the repository:

```bash
# 1. Fork the repository on GitHub (click "Fork" button on the original repo)
# 2. Clone your fork locally
git clone https://github.com/YourUsername/Fedrated_DDoS_Detection.git
cd Fedrated_DDoS_Detection

# 3. Add the original repository as upstream remote
git remote add upstream https://github.com/HemanthKumar-CS/Fedrated_DDoS_Detection.git

# 4. Verify your remotes
git remote -v
# Should show:
# origin    https://github.com/YourUsername/Fedrated_DDoS_Detection.git (fetch)
# origin    https://github.com/YourUsername/Fedrated_DDoS_Detection.git (push)
# upstream  https://github.com/HemanthKumar-CS/Fedrated_DDoS_Detection.git (fetch)
# upstream  https://github.com/HemanthKumar-CS/Fedrated_DDoS_Detection.git (push)
```

#### 2. Working with Branches

```bash
# 1. Make sure you're on the main branch and it's up to date
git checkout main
git pull upstream main

# 2. Create a new branch for your feature/fix (replace 'mark2' with your branch name)
git checkout -b mark2

# 3. Make your changes and commit them
git add .
git commit -m "Your descriptive commit message"

# 4. Push the branch to YOUR fork (not the upstream)
git push origin mark2
```

#### 3. Creating a Pull Request

After pushing your branch to your fork:

1. **Go to GitHub** and navigate to your fork
2. **Click "Compare & pull request"** (GitHub usually shows this banner after pushing)
3. **Or manually create PR**:
   - Go to the original repository (upstream)
   - Click "New pull request"
   - Click "compare across forks"
   - Select:
     - Base repository: `HemanthKumar-CS/Fedrated_DDoS_Detection` (upstream)
     - Base branch: `main` (or target branch)
     - Head repository: `YourUsername/Fedrated_DDoS_Detection` (your fork)
     - Compare branch: `mark2` (your feature branch)

4. **Fill out the PR template** with:
   - Clear title describing your changes
   - Detailed description of what you changed and why
   - Any testing you've done
   - Screenshots if UI changes are involved

#### 4. After Creating the PR

- **Monitor the PR** for comments and requested changes
- **Make updates** if needed:
  ```bash
  # Make changes on your local branch
  git add .
  git commit -m "Address review feedback"
  git push origin mark2  # This automatically updates the PR
  ```

### Common Commands Reference

```bash
# Check current branch and status
git status
git branch -a

# Sync your fork with upstream changes
git checkout main
git pull upstream main
git push origin main

# Update your feature branch with latest main
git checkout mark2
git merge main  # or git rebase main

# Push changes to your fork
git push origin mark2

# Delete branch after PR is merged
git branch -d mark2
git push origin --delete mark2
```

### Troubleshooting

#### "Permission denied" when pushing to upstream
- **Problem**: You're trying to push directly to the upstream repository
- **Solution**: Always push to your fork (`origin`), not upstream

#### "Branch not found" on GitHub
- **Problem**: You pushed to wrong remote or branch name mismatch
- **Solution**: Check `git remote -v` and ensure you're pushing to `origin`

#### "Conflicts" in Pull Request
- **Problem**: Your branch conflicts with changes in upstream
- **Solution**: Update your branch with latest upstream changes:
  ```bash
  git checkout main
  git pull upstream main
  git checkout mark2
  git merge main
  # Resolve conflicts, then commit and push
  ```

### Best Practices

1. **Keep branches focused**: One feature/fix per branch
2. **Use descriptive names**: `feature/ddos-detection-improvement` instead of `mark2`
3. **Write clear commit messages**: Explain what and why, not just what
4. **Test your changes**: Run tests before submitting PR
5. **Keep PRs small**: Easier to review and merge
6. **Update regularly**: Sync with upstream frequently to avoid conflicts

## Development Workflow

### Setting Up Development Environment

```bash
# Create virtual environment
python -m venv fl_env
source fl_env/bin/activate  # On Windows: fl_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import tensorflow as tf; print(f'TensorFlow version: {tf.__version__}')"
```

### Running Tests

```bash
# Run centralized baseline
python train_centralized.py --data_dir data/optimized/clean_partitions --epochs 25

# Test federated setup
python server.py --rounds 5 --address 127.0.0.1:8080 &
python client.py --cid 0 --server 127.0.0.1:8080 --data_dir data/optimized
```

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings for public functions
- Keep functions focused and small

## Questions?

If you're still unsure about the workflow or encounter issues:

1. Check this guide again
2. Look at existing PRs for examples
3. Open an issue for questions
4. Contact the maintainers

Remember: **You cannot push directly to the upstream repository**. All contributions must go through the fork → pull request workflow.