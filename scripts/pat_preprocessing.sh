#!/bin/bash
# Run the pat preprocessing scripts to prepare the documentation for building.
set -e

# Change to the project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

# Generate patimokkha
uv run python scripts/generate_patimokkha.py

# Fix tables
uv run python scripts/fix_pali_tables.py

