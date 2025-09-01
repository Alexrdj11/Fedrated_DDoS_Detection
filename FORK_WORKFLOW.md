# Quick Reference: Fork to Upstream Workflow

## The Simple Answer

**You cannot push directly to the owner's repository.** Instead, you create a **Pull Request** from your fork.

## Step-by-Step for Your "mark2" Branch

### 1. First, check your current setup:
```bash
python scripts/git_fork_helper.py
```

### 2. If you have a "mark2" branch locally:
```bash
# Switch to your branch
git checkout mark2

# Push it to YOUR fork (not the owner's repo)
git push origin mark2
```

### 3. If you need to create the "mark2" branch:
```bash
# Create and switch to new branch
git checkout -b mark2

# Make your changes, then commit
git add .
git commit -m "Describe your changes"

# Push to YOUR fork
git push origin mark2
```

### 4. Create Pull Request on GitHub:
1. Go to **your fork** on GitHub
2. Click "Compare & pull request" (appears after pushing)
3. Or go to the **original owner's repository** and click "New pull request"
4. Select "compare across forks"
5. Choose:
   - Base: `owner/repo` (original repository)
   - Head: `yourfork/repo` branch `mark2`

## Key Points

- ✅ **DO**: Push to your fork (`git push origin mark2`)
- ❌ **DON'T**: Try to push directly to upstream repository
- 🔄 **WORKFLOW**: Fork → Branch → Commit → Push to Fork → Pull Request

## Need Help?

Run `python scripts/git_fork_helper.py` for personalized guidance based on your current setup.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions.