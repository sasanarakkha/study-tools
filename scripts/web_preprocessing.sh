#!/bin/bash
set -e

# Change to the project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

# Set PYTHONPATH to include project root for tools.printer
export PYTHONPATH="$PROJECT_ROOT:$PYTHONPATH"

# Localize assets
uv run python scripts/localize_assets.py

# Repair broken links
uv run python scripts/fix_links.py

# Clean dead links
uv run python scripts/clean_dead_links.py

# Fix heading hierarchy
uv run python scripts/fix_heading_hierarchy.py

# Generate index pages
uv run python scripts/generate_indexes.py

# Generate mkdocs.yaml
uv run python scripts/generate_mkdocs_yaml.py
