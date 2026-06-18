# Spec: PDF & DOCX Generators — Pāli Class Content

## Overview

Port the PDF and DOCX generation pipeline from `dpd-pali-courses` to `study-tools`,
adapted for three content folders in `docs/6-pali-class/`. Same algorithms, same CLI
interface, SBS branding. Add a GitHub Actions workflow that appends the generated files
to the latest release, or creates a new release if the latest already contains them.

Reference scripts (source of truth for all algorithms):
  /Users/deva/Documents/dpd-pali-courses/scripts/generate_pdfs.py   (554 lines)
  /Users/deva/Documents/dpd-pali-courses/scripts/generate_docx.py   (368 lines)
Reference CSS: /Users/deva/Documents/dpd-pali-courses/identity/

## Three target folders

| Key | Title in PDF/DOCX | Index file | Structure |
|---|---|---|---|
| `bhikkhu-patimokkha` | Bhikkhu Pātimokkha - Word by Word Analysis | `docs/6-pali-class/bhikkhu-patimokkha/index.md` | flat, ~218 files |
| `sbs-per-analysis` | SBS Pāḷi-English Recitations - Analysis | `docs/6-pali-class/sbs-per-analysis.md` | flat, ~77 files |
| `suttas` | Suttas and Passages - Word by Word Analysis | `docs/6-pali-class/1-pali-class-adv.md` | two-level (see below) |

### Suttas two-level structure (option B — full expansion)
Top-level files (e.g. `suttas/sacca-samyutta-sn-56.md`) are sub-indices linking
into subdirs (`sn-56/56-1.md`, etc.). The PDF expands them recursively:
chapter header file → then each linked subdir file in order.
The index `1-pali-class-adv.md` is used only for top-level file ordering.

## Scripts

### generate_pdfs.py
- Run all:  `uv run python scripts/generate_pdfs.py`
- Run one:  `uv run python scripts/generate_pdfs.py bhikkhu-patimokkha`
- Debug:    `uv run python scripts/generate_pdfs.py bhikkhu-patimokkha --html-only`
- Output:   `output/pdf/bhikkhu-patimokkha.pdf`, etc.

### generate_docx.py
- Run all:  `uv run python scripts/generate_docx.py`
- Run one:  `uv run python scripts/generate_docx.py --folder sbs-per-analysis`
- Output:   `output/docs/sbs-per-analysis.docx`, etc.

### Behavior (all three folders — bpc_key style)
- No about / literature pages
- No heading level shift
- TOC generated programmatically from headings
- Nav-link HTML stripped from source (clean_markdown_content)
- Page break between each content file (PDF and DOCX)
- Manual TOC in DOCX (not Pandoc field-based)

## File discovery (custom — not mkdocs.yaml)
The three folders are NOT in mkdocs.yaml nav. File order comes from parsing
markdown links (`[text](path.md)`) from each folder's index file in document order.
For `suttas`: each top-level file is also parsed for its child links (one level deep).
Index files themselves are NOT included as content (used only for ordering/TOC).

## CSS (new SBS-branded PDF files)
Four new CSS files in `identity/`, parallel to dpd-pali-courses structure:
- `identity/sbs-pdf-fonts.css`      — @font-face for static Inter TTF
- `identity/sbs-pdf-variables.css`  — CSS variables (primary: #593e26)
- `identity/sbs-pdf.css`            — content component styles
- `identity/sbs-pdf-extra.css`      — @media print rules only

Static Inter fonts (Regular, Bold, Italic, BoldItalic TTF) at `identity/fonts/`.
Committed to the repo (not downloaded per CI run).

## GitHub Actions workflow (.github/workflows/generate_documents.yaml)
Trigger: `workflow_dispatch` + push to `docs/6-pali-class/**`

Logic:
1. Generate all PDFs and DOCXs.
2. Fetch latest release tag via `gh release list`.
3. Check if latest release already has `.pdf` or `.docx` assets.
4. If NO  (normal case) → `gh release upload <tag> output/pdf/*.pdf output/docs/*.docx`
5. If YES (re-run case) → `gh release create` with new timestamped tag.

Existing release naming pattern: `artifacts-DD.MM.YYYY_HH-MM-SS`

## Assumptions & uncertainties

1. `suttas` top-level files are link-only indices (verified: sacca-samyutta-sn-56.md
   contains only links, no sutta text). PDF must include child files from subdirs.

2. Static Inter fonts not present in project. Must be downloaded from GitHub release
   and committed. ~800KB total for four TTF files.

3. macOS WeasyPrint Homebrew deps (`pango cairo gdk-pixbuf libffi`) assumed locally
   installed. CI uses `apt-get install libpango-1.0-0 libpangoft2-1.0-0`.

4. `gh release upload` appends assets to existing release without changing its date
   or re-publishing it.

## Constraints
- `docs/` is read-only — never modified by these scripts.
- Run from project root via `uv run python scripts/...`.
- No `sys.path` hacks. Hatch package structure (`from tools.printer import printer as pr`).
- Scripts added to README.md script registry.
- Output dirs (`output/pdf/`, `output/docs/`) gitignored.
- All new scripts start with a one-sentence docstring.
- Use `pr.bip()` before work begins, `pr.yes("ok")` / `pr.no(msg)` for results.

## How we'll know it's done
- `uv run python scripts/generate_pdfs.py` → 3 PDF files in `output/pdf/`, no exceptions.
- `uv run python scripts/generate_docx.py` → 3 DOCX files in `output/docs/`, no exceptions.
- PDF opens with title page, TOC, and readable Pāḷi diacritics (ṭ, ā, ḷ, etc.).
- DOCX opens in Word/LibreOffice with headings and TOC intact.
- GitHub Action runs on `workflow_dispatch` and uploads files to latest release.

## What's not included
- Verify scripts (`verify_pdf_content.py`, `verify_docx_content.py`) — follow-up if needed.
- Anki deck generation — separate system.
- Website build integration — these scripts run independently of MkDocs.
