#!/bin/bash
# Locally regenerate the Pātimokkha pages exactly as regen_patimokkha.yaml does, minus git steps.
set -e

# Change to the project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

# Download the latest spreadsheet from Google Sheets
bash scripts/download_patimokkha.sh

# Generate patimokkha
uv run python scripts/generate_patimokkha.py

# Fix tables
uv run python scripts/fix_pali_tables.py --dir docs/6-pali-class/bhikkhu-patimokkha

