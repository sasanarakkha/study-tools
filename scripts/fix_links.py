import os
import re
from pathlib import Path
from typing import Dict
from tools.printer import printer as pr

# Configuration
DOCS_DIR = Path("docs")

def normalize_name(name: str) -> str:
    """Normalizes a filename for fuzzy matching."""
    # Remove extension
    name = os.path.splitext(name)[0]
    # Remove leading digits and dash/underscore
    name = re.sub(r"^\d+[-_]", "", name)
    # Replace underscores with dashes
    name = name.replace("_", "-")
    return name.lower()

def build_file_map() -> Dict[str, Path]:
    """Builds a map of normalized filename to its absolute path."""
    file_map = {}
    for item in DOCS_DIR.rglob("*"):
        if item.is_file():
            # Store exact name (for exact matches)
            file_map[item.name.lower()] = item.resolve()
            
            # Store normalized name
            norm = normalize_name(item.name)
            if norm not in file_map:
                file_map[norm] = item.resolve()
            
            # Special case for SBS vocab
            if "sbs" in norm and "vocab" in norm:
                file_map["sbs-pali-english-vocab"] = item.resolve()
                
    return file_map

def fix_links():
    file_map = build_file_map()
    md_files = list(DOCS_DIR.rglob("*.md"))

    patterns = [
        (re.compile(r"\[([^\]]+)\]\(([^)]+)\)"), 0, 1), # [text](link)
        (re.compile(r'<img\s+[^>]*src=["\'](.*?)["\'][^>]*>'), -1, 0) # <img src="link">
    ]

    count = 0
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content
        
        for pattern, text_idx, link_idx in patterns:
            def replace_link(match):
                if text_idx != -1:
                    text = match.group(text_idx + 1)
                    link = match.group(link_idx + 1)
                else:
                    link = match.group(link_idx + 1)
                
                if link.startswith(("http", "mailto", "#")):
                    return match.group(0)

                anchor = ""
                if "#" in link:
                    link_no_anchor, anchor = link.split("#", 1)
                    anchor = "#" + anchor
                else:
                    link_no_anchor = link
                
                target_name = os.path.basename(link_no_anchor)
                if target_name.endswith(".html"):
                    target_name = target_name.replace(".html", ".md")
                
                current_target_path = (md_file.parent / link_no_anchor).resolve()
                if not current_target_path.exists():
                    found_path = None
                    norm_target = normalize_name(target_name)
                    
                    if target_name.lower() in file_map:
                        found_path = file_map[target_name.lower()]
                    elif norm_target in file_map:
                        found_path = file_map[norm_target]
                    
                    if found_path:
                        # CRITICAL: Do not automatically resolve to 'index.md' if it's in a 'templates' folder 
                        # unless it was an exact match.
                        if found_path.name == "index.md" and "templates" in str(found_path) and "template" not in norm_target:
                            return match.group(0)

                        rel_link = os.path.relpath(found_path, md_file.parent)
                        rel_link += anchor
                        if text_idx != -1:
                            return f"[{text}]({rel_link})"
                        else:
                            return match.group(0).replace(link, rel_link)

                return match.group(0)

            new_content = pattern.sub(replace_link, new_content)

        if new_content != content:
            with open(md_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            pr.yes(f"Fixed links in {md_file}")
            count += 1
    return count

if __name__ == "__main__":
    pr.green("Repairing broken links")
    count = fix_links()
    if count > 0:
        pr.yes(f"{count} files")
    else:
        pr.yes("ok")
