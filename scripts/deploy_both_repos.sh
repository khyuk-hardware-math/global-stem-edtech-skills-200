#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PARENT_DIR="$(cd "$DIR/.." && pwd)"

echo "=== [1/2] Pushing global-stem-edtech-skills-200 ==="
git -C "$DIR" push -u origin main

if [ -d "$PARENT_DIR/khyuk-hardware-math" ]; then
    echo "=== [2/2] Pushing khyuk-hardware-math profile repo ==="
    git -C "$PARENT_DIR/khyuk-hardware-math" push -u origin main
fi

echo "=== All repositories successfully pushed to GitHub! ==="
