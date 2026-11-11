#!/bin/bash
# Regenerate the Pātimokkha pages from data/patimokkha_word_by_word.tsv (also run by the patimokkha-regen pre-commit hook).
set -e

# Change to the project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

# Generate patimokkha
uv run python scripts/generate_patimokkha.py

# Fix tables
uv run python scripts/fix_pali_tables.py --dir docs/6-pali-class/bhikkhu-patimokkha

