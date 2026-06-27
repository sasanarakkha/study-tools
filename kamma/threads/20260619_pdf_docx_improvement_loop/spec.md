# Spec: PDF & DOCX Generator Improvement Loop

> **Thread type:** Loop (standing thread)

## Overview

Standing improvement loop for the PDF/DOCX generation pipeline built in
`kamma/threads/20260520_pdf_docx_pali_class/` (see that thread's `spec.md` and
`handoff.md` for full background). Each cycle picks up one known issue or
improvement, gets it approved, implements it, and validates it against the
real output.

## Loop Domain

The PDF/DOCX generation pipeline for `docs/6-pali-class/` content:
- `scripts/generate_pdfs.py`
- `scripts/generate_docx.py`
- `identity/sbs-pdf-*.css`, `identity/fonts/`
- `.github/workflows/generate_documents.yaml`

## In-Scope vs Out-of-Scope

**In-scope:**
- Rendering/fidelity fixes (diacritics, TOC, page breaks, headings)
- Generator bugs and edge cases (e.g. the known Pandoc image-path warning)
- CSS/font adjustments for the existing three target folders
- GitHub Actions workflow reliability (release upload/create logic)
- Adding the follow-up verify scripts (`verify_pdf_content.py`,
  `verify_docx_content.py`) mentioned as "not included" in the original spec,
  if a cycle is opened for them

**Out-of-scope:**
- Edits to `docs/6-pali-class/**` source content itself
- Adding new target folders beyond `bhikkhu-patimokkha`, `sbs-per-analysis`,
  `suttas` (would need its own thread/spec)
- Anki deck generation and MkDocs website build (separate systems)

## Validation Standards

Every cycle, before being marked done:
1. Regenerate affected output(s): `uv run python scripts/generate_pdfs.py [folder]`
   and/or `uv run python scripts/generate_docx.py [--folder folder]` — no exceptions.
2. Run the project's mandatory pre-completion checks on touched files:
   `ruff check --fix`, `ruff format`, `pyright`, `pyrefly check --min-severity warn`.
3. Manually open the affected PDF/DOCX output and confirm correct rendering
   (diacritics, TOC, headings) — report this as tested/not tested per CLAUDE.md
   Verification rules.
4. Run relevant tests under `tests/` if any exist for the touched script.

## Completion Condition

This loop is closed when there is no remaining backlog of known generator
issues and the user doesn't anticipate further improvement cycles soon.
Closure is a manual decision by the user, not automatic.

## Assumptions & Uncertainties

- The three target folders and their file-discovery logic (link-parsing from
  index files) are stable and not being revisited here.
- macOS WeasyPrint/Homebrew dependency setup from the original thread remains
  valid; CI apt-get deps remain valid.

## Constraints

- `docs/` is read-only — never modified.
- Run scripts from project root via `uv run python scripts/...`.
- No `sys.path` hacks; use `from tools.printer import printer as pr`.
- Output dirs (`output/pdf/`, `output/docs/`) remain gitignored.
- Each cycle's read contract: `spec.md`, `plan.md`, `handoff.md`, `learnings.md`
  only — full cycle records read on demand.

## How We'll Know It's Done (Overall)

- No open known issues against the generator pipeline.
- `learnings.md` reflects accumulated, still-relevant lessons (stale ones pruned).
- User confirms no further cycles are needed.
