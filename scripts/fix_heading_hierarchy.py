"""Normalize heading hierarchy: convert bold first lines to headings, fix skipped levels."""

import re
import glob
from tools.printer import printer as pr

def process_file(filepath: str) -> bool:
    """Process a single markdown file. Returns True if changes were made."""
    with open(filepath, "r", encoding="utf-8") as f:
        original = f.read()

    lines = original.split("\n")

    # Skip YAML frontmatter
    content_start = 0
    if lines and lines[0].strip() == "---":
        content_start = 1
        while content_start < len(lines) and lines[content_start].strip() != "---":
            content_start += 1
        content_start += 1

    # Find first non-empty content line
    first_content = content_start
    while first_content < len(lines) and not lines[first_content].strip():
        first_content += 1

    # Convert bold first line to heading
    if first_content < len(lines):
        m = re.match(r"^\*\*([^*]+)\*\*$", lines[first_content].strip())
        if m:
            lines[first_content] = f"# {m.group(1)}"

    # Fix skipped heading levels
    prev_level = 0
    for i in range(content_start, len(lines)):
        m = re.match(r"^(#{1,6})\s+(.*)", lines[i])
        if m:
            level = len(m.group(1))
            text = m.group(2)
            if prev_level > 0 and level > prev_level + 1:
                new_level = prev_level + 1
                lines[i] = f"{'#' * new_level} {text}"
                prev_level = new_level
            else:
                prev_level = level

    result = "\n".join(lines)
    if result != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(result)
        return True
    return False


def main() -> None:
    pr.green("Fixing heading hierarchy")
    files = sorted(glob.glob("docs/**/*.md", recursive=True))
    count = 0
    for filepath in files:
        if process_file(filepath):
            count += 1

    if count > 0:
        pr.yes(f"{count} files")
    else:
        pr.yes("ok")


if __name__ == "__main__":
    main()
