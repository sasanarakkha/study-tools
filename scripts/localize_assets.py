import os
import re
import requests
import hashlib
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.parse import urlparse
from tools.printer import printer as pr

# Configuration
DOCS_DIR = Path("docs")
ASSETS_DIR = DOCS_DIR / "assets" / "images"
GITHUB_ASSET_PATTERNS = [
    re.compile(r"https://github\.com/[^/]+/[^/]+/assets/[^/]+/[a-f0-9-]+"),
    re.compile(r"https://github\.com/user-attachments/assets/[a-f0-9-]+"),
    re.compile(r"https://user-images\.githubusercontent\.com/\d+/[a-f0-9-]+\.png")
]
LOCAL_GH_PATTERN = re.compile(r"gh-[a-f0-9]+\.png")

# To keep track of processed assets and their new names
# Key: original source (URL or relative path), Value: new filename (just the name)
asset_map: Dict[str, str] = {}

def get_contextual_name(file_path: Path, match_start: int, alt_text: str = "") -> str:
    """Generates a contextual name from alt text or nearest heading."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Try alt text if it's descriptive
    if alt_text and len(alt_text) > 3 and alt_text.lower() not in ["image", "pali", "picture"]:
        name = re.sub(r"[^a-z0-9]+", "-", alt_text.lower()).strip("-")
        if name:
            return name

    # 2. Search for the nearest preceding heading
    preceding_content = content[:match_start]
    headings = re.findall(r"^#+\s+(.+)$", preceding_content, re.MULTILINE)
    if headings:
        last_heading = headings[-1]
        name = re.sub(r"[^a-z0-9]+", "-", last_heading.lower()).strip("-")
        if name:
            return name

    # 3. Fallback to filename or hash (handled by caller)
    return ""

def download_asset(url: str, dest_dir: Path, base_name: str) -> str:
    """Downloads an asset and returns the final filename."""
    ext = ".png" # Assume png for these github assets
    final_name = f"{base_name}{ext}"
    dest_path = dest_dir / final_name
    
    # Ensure name is unique
    counter = 1
    while dest_path.exists():
        final_name = f"{base_name}-{counter}{ext}"
        dest_path = dest_dir / final_name
        counter += 1
    
    pr.blue(f"Downloading {url} to {dest_path}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(dest_path, "wb") as f:
            f.write(response.content)
        return final_name
    except Exception as e:
        pr.red(f"Error downloading {url}: {e}")
        return ""

def process_markdown_files():
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    
    md_files = list(DOCS_DIR.rglob("*.md"))
    
    # First pass: identify and localize/rename all assets
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Find Markdown image tags ! [alt] (url)
        for match in re.finditer(r"!\[(.*?)\]\((.*?)\)", content):
            alt, src = match.groups()
            process_asset(md_file, src, alt, match.start())

        # Find HTML image tags <img ... src="url" ... alt="alt" ... >
        for match in re.finditer(r'<img\s+[^>]*src=["\'](.*?)["\'][^>]*>', content):
            src = match.group(1)
            # Try to find alt in the same tag
            alt_match = re.search(r'alt=["\'](.*?)["\']', match.group(0))
            alt = alt_match.group(1) if alt_match else ""
            process_asset(md_file, src, alt, match.start())

    # Second pass: update all markdown files with new names and relative paths
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        
        def replace_link(match):
            full_match = match.group(0)
            alt, src = match.groups()
            if src in asset_map:
                new_filename = asset_map[src]
                rel_assets_dir = os.path.relpath(ASSETS_DIR, md_file.parent)
                new_src = os.path.join(rel_assets_dir, new_filename)
                return f"![{alt}]({new_src})"
            return full_match

        new_content = re.sub(r"!\[(.*?)\]\((.*?)\)", replace_link, new_content)

        def replace_html(match):
            full_tag = match.group(0)
            src = match.group(1)
            if src in asset_map:
                new_filename = asset_map[src]
                rel_assets_dir = os.path.relpath(ASSETS_DIR, md_file.parent)
                new_src = os.path.join(rel_assets_dir, new_filename)
                return full_tag.replace(src, new_src)
            return full_tag

        new_content = re.sub(r'<img\s+[^>]*src=["\'](.*?)["\'][^>]*>', replace_html, new_content)
        
        if new_content != content:
            with open(md_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            pr.yes(f"Updated links in {md_file}")

def process_asset(md_file: Path, src: str, alt: str, match_pos: int):
    if src in asset_map:
        return

    is_github = any(p.match(src) for p in GITHUB_ASSET_PATTERNS)
    is_local_gh = LOCAL_GH_PATTERN.search(src)
    
    if not is_github and not is_local_gh:
        return

    # Determine contextual name
    base_name = get_contextual_name(md_file, match_pos, alt)
    if not base_name:
        # Fallback to a hash of the source to keep it unique
        base_name = "asset-" + hashlib.md5(src.encode()).hexdigest()[:8]

    if is_github:
        new_filename = download_asset(src, ASSETS_DIR, base_name)
        if new_filename:
            asset_map[src] = new_filename
    elif is_local_gh:
        # Find the existing file
        old_filename = Path(src).name
        old_path = ASSETS_DIR / old_filename
        if not old_path.exists():
            # Try searching for it relative to md_file
            old_path = (md_file.parent / src).resolve()
        
        if old_path.exists():
            ext = old_path.suffix
            new_filename = f"{base_name}{ext}"
            new_path = ASSETS_DIR / new_filename
            
            # Ensure name is unique
            counter = 1
            while new_path.exists() and new_path != old_path:
                new_filename = f"{base_name}-{counter}{ext}"
                new_path = ASSETS_DIR / new_filename
                counter += 1
            
            if new_path != old_path:
                pr.blue(f"Renaming {old_path} to {new_path}")
                os.rename(old_path, new_path)
            
            asset_map[src] = new_filename

if __name__ == "__main__":
    pr.green("Localizing assets")
    process_markdown_files()
    pr.yes("ok")
