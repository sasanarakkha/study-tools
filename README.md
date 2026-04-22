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

### Regenerating Pāṭimokkha Pages

The word-by-word Pāṭimokkha analysis pages are generated from an Excel spreadsheet:
```bash
uv run python scripts/generate_patimokkha.py [path/to/patimokkha.xlsx]
```
If no path is provided, it defaults to `temp/patimokkha.xlsx`.

## Project Structure

- `docs/` — Markdown source files and assets.
- `scripts/` — Python and Bash scripts for content generation and maintenance.
- `identity/` — Custom CSS and JavaScript for the SBS brand.
- `tools/` — Shared utilities and MkDocs hooks.
