# Tech Notes: SBS DhammaVinaya Learning Tools

## Tools & Platforms

- **Static site generator:** MkDocs with Material theme
- **Python:** 3.12+ with uv, pandas, openpyxl, tabulate, beautifulsoup4
- **Hosting:** GitHub Pages
- **CI/CD:** GitHub Actions

## Build Workflow

1. Run `bash scripts/web_preprocessing.sh` to generate indices, update navigation, and localize assets.
2. Run `uv run mkdocs build` to generate the static site.

## Who This Is For

Developers maintaining the study-tools website.

## Constraints

- Must preserve existing `.html` URLs (use_directory_urls: false)
- Release mechanism must remain unchanged (temp-push/ git-ignored)

## Resources

- MkDocs Material documentation
- Reference: dpd-pali-courses repo structure

## Quality Assurance & Maintenance

- **Data Preservation:** Before mass reformatting or structural changes, use `scripts/compare_pali_sources.py --commit <baseline_hash> --dir <path>` to ensure no data loss.
- **Automation First:** Prefer scripts over manual edits for large-scale formatting changes to ensure consistency and repeatability.

## What the output looks like

- Static HTML site in `site/` directory
- Built via `uv run mkdocs build`