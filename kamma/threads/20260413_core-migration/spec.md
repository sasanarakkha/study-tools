# spec.md — Thread 1: Core Migration (Jekyll → MkDocs)

**GitHub issue:** sasanarakkha/dpd-db-sbs#21
**Thread type:** refactor
**Blocks:** Threads 20260413_patimokkha-gen and 20260413_anki-style-docs

---

## Overview

Replace the near-empty Jekyll setup with MkDocs + Material theme,
reorganize all website content under `docs/`, establish the `identity/`
theme (sasanarakkha.org palette), and ship a working GitHub Actions
deploy pipeline. This is the structural foundation the other threads
build on.

---

## What It Should Do

### 1. Python tooling
- Create `pyproject.toml` with uv: `mkdocs`, `mkdocs-material`, `requests`
- Run `uv sync` to produce `uv.lock`
- Delete `_config.yml`

### 2. MkDocs config (`mkdocs.yaml`)
- Material theme, `docs_dir: docs`, `site_dir: site`
- `use_directory_urls: true` (MkDocs default — clean URLs)
- `identity/` as `custom_dir` for theme overrides
- Nav covering all content in `docs/`
- Extensions: `tables`, `toc`, `attr_list`, `md_in_html`, `nl2br`

### 3. Theme (`identity/sbs.css`)
- Primary / header: `#b6825e` (bronze, matches sasanarakkha.org)
- Tabs: `#8f6244`
- System font stack (matches sasanarakkha.org)
- Light + dark palette toggle

### 4. Content reorganization

Move into `docs/`:
- Root `.md` files → `docs/` (`README.md` copied as `docs/index.md`;
  root README simplified to a one-liner pointing at the live site)
- `anki-decks/*.md` → `docs/anki-decks/`
- `dict/` → `docs/dict/`
- `pali-class/*.md` → `docs/pali-class/`
- `pict/` → `docs/assets/`
- `videos/` → `docs/assets/videos/`

Delete entirely:
- `pali-class/vocab/` — outdated
- `pali-class/wordtree/` — outdated
- `id-aug-23/`, `id-feb-23/` — old 52MB CSV archives
- All `.csv` files anywhere in the repo — outdated; live CSVs are in GitHub Releases
- `anki-decks/(del) roots.md`, `(del) sutta-pitaka-vocab.md`
- `bhikkhu_patimokkha/` — HTML tree deleted here; `docs/bhikkhu_patimokkha/`
  will be populated by Thread 2's generation script

### 5. Link rewriting (`scripts/fix_links.py`)

The existing `.md` files have three classes of link to fix:

**a. GitHub user-image links** (`https://user-images.githubusercontent.com/...`)
- Download each image to `docs/assets/`
- Rewrite `![alt](url)` to a relative path: `![alt](../assets/filename.png)`

**b. `github.com/sasanarakkha/study-tools/blob/main/anki-style/…` links**
- Rewrite to future relative path: `../anki/filename.md`
  (Thread 3 creates the target files; Thread 1 fixes the link format)

**c. Absolute `sasanarakkha.github.io/study-tools/…` links**
- Rewrite to relative paths where the target exists in `docs/`

Script is idempotent and prints a report of every change made.

### 6. GitHub Actions deploy workflow
Replace `jekyll-gh-pages.yml` with `.github/workflows/deploy_site.yaml`:
- Trigger: push to `main` affecting `docs/**`, `mkdocs.yaml`, `identity/**`
- Steps: checkout → uv install → `uv sync --frozen` → `uv run mkdocs build`
  → `peaceiris/actions-gh-pages@v4` → `gh-pages` branch
- `workflow_dispatch` for manual runs

Post-deploy (manual step): GitHub repo Settings → Pages → Source →
branch `gh-pages`, folder `/`

### 7. Update `.gitignore`
Add: `site/`, `.venv/`, `__pycache__/`, `temp/`

---

## Assumptions & Uncertainties

- `bhikkhu_patimokkha/` nav entry is added by Thread 2, not here.
  `docs/bhikkhu_patimokkha/` directory is created empty as a placeholder.
- `anki-style/` stays at root for now — Thread 3 moves it. `fix_links.py`
  rewrites links to point at the future `docs/anki/` location.
- `primary: custom` in `mkdocs.yaml` may require an `identity/main.html`
  partial. Fallback: `primary: brown` + CSS-only overrides in `sbs.css`.
- GitHub user-image URLs may 404 if images were deleted. Script logs
  failures and skips rather than aborting.
- Videos (3 MP4 files, ~16MB) kept in repo under `docs/assets/videos/`.

---

## Constraints

- `temp-push/` stays git-ignored at root — external release mechanism
  depends on this exact path
- Commit references `sasanarakkha/dpd-db-sbs#21`

---

## How We'll Know It's Done

- `uv run mkdocs build` — 0 errors
- `uv run mkdocs serve` — all nav pages load, header is bronze `#b6825e`,
  dark mode toggle works, no broken image links
- `scripts/fix_links.py` runs and reports 0 unfixed links remaining
- `deploy_site.yaml` runs green on push to main
- `temp-push/` still git-ignored; Anki release mechanism unaffected

---

## What's Not Included

- Pātimokkha generation (Thread 2)
- `anki-style/` migration (Thread 3)
- PDF/DOCX generation, Python hooks, Git LFS
