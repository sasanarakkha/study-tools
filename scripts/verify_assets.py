"""Verify all image references in docs/ point to existing files."""

import re
import sys
from pathlib import Path

from tools.printer import printer as pr

PROJECT_ROOT = Path(__file__).parent.parent
DOCS_DIR = PROJECT_ROOT / "docs"
IMG_REF_RE = re.compile(r"!\[.*?\]\(([^)]+)\)")


def main() -> None:
    pr.green("verify assets")
    broken = []

    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        for match in IMG_REF_RE.finditer(content):
            path_str = match.group(1)
            if path_str.startswith(("http://", "https://")):
                continue
            resolved = (md_file.parent / path_str).resolve()
            if not resolved.exists():
                broken.append(f"{md_file.relative_to(PROJECT_ROOT)}: {path_str}")

    if broken:
        pr.no(f"{len(broken)} broken")
        for item in broken:
            pr.warning(item)
        sys.exit(1)

    pr.yes("ok")


if __name__ == "__main__":
    main()
