"""Generate PDF documents from Pāli class markdown content using WeasyPrint."""

import argparse
import os
import re
import sys
import markdown
from bs4 import BeautifulSoup
from tools.printer import printer as pr

# Ensure Homebrew libraries are found on macOS
if sys.platform == "darwin":
    homebrew_lib = "/opt/homebrew/lib"
    if os.path.exists(homebrew_lib):
        if "DYLD_LIBRARY_PATH" in os.environ:
            os.environ["DYLD_LIBRARY_PATH"] = (
                f"{homebrew_lib}:{os.environ['DYLD_LIBRARY_PATH']}"
            )
        else:
            os.environ["DYLD_LIBRARY_PATH"] = homebrew_lib

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

CSS_PATHS = [
    "identity/sbs-pdf-fonts.css",
    "identity/sbs-pdf-variables.css",
    "identity/sbs-pdf.css",
    "identity/sbs-pdf-extra.css",
]


def clean_markdown_content(content):
    """Remove UI elements not suitable for PDF."""
    content = re.sub(r'<div class="nav-links">.*?</div>', "", content, flags=re.DOTALL)
    content = re.sub(r'<div class="feedback">.*?</div>', "", content, flags=re.DOTALL)
    content = re.sub(
        r'<a[^>]+class="(prev|previous|next|cross)"[^>]*>.*?</a>', "", content
    )
    return content


def pre_process_content(text):
    """Protects source footnote and list markers from renumbering."""

    def repl_newlines(m):
        count = m.group(0).count("\n")
        if count > 2:
            return "\n\n" + "<br>\n" * (count - 2)
        return m.group(0)

    text = re.sub(r"\n{3,}", repl_newlines, text)

    def repl_def(m):
        prefix = m.group(1)
        fn_num = m.group(2)
        content = m.group(3).strip()
        return f"\n<div class='manual-fn-def' data-fn='{fn_num}' markdown='1'>\n\n{prefix}{content}\n\n</div>\n\n"

    pattern = r"^([ \t*_]*)\[\^(\d+)\]:\s*(.*?)(?=\n[ \t]*\n|\n[ \t]*[-*_]{3,}|\n[ \t]*#|\n\[\^|\Z)"
    text = re.sub(pattern, repl_def, text, flags=re.MULTILINE | re.DOTALL)
    text = re.sub(
        r"\[\^(\d+)\]", r"<sup class='manual-fn-ref' data-fn='\1'>\1</sup>", text
    )

    def repl_list(m):
        num = m.group(1)
        return f"\n<div class='manual-list-start' data-start='{num}'></div>\n\n{num}. "

    text = re.sub(r"^\s*(\d+)\.\s+", repl_list, text, flags=re.MULTILINE)
    text = re.sub(r"(<br>\n)+(\|)", r"\n\2", text)
    return text


def resolve_image_paths(content: str, file_path: str) -> str:
    """Convert relative image paths to absolute so WeasyPrint can find them."""
    file_dir = os.path.dirname(os.path.abspath(file_path))

    def replacer(match):
        alt, src = match.group(1), match.group(2)
        if not src.startswith("http") and not os.path.isabs(src):
            src = os.path.normpath(os.path.join(file_dir, src))
        return f"![{alt}]({src})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replacer, content)


def mark_wide_tables(
    html_content: str, col_threshold: int = 7, row_threshold: int = 12
) -> str:
    """Add sizing and layout classes to tables based on column count and row count."""
    soup = BeautifulSoup(html_content, "html.parser")
    for table in soup.find_all("table"):
        first_row = table.find("tr")
        if not first_row:
            continue
        cols = len(first_row.find_all(["td", "th"]))
        rows = len(table.find_all("tr"))
        classes = list(table.get("class") or [])
        if cols >= col_threshold:
            text_len = len(table.get_text())
            effective_cols = cols
            if text_len > 800 and cols < 10:
                effective_cols = cols + 1
            capped = min(effective_cols, 10)
            classes += ["wide-table", f"cols-{capped}"]
        if rows > row_threshold:
            classes.append("long-table")
        if classes:
            table["class"] = " ".join(classes)
    return str(soup)


def equalize_table_columns(html_content: str) -> str:
    """Set explicit equal-width on every cell so WeasyPrint renders truly equal columns."""
    soup = BeautifulSoup(html_content, "html.parser")
    for table in soup.find_all("table"):
        first_row = table.find("tr")
        if not first_row:
            continue
        n = len(first_row.find_all(["td", "th"]))
        if n < 2:
            continue
        col_width = f"{100 / n:.4f}%"
        for cell in table.find_all(["td", "th"]):
            cell["style"] = f"width: {col_width};"
    return str(soup)


def remove_empty_thead(html_content):
    """Removes thead elements where all th cells are empty, preventing double borders."""
    soup = BeautifulSoup(html_content, "html.parser")
    for thead in soup.find_all("thead"):
        th_cells = thead.find_all("th")
        if th_cells and all(not th.get_text(strip=True) for th in th_cells):
            thead.decompose()
    return str(soup)


def process_footnotes_for_pdf(html_content):
    """Moves manual footnote definitions into WeasyPrint-compatible floats with bidirectional links.
    Also marks standalone image paragraphs in the same pass to avoid an extra parse cycle."""
    soup = BeautifulSoup(html_content, "html.parser")
    for p in soup.find_all("p"):
        meaningful = [
            c for c in p.children if getattr(c, "name", None) or str(c).strip()
        ]
        if len(meaningful) == 1 and getattr(meaningful[0], "name", None) == "img":
            existing = p.get("class") or []
            if isinstance(existing, list):
                existing = " ".join(str(c) for c in existing)
            p["class"] = f"{existing} standalone-image".strip()
    defs = {d["data-fn"]: d for d in soup.find_all("div", class_="manual-fn-def")}
    for ref in soup.find_all("sup", class_="manual-fn-ref"):
        fn_num = ref["data-fn"]
        ref["id"] = f"fnref-{fn_num}"
        a_link = soup.new_tag("a", href=f"#fn-{fn_num}")
        a_link.string = str(fn_num)
        ref.clear()
        ref.append(a_link)
        if fn_num in defs:
            new_span = soup.new_tag(
                "span", attrs={"class": "pdf-footnote", "id": f"fn-{fn_num}"}
            )
            label = soup.new_tag("b", attrs={"class": "pdf-footnote-label"})
            label.string = f"{fn_num}. "
            new_span.append(label)
            fn_soup = BeautifulSoup(defs[fn_num].decode_contents(), "html.parser")
            for p in fn_soup.find_all("p"):
                p.unwrap()
            new_span.append(fn_soup)
            backref = soup.new_tag(
                "a", href=f"#fnref-{fn_num}", attrs={"class": "pdf-footnote-backref"}
            )
            backref.string = " ↩"
            new_span.append(backref)
            ref.insert_after(new_span)
    for d in defs.values():
        d.decompose()
    for strong in soup.find_all("strong"):
        fn_spans = strong.find_all("span", class_="pdf-footnote")
        for fn_span in reversed(fn_spans):
            fn_span.extract()
            strong.insert_after(fn_span)
    return str(soup)


def post_process_html(html_content: str) -> str:
    """Single-pass HTML post-processor combining link fixing, table marking, footnote processing."""
    soup = BeautifulSoup(html_content, "html.parser")

    for a in soup.find_all("a", href=True):
        href = str(a["href"])
        if ".md" in href and not href.startswith("http"):
            file_part = href.split("#")[0] if "#" in href else href
            basename = os.path.basename(file_part)
            if basename == "index.md":
                parts = [
                    p
                    for p in file_part.replace("\\", "/").split("/")
                    if p and p != ".."
                ]
                anchor_id = "_".join(parts).replace(".", "_")
            else:
                anchor_id = basename.replace(".", "_")
            a["href"] = f"#{anchor_id}"

    for marker in soup.find_all("div", class_="manual-list-start"):
        start_val = str(marker.get("data-start") or "1")
        next_ol = marker.find_next_sibling("ol")
        if next_ol:
            next_ol["start"] = start_val
            next_ol["style"] = f"counter-reset: list-item {int(start_val) - 1};"
        marker.decompose()

    for thead in soup.find_all("thead"):
        th_cells = thead.find_all("th")
        if th_cells and all(not th.get_text(strip=True) for th in th_cells):
            thead.decompose()

    for table in soup.find_all("table"):
        first_row = table.find("tr")
        if not first_row:
            continue
        cols = len(first_row.find_all(["td", "th"]))
        rows = len(table.find_all("tr"))
        classes = list(table.get("class") or [])
        if cols >= 7:
            effective_cols = (
                cols + 1 if len(table.get_text()) > 800 and cols < 10 else cols
            )
            classes += ["wide-table", f"cols-{min(effective_cols, 10)}"]
        if rows > 12:
            classes.append("long-table")
        if classes:
            table["class"] = " ".join(classes)

    for p in soup.find_all("p"):
        meaningful = [
            c for c in p.children if getattr(c, "name", None) or str(c).strip()
        ]
        if len(meaningful) == 1 and getattr(meaningful[0], "name", None) == "img":
            existing = p.get("class") or []
            if isinstance(existing, list):
                existing = " ".join(str(c) for c in existing)
            p["class"] = f"{existing} standalone-image".strip()

    defs = {d["data-fn"]: d for d in soup.find_all("div", class_="manual-fn-def")}
    for ref in soup.find_all("sup", class_="manual-fn-ref"):
        fn_num = ref["data-fn"]
        ref["id"] = f"fnref-{fn_num}"
        a_link = soup.new_tag("a", href=f"#fn-{fn_num}")
        a_link.string = str(fn_num)
        ref.clear()
        ref.append(a_link)
        if fn_num in defs:
            new_span = soup.new_tag(
                "span", attrs={"class": "pdf-footnote", "id": f"fn-{fn_num}"}
            )
            label = soup.new_tag("b", attrs={"class": "pdf-footnote-label"})
            label.string = f"{fn_num}. "
            new_span.append(label)
            fn_soup = BeautifulSoup(defs[fn_num].decode_contents(), "html.parser")
            for fp in fn_soup.find_all("p"):
                fp.unwrap()
            new_span.append(fn_soup)
            backref = soup.new_tag(
                "a", href=f"#fnref-{fn_num}", attrs={"class": "pdf-footnote-backref"}
            )
            backref.string = " ↩"
            new_span.append(backref)
            ref.insert_after(new_span)
    for d in defs.values():
        d.decompose()
    for strong in soup.find_all("strong"):
        fn_spans = strong.find_all("span", class_="pdf-footnote")
        for fn_span in reversed(fn_spans):
            fn_span.extract()
            strong.insert_after(fn_span)

    return str(soup)


def build_html_document(
    title,
    files_data,
    title_md_content="",
    literature_md_content="",
    folder_type="",
    root_index_content="",
):
    md = markdown.Markdown(
        extensions=[
            "toc",
            "tables",
            "fenced_code",
            "attr_list",
            "sane_lists",
            "md_in_html",
            "nl2br",
        ]
    )

    def conv(t):
        return md.convert(pre_process_content(t))

    title_html = f'<div class="pdf-title-page"><h1>{title}</h1></div>'
    about_html = (
        f'<div class="pdf-about-page">{conv(title_md_content)}</div>'
        if title_md_content
        else ""
    )
    lit_html = (
        f'<div class="pdf-literature-page">{conv(literature_md_content)}</div>'
        if literature_md_content
        else ""
    )

    # Sentinel-marker approach: convert all files in one pass to fix TOC dedup
    SENTINEL = "<!--FILE-BOUNDARY:{idx}-->"
    raw_chunks = []
    file_metadata = []
    for idx, (file_path, content) in enumerate(files_data):
        is_idx = os.path.basename(file_path) == "index.md"
        c = clean_markdown_content(content)
        c = resolve_image_paths(c, file_path)

        if not is_idx and not (
            folder_type.endswith("_ex") or folder_type.endswith("_key")
        ):
            c = re.sub(r"^# Class \d+.*?\n", "", c, flags=re.MULTILINE)

        raw_chunks.append(SENTINEL.format(idx=idx) + "\n\n" + pre_process_content(c))
        file_metadata.append({"file_path": file_path, "is_idx": is_idx})

    # Convert all files' markdown in a single pass so toc extension dedup sees all headings
    combined_md = "\n\n".join(raw_chunks)
    md.reset()
    combined_html = md.convert(combined_md)
    combined_toc = getattr(md, "toc", "")  # Capture TOC before it may be overwritten

    # Split on sentinel markers to recover per-file HTML
    pattern = r"<!--FILE-BOUNDARY:(\d+)-->"
    parts = re.split(pattern, combined_html)
    # parts[0]=leading content, parts[1]='0', parts[2]=file0 html, parts[3]='1', parts[4]=file1 html...

    full_course_html = ""
    for i in range(1, len(parts), 2):
        file_idx = int(parts[i])
        chunk_html = parts[i + 1] if i + 1 < len(parts) else ""

        metadata = file_metadata[file_idx]
        is_idx = metadata["is_idx"]
        file_path = metadata["file_path"]

        # Apply per-file heading shift for bpc/ipc non-index files
        if not is_idx and folder_type in ("bpc", "ipc"):
            chunk_html = re.sub(
                r"<(/?)h([1-5])",
                lambda m: f"<{m.group(1)}h{int(m.group(2)) + 1}",
                chunk_html,
            )

        # Compute file id and div class
        if is_idx:
            parent = os.path.basename(os.path.dirname(file_path))
            file_id = f"{parent}_index_md"
        else:
            file_id = os.path.basename(file_path).replace(".", "_")
        div_class = "pdf-class-header" if is_idx else "pdf-topic-page"

        full_course_html += (
            f"<div class='{div_class}' id='{file_id}'>{chunk_html}</div>"
        )

    if root_index_content:
        md.reset()
        toc_html = f'<div class="pdf-toc-page" id="toc-page">{md.convert(pre_process_content(root_index_content))}</div>'
    else:
        # Use the correctly de-duplicated TOC from the combined conversion above
        toc_html = (
            f'<div class="pdf-toc-page"><h1>Table of Contents</h1>{combined_toc}</div>'
        )

    full_body_html = f"{title_html}{about_html}{lit_html}{toc_html}<div class='content'>{full_course_html}</div>"
    full_body_html = post_process_html(full_body_html)
    if folder_type in ("bpc_ex", "ipc_ex"):
        full_body_html = equalize_table_columns(full_body_html)

    body_class = f' class="{folder_type}"' if folder_type else ""
    return f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>{title}</title><style>.pdf-title-page, .pdf-about-page, .pdf-literature-page, .pdf-toc-page, .pdf-class-header, .pdf-topic-page {{ page-break-before: always; }} .pdf-title-page {{ page-break-before: avoid; }} .manual-list-start {{ display: none; }} p:not(.standalone-image) img, td img, li img {{ height: 1em; width: auto; vertical-align: middle; }} .standalone-image {{ text-align: center; margin: 1em 0; }} .standalone-image img {{ height: auto !important; width: auto !important; max-width: 90%; display: block; margin: 0 auto; }} sup.manual-fn-ref a {{ text-decoration: none; color: inherit; }} .pdf-footnote-backref {{ font-style: normal; text-decoration: none; color: inherit; margin-left: 0.2em; }}</style></head><body{body_class}>{full_body_html}</body></html>"


def generate_pdf(html_content, output_pdf, css_paths=None):
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration

    font_config = FontConfiguration()
    css_objs = [
        CSS(filename=p, font_config=font_config)
        for p in (css_paths or [])
        if os.path.exists(p)
    ]
    HTML(string=html_content, base_url=os.path.abspath(".")).write_pdf(
        output_pdf, stylesheets=css_objs, font_config=font_config
    )


def _is_within(path: str, base_dir: str) -> bool:
    """Check if path is within base_dir (inclusive)."""
    base_abs = os.path.abspath(base_dir)
    path_abs = os.path.abspath(path)
    return path_abs == base_abs or path_abs.startswith(base_abs + os.sep)


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


def extract_suttas_toc_source(suttas_files: list[str]) -> str:
    """Curated TOC markdown: the 'Suttas and passages' section of
    1-pali-class-adv.md, limited to links we actually kept."""
    index_path = INDEX_FILES["suttas"]
    index_base = os.path.dirname(os.path.abspath(index_path))
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    m = re.search(r"## \*\*Suttas and passages\*\*\n(.*?)(?=\n## )", content, re.DOTALL)
    section = m.group(1) if m else ""
    kept = {os.path.abspath(p) for p in suttas_files}

    def keep_link(match):
        href = match.group(2)
        if href.startswith("http"):
            return match.group(0)
        abs_path = os.path.normpath(os.path.join(index_base, href))
        return match.group(0) if abs_path in kept else match.group(1)

    return re.sub(r"\[([^\]]+)\]\(([^)#\s]+\.md)\)", keep_link, section)


def get_markdown_files() -> dict[str, list[str]]:
    """Discover content files for each folder by parsing markdown links in index files."""
    result: dict[str, list[str]] = {}
    for folder_key, index_path in INDEX_FILES.items():
        index_base = os.path.dirname(os.path.abspath(index_path))
        with open(index_path, "r", encoding="utf-8") as f:
            index_content = f.read()

        if folder_key == "suttas":
            suttas_dir = FOLDER_DIRS["suttas"]
            files: list[str] = []
            for top_file in parse_md_links(index_content, index_base):
                if not _is_within(top_file, suttas_dir):
                    continue
                files.append(top_file)
                with open(top_file, "r", encoding="utf-8") as f:
                    sub_content = f.read()
                top_base = os.path.dirname(top_file)
                for child in parse_md_links(sub_content, top_base):
                    if _is_within(child, suttas_dir) and child not in files:
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
        description="Generate PDF documents from Pāli class markdown."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        choices=list(FOLDER_NAMES.keys()),
        help="Generate only this folder (default: all)",
    )
    parser.add_argument(
        "--html-only",
        action="store_true",
        help="Write intermediate HTML to output/pdf/<folder>_debug.html, skip WeasyPrint",
    )
    args = parser.parse_args()

    output_dir = "output/pdf"
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

        root_index = ""
        if fld == "suttas":
            root_index = extract_suttas_toc_source(files)

        html = build_html_document(
            title=FOLDER_NAMES[fld],
            files_data=data,
            title_md_content="",
            literature_md_content="",
            folder_type=fld,
            root_index_content=root_index,
        )

        if args.html_only:
            debug_path = os.path.join(output_dir, f"{fld}_debug.html")
            with open(debug_path, "w", encoding="utf-8") as f:
                f.write(html)
            pr.yes(f"html → {debug_path}")
        else:
            out_path = os.path.join(output_dir, f"{fld}.pdf")
            generate_pdf(html, out_path, css_paths=CSS_PATHS)
            pr.yes("ok")


if __name__ == "__main__":
    main()
