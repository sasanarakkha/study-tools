"""
Script to automatically fix broken relative links in Markdown files after a reorganization.
It searches for the target filename in the entire docs/ directory if the relative link is broken.
"""
import os
import re
from pathlib import Path

def resolve_link(base_file: Path, link_target: str) -> Path | None:
    # Strip anchor
    if '#' in link_target:
        link_target = link_target.split('#')[0]
    
    # Only handle .md and image files for now
    if not any(link_target.endswith(ext) for ext in ['.md', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp']):
        return None

    # Resolve relative path
    try:
        # Check if it's already an absolute path (starts with /)
        if link_target.startswith('/'):
            return None # Skip absolute paths for now
            
        target_path = (base_file.parent / link_target).resolve()
        return target_path
    except Exception:
        return None

def find_file_in_docs(filename, docs_dir):
    """Search for a file with the given name in the docs directory."""
    for root, _, files in os.walk(docs_dir):
        if filename in files:
            return Path(root) / filename
    return None

def fix_links_in_file(file_path, docs_dir):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    # Match markdown links: [text](target)
    link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
    # Match image links: ![alt](target)
    img_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
    
    def replace_link(match):
        text = match.group(1)
        target = match.group(2)
        
        # Skip external links
        if target.startswith(('http://', 'https://', 'mailto:', 'ftp:')):
            return match.group(0)
            
        # Skip anchors
        if target.startswith('#'):
            return match.group(0)
            
        resolved_path = resolve_link(file_path, target)
        
        # If link is broken
        if not resolved_path or not resolved_path.exists():
            # Get just the filename
            filename = target.split('/')[-1]
            if '#' in filename:
                filename = filename.split('#')[0]
                
            # If target was something like '../anki-decks/ru-pali-vocab.md'
            # filename is 'ru-pali-vocab.md'
            
            new_path = find_file_in_docs(filename, docs_dir)
            if new_path:
                # Calculate new relative path
                rel_path = os.path.relpath(new_path, file_path.parent)
                # Keep anchor if it existed
                anchor = target.split('#')[1] if '#' in target else None
                final_target = rel_path + (f"#{anchor}" if anchor else "")
                print(f"  Fixed link in {file_path.name}: {target} -> {final_target}")
                return f"[{text}]({final_target})"
            else:
                # Special case: maybe it was a .html link that should be .md
                if filename.endswith('.html'):
                    md_filename = filename.replace('.html', '.md')
                    new_path = find_file_in_docs(md_filename, docs_dir)
                    if new_path:
                        rel_path = os.path.relpath(new_path, file_path.parent)
                        anchor = target.split('#')[1] if '#' in target else None
                        final_target = rel_path + (f"#{anchor}" if anchor else "")
                        print(f"  Fixed link (.html->.md) in {file_path.name}: {target} -> {final_target}")
                        return f"[{text}]({final_target})"

        return match.group(0)

    def replace_img(match):
        alt = match.group(1)
        target = match.group(2)
        
        if target.startswith(('http://', 'https://')):
            return match.group(0)
            
        resolved_path = resolve_link(file_path, target)
        
        if not resolved_path or not resolved_path.exists():
            filename = target.split('/')[-1]
            new_path = find_file_in_docs(filename, docs_dir)
            if new_path:
                rel_path = os.path.relpath(new_path, file_path.parent)
                print(f"  Fixed image in {file_path.name}: {target} -> {rel_path}")
                return f"![{alt}]({rel_path})"
        
        return match.group(0)

    content = link_pattern.sub(replace_link, content)
    content = img_pattern.sub(replace_img, content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("Fixing moved links...")
    docs_dir = Path('docs').resolve()
    count = 0

    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                if fix_links_in_file(file_path, docs_dir):
                    count += 1

    if count > 0:
        print(f"Fixed links in {count} files")
    else:
        print("No broken links fixed.")

if __name__ == '__main__':
    main()
