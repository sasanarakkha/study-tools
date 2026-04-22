#!/bin/bash
# Create a new GitHub release and upload assets from temp-push/

# 1. Determine project root and move there
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd)"
cd "$PROJECT_ROOT" || exit 1

# Configuration
ASSET_DIR="temp-push"
SOURCE_SCRIPT="$ASSET_DIR/github-assets-uploader.sh"

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

# 3. Extract asset list
echo "Reading asset list from tools/for_release.py..."
assets=($(python3 tools/for_release.py))

if [ ${#assets[@]} -eq 0 ]; then
    echo "Error: Could not extract asset list from tools/for_release.py"
    exit 1
fi

# 4. Setup names
TAG="artifacts-$(date -u +'%d.%m.%Y_%H-%M-%S')"
NAME="Build $(date -u +'%d.%m.%Y %H:%M') UTC"
BODY=$(python3 tools/for_release.py body)

echo "Creating new draft release: $NAME"
echo "Tag: $TAG"

# 5. Create the release
gh release create "$TAG" \
    --title "$NAME" \
    --notes "$BODY" \
    --draft

# 6. Upload assets
echo "Uploading ${#assets[@]} assets from $ASSET_DIR/..."
for asset in "${assets[@]}"; do
    full_path="$ASSET_DIR/$asset"
    if [ ! -f "$full_path" ]; then
        echo "Warning: File $full_path not found, skipping..."
        continue
    fi
    echo "--> Uploading $asset"
    gh release upload "$TAG" "$full_path"
done

echo "Successfully created draft release and uploaded assets."
echo "Link: https://github.com/$GH_REPO/releases/tag/$TAG"
