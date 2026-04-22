#!/bin/bash
# Upload a single specific asset from temp-push/ to the latest draft release.

# 1. Determine project root and move there
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd)"
cd "$PROJECT_ROOT" || exit 1

# Configuration
ASSET_DIR="temp-push"

# 2. Handle Authentication
if [ -f "$ASSET_DIR/.env" ]; then
  source "$ASSET_DIR/.env"
  export GITHUB_TOKEN="$token"
elif [ -f ".env" ]; then
  source ".env"
  export GITHUB_TOKEN="$token"
fi

if ! gh auth status &>/dev/null && [ -z "$GITHUB_TOKEN" ]; then
  echo "Error: Not authenticated. Please run 'gh auth login' or provide a .env file."
  exit 1
fi

export GH_REPO="sasanarakkha/study-tools"

# 3. Detect latest draft
echo "Detecting latest draft release..."
TAG=$(gh release list --exclude-drafts=false --limit 10 --json isDraft,tagName --jq '.[] | select(.isDraft == true) | .tagName' | head -n 1)

if [ -z "$TAG" ]; then
    echo "Error: No draft release found."
    exit 1
fi

# 4. Handle asset selection
ASSET_NAME="$1"

if [ -z "$ASSET_NAME" ]; then
    echo "No asset name provided. Available files in $ASSET_DIR/:"
    echo "------------------------------------------------"
    ls -1 "$ASSET_DIR" | grep -vE "(\.sh|\.env|head\.md)"
    echo "------------------------------------------------"
    echo "Usage: ./scripts/upload_asset.sh <filename>"
    exit 0
fi

FULL_PATH="$ASSET_DIR/$ASSET_NAME"

if [ ! -f "$FULL_PATH" ]; then
    echo "Error: File $FULL_PATH not found."
    exit 1
fi

# 5. Upload
echo "Uploading $ASSET_NAME to release $TAG..."
gh release upload "$TAG" "$FULL_PATH" --clobber

echo "Upload complete."
