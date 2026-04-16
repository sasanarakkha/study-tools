# Spec: Dynamic Site Architecture & Docs Reorganization

## Overview
Transition the website architecture to use dynamically generated MkDocs navigation and auto-generated directory index pages, inspired by the `dpd-pali-courses` project. This requires a structural reorganization of the `docs/` folder (especially unifying Anki documentation) so that the folder hierarchy cleanly maps to the site navigation.

## What it should do
1. **Reorganize Content:** 
   - Unify `docs/anki/` and `docs/anki-decks/` into a structured `docs/anki/` directory.
   - Create `docs/anki/general/` for overarching guides.
   - Create `docs/anki/decks/` with subdirectories for specific decks (e.g., `dhp`, `patimokkha`, `vibhanga`, `sbs`, `grammar`, `roots`, `class`). Move related front/back templates, field lists, and user guides into these deck-specific folders.
   - Ensure other top-level folders (`dict/`, `bhikkhu_patimokkha/`, `pali-class/`) are structured logically for auto-generation.
2. **Port/Create Build Scripts:**
   - Adapt `scripts/clean_dead_links.py` from `dpd-pali-courses`: Target `docs/` directory, verify it successfully identifies and removes dead links from markdown lists.
   - Adapt `scripts/generate_indexes.py` from `dpd-pali-courses`: Modify to iterate over `docs/` subdirectories (`anki`, `bhikkhu_patimokkha`, `dict`, `pali-class`). Extract the first `# Heading` of each `.md` file to build a bulleted list of links in an `index.md` file within each directory. Handle nested directories recursively if needed.
   - Adapt `scripts/generate_mkdocs_yaml.py` from `dpd-pali-courses`: 
     - Read the existing `mkdocs.yaml` to preserve base configurations (`site_name`, `theme`, `plugins`, `markdown_extensions`, `extra_css`, etc.). Use the `ruamel.yaml` or `PyYAML` library to safely load and dump.
     - Dynamically scan `docs/` to build the `nav:` tree. Top-level files (like `index.md`, `patimokkha.md`) become top-level nav items. Subdirectories become nested nav sections. 
     - The script MUST rewrite `mkdocs.yaml` with the newly generated `nav:` section while keeping everything else intact.
3. **Build Pipeline Integration:**
   - Create `scripts/web_preprocessing.sh` that sequentially runs:
     1. `uv run python scripts/clean_dead_links.py`
     2. `uv run python scripts/generate_indexes.py`
     3. `uv run python scripts/generate_mkdocs_yaml.py`
   - Make the script executable (`chmod +x scripts/web_preprocessing.sh`).
   - Update `.github/workflows/deploy_site.yaml` (and any other relevant workflows) to execute `bash scripts/web_preprocessing.sh` before `uv run mkdocs gh-deploy` or `mkdocs build`.

## Assumptions & uncertainties
- We assume Python is available and we can add required libraries (like `pyyaml` or `ruamel.yaml`) via `uv add` if they aren't already in `pyproject.toml`.
- We assume the heading extraction logic from `dpd-pali-courses` (`get_first_heading()`) is robust enough for this project's markdown files. If not, the script will need to fallback to formatting the filename as the link title.

## Constraints
- **CRITICAL:** Do not delete or lose any markdown content from `docs/`. All content MUST be preserved.
- The site must continue to build successfully on GitHub Pages.
- Must use `uv` for python dependencies.

## How we'll know it's done
- `docs/anki-decks/` is completely merged into `docs/anki/` and deleted.
- Running `bash scripts/web_preprocessing.sh` successfully generates `index.md` files and updates `mkdocs.yaml`.
- `uv run mkdocs build` runs without errors and produces a correctly structured site.