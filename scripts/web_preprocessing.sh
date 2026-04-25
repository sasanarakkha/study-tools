#!/bin/bash
# Run the full suite of preprocessing scripts to prepare the documentation for building.
set -e

# Change to the project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

# Generate patimokkha
uv run python scripts/generate_patimokkha.py

# Fix tables
uv run python scripts/fix_pali_tables.py

# Clean dead links
uv run python scripts/clean_dead_links.py

# Fix heading hierarchy
uv run python scripts/fix_heading_hierarchy.py

# Generate index pages
uv run python scripts/generate_indexes.py

# Generate mkdocs.yaml
uv run python scripts/generate_mkdocs_yaml.py
