#!/usr/bin/env bash
# ==============================================================================
# sync_to_github.sh
# Push and synchronize global-stem-edtech-skills-200 repository to GitHub
# ==============================================================================
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_DIR}"

DEFAULT_GITHUB_URL="${1:-git@github.com:khyuk-hardware-math/global-stem-edtech-skills-200.git}"

if git remote | grep -q "^origin$"; then
  git remote set-url origin "${DEFAULT_GITHUB_URL}"
else
  git remote add origin "${DEFAULT_GITHUB_URL}"
fi

echo "Adding all files..."
git add -A

COMMIT_MSG="chore: release global-stem-edtech-skills-200 for GitHub open-source ecosystem [verified]"
if git diff-index --quiet HEAD --; then
  echo "Working tree clean, nothing to commit."
else
  git commit -m "${COMMIT_MSG}"
fi

CURRENT_BRANCH=$(git branch --show-current || echo "main")
echo "Pushing to GitHub remote origin branch ${CURRENT_BRANCH}..."

if git push -u origin "${CURRENT_BRANCH}"; then
  echo "================================================================="
  echo "🎉 SUCCESS: Successfully published to GitHub!"
  echo "Public Repository URL: https://github.com/khyuk-hardware-math/global-stem-edtech-skills-200"
  echo "================================================================="
else
  echo "================================================================="
  echo "⚠️ Push failed: GitHub repository not found."
  echo "Please ensure the repository has been created at:"
  echo "👉 https://github.com/new"
  echo "   - Repository name: global-stem-edtech-skills-200"
  echo "   - Visibility: Public"
  echo "   - Do NOT initialize with README/license (already provided locally)"
  echo "Once created, re-run: ./scripts/sync_to_github.sh"
  echo "================================================================="
  exit 1
fi
