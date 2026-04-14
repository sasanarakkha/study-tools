# Tech Notes: SBS DhammaVinaya Learning Tools

## Tools & Platforms

- **Static site generator:** MkDocs with Material theme
- **Python:** 3.12+ with uv, pandas, openpyxl, tabulate
- **Hosting:** GitHub Pages
- **CI/CD:** GitHub Actions

## Who This Is For

Developers maintaining the study-tools website.

## Constraints

- Must preserve existing `.html` URLs (use_directory_urls: false)
- Release mechanism must remain unchanged (temp-push/ git-ignored)

## Resources

- MkDocs Material documentation
- Reference: dpd-pali-courses repo structure

## What the output looks like

- Static HTML site in `site/` directory
- Built via `uv run mkdocs build`