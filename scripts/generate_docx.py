"""Generate DOCX documents from Pāli class markdown content using Pandoc."""

import argparse
import os
import re
import pypandoc
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from tools.printer import printer as pr

# Ensure pandoc is available
try:
    pypandoc.get_pandoc_version()
except OSError:
    pr.warning("Pandoc not found. Downloading...")  # type: ignore[attr-defined]
    pypandoc.download_pandoc()

FOLDER_NAMES = {
    "bhikkhu-patimokkha": "Bhikkhu Pātimokkha - Word by Word Analysis",
    "sbs-per-analysis": "SBS Pāḷi-English Recitations - Analysis",
    "suttas": "Suttas and Passages - Word by Word Analysis",
}

INDEX_FILES = {
    "bhikkhu-patimokkha": "docs/6-pali-class/bhikkhu-patimokkha/index.md",
    "sbs-per-analysis": "docs/6-pali-class/sbs-per-analysis.md",
    "suttas": "docs/6-pali-class/1-pali-class-adv.md",
}

FOLDER_DIRS = {
    "bhikkhu-patimokkha": "docs/6-pali-class/bhikkhu-patimokkha",
    "sbs-per-analysis": "docs/6-pali-class/sbs-per-analysis",
    "suttas": "docs/6-pali-class/suttas",
}

SBS_FOLDERS = frozenset(FOLDER_NAMES.keys())

PAGEBREAK = '\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'


def clean_markdown_content(content: str) -> str:
    """Remove UI elements not suitable for DOCX."""
    content = re.sub(r'<div class="nav-links">.*?</div>', "", content, flags=re.DOTALL)
    content = re.sub(r'<div class="feedback">.*?</div>', "", content, flags=re.DOTALL)
    content = re.sub(
        r'<a[^>]+class="(prev|previous|next|cross)"[^>]*>.*?</a>', "", content
    )
    return content


def fix_internal_links(content: str) -> str:
    """Converts relative links to internal PDF/DOCX anchors."""

    def replacer(match):
        text = match.group(1)
        href = match.group(2)
        if (".md" in href) and not href.startswith("http"):
            file_part = href.split("#")[0] if "#" in href else href
            anchor_id = os.path.basename(file_part).replace(".", "_")
            return f"[{text}](#{anchor_id})"
        return match.group(0)

    pattern = r"\[([^\]]+)\]\(([^\)]+)\)"
    return re.sub(pattern, replacer, content)


def preprocess_inline_images(content: str) -> str:
    """Add height attribute to inline images so they render at symbol size in DOCX."""
    return re.sub(r"(!\[[^\]]*\]\([^)]+\))(?!\{)", r"\1{height=18px}", content)


def insert_h2_page_breaks(content: str) -> str:
    """Insert page breaks before ## headings in _ex files."""
    lines = content.split("\n")
    result = []
    for line in lines:
        if re.match(r"^## ", line):
            result.extend(
                [
                    "",
                    "```{=openxml}",
                    '<w:p><w:r><w:br w:type="page"/></w:r></w:p>',
                    "```",
                    "",
                ]
            )
        result.append(line)
    return "\n".join(result)


def make_heading_slug(text: str) -> str:
    """Convert heading text to Pandoc's auto-generated header identifier."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`#]", "", text)
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    text = re.sub(r"^[^a-z]+", "", text)
    return text or "section"


def build_manual_toc(files_data: list[tuple[str, str]]) -> str:
    """Build a Table of Contents from H1 and H2 headings across all source files."""
    lines = ["# Table of Contents", ""]
    for _file_path, content in files_data:
        for line in content.split("\n"):
            m = re.match(r"^(#{1,2}) (.+)", line)
            if m:
                level = len(m.group(1))
                text = re.sub(r"\s*\{[^}]+\}\s*$", "", m.group(2).strip())
                slug = make_heading_slug(text)
                indent = "    " if level == 2 else ""
                lines.append(f"{indent}- [{text}](#{slug})")
    lines.append("")
    return "\n".join(lines)


def aggregate_markdown(
    title: str,
    files_data: list[tuple[str, str]],
    folder: str = "",
    about_content: str = "",
    lit_content: str = "",
) -> str:
    """Combines multiple Markdown files into one."""
    aggregated = f"# {title}\n\n"
    if about_content:
        aggregated += f"{about_content}\n\n"
    if lit_content:
        aggregated += f"{lit_content}\n\n"

    if folder.endswith(("_ex", "_key")) or folder in SBS_FOLDERS:
        aggregated += build_manual_toc(files_data) + PAGEBREAK

    needs_file_pagebreaks = (
        folder in SBS_FOLDERS
        or folder in ("bpc", "ipc")
        or folder.endswith(("_ex", "_key"))
    )
    is_ex = folder.endswith("_ex")

    for i, (file_path, content) in enumerate(files_data):
        c = clean_markdown_content(content)
        c = fix_internal_links(c)
        c = preprocess_inline_images(c)

        if i > 0 and needs_file_pagebreaks:
            aggregated += PAGEBREAK

        if is_ex:
            c = insert_h2_page_breaks(c)

        anchor_id = os.path.basename(file_path).replace(".", "_")
        aggregated += f"[]{{#{anchor_id}}}\n\n"
        aggregated += f"{c}\n\n"

    return aggregated


def generate_docx(aggregated_md: str, output_docx: str, folder: str = "") -> None:
    """Converts aggregated markdown to .docx using pypandoc."""
    use_pandoc_toc = not (folder.endswith(("_ex", "_key")) or folder in SBS_FOLDERS)
    extra_args = ["--standalone", "--resource-path=docs:docs/assets/images:."]
    if use_pandoc_toc:
        extra_args += ["--toc", "--toc-depth=2"]
    pypandoc.convert_text(
        aggregated_md,
        "docx",
        format="markdown",
        outputfile=output_docx,
        extra_args=extra_args,
    )


def post_process_docx(docx_path: str, folder: str) -> None:
    """Post-process DOCX: merge exercise table footer rows and force field updates."""
    doc = Document(docx_path)

    if folder.endswith("_ex"):
        for table in doc.tables:
            if len(table.rows) < 2:
                continue
            last_row = table.rows[-1]
            if len(last_row.cells) <= 1:
                continue
            non_empty = sum(1 for c in last_row.cells if c.text.strip())
            if non_empty <= 1:
                last_row.cells[0].merge(last_row.cells[-1])

    update_fields = OxmlElement("w:updateFields")
    update_fields.set(qn("w:val"), "true")
    doc.settings.element.append(update_fields)

    doc.save(docx_path)


def parse_md_links(md_content: str, base_dir: str) -> list[str]:
    """Extract ordered .md file paths from markdown link syntax in document order."""
    paths = []
    for match in re.finditer(r"\[([^\]]+)\]\(([^)#\s]+\.md)\)", md_content):
        href = match.group(2)
        if href.startswith("http"):
            continue
        abs_path = os.path.normpath(os.path.join(base_dir, href))
        if os.path.isfile(abs_path) and abs_path not in paths:
            paths.append(abs_path)
    return paths


def get_markdown_files() -> dict[str, list[str]]:
    """Discover content files for each folder by parsing markdown links in index files."""
    result: dict[str, list[str]] = {}
    for folder_key, index_path in INDEX_FILES.items():
        index_base = os.path.dirname(os.path.abspath(index_path))
        with open(index_path, "r", encoding="utf-8") as f:
            index_content = f.read()

        if folder_key == "suttas":
            files: list[str] = []
            for top_file in parse_md_links(index_content, index_base):
                files.append(top_file)
                with open(top_file, "r", encoding="utf-8") as f:
                    sub_content = f.read()
                top_base = os.path.dirname(top_file)
                for child in parse_md_links(sub_content, top_base):
                    if child not in files:
                        files.append(child)
            result[folder_key] = files
        else:
            index_abs = os.path.abspath(index_path)
            files = [
                f
                for f in parse_md_links(index_content, index_base)
                if os.path.abspath(f) != index_abs
            ]
            result[folder_key] = files
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate DOCX documents from Pāli class markdown."
    )
    parser.add_argument(
        "--folder",
        choices=list(FOLDER_NAMES.keys()),
        help="Specific folder to generate (default: all)",
    )
    args = parser.parse_args()

    output_dir = "output/docs"
    os.makedirs(output_dir, exist_ok=True)

    pr.bip()
    f_by_dir = get_markdown_files()

    for fld, files in f_by_dir.items():
        if args.folder and fld != args.folder:
            continue
        if not files:
            pr.no(f"{fld}: no files found")
            continue

        pr.green(f"{fld}")
        data = []
        for file_path in files:
            with open(file_path, "r", encoding="utf-8") as f:
                data.append((file_path, f.read()))

        agg_md = aggregate_markdown(
            title=FOLDER_NAMES[fld],
            files_data=data,
            folder=fld,
        )

        out_path = os.path.join(output_dir, f"{fld}.docx")
        generate_docx(agg_md, out_path, folder=fld)
        post_process_docx(out_path, fld)
        pr.yes("ok")


if __name__ == "__main__":
    main()
