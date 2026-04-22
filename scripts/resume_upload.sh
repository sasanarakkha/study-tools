#!/bin/bash
# Resume an interrupted GitHub release upload for the latest draft.

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

echo "Detecting latest draft release..."
TAG=$(gh release list --exclude-drafts=false --limit 10 --json isDraft,tagName --jq '.[] | select(.isDraft == true) | .tagName' | head -n 1)

if [ -z "$TAG" ]; then
    echo "Error: No draft release found."
    exit 1
fi

echo "Found draft release: $TAG"

# 3. Extract asset list
echo "Reading asset list from tools/for_release.py..."
assets=($(python3 tools/for_release.py))

if [ ${#assets[@]} -eq 0 ]; then
    echo "Error: Could not extract asset list from tools/for_release.py"
    exit 1
fi

# 4. Get list of already uploaded assets
echo "Fetching already uploaded assets for $TAG..."
uploaded_assets=$(gh release view "$TAG" --json assets --jq '.assets[].name' 2>/dev/null)

echo "Checking ${#assets[@]} assets in $ASSET_DIR/..."

for asset in "${assets[@]}"; do
    full_path="$ASSET_DIR/$asset"
    if [ ! -f "$full_path" ]; then
        echo "Warning: File $full_path not found, skipping..."
        continue
    fi
    
    # Check if the asset is already in the release
    if echo "$uploaded_assets" | grep -qx "$asset"; then
        echo "Skipping $asset (already uploaded)"
        continue
    fi
    
    echo "Uploading $asset..."
    # --clobber: overwrite if exists (fixes partial/stuck uploads)
    gh release upload "$TAG" "$full_path" --clobber
done

echo "Verification and upload complete for $TAG."
