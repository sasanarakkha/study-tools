# spec.md — Thread 3: Anki Style Docs

**GitHub issue:** sasanarakkha/dpd-db-sbs#21
**Thread type:** refactor
**Depends on:** 20260413_core-migration merged
**Open question:** generation method — see Assumptions section

---

## Overview

Move `anki-style/` (Anki card templates, field lists, CSS) into
`docs/anki/` so they render as readable documentation on the MkDocs
site. Convert all `.txt` files to `.md`. Update all deck doc links
to use relative paths. The `anki-style/` root directory is removed.

---

## What It Should Do

### 1. Move and rename
`anki-style/*.txt` → `docs/anki/*.md`

Content reformatted for readable web display:
- `field-list-*.md` — simple list or table of field names
- `*-front.md`, `*-back.md` — HTML template in a fenced `html` code block
- `styling.md`, `pat-styling.md` — CSS in a fenced `css` code block

### 2. Update deck doc links
Links in `docs/anki-decks/` currently point at:
`https://github.com/sasanarakkha/study-tools/blob/main/anki-style/<file>.txt`

Thread 1's `fix_links.py` rewrites these to:
`../anki/<file>.md`

This thread ensures the target files exist at those paths.

### 3. Add `docs/anki/` to MkDocs nav
Add an "Anki Templates" section to `mkdocs.yaml` listing the key
template and field-list files (front/back/styling per deck type).

### 4. Generation method (TBD — confirm before plan is written)
**Option A (default assumption):** Files are hand-maintained.
Just rename + reformat. No generation script needed.

**Option B:** A script (possibly extending `dpd-db/scripts/export/anki_csv.py`
or a new `scripts/generate_anki_docs.py`) generates `.md` documentation
into `docs/anki/` automatically, and a GitHub Action runs it on a schedule
(similar to Thread 2).

If Option B, the plan gains a Phase for the generation script and action.

---

## Assumptions & Uncertainties

- **Generation method:** Assumed Option A (hand-maintained) until confirmed.
  If Option B, plan must be expanded before execution.
- `anki-style/` files appear hand-maintained based on content inspection.
  Verify by checking whether any dpd-db script writes to `anki-style/`
  before proceeding.
- Thread 1's `fix_links.py` rewrites the link text; this thread provides
  the targets. Both must be applied for links to resolve correctly.

---

## Constraints

- Commit references `sasanarakkha/dpd-db-sbs#21`
- Must be applied after Thread 1 (`docs/` structure must exist)

---

## How We'll Know It's Done

- `anki-style/` absent from repo root
- `docs/anki/` contains `.md` versions of all former `.txt` files
- `uv run mkdocs serve` — Anki template pages render with syntax-
  highlighted code blocks
- No broken links in `docs/anki-decks/` pointing to templates
- `uv run mkdocs build` — 0 errors

---

## What's Not Included

- Actual Anki CSV generation (remains in dpd-db)
- Changes to card template content
- Any dpd-db modifications (unless Option B is chosen)
