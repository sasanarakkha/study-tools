"""Update mkdocs.yaml navigation based on the actual directory structure and first headings."""
import yaml
import os
import re
from pathlib import Path
from typing import List, Dict, Union, Any
from tools.printer import printer as pr

# Configuration
DOCS_DIR = Path("docs")
MKDOCS_YAML = Path("mkdocs.yaml")

def get_first_heading(file_path: Path) -> str:
    """Extracts the first # Heading from a markdown file."""
    if not file_path or not file_path.exists():
        return ""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(r"^#\s+(.+)$", line)
            if match:
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

def get_nav_for_dir(dir_path: Path, is_root: bool = False) -> Union[List[Any], Dict[str, str]]:
    """Recursively builds navigation list for a directory."""
    
    # Get all children that start with a digit
    digit_children = sorted([
        item for item in dir_path.iterdir() 
        if is_digit_prefixed(item.name) and not item.name.startswith(".")
    ], key=get_sort_key)

    # Combine for the full list of content
    all_children = digit_children

    # Promotion Logic: If NOT root and exactly one child in total and NO index.md in this dir
    if not is_root and len(all_children) == 1 and not (dir_path / "index.md").exists():
        child = all_children[0]
        if child.is_file() and child.suffix == ".md":
            title = get_first_heading(child)
            return {title: str(child.relative_to(DOCS_DIR))}
        elif child.is_dir():
            return get_nav_for_dir(child, is_root=False)

    items = []
    # If root, we handle Home separately, otherwise we might include index.md as first item
    index_file = dir_path / "index.md"
    
    # Use digit children first
    for child in digit_children:
        if child.is_file() and child.suffix == ".md":
            title = get_first_heading(child)
            items.append({title: str(child.relative_to(DOCS_DIR))})
        elif child.is_dir():
            sub_res = get_nav_for_dir(child, is_root=False)
            if isinstance(sub_res, dict):
                items.append(sub_res)
            elif sub_res:
                child_index = child / "index.md"
                title = get_first_heading(child_index) if child_index.exists() else child.name.split("-", 1)[-1].replace("-", " ").title()
                if child_index.exists():
                    items.append({title: [str(child_index.relative_to(DOCS_DIR))] + sub_res})
                else:
                    items.append({title: sub_res})
            elif (child / "index.md").exists():
                child_index = child / "index.md"
                items.append({get_first_heading(child_index): str(child_index.relative_to(DOCS_DIR))})

    return items

def main():
    pr.green("Updating mkdocs.yaml navigation")
    
    with open(MKDOCS_YAML, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # Build nav recursively from root
    new_nav = [{"Home": "index.md"}]
    root_items = get_nav_for_dir(DOCS_DIR, is_root=True)
    if isinstance(root_items, list):
        new_nav.extend(root_items)
    else:
        new_nav.append(root_items)

    config["nav"] = new_nav

    class MyDumper(yaml.SafeDumper):
        def increase_indent(self, flow=False, indentless=False):
            return super(MyDumper, self).increase_indent(flow, False)

    with open(MKDOCS_YAML, "w", encoding="utf-8") as f:
        yaml.dump(config, f, Dumper=MyDumper, allow_unicode=True, sort_keys=False, default_flow_style=False)
    
    pr.yes("ok")

if __name__ == "__main__":
    main()
