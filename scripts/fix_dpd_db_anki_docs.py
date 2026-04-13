"""Update dpd-db scripts to write formatted Markdown files for anki field lists."""
import re
from pathlib import Path

FILES = [
    Path("/Users/deva/Documents/dpd-db/scripts/work_with_csv/anki_class_grammar.py"),
    Path("/Users/deva/Documents/dpd-db/scripts/dps_archive/from_dps_csv_to_anki_csvs.py"),
    Path("/Users/deva/Documents/dpd-db/scripts/export/anki_csv.py")
]

def update_file(p: Path):
    if not p.exists():
        print(f"Skipping {p}: not found")
        return
    
    content = p.read_text(encoding="utf-8")
    
    # 1. Update filenames from .txt to .md
    content = content.replace('.txt"', '.md"')

    # 2. Update field-list writing to include Markdown formatting
    def replacer(match):
        indent = match.group(1)
        path_expr = match.group(2)
        var_name = match.group(3)
        extra_lines = match.group(4) # Lines between with open and write
        content_expr = match.group(5)
        
        # Extract deck name from path for title
        deck = "Unknown"
        deck_match = re.search(r"field-list-([\w-]+)\.md", path_expr) or re.search(r"field-list-([\w-]+)\.md", content)
        if deck_match:
            deck = deck_match.group(1).replace("-", " ").title()
        elif "grammar_abbr_path" in path_expr:
            deck = "Grammar Abbr"
        elif "grammar_sandhi_path" in path_expr:
            deck = "Grammar Sandhi"
        elif "grammar_grammar_path" in path_expr:
            deck = "Grammar Gramm"
        
        return (f'{indent}with open({path_expr}, "w") as {var_name}:\n'
                f'{extra_lines}'
                f'{indent}    {var_name}.write("# Field List: {deck}\\n\\n```\\n")\n'
                f'{indent}    {var_name}.write({content_expr})\n'
                f'{indent}    {var_name}.write("\\n```\\n")')

    # Matches: with open(..., "w") as ...:\n(maybe some lines)\n    ....write(...)
    # Group 4 is the extra lines
    pattern = re.compile(r'^(\s+)with open\((.+?), "w"\) as (.+?):\n((?:\s+.+\n)*?)\s+\3\.write\((.+?)\)', re.MULTILINE)
    
    new_content = pattern.sub(replacer, content)
    
    if new_content != content:
        p.write_text(new_content, encoding="utf-8")
        print(f"Updated {p}")
    else:
        print(f"No changes in {p}")

if __name__ == "__main__":
    for f in FILES:
        update_file(f)
