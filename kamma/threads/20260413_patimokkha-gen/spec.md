# spec.md — Thread 2: Pātimokkha Generation

**GitHub issue:** sasanarakkha/dpd-db-sbs#21
**Thread type:** feat
**Depends on:** 20260413_core-migration merged (docs/ structure must exist)

---

## Overview

Move Bhikkhu Pātimokkha page generation fully into study-tools.
Replace the current dpd-db HTML pipeline with a Markdown generator
that lives in this repo. Add a weekly GitHub Action that downloads
the latest Google Sheets data and regenerates the pages automatically.

dpd-db patimokkha scripts are left unchanged — the owner will clean
them up manually.

---

## What It Should Do

### 1. Download script (`scripts/download_patimokkha.sh`)
Mirrors `dpd-db/scripts/bash/download_patimokkha.sh` behaviour:
- Checks internet connection
- Downloads from Google Sheets export URL:
  `https://docs.google.com/spreadsheets/d/1rS-IlX4DvKmnBO58KON37eVnOZqwfkG-ot-zIjCuzH4/export?format=xlsx`
- Saves to `temp/patimokkha.xlsx` (creates `temp/` if needed;
  `temp/` is git-ignored per Thread 1)
- Usable both locally and called from GitHub Actions

### 2. Generation script (`scripts/generate_patimokkha.py`)
Refactored from `dpd-db/scripts/other/patimokkha_dict.py`:

- Reads XLSX from path passed as CLI argument (default: `temp/patimokkha.xlsx`)
- Outputs to `docs/bhikkhu_patimokkha/`:
  - `index.md` — heading + list of all rules with relative links:
    `- [abbrev rule-name](rule-name.md)`
  - `[rule-name].md` per rule (~229 files):
    - Heading: `# [abbrev] rule-name`
    - Per-sentence `## sentence text` subheading
    - Word-by-word table via `pandas.to_markdown()`
    - Footer: `[← Home](index.md) | [Feedback](google-form-url)`
- All links are **relative** — no absolute web URLs anywhere
- Columns exported per row: `pali_1`, `pos`, `grammar`, `case`,
  `meaning`, `meaning_lit`, `root`, `base`, `construction`,
  `compound_type`, `compound_construction`

### 3. MkDocs nav update
Add Bhikkhu Pātimokkha section to `mkdocs.yaml` nav:
```yaml
- Bhikkhu Pātimokkha:
  - Index: bhikkhu_patimokkha/index.md
```

### 4. Weekly GitHub Action (`.github/workflows/regen_patimokkha.yaml`)
- Schedule: `cron: '0 3 * * 1'` (Monday 03:00 UTC)
- `workflow_dispatch` for manual runs
- Steps:
  1. Checkout repo (with write access)
  2. uv + Python 3.12, `uv sync --frozen`
  3. `bash scripts/download_patimokkha.sh`
  4. `uv run python scripts/generate_patimokkha.py`
  5. If files changed: git commit + push to main
     Message: `regen: patimokkha pages (sasanarakkha/dpd-db-sbs#21)`
  6. If no changes: exit clean (no commit)
  7. Push to main triggers `deploy_site.yaml` automatically

---

## Assumptions & Uncertainties

- Google Sheets URL is publicly accessible without auth — confirmed
  by existing `download_patimokkha.sh` using plain `curl`
- `GITHUB_TOKEN` can push to main in the Actions workflow. If branch
  protection blocks it, a PAT stored as repo secret will be needed.
- Pāli diacritic characters in filenames (e.g. `pārājikasikkhāpadaṃ.md`)
  assumed to work with MkDocs URL encoding — verify during local serve
- `pandas` and `tabulate` (for `to_markdown()`) added to `pyproject.toml`
  in this thread; `openpyxl` also needed for Excel reading
- `temp/` already git-ignored per Thread 1

---

## Constraints

- All internal links in generated MD must be relative (no absolute URLs)
- dpd-db scripts are not touched — owner handles cleanup separately
- Commit references `sasanarakkha/dpd-db-sbs#21`

---

## How We'll Know It's Done

- `bash scripts/download_patimokkha.sh` downloads XLSX to `temp/patimokkha.xlsx`
- `uv run python scripts/generate_patimokkha.py` produces
  `docs/bhikkhu_patimokkha/index.md` + ~229 rule `.md` files
- `uv run mkdocs serve` — Pātimokkha pages render with Markdown tables,
  relative links work (`[← Home]` navigates back), feedback link present
- `regen_patimokkha.yaml` runs green on manual `workflow_dispatch`
- Second run with unchanged XLSX produces no git commit (idempotent)

---

## What's Not Included

- Any changes to dpd-db
- Anki CSV generation for the patimokkha deck
- Any other dpd-db scripts
