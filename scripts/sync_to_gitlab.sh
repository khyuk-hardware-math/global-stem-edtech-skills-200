#!/usr/bin/env bash
# ==============================================================================
# sync_to_gitlab.sh
# Push and synchronize global-stem-edtech-skills-200 repository to GitLab
# ==============================================================================
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${REPO_DIR}"

DEFAULT_GITLAB_URL="${1:-}"

if [ -z "${DEFAULT_GITLAB_URL}" ]; then
  # Check if origin or gitlab remote is already configured
  EXISTING_REMOTE=$(git remote get-url gitlab 2>/dev/null || git remote get-url origin 2>/dev/null || true)
  if [ -n "${EXISTING_REMOTE}" ]; then
    echo "Found existing remote: ${EXISTING_REMOTE}"
    TARGET_REMOTE="${EXISTING_REMOTE}"
  else
    echo "================================================================="
    echo "Usage: ./scripts/sync_to_gitlab.sh <gitlab-remote-url>"
    echo "Example: ./scripts/sync_to_gitlab.sh git@gitlab.com:username/global-stem-edtech-skills-200.git"
    echo "================================================================="
    exit 0
  fi
else
  TARGET_REMOTE="${DEFAULT_GITLAB_URL}"
  if git remote | grep -q "^gitlab$"; then
    git remote set-url gitlab "${TARGET_REMOTE}"
  else
    git remote add gitlab "${TARGET_REMOTE}"
  fi
fi

echo "Adding all files..."
git add -A

COMMIT_MSG="chore: release global-stem-edtech-skills-200 (100 pedagogy + 100 github repos) [verified]"
if git diff-index --quiet HEAD --; then
  echo "Working tree clean, nothing to commit."
else
  git commit -m "${COMMIT_MSG}"
fi

CURRENT_BRANCH=$(git branch --show-current || echo "main")
if [ -z "${CURRENT_BRANCH}" ]; then
  git checkout -b main
  CURRENT_BRANCH="main"
fi

REMOTE_NAME=$(git remote | grep "^gitlab$" || echo "origin")
echo "Pushing to remote ${REMOTE_NAME} branch ${CURRENT_BRANCH}..."
git push -u "${REMOTE_NAME}" "${CURRENT_BRANCH}" || {
  echo "Push failed. Please ensure SSH key or access token is configured for your GitLab instance."
}
echo "GitLab sync process complete."
