#!/usr/bin/env python3
"""
Git Fork Helper Script

This script helps you understand your current git configuration and provides
guidance on how to contribute to the Federated DDoS Detection project.

Usage:
    python scripts/git_fork_helper.py
"""

import subprocess
import sys
from pathlib import Path


def run_git_command(cmd):
    """Run a git command and return the output."""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"


def check_git_status():
    """Check and display current git configuration."""
    print("=" * 60)
    print("🔍 Git Configuration Analysis")
    print("=" * 60)
    
    # Check if we're in a git repository
    try:
        repo_root = run_git_command("git rev-parse --show-toplevel")
        print(f"✅ Git repository found: {repo_root}")
    except:
        print("❌ Not in a git repository!")
        return False
    
    # Current branch
    current_branch = run_git_command("git branch --show-current")
    print(f"📍 Current branch: {current_branch}")
    
    # Remote configuration
    print("\n🔗 Remote repositories:")
    remotes_output = run_git_command("git remote -v")
    if remotes_output:
        for line in remotes_output.split('\n'):
            print(f"   {line}")
    else:
        print("   No remotes configured")
    
    # Recent commits
    print("\n📝 Recent commits:")
    recent_commits = run_git_command("git log --oneline -5")
    for line in recent_commits.split('\n')[:5]:
        print(f"   {line}")
    
    # Working directory status
    print("\n📋 Working directory status:")
    status = run_git_command("git status --porcelain")
    if status:
        print("   Modified files:")
        for line in status.split('\n'):
            print(f"   {line}")
    else:
        print("   ✅ Working directory clean")
    
    return True


def analyze_fork_setup():
    """Analyze if the repository is properly set up for fork workflow."""
    print("\n" + "=" * 60)
    print("🔧 Fork Setup Analysis")
    print("=" * 60)
    
    remotes = run_git_command("git remote -v")
    has_origin = "origin" in remotes
    has_upstream = "upstream" in remotes
    
    print(f"{'✅' if has_origin else '❌'} Origin remote configured: {has_origin}")
    print(f"{'✅' if has_upstream else '❌'} Upstream remote configured: {has_upstream}")
    
    if has_origin and has_upstream:
        print("\n🎉 Perfect! Your repository is properly configured for fork workflow.")
        return True
    elif has_origin and not has_upstream:
        print("\n⚠️  You have a fork but upstream is not configured.")
        print("   Add upstream remote with:")
        print("   git remote add upstream https://github.com/HemanthKumar-CS/Fedrated_DDoS_Detection.git")
        return False
    else:
        print("\n❌ Repository setup needs attention.")
        return False


def provide_guidance():
    """Provide step-by-step guidance based on current setup."""
    print("\n" + "=" * 60)
    print("📚 Next Steps Guidance")
    print("=" * 60)
    
    current_branch = run_git_command("git branch --show-current")
    
    if current_branch == "main" or current_branch == "master":
        print("🔄 You're on the main branch. To create a new feature branch:")
        print("   1. git checkout -b your-feature-branch-name")
        print("   2. Make your changes")
        print("   3. git add .")
        print("   4. git commit -m 'Your descriptive message'")
        print("   5. git push origin your-feature-branch-name")
        print("   6. Create Pull Request on GitHub")
    else:
        print(f"🚀 You're on branch '{current_branch}'. To contribute:")
        print("   1. Make your changes")
        print("   2. git add .")
        print("   3. git commit -m 'Your descriptive message'")
        print("   4. git push origin " + current_branch)
        print("   5. Create Pull Request on GitHub")
    
    print("\n📖 For detailed instructions, see CONTRIBUTING.md")


def check_for_mark2_branch():
    """Check if the user mentioned 'mark2' branch exists."""
    print("\n" + "=" * 60)
    print("🔍 Checking for 'mark2' branch")
    print("=" * 60)
    
    all_branches = run_git_command("git branch -a")
    
    if "mark2" in all_branches:
        if "* mark2" in all_branches:
            print("✅ You're currently on the 'mark2' branch!")
        elif "remotes/origin/mark2" in all_branches:
            print("📡 'mark2' branch exists on your remote fork.")
            print("   To work on it locally: git checkout mark2")
        else:
            print("📂 'mark2' branch exists locally.")
            print("   To switch to it: git checkout mark2")
            print("   To push it: git push origin mark2")
    else:
        print("❓ No 'mark2' branch found.")
        print("   If you want to create it: git checkout -b mark2")


def main():
    """Main function to run all checks and provide guidance."""
    print("🛡️ Federated DDoS Detection - Git Fork Helper")
    print("This tool helps you understand your git setup and contribution workflow.\n")
    
    if not check_git_status():
        return 1
    
    fork_setup_ok = analyze_fork_setup()
    check_for_mark2_branch()
    provide_guidance()
    
    print("\n" + "=" * 60)
    print("📋 Summary")
    print("=" * 60)
    
    if fork_setup_ok:
        print("✅ Your repository is properly configured for contributions!")
        print("📝 Follow the guidance above to create and submit your pull request.")
    else:
        print("⚠️  Your repository setup needs some adjustments.")
        print("📖 See CONTRIBUTING.md for detailed setup instructions.")
    
    print("\n🤝 Remember: You cannot push directly to the upstream repository.")
    print("   All contributions must go through the fork → pull request workflow.")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())