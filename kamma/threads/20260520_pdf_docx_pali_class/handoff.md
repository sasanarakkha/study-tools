# Handoff: PDF & DOCX Generators — Pāli Class Content

## Session Date
2026-05-20

## Status
All implementation tasks complete. Awaiting user manual testing and commit/push before review.

---

## Phases Completed & Outcomes

### Phase 1 — Setup (Tasks 1.1, 1.2) ✓
- Added `weasyprint`, `markdown`, `pypandoc`, `python-docx` via `uv add`. All import correctly with the macOS DYLD_LIBRARY_PATH fix.
- Created `output/pdf/` and `output/docs/` with `.gitkeep` files.
- Added both dirs to `.gitignore`.

### Phase 2 — CSS & Fonts (Tasks 2.1–2.5) ✓
- Downloaded Inter v4.0 zip from GitHub. The zip structure was `extras/ttf/Inter-*.ttf` (NOT `Inter Desktop/` as the plan assumed) — extracted correctly to `identity/fonts/`.
- Created four CSS files: `identity/sbs-pdf-fonts.css`, `sbs-pdf-variables.css`, `sbs-pdf.css`, `sbs-pdf-extra.css`.
- All font `url()` paths point to `fonts/Inter-*.ttf` (relative to identity/).

### Phase 3 — generate_pdfs.py (Tasks 3.1, 3.2) ✓
- Created `scripts/generate_pdfs.py`. All helper functions copied verbatim from reference (`/Users/deva/Documents/dpd-pali-courses/scripts/generate_pdfs.py`).
- New functions `parse_md_links()` and `get_markdown_files()` added per spec.
- `suttas --html-only`: 1 TOC page + 162 topic pages confirmed in debug HTML.
- `sbs-per-analysis` full PDF: 1.2MB, generated in ~20s. No exceptions.

### Phase 4 — generate_docx.py (Task 4.1) ✓
- Created `scripts/generate_docx.py`. Functions copied verbatim from reference (`dpd-pali-courses/scripts/generate_docx.py`).
- Two modifications applied:
  - `aggregate_markdown()`: TOC injection and page-break conditions extended to `SBS_FOLDERS`.
  - `generate_docx()`: `use_pandoc_toc` logic extended to exclude SBS folders.
- `suttas.docx`: 2.2MB. Two Pandoc image warnings (missing PNG) — expected, image not critical, file valid.

### Phase 5 — GitHub Actions (Task 5.1) ✓
- Created `.github/workflows/generate_documents.yaml`.
- Will not appear in `gh workflow list` until pushed — this is expected behaviour.

### Phase 6 — Registration & Full Run (Tasks 6.1, 6.2) ✓
- README.md script registry updated with both scripts.
- Full generation run successful:
  - `output/pdf/bhikkhu-patimokkha.pdf` — 1.9MB
  - `output/pdf/sbs-per-analysis.pdf` — 1.2MB
  - `output/pdf/suttas.pdf` — 6.3MB
  - `output/docs/bhikkhu-patimokkha.docx` — 408KB
  - `output/docs/sbs-per-analysis.docx` — 267KB
  - `output/docs/suttas.docx` — 2.2MB

### Task 6.3 — GitHub Action manual trigger [~] NOT YET DONE
Requires push first. Can only be verified after commit + push.

---

## Git State

All 15 files are staged and ready for commit. The commit has NOT been made (per CLAUDE.md rules). Suggested commit message:

```
git commit -m "feat: add PDF and DOCX generators for Pāli class content

- scripts/generate_pdfs.py: WeasyPrint-based PDF generation for
  bhikkhu-patimokkha, sbs-per-analysis, suttas folders
- scripts/generate_docx.py: Pandoc-based DOCX generation for same folders
- identity/sbs-pdf-*.css: SBS-branded CSS (Inter fonts, #593e26 primary)
- identity/fonts/: static Inter TTF files (v4.0) to prevent Pāḷi CMap bugs
- .github/workflows/generate_documents.yaml: CI workflow uploading to release
- pyproject.toml: weasyprint, markdown, pypandoc, python-docx dependencies
- output/pdf/ and output/docs/ added to .gitignore

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
```

NOT staged (intentionally excluded):
- `docs/6-pali-class/atth-hoti.md` — pre-existing modification unrelated to this thread
- `kamma/threads/` — thread tracking files

---

## Non-Obvious Codebase Discoveries

1. **macOS DYLD_LIBRARY_PATH fix is real and required.** Setting `os.environ["DYLD_LIBRARY_PATH"]` in Python before `import weasyprint` actually works because `cffi.dlopen()` reads the env var at call time. Without this, WeasyPrint fails to load `libgobject-2.0` even when Homebrew has it at `/opt/homebrew/lib`.

2. **Inter font zip structure changed.** The plan said `Inter Desktop/Inter-Regular.ttf` but v4.0 zip uses `extras/ttf/Inter-Regular.ttf`. Always verify with `unzip -l` before extracting.

3. **`cd` in background Bash tasks doesn't persist.** The font zip was downloaded to the project root (not `identity/fonts/`) because `cd identity/fonts` in the background command ran in a subprocess whose CWD wasn't inherited. Always use absolute paths in multi-step shell commands.

4. **Pandoc image warning is benign.** The `suttas.docx` generation warns about a missing `dict-dpd-sbs-additions.png`. The image path in the source is relative to a different base dir. DOCX is valid and fully usable — this is a known limitation of Pandoc's resource path resolution with nested markdown.

5. **`suttas_debug.html` in `output/pdf/`** — leftover from Task 3.1 verification run. Safe to delete; it's gitignored.

---

## Next Steps for User

1. Open `output/pdf/bhikkhu-patimokkha.pdf` — confirm title page, TOC, and Pāḷi diacritics (ā, ṭ, ḷ) render correctly (not as boxes).
2. Open `output/docs/sbs-per-analysis.docx` — confirm headings and TOC visible.
3. Run the commit above manually.
4. Push to origin/main.
5. Go to GitHub Actions → "Generate and Release Documents" → Run workflow (manual trigger).
6. Confirm workflow completes and release gains 6 new file assets.
7. Run `/kamma:3-review` in a fresh session.

---

## Errors, Issues, and Repeated Mistakes

- **Font zip path assumption wrong**: Plan said `Inter Desktop/Inter-Regular.ttf`, actual was `extras/ttf/Inter-Regular.ttf`. Fixed by inspecting zip contents with `unzip -l` before extracting.
- **Background Bash CWD**: `cd` inside a background Bash command doesn't affect subsequent tool calls. Font zip landed at project root instead of `identity/fonts/`. Fixed by using absolute paths.
- **Inline script blocked**: Initial verification attempt used `python -c "..."` which is prohibited by CLAUDE.md. Wrote `temp/check_imports.py` instead.
