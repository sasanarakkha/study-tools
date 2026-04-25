# Project Rules

Apply these in addition to your baseline global instructions `~/.claude/CLAUDE.md`.

## Project Overview

This project contains materials for Pāḷi language study.

**CRITICAL: DATA PRESERVATION:** Never remove data from the `docs/` folder. Only rearrange content without any loss. This is the MOST essential principle of this repository.

## Project Principles
- **Clean Markdown Sources:** Keep `.md` files extremely user-friendly and focused on content. NEVER use raw HTML, special symbols like `&nbsp;`, or complex `<div>` wraps in the source files. All necessary formatting fixes or UI elements (like navigation buttons or table adjustments) MUST be implemented via scripts or build hooks.
- **Data Integrity:** All automated changes must be verified against original meaning and structure.
- **Python Imports:** Prefer using a Hatch-based package structure (configured in `pyproject.toml`) for internal script and tool imports. Avoid `sys.path` hacks or `PYTHONPATH` exports in shell scripts.

## GitHub (upstream repository)
- Unless otherwise specified the repository in question is https://github.com/sasanarakkha/study-tools.

## Script Registry
If a script is intended to be run regularly (e.g., generators, verifiers, cleanup tools), it MUST be added to the project's root README.md with a brief explanation of how to use it.

## CLI Scripts (`scripts/cl/`)
All files placed in `scripts/cl/` MUST be made executable with `chmod +x` immediately after creation.

## One-Time Scripts
Scripts that run once (like data migrations or one-time transformations) MUST be moved to `scripts/archive/` after they complete successfully. This distinguishes them from permanent preprocessing or maintenance scripts. Place them in the active `scripts/` directory during development, then move to `scripts/archive/` during the finalize step.
