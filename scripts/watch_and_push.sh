#!/usr/bin/env bash
# Automatically attempts push to GitHub once the remote repository is detected.
REPO_URL="git@github.com:khyuk-hardware-math/global-stem-edtech-skills-200.git"
PROFILE_REPO_URL="git@github.com:khyuk-hardware-math/khyuk-hardware-math.git"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PARENT_DIR="$(cd "$DIR/.." && pwd)"

echo "Watching for remote repository creation on GitHub (waiting up to 60 mins)..."
for i in {1..360}; do
    if git ls-remote "$REPO_URL" &>/dev/null; then
        echo "Detected $REPO_URL! Triggering push..."
        git -C "$DIR" push -u origin main
        
        if git ls-remote "$PROFILE_REPO_URL" &>/dev/null && [ -d "$PARENT_DIR/khyuk-hardware-math" ]; then
            echo "Detected $PROFILE_REPO_URL! Triggering push..."
            git -C "$PARENT_DIR/khyuk-hardware-math" push -u origin main
        fi
        echo "Push completed successfully!"
        exit 0
    fi
    sleep 10
done
echo "Timeout waiting for repository creation."
