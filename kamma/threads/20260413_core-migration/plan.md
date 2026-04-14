# plan.md — Thread 1: Core Migration (Jekyll → MkDocs)

**GitHub issue:** sasanarakkha/dpd-db-sbs#21
**Depends on:** nothing (this is the foundation thread)

---

## Phase 1 — Python Tooling & MkDocs Config

- [x] Create `pyproject.toml` at repo root:
  ```toml
  [project]
  name = "study-tools"
  version = "0.1.0"
  description = "SBS DhammaVinaya Learning Tools website"
  requires-python = ">=3.12"
  dependencies = [
      "mkdocs>=1.6.0",
      "mkdocs-material>=9.5.0",
      "requests>=2.31",
  ]
  [build-system]
  requires = ["setuptools>=61.0"]
  build-backend = "setuptools.build_meta"
  ```
  → verify: `uv sync` completes without error, `.venv/` created

- [x] Create `identity/` directory with `identity/sbs.css`:
  ```css
  [data-md-color-scheme="default"] {
    --md-primary-fg-color: #593E26; /* Forest monk brown */
    --md-primary-fg-color--light: #7A5C43;
    --md-primary-fg-color--dark: #3D2614;
    --md-accent-fg-color: #593E26;
    --md-typeset-a-color: #593E26;
  }
  ... (overrides for slate and dark mode toggle)
  ```
  → verify: file exists at `identity/sbs.css` with dark monk-robe brown palette.

- [x] Create `mkdocs.yaml` at repo root.
  Note: This is now generated dynamically by `scripts/generate_mkdocs_yaml.py`.
  → verify: `uv run python scripts/generate_mkdocs_yaml.py` creates a valid `mkdocs.yaml` with dynamic navigation and `hide.generator`.

---

## Phase 2 — Content Migration

- [x] Create `docs/` directory (empty placeholder)
  → verify: `docs/` exists

- [x] Copy `README.md` → `docs/index.md` (updated with summary):
  → verify: `docs/index.md` contains the new welcoming summary.

- [x] `git mv` root-level `.md` files into `docs/`:
  → verify: files present in `docs/`, absent at root

- [x] `git mv` directories into `docs/`:
  → verify: directories present under `docs/`

- [x] Move images and videos to `docs/assets/`:
  → verify: `docs/assets/` contains the PNGs and `docs/assets/videos/` contains the MP4s

- [x] Create `docs/bhikkhu_patimokkha/` placeholder:
  → verify: `docs/bhikkhu_patimokkha/index.md` exists

- [x] Delete obsolete files and directories:
  → verify: outdated HTML and CSV archives removed.

- [x] Delete `_config.yml`:
  → verify: file absent

---

## Phase 3 — Link Rewriting & Refinements

- [x] Create and run `scripts/fix_links.py`:
  → verify: all GitHub user-images downloaded to `docs/assets/`, links rewritten to relative.

- [x] **New: Dynamic Navigation**:
  Created `scripts/generate_mkdocs_yaml.py` to build the nav from `docs/` folders.
  → verify: `scripts/cl/sbs-build-website` runs the generator automatically.

- [x] **New: Anki Deck Consolidation**:
  Moved verbose updating instructions to shared files (`updating.md`, etc.) and cleaned individual deck files.
  → verify: Individual deck pages are clean and link to shared Study Tools.

---

## Phase 4 — GitHub Actions & .gitignore

- [x] Delete old workflow:
  → verify: `jekyll-gh-pages.yml` absent

- [x] Create `.github/workflows/deploy_site.yaml`:
  → verify: file created at `.github/workflows/deploy_site.yaml`

- [x] Update `.gitignore`:
  → verify: `site/`, `.venv/`, `__pycache__`, `temp/` ignored.

---

## Phase 5 — Local Verification

- [x] Full local build:
  ```bash
  uv run mkdocs build
  ```
  → verify: exits 0.

- [x] Local serve and visual check:
  ```bash
  uv run mkdocs serve
  ```
  Open http://127.0.0.1:8000/ and check:
  - Header is dark monk-robe brown `#593E26`
  - Dark mode toggle works
  - Nav tabs visible (dynamically generated)
  - Home page loads with summary
  - Anki decks are clean and reorganized
  - Images render
  → verify: all above pass

- [x] Commit preparation (user executes):
  ```bash
  git add docs/ identity/ scripts/ mkdocs.yaml pyproject.toml uv.lock \
    .gitignore .github/workflows/deploy_site.yaml README.md
  ```
  Draft commit message:
  ```
  refactor: core migration SUCCESS, dynamic nav, monk brown theme, anki consolidation
  ```

---

## Phase 6 — Deploy & GitHub Pages Switch

- [x] Push to main and confirm `deploy_site.yaml` workflow runs green
  → verify: GitHub Actions tab shows green check on `Deploy Site`

- [x] Switch GitHub Pages source (manual — user does this):
  Settings → Pages → Source → branch: `gh-pages`, folder: `/`
  → verify: `https://sasanarakkha.github.io/study-tools/` loads the
    new MkDocs site with dark brown header
