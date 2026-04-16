# Plan: Dynamic Site Architecture & Asset Localization (COMPLETED)

## Objective
Implement a "Digit-First" auto-indexing system, localize and contextually rename all GitHub assets, repair broken links, and implement advanced document cleanup (dead links & heading hierarchy).

## Status: COMPLETED

### Phase 1: Asset Localization & Renaming (DONE)
- [x] Created `scripts/localize_assets.py`.
- [x] Downloaded all GitHub-hosted images to `docs/assets/images/`.
- [x] Renamed assets contextually (e.g., `add-on-special-fields.png`).
- [x] Updated all markdown references to use relative local paths.

### Phase 2: Link Repair (DONE)
- [x] Created `scripts/fix_links.py`.
- [x] Implemented fuzzy matching for digit-prefixed files.
- [x] Implemented underscore/dash normalization for robust matching.
- [x] Repaired all broken relative links across the documentation.

### Phase 3: Digit-First Indexing & Navigation (DONE)
- [x] Implemented `scripts/generate_indexes.py` with digit-promotion logic.
- [x] Implemented `scripts/generate_mkdocs_yaml.py` with numeric sorting and promotion rules.
- [x] Extracted titles from first `# Heading` of markdown files.
- [x] Ensured non-digit items are excluded from auto-generation (except home and explicit extras).

### Phase 4: Manual & Pipeline Integration (DONE)
- [x] Populated `docs/5-anki/templates/index.md` with links to all template files.
- [x] Updated `scripts/web_preprocessing.sh` to run the full pipeline.
- [x] Updated `scripts/cl/sbs-build-website` to use the preprocessing pipeline.

### Phase 5: Advanced Document Cleanup (DONE)
- [x] Integrated `tools/printer.py` for consistent colorized CLI output (requires `rich`).
- [x] Added `rich` to `pyproject.toml`.
- [x] Created `scripts/clean_dead_links.py` (removes list items with broken links).
- [x] Created `scripts/fix_heading_hierarchy.py` (normalizes H1 and level sequences).
- [x] All scripts now use the `tools.printer` interface.

## Verification Result
- `bash scripts/web_preprocessing.sh` runs flawlessly with clean, colorized output.
- `uv run mkdocs build` completes with **0 warnings** related to broken links or missing files.
- Navigation accurately reflects the digit-prefixed folders and files.
- Images are served locally from `docs/assets/images/`.
