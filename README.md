# SBS DhammaVinaya Learning Tools

This repository contains source materials, study tools, and documentation for the SBS Pāḷi-English study curriculum. It generates the [SBS DhammaVinaya Learning Tools](https://sasanarakkha.github.io/study-tools/) website.

## Main Sections

- **Foundation in Dhamma-Vinaya** — Pre-Pāli study materials.
- **SBS Pāḷi-English Recitations** — Companion for the SBS chanting book.
- **Pāṭimokkha Book** — Bhikkhu Pāṭimokkha study resources.
- **Dictionaries** — Hub for digital Pāḷi dictionaries, including the Digital Pāḷi Dictionary (DPD).
- **Anki Decks** — Comprehensive collection of Anki flashcard decks for vocabulary, grammar, and Pāṭimokkha.
- **Pāḷi Classes** — Materials for Advanced Pāḷi education and Pāṭimokkha word-by-word classes.

## Development

The site is built using [MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/).

### Local Setup

1. Install dependencies using [uv](https://docs.astral.sh/uv/):
   ```bash
   uv sync
   ```
2. Pre-process the content (generate indexes and navigation):
   ```bash
   bash scripts/web_preprocessing.sh
   ```
3. Start the local development server:
   ```bash
   uv run mkdocs serve
   ```

### Building the Site

To generate the static site in the `site/` directory:
```bash
bash scripts/web_preprocessing.sh && uv run mkdocs build
```

### Script Registry

These scripts are used for content generation, maintenance, and data integrity:

- `scripts/web_preprocessing.sh`: Main entry point for site generation prep — runs localization, link repair, heading normalization, and index generation.
  - Usage: `bash scripts/web_preprocessing.sh`
- `scripts/verify_assets.py`: Verifies that all image references in documentation point to existing files.
  - Usage: `uv run python scripts/verify_assets.py`
- `scripts/compare_pali_sources.py`: Identifies data loss between current Markdown files and a past Git commit.
  - Usage: `uv run scripts/compare_pali_sources.py --commit <hash> --dir <path>`
- `scripts/generate_patimokkha.py`: Generates word-by-word Pāṭimokkha analysis pages from an Excel spreadsheet.
  - Usage: `uv run scripts/generate_patimokkha.py`
- `scripts/download_patimokkha.sh`: Downloads the Pātimokkha Word by Word spreadsheet from Google Sheets.
  - Usage: `bash scripts/download_patimokkha.sh`
- `scripts/upload.sh`: Creates a new GitHub release and uploads assets from `temp-push/`.
  - Usage: `bash scripts/upload.sh`
- `scripts/upload_asset.sh`: Uploads a single specific asset to the latest draft release.
  - Usage: `bash scripts/upload_asset.sh`
- `scripts/resume_upload.sh`: Resumes an interrupted GitHub release upload.
  - Usage: `bash scripts/resume_upload.sh`

## Project Structure

- `docs/` — Markdown source files and assets.
- `scripts/` — Python and Bash scripts for content generation and maintenance.
- `identity/` — Custom CSS and JavaScript for the SBS brand.
- `tools/` — Shared utilities and MkDocs hooks.
