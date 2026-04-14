# plan.md — Thread 3: Anki Style Docs

**GitHub issue:** sasanarakkha/dpd-db-sbs#21
**Depends on:** 20260413_core-migration merged

⚠️ **Open question:** Generation method (Option A vs B) must be confirmed
before Phase 2 is executed.
*Decision:* Option B+ (Direct Markdown Generation).

---

## Phase 1 — Verify No Generation Dependency
- [x] Check whether any `dpd-db` script writes to `anki-style/`
  → verify: `grep -r "anki-style" /Users/deva/Documents/dpd-db/scripts/`
  *Result:* Found dependencies in `anki_csv.py`, `anki_class_grammar.py`, `from_dps_csv_to_anki_csvs.py`.
- [x] List all files in `anki-style/` and count.
  → verify: `ls anki-style/ | wc -l` (should be ~40)
  *Result:* 43 files.

**Phase 1 complete when:** Option B (Direct Markdown Generation) confirmed and dependencies mapped.

---

## Phase 2 — Move and Reformat Files
- [x] Create `docs/anki/` directory.
- [x] Update `dpd-db/tools/paths_dps.py` to point to `study-tools/docs/anki/`.
- [x] Write `scripts/convert_anki_style.py` to reformat existing `.txt` to `.md`.
- [x] Run conversion script.
- [x] Remove `anki-style/` from repo.
- [x] Add new files to git.

**Phase 2 complete when:** `anki-style/` is gone, `docs/anki/` exists with `.md` files.

---

## Phase 3 — Update MkDocs Nav
- [x] Add "Anki Templates" section to `mkdocs.yaml` grouped by deck type.
  → verify: section exists in `nav:`

**Phase 3 complete when:** `mkdocs.yaml` reflects the new structure.

---

## Phase 4 — Verification
- [x] Run `uv run mkdocs build`.
  → verify: 0 errors related to `anki/` paths.
- [x] Check for remaining `anki-style` links in `docs/`.
  → verify: `grep -r "anki-style" docs/` (should be empty)
- [x] Update `dpd-db` scripts to write formatted Markdown directly.
  → verify: `scripts/fix_dpd_db_anki_docs.py` ran successfully.

**Phase 4 complete when:** Build passes and no stale links remain.

---

## Phase 5 — Commit Preparation
- [x] Stage all changes.
- [x] Prepare draft commit message.
  ```text
  #21 anki-style: move to docs/anki/, convert to md, update dpd-db generation
  ```

**Phase 5 complete when:** commit staged and ready for user review.

---

## Errors & Issues Log

- Found that `dpd-db` scripts write to `anki-style/`.
- Decided on "Direct Markdown Generation" (Option B+).
- Updated `dpd-db` paths and scripts to support the new structure.
