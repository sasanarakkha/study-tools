#!/usr/bin/env python3
"""Fix external and absolute links in docs/ Markdown files by downloading images and rewriting paths."""

import os
import re
import requests
import hashlib
from pathlib import Path

# Configuration
DOCS_DIR = Path("docs")
ASSETS_DIR = DOCS_DIR / "assets"
ANKI_TARGET_DIR = Path("../anki")  # Relative to where the .md file is moved later
BASE_URL = "https://sasanarakkha.github.io/study-tools/"
GITHUB_BLOB_PREFIX = "https://github.com/sasanarakkha/study-tools/blob/main/anki-style/"

# Regex patterns
IMG_PATTERN = re.compile(r'!\[([^\]]*)\]\((https://user-images\.githubusercontent\.com/[^\)]+)\)')
ANKI_STYLE_PATTERN = re.compile(rf'{re.escape(GITHUB_BLOB_PREFIX)}([^\s\)]+)\.txt')
ABSOLUTE_LINK_PATTERN = re.compile(rf'{re.escape(BASE_URL)}([^\s\)]+)')

def download_image(url):
    """Download image and return the local filename."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Use hash of URL for filename to keep it stable and avoid collision
        ext = url.split('.')[-1]
        if '?' in ext:
            ext = ext.split('?')[0]
        if len(ext) > 4 or not ext.isalnum():
            ext = "png" # Fallback
            
        filename = f"gh-{hashlib.md5(url.encode()).hexdigest()[:10]}.{ext}"
        filepath = ASSETS_DIR / filename
        
        if not filepath.exists():
            ASSETS_DIR.mkdir(parents=True, exist_ok=True)
            with open(filepath, "wb") as f:
                f.write(response.content)
            return filename, True
        return filename, False # Already exists
    except Exception as e:
        print(f"  FAILED to download {url}: {e}")
        return None, False

def fix_file(file_path):
    """Process a single Markdown file."""
    content = file_path.read_text()
    original_content = content
    
    # 1. GitHub user-image links
    matches = IMG_PATTERN.findall(content)
    for alt, url in matches:
        filename, downloaded = download_image(url)
        if filename:
            # Calculate relative path from this file to assets/
            # For a file in docs/subdir/file.md, assets is at ../assets/
            rel_assets = os.path.relpath(ASSETS_DIR, file_path.parent)
            new_link = f"![{alt}]({rel_assets}/{filename})"
            content = content.replace(f"![{alt}]({url})", new_link)
            status = "DOWNLOADED" if downloaded else "EXISTED"
            print(f"  {status}: {url} -> {rel_assets}/{filename}")

    # 2. anki-style github blob links
    # Action: rewrite -> relative path to docs/anki/<file>.md
    matches = ANKI_STYLE_PATTERN.findall(content)
    for filename in matches:
        # The spec says Thread 3 moves anki-style to docs/anki/ and converts to .md
        # We rewrite the link format now.
        # We need a relative path to docs/anki/ from the current file
        rel_anki = os.path.relpath(DOCS_DIR / "anki", file_path.parent)
        old_link = f"{GITHUB_BLOB_PREFIX}{filename}.txt"
        new_link = f"{rel_anki}/{filename}.md"
        content = content.replace(old_link, new_link)
        print(f"  REWRITTEN: {old_link} -> {new_link}")

    # 3. Absolute site links
    # Pattern: https://sasanarakkha.github.io/study-tools/<path>
    matches = ABSOLUTE_LINK_PATTERN.findall(content)
    for path in matches:
        # Check if it points to a file that exists in docs/
        # path might be "anki-decks/sbs-pali-english-vocab.html" or similar
        # Jekyll used .html, MkDocs uses .md or directory URLs
        clean_path = path.replace(".html", "")
        potential_md = DOCS_DIR / f"{clean_path}.md"
        potential_index = DOCS_DIR / clean_path / "index.md"
        
        if potential_md.exists() or potential_index.exists():
            rel_path = os.path.relpath(DOCS_DIR / clean_path, file_path.parent)
            # MkDocs likes clean URLs, so if it's a .md we can just point to the name without .md
            # or with .md for local linking. MkDocs handles .md links by converting them.
            new_link = f"{rel_path}.md"
            old_full = f"{BASE_URL}{path}"
            content = content.replace(old_full, new_link)
            print(f"  REWRITTEN ABSOLUTE: {old_full} -> {new_link}")

    if content != original_content:
        file_path.write_text(content)
        return True
    return False

def main():
    print("Starting link fix script...")
    files_fixed = 0
    for md_file in DOCS_DIR.rglob("*.md"):
        print(f"Processing {md_file}...")
        if fix_file(md_file):
            files_fixed += 1
            
    print(f"\nFinished. Fixed {files_fixed} files.")

if __name__ == "__main__":
    main()
