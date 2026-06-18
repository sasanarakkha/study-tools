# Plan: PDF & DOCX Generators — Pāli Class Content

## Architecture Decisions

- **File discovery**: Custom `parse_md_links()` + `get_markdown_files()` replaces the
  reference's `mkdocs.yaml`-based approach. The three target folders are not in the nav.
- **Behavior**: All three folders are treated as `bpc_key`-style (flat, no about page,
  programmatic TOC from headings). Controlled via a `SBS_FOLDERS` constant set.
- **CSS**: Four parallel files in `identity/` with SBS brown (#593e26) replacing DPD blue.
  Static Inter TTF files committed to `identity/fonts/` — variable fonts cause Pāḷi
  character rendering bugs in WeasyPrint (CMap corruption of ṭ, ā, ḷ, etc.).
- **Output dirs**: `output/pdf/` and `output/docs/` (gitignored).
- **Suttas two-level**: Top-level suttas files (e.g. `sacca-samyutta-sn-56.md`) contain
  only links to child files in subdirs. The PDF must recursively expand them: include the
  top-level file as a chapter header, then each linked child file as content.
- **DOCX folder behaviour**: `SBS_FOLDERS` drives the same `_key`-style path in
  `aggregate_markdown()`: manual TOC from headings, page breaks between files,
  no Pandoc field-based TOC.
- **GitHub Action**: `gh release upload` appends to existing latest release (normal case).
  Creates a new release only if the latest already has `.pdf` / `.docx` assets.

---

## Phase 1 — Setup: Dependencies & Directories

### Task 1.1 [x] — Add Python dependencies
File to edit: `pyproject.toml`
Run from project root:
```
uv add weasyprint markdown pypandoc python-docx
```
This updates `pyproject.toml` and `uv.lock` automatically.

→ verify: `uv run python -c "import weasyprint, markdown, pypandoc, docx; print('ok')"` prints `ok`

### Task 1.2 [x] — Create output directories and update .gitignore
Create these two files (content is a single empty line):
```
output/pdf/.gitkeep
output/docs/.gitkeep
```
Edit `.gitignore` — append these two lines at the end:
```
output/pdf/
output/docs/
```

→ verify: `ls output/pdf/ output/docs/` shows `.gitkeep` in each; `cat .gitignore | grep output` shows both lines.

---

## Phase 2 — CSS & Fonts

### Task 2.1 [x] — Download static Inter fonts

Download the Inter v4.0 static fonts release. Static TTF files are required (NOT the
variable font) to prevent WeasyPrint CMap corruption of Pāḷi diacritics.

Run from project root:
```
mkdir -p identity/fonts
cd identity/fonts
curl -L -o inter-static.zip "https://github.com/rsms/inter/releases/download/v4.0/Inter-4.0.zip"
unzip -j inter-static.zip "Inter Desktop/Inter-Regular.ttf" -d .
unzip -j inter-static.zip "Inter Desktop/Inter-Bold.ttf" -d .
unzip -j inter-static.zip "Inter Desktop/Inter-Italic.ttf" -d .
unzip -j inter-static.zip "Inter Desktop/Inter-BoldItalic.ttf" -d .
rm inter-static.zip
```

If the zip path inside the archive differs, run `unzip -l inter-static.zip | grep -i "Regular\|Bold\|Italic"` to find the correct paths.

→ verify: `ls identity/fonts/` shows `Inter-Regular.ttf Inter-Bold.ttf Inter-Italic.ttf Inter-BoldItalic.ttf`

### Task 2.2 [x] — Create identity/sbs-pdf-fonts.css

Create file `identity/sbs-pdf-fonts.css` with this exact content:
```css
/* Registers Inter static fonts for WeasyPrint PDF generation.
   Static instances used (not variable font) to avoid Pango CMap corruption
   of composed Unicode characters (ṭ, ṃ, ḷ, ā etc.) used in Pāḷi text. */

@font-face {
    font-family: "Inter";
    src: url("fonts/Inter-Regular.ttf") format("truetype");
    font-weight: 400;
    font-style: normal;
}

@font-face {
    font-family: "Inter";
    src: url("fonts/Inter-Bold.ttf") format("truetype");
    font-weight: 700;
    font-style: normal;
}

@font-face {
    font-family: "Inter";
    src: url("fonts/Inter-Italic.ttf") format("truetype");
    font-weight: 400;
    font-style: italic;
}

@font-face {
    font-family: "Inter";
    src: url("fonts/Inter-BoldItalic.ttf") format("truetype");
    font-weight: 700;
    font-style: italic;
}

body {
    font-variant-ligatures: none;
    font-feature-settings: "liga" 0, "clig" 0;
}
```

→ verify: file exists at `identity/sbs-pdf-fonts.css`, url() paths point to `fonts/Inter-*.ttf`

### Task 2.3 [x] — Create identity/sbs-pdf-variables.css

Create file `identity/sbs-pdf-variables.css` with this exact content
(SBS brown replaces DPD blue):
```css
:root {
    --light: hsl(30, 30%, 96%);
    --light-shade: hsl(30, 30%, 92%);
    --dark: hsl(25, 40%, 10%);
    --dark-shade: hsl(25, 40%, 14%);
    --primary: #593e26;
    --primary-alt: #3d2614;
    --primary-text: #593e26;
    --shadow-default: 2px 2px 4px hsla(0, 0%, 20%, 0.4);
    --shadow-hover: 2px 2px 4px hsla(0, 0%, 20%, 0.5);
    --gray: hsl(0, 0%, 50%);
    --gray-light: hsl(0, 0%, 75%);
    --gray-dark: hsl(0, 0%, 25%);
    --gray-transparent: hsla(0, 0%, 50%, 0.25);
    --secondary: hsl(25, 60%, 45%);
}
```

→ verify: file exists, `--primary: #593e26` is present

### Task 2.4 [x] — Create identity/sbs-pdf.css

Create file `identity/sbs-pdf.css` with this exact content:
```css
body {
    font-family: "Inter", sans-serif;
}

p {
    line-height: 150%;
    margin: 0.8em 0;
    vertical-align: middle;
    text-align: left;
}

b {
    font-weight: 700;
}

a {
    color: var(--primary);
}

h1, h2, h3, h4, h5, h6 {
    color: var(--dark);
    margin-top: 1em;
    margin-bottom: 0.4em;
}

table {
    width: 100%;
    border-collapse: collapse;
    border-top: 1px solid var(--gray);
    border-bottom: 1px solid var(--gray);
    margin-bottom: 1em;
}

td, th {
    font-size: 1rem;
    padding: 8px;
    vertical-align: middle;
    text-align: left;
    border-bottom: 1px solid var(--gray-transparent);
}

th {
    font-weight: 700;
    background-color: var(--light-shade);
}

code {
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    font-size: 0.9em;
    background-color: var(--light-shade);
    padding: 1px 4px;
    border-radius: 3px;
}

hr {
    border: none;
    border-top: 1px solid var(--gray-transparent);
    margin: 1em 0;
}

.pdf-title-page h1 {
    font-size: 2.5em;
    text-align: center;
    margin-top: 40%;
    color: var(--primary);
}

.pdf-toc-page h1 {
    font-size: 1.8em;
    color: var(--primary);
    border-bottom: 2px solid var(--primary);
    padding-bottom: 0.3em;
}

.pdf-toc-page nav ul {
    list-style: none;
    padding-left: 0;
}

.pdf-toc-page nav ul li {
    margin: 0.3em 0;
}

.pdf-toc-page nav ul ul {
    padding-left: 1.5em;
}

.content h1 {
    font-size: 1.6em;
    color: var(--primary);
    border-bottom: 1px solid var(--gray-transparent);
    padding-bottom: 0.2em;
}

.content h2 {
    font-size: 1.3em;
    color: var(--primary-alt);
}
```

→ verify: file exists at `identity/sbs-pdf.css`

### Task 2.5 [x] — Create identity/sbs-pdf-extra.css

Create file `identity/sbs-pdf-extra.css`. This file contains ONLY `@media print` rules
(adapted from lines 277-404 of `/Users/deva/Documents/dpd-pali-courses/identity/extra.css`),
plus SBS-folder-specific body class overrides replacing the bpc/ipc ones:

```css
@media print {
    @page {
        margin-left: 10mm;
        margin-right: 10mm;
        @footnote {
            border-top: 1px solid black;
            padding-top: 0.5em;
            text-align: left;
        }
    }

    .pdf-footnote {
        float: footnote;
        text-align: left;
        font-size: 0.9em;
        font-style: italic;
        font-weight: normal !important;
        line-height: 1.2;
    }

    .pdf-footnote::footnote-call,
    .pdf-footnote::footnote-marker {
        content: "";
    }

    .pdf-footnote-label {
        font-weight: bold;
        font-style: normal;
        margin-right: 0.3em;
    }

    sup.manual-fn-ref a {
        text-decoration: none;
        color: inherit;
    }

    .pdf-footnote-backref {
        font-style: normal;
        text-decoration: none;
        color: inherit;
    }

    .standalone-image {
        text-align: center;
        margin: 1em 0;
    }

    .standalone-image img {
        display: block !important;
        height: auto !important;
        width: auto !important;
        max-width: 90% !important;
        margin: 0 auto !important;
    }

    table {
        break-inside: avoid;
        break-before: avoid;
    }

    table.long-table {
        break-inside: auto;
    }

    .content table.cols-7 td, .content table.cols-7 th {
        font-size: 0.9rem !important;
        padding: 4px 3px !important;
    }

    .content table.cols-8 td, .content table.cols-8 th {
        font-size: 0.85rem !important;
        padding: 3px 2px !important;
    }

    .content table.cols-9 td, .content table.cols-9 th {
        font-size: 0.8rem !important;
        padding: 3px 2px !important;
    }

    .content table.cols-10 td, .content table.cols-10 th {
        font-size: 0.7rem !important;
        padding: 3px 2px !important;
    }

    h1, h2, h3, h4, h5, h6 {
        break-after: avoid;
    }

    p {
        orphans: 2;
        widows: 2;
    }

    /* SBS folders: allow all tables to flow freely across pages */
    body.bhikkhu-patimokkha table,
    body.sbs-per-analysis table,
    body.suttas table {
        break-inside: auto;
        break-before: auto;
    }

    /* Exclude cover and TOC sub-headings from PDF bookmark sidebar */
    .pdf-title-page h1,
    .pdf-toc-page h2,
    .pdf-toc-page h3 {
        bookmark-level: none;
    }
}
```

→ verify: file exists, contains `@media print`, contains `body.bhikkhu-patimokkha table`

---

## Phase 3 — generate_pdfs.py

### Task 3.1 [x] — Create scripts/generate_pdfs.py

Create file `scripts/generate_pdfs.py`. Complete content below.

The script structure is:
1. One-sentence module docstring
2. macOS library path fix (verbatim from reference)
3. Constants: FOLDER_NAMES, INDEX_FILES, FOLDER_DIRS, SBS_FOLDERS, CSS_PATHS
4. Helper functions — most verbatim from reference, with one new one
5. Custom get_markdown_files() — key difference from reference
6. main()

**Exact constants section** (replace reference FOLDER_NAMES entirely):
```python
FOLDER_NAMES = {
    'bhikkhu-patimokkha': 'Bhikkhu Pātimokkha - Word by Word Analysis',
    'sbs-per-analysis':   'SBS Pāḷi-English Recitations - Analysis',
    'suttas':             'Suttas and Passages - Word by Word Analysis',
}

INDEX_FILES = {
    'bhikkhu-patimokkha': 'docs/6-pali-class/bhikkhu-patimokkha/index.md',
    'sbs-per-analysis':   'docs/6-pali-class/sbs-per-analysis.md',
    'suttas':             'docs/6-pali-class/1-pali-class-adv.md',
}

FOLDER_DIRS = {
    'bhikkhu-patimokkha': 'docs/6-pali-class/bhikkhu-patimokkha',
    'sbs-per-analysis':   'docs/6-pali-class/sbs-per-analysis',
    'suttas':             'docs/6-pali-class/suttas',
}

SBS_FOLDERS = frozenset(FOLDER_NAMES.keys())

CSS_PATHS = [
    'identity/sbs-pdf-fonts.css',
    'identity/sbs-pdf-variables.css',
    'identity/sbs-pdf.css',
    'identity/sbs-pdf-extra.css',
]
```

**Functions to copy verbatim from reference** (no changes needed):
- `clean_markdown_content(content)`
- `pre_process_content(text)`
- `resolve_image_paths(content, file_path)`
- `mark_wide_tables(html_content, col_threshold, row_threshold)`
- `equalize_table_columns(html_content)`
- `remove_empty_thead(html_content)`
- `process_footnotes_for_pdf(html_content)`
- `post_process_html(html_content)`
- `build_html_document(title, files_data, title_md_content, literature_md_content, folder_type, root_index_content)`
- `generate_pdf(html_content, output_pdf, css_paths)`

**New function — add after the helper functions block**:
```python
def parse_md_links(md_content: str, base_dir: str) -> list[str]:
    """Extract ordered .md file paths from markdown link syntax in document order."""
    paths = []
    for match in re.finditer(r'\[([^\]]+)\]\(([^)#\s]+\.md)\)', md_content):
        href = match.group(2)
        if href.startswith('http'):
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
        with open(index_path, 'r', encoding='utf-8') as f:
            index_content = f.read()

        if folder_key == 'suttas':
            # Two-level: index → top-level files → child files in subdirs
            files: list[str] = []
            for top_file in parse_md_links(index_content, index_base):
                files.append(top_file)
                with open(top_file, 'r', encoding='utf-8') as f:
                    sub_content = f.read()
                top_base = os.path.dirname(top_file)
                for child in parse_md_links(sub_content, top_base):
                    if child not in files:
                        files.append(child)
            result[folder_key] = files
        else:
            # Flat: parse links directly from index file
            index_abs = os.path.abspath(index_path)
            files = [f for f in parse_md_links(index_content, index_base)
                     if os.path.abspath(f) != index_abs]
            result[folder_key] = files
    return result
```

**main() function** — adapt from reference main(), replacing all folder/path logic:
```python
def main() -> None:
    parser = argparse.ArgumentParser(description='Generate PDF documents from Pāli class markdown.')
    parser.add_argument('folder', nargs='?', choices=list(FOLDER_NAMES.keys()),
                        help='Generate only this folder (default: all)')
    parser.add_argument('--html-only', action='store_true',
                        help='Write intermediate HTML to output/pdf/<folder>_debug.html, skip WeasyPrint')
    args = parser.parse_args()

    output_dir = 'output/pdf'
    os.makedirs(output_dir, exist_ok=True)

    pr.bip()
    f_by_dir = get_markdown_files()

    for fld, files in f_by_dir.items():
        if args.folder and fld != args.folder:
            continue
        if not files:
            pr.no(f'{fld}: no files found')
            continue

        pr.green(f'{fld}')
        data = []
        for file_path in files:
            with open(file_path, 'r', encoding='utf-8') as f:
                data.append((file_path, f.read()))

        html = build_html_document(
            title=FOLDER_NAMES[fld],
            files_data=data,
            title_md_content='',
            literature_md_content='',
            folder_type=fld,
            root_index_content='',
        )

        if args.html_only:
            debug_path = os.path.join(output_dir, f'{fld}_debug.html')
            with open(debug_path, 'w', encoding='utf-8') as f:
                f.write(html)
            pr.yes(f'html → {debug_path}')
        else:
            out_path = os.path.join(output_dir, f'{fld}.pdf')
            generate_pdf(html, out_path, css_paths=CSS_PATHS)
            pr.yes('ok')
```

**Imports needed** (top of file after docstring, before macOS fix):
```python
import argparse
import os
import re
import sys
import time
import markdown
from bs4 import BeautifulSoup
from tools.printer import printer as pr
```

→ verify:
```
uv run python scripts/generate_pdfs.py suttas --html-only
```
Check `output/pdf/suttas_debug.html` exists and contains a `<div class='pdf-toc-page'>` and multiple `<div class='pdf-topic-page'>` sections.

### Task 3.2 [x] — Test full PDF generation on one folder
Run:
```
uv run python scripts/generate_pdfs.py sbs-per-analysis
```
→ verify: `output/pdf/sbs-per-analysis.pdf` created, file size > 100KB, no Python exceptions.
Open the PDF and confirm Pāḷi diacritics render correctly (ā, ṭ, ḷ visible, not as boxes).

---

## Phase 4 — generate_docx.py

### Task 4.1 [x] — Create scripts/generate_docx.py

Create file `scripts/generate_docx.py`. Structure:
1. One-sentence module docstring
2. Pandoc availability check (verbatim from reference)
3. Same constants as generate_pdfs.py: FOLDER_NAMES, INDEX_FILES, FOLDER_DIRS, SBS_FOLDERS
4. PAGEBREAK constant (verbatim)
5. Helper functions — most verbatim from reference
6. Same `parse_md_links()` and `get_markdown_files()` functions as in generate_pdfs.py
7. Modified `aggregate_markdown()` — treat SBS_FOLDERS like `_key`
8. main()

**Imports** (top of file after docstring):
```python
import argparse
import os
import re
import subprocess
import pypandoc
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from tools.printer import printer as pr
```

**Same constants as generate_pdfs.py** — copy FOLDER_NAMES, INDEX_FILES, FOLDER_DIRS, SBS_FOLDERS exactly.

**Functions to copy verbatim from reference**:
- `clean_markdown_content(content)`
- `fix_internal_links(content)`
- `preprocess_inline_images(content)`
- `insert_h2_page_breaks(content)`
- `make_heading_slug(text)`
- `build_manual_toc(files_data)`
- `generate_docx(aggregated_md, output_docx, folder)`
- `post_process_docx(docx_path, folder)`

**Also copy `parse_md_links()` and `get_markdown_files()` verbatim** from the
generate_pdfs.py version written in Task 3.1.

**Modified `aggregate_markdown()`** — change the folder-type checks to include SBS folders.
Take the reference version and change every occurrence of:
```python
folder.endswith(('_ex', '_key'))
```
to:
```python
folder.endswith(('_ex', '_key')) or folder in SBS_FOLDERS
```
And change:
```python
needs_file_pagebreaks = folder in ('bpc', 'ipc') or folder.endswith(('_ex', '_key'))
```
to:
```python
needs_file_pagebreaks = folder in SBS_FOLDERS or folder in ('bpc', 'ipc') or folder.endswith(('_ex', '_key'))
```
Do NOT change the `is_ex` variable — it stays as `folder.endswith('_ex')` (SBS folders
do not need the `insert_h2_page_breaks` behaviour).

**Modified `generate_docx()` function** — the `use_pandoc_toc` line:
Change:
```python
use_pandoc_toc = not folder.endswith(('_ex', '_key'))
```
to:
```python
use_pandoc_toc = not (folder.endswith(('_ex', '_key')) or folder in SBS_FOLDERS)
```

**main() function**:
```python
def main() -> None:
    parser = argparse.ArgumentParser(description='Generate DOCX documents from Pāli class markdown.')
    parser.add_argument('--folder', choices=list(FOLDER_NAMES.keys()),
                        help='Specific folder to generate (default: all)')
    args = parser.parse_args()

    output_dir = 'output/docs'
    os.makedirs(output_dir, exist_ok=True)

    pr.bip()
    f_by_dir = get_markdown_files()

    for fld, files in f_by_dir.items():
        if args.folder and fld != args.folder:
            continue
        if not files:
            pr.no(f'{fld}: no files found')
            continue

        pr.green(f'{fld}')
        data = []
        for file_path in files:
            with open(file_path, 'r', encoding='utf-8') as f:
                data.append((file_path, f.read()))

        agg_md = aggregate_markdown(
            title=FOLDER_NAMES[fld],
            files_data=data,
            folder=fld,
        )

        out_path = os.path.join(output_dir, f'{fld}.docx')
        generate_docx(agg_md, out_path, folder=fld)
        post_process_docx(out_path, fld)
        pr.yes('ok')
```

→ verify:
```
uv run python scripts/generate_docx.py --folder suttas
```
Check `output/docs/suttas.docx` created, no exceptions.
Open file in LibreOffice Writer and confirm: headings visible, TOC present, page breaks between sections.

---

## Phase 5 — GitHub Actions Workflow

### Task 5.1 [x] — Create .github/workflows/generate_documents.yaml

Create file `.github/workflows/generate_documents.yaml` with this content:

```yaml
name: Generate and Release Documents

on:
  push:
    paths:
      - 'docs/6-pali-class/**'
  workflow_dispatch:

jobs:
  generate-and-release:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Fetch printer.py from dpd-db-sbs
        run: |
          rm -f tools/printer.py
          curl -fsSL "https://raw.githubusercontent.com/sasanarakkha/dpd-db-sbs/main/tools/printer.py" -o tools/printer.py

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y libpango-1.0-0 libpangoft2-1.0-0 pandoc

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
          python-version: "3.12"

      - name: Install Python dependencies
        run: uv sync --frozen

      - name: Generate PDFs
        run: uv run python scripts/generate_pdfs.py

      - name: Generate DOCX files
        run: uv run python scripts/generate_docx.py

      - name: Upload to release
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          LATEST_TAG=$(gh release list --limit 1 --json tagName -q '.[0].tagName')
          echo "Latest release tag: $LATEST_TAG"

          HAS_DOCS=$(gh release view "$LATEST_TAG" --json assets \
            -q '[.assets[].name | select(endswith(".pdf") or endswith(".docx"))] | length > 0')

          if [ "$HAS_DOCS" = "true" ]; then
            echo "Latest release already has PDF/DOCX assets — creating new release"
            NEW_TAG="artifacts-$(date +'%d.%m.%Y_%H-%M-%S')"
            gh release create "$NEW_TAG" \
              --title "Build $(date +'%d.%m.%Y %H:%M UTC')" \
              --notes "PDF and DOCX documents generated from latest Pāli class source files." \
              output/pdf/*.pdf output/docs/*.docx
          else
            echo "Appending PDF/DOCX to existing release: $LATEST_TAG"
            gh release upload "$LATEST_TAG" output/pdf/*.pdf output/docs/*.docx
          fi
```

→ verify: file exists at `.github/workflows/generate_documents.yaml`; run `gh workflow list` and confirm `Generate and Release Documents` appears.

---

## Phase 6 — Registration & Final Verification

### Task 6.1 [x] — Update README.md script registry

Find the script registry section in `README.md`. Add these two entries:

```
- `scripts/generate_pdfs.py` — generates PDF for bhikkhu-patimokkha, sbs-per-analysis,
  and suttas content folders. Output: `output/pdf/`. Run: `uv run python scripts/generate_pdfs.py`
  (all folders) or `uv run python scripts/generate_pdfs.py <folder>` (single folder).
  Use `--html-only` for a debug HTML output without running WeasyPrint.

- `scripts/generate_docx.py` — generates DOCX for the same three folders. Output: `output/docs/`.
  Run: `uv run python scripts/generate_docx.py` (all) or with `--folder <name>` (single).
```

→ verify: `grep -n "generate_pdfs\|generate_docx" README.md` shows both entries.

### Task 6.2 [x] — Full generation run

Run all generators and confirm all six files are produced:
```
uv run python scripts/generate_pdfs.py
uv run python scripts/generate_docx.py
ls output/pdf/ output/docs/
```

Expected output:
```
output/pdf/:
bhikkhu-patimokkha.pdf   sbs-per-analysis.pdf   suttas.pdf

output/docs/:
bhikkhu-patimokkha.docx  sbs-per-analysis.docx  suttas.docx
```

→ verify:
- All 6 files exist with size > 100KB.
- No Python exceptions during either run.
- Open `output/pdf/bhikkhu-patimokkha.pdf` — title page shows "Bhikkhu Pātimokkha - Word by Word Analysis", TOC is present, Pāḷi diacritics render correctly.
- Open `output/docs/sbs-per-analysis.docx` — headings and content visible, TOC present.

### Task 6.3 [~] — Test GitHub Action (manual trigger)
Go to GitHub Actions tab → "Generate and Release Documents" → Run workflow.
→ verify: workflow completes without errors; latest release gains the 6 new files as assets.
