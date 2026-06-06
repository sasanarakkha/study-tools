#!/bin/bash
# Upload a file to the latest release (draft or published).
# Usage: ./scripts/upload_asset.sh <file-or-path>
#   <file-or-path>  path to a file, or a bare filename resolved under temp-push/

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

# 3. Detect latest release (draft or published)
echo "Detecting latest release..."
TAG=$(gh release list --exclude-drafts=false --limit 1 --json tagName --jq '.[0].tagName')

if [ -z "$TAG" ]; then
    echo "Error: No release found."
    exit 1
fi

echo "Target release: $TAG"

# 4. Handle asset selection
ASSET_NAME="$1"

if [ -z "$ASSET_NAME" ]; then
    echo "No file provided. Available files in $ASSET_DIR/:"
    echo "------------------------------------------------"
    ls -1 "$ASSET_DIR" | grep -vE "(\.sh|\.env|head\.md)"
    echo "------------------------------------------------"
    echo "Usage: ./scripts/upload_asset.sh <file-or-path>"
    exit 0
fi

# Resolve: try as a path first, then under temp-push/
if [ -f "$ASSET_NAME" ]; then
    FULL_PATH="$ASSET_NAME"
elif [ -f "$ASSET_DIR/$ASSET_NAME" ]; then
    FULL_PATH="$ASSET_DIR/$ASSET_NAME"
else
    echo "Error: File not found: '$ASSET_NAME' (tried as path and under $ASSET_DIR/)"
    exit 1
fi

BASENAME="$(basename "$FULL_PATH")"

# 5. Upload
echo "Uploading $BASENAME to release $TAG..."
gh release upload "$TAG" "$FULL_PATH" --clobber

echo "Upload complete."
