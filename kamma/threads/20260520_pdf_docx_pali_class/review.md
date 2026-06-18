## Thread
- **ID:** 20260520_pdf_docx_pali_class
- **Objective:** Port PDF and DOCX generation pipeline from dpd-pali-courses to study-tools for three pali-class content folders, with SBS branding and GitHub Actions release workflow.

## Files Changed
- `scripts/generate_pdfs.py` — WeasyPrint-based PDF generator for three folders
- `scripts/generate_docx.py` — Pandoc-based DOCX generator for same folders
- `identity/sbs-pdf-fonts.css` — Inter font @font-face declarations
- `identity/sbs-pdf-variables.css` — CSS variables with SBS brown (#593e26)
- `identity/sbs-pdf.css` — content component styles
- `identity/sbs-pdf-extra.css` — @media print rules with SBS body-class overrides
- `identity/fonts/Inter-{Regular,Bold,Italic,BoldItalic}.ttf` — static Inter v4.0 fonts
- `.github/workflows/generate_documents.yaml` — CI workflow: generate + upload to release
- `pyproject.toml` + `uv.lock` — added weasyprint, markdown, pypandoc, python-docx
- `.gitignore` — added output/pdf/ and output/docs/
- `README.md` — script registry entries for both generators

## Findings
| # | Severity | Location | What | Why | Fix |
|---|----------|----------|------|-----|-----|
| 1 | minor | `generate_pdfs.py:6` | `import time` unused | ruff F401 | Removed |
| 2 | minor | `generate_docx.py:5` | `import subprocess` unused | ruff F401 | Removed |
| 3 | nit | `generate_docx.py:16` | bare `print()` in pandoc-missing path | CLAUDE.md requires pr.warning() | Fixed to pr.warning() |
| 4 | nit | both scripts | `FOLDER_DIRS` constant defined but never referenced | dead code copied from reference | Left in; harmless, documents intended folder paths |

## Fixes Applied
- Removed `import time` from `generate_pdfs.py`
- Removed `import subprocess` from `generate_docx.py`
- Changed `print("Pandoc not found...")` → `pr.warning(...)` in `generate_docx.py`

## Test Evidence
- `uv run python scripts/generate_pdfs.py` → 3 PDFs in output/pdf/ (1.9MB, 1.2MB, 6.3MB)
- `uv run python scripts/generate_docx.py` → 3 DOCXs in output/docs/ (408KB, 267KB, 2.2MB)
- `suttas --html-only` → 1 TOC + 162 topic pages confirmed in debug HTML
- `uv tool run ruff check scripts/generate_pdfs.py scripts/generate_docx.py` → All checks passed
- GitHub Action trigger (Task 6.3) — pending; requires push first

## Verdict
PASSED
- Review date: 2026-05-20
- Reviewer: Claude Sonnet 4.6 (same session as implementation — review is less independent)
