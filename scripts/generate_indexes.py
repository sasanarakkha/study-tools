import os
import re
from pathlib import Path
from typing import List, Tuple, Optional
from tools.printer import printer as pr

# Configuration
DOCS_DIR = Path("docs")

def get_first_heading(file_path: Path) -> str:
    """Extracts the first # Heading from a markdown file."""
    if not file_path.exists():
        return file_path.stem
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"^#\s+(.+)$", line)
            if match:
                # Remove any markdown links from the heading
                heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", match.group(1))
                return heading.strip()
    return file_path.stem

def is_digit_prefixed(name: str) -> bool:
    return bool(re.match(r"^\d+", name))

def get_sort_key(item: Path) -> int:
    """Extracts leading digit for sorting, or 9999 if no digit."""
    match = re.match(r"^(\d+)", item.name)
    if match:
        return int(match.group(1))
    return 9999

def generate_index_for_dir(dir_path: Path, is_root: bool = False) -> Optional[Tuple[str, str]]:
    """
    Generates an index.md for the directory.
    Returns (Title, Link) for the parent to use.
    """
    # Get all digit-prefixed children (files and folders)
    # Plus specific non-digit ones we want to include (like Notebook LM if it's in root)
    digit_children = sorted([
        item for item in dir_path.iterdir() 
        if (is_digit_prefixed(item.name) or (is_root and item.suffix == ".md" and item.name != "index.md"))
        and not item.name.startswith(".")
    ], key=get_sort_key)

    if not digit_children and not is_root and not (dir_path / ".header.md").exists():
        return None

    # Promotion Logic: If NOT root and exactly one digit child and NO .header.md in this dir
    if not is_root and len(digit_children) == 1 and not (dir_path / ".header.md").exists():
        child = digit_children[0]
        if child.is_file() and child.suffix == ".md":
            return get_first_heading(child), os.path.relpath(child, dir_path.parent)
        elif child.is_dir():
            res = generate_index_for_dir(child)
            if res:
                title, rel_link = res
                return title, os.path.join(child.name, rel_link)

    # Collect items for the list
    items = []
    for child in digit_children:
        if child.is_file():
            if child.suffix == ".md" and child.name != "index.md":
                items.append((get_first_heading(child), child.name))
        elif child.is_dir():
            # For folders, recursively find what to link to
            res = generate_index_for_dir(child)
            if res:
                items.append(res)

    # Write index.md
    content = []
    header_file = dir_path / ".header.md"
    if header_file.exists():
        with open(header_file, "r", encoding="utf-8") as f:
            content.append(f.read().strip())
            content.append("") # Spacer
    else:
        # Fallback heading
        title = "Home" if is_root else dir_path.name.split("-", 1)[-1].replace("-", " ").replace("_", " ").title()
        content.append(f"# {title}")
        content.append("")

    for title, link in items:
        content.append(f"- [{title}]({link})")

    index_file = dir_path / "index.md"
    with open(index_file, "w", encoding="utf-8") as f:
        f.write("\n".join(content) + "\n")
    
    # Return info for parent
    dir_title = get_first_heading(index_file)
    return dir_title, os.path.join(dir_path.name, "index.md")

def main():
    pr.green("Generating index pages")
    
    # Generate root index first (which will recursively generate all others)
    generate_index_for_dir(DOCS_DIR, is_root=True)
    
    pr.yes("ok")

if __name__ == "__main__":
    main()
