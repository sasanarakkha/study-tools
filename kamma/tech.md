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

## Content Improvement & Quality Assurance

- **Asset Verification:** Every build runs `scripts/verify_assets.py` (via `web_preprocessing.sh`) to ensure no broken image references in markdown files.
- **Data Preservation:** Before mass reformatting or structural changes, use `scripts/compare_pali_sources.py --commit <baseline_hash> --dir <path>` to ensure no data loss.
- **Automation First:** Prefer scripts over manual edits for large-scale formatting changes to ensure consistency and repeatability.
- **Prose Improvement:** Use `scripts/rewrite_english.py` for AI-assisted interactive rewriting of English prose with Pāḷi term preservation.
- **Grammar Validation:** Use `scripts/grammar_check.py` for offline LanguageTool-based grammar and spelling checks.

## Website Styling (`identity/sbs.css`)

`identity/sbs.css` is the only custom stylesheet (`extra_css` + `custom_dir` in `mkdocs.yaml`).

- **Scheme-scoped colour variables.** Material's light (`default`) and dark (`slate`) schemes need
  different values; a single `:root` colour cannot pass WCAG AA on both `#ffffff` and `#242424`.
  `:root` and `[data-md-color-scheme="slate"]` have *equal* specificity, so the slate block must be
  declared **after** the light block.
- **Body links carry no underline** in this theme, so colour is the only default cue. `identity/sbs.css`
  adds `font-weight: 700` on `.md-typeset a` as the non-colour cue (WCAG 1.4.1); hover rules set
  colour only and must never reset the weight.
- **`--md-accent-fg-color` is functional, not decorative.** It drives sidebar link hover/focus,
  meta/clipboard hover and every focus `outline-color`, so it must stay legible in both schemes.
- **Scheme backgrounds/text for contrast work:** light bg `#ffffff`, light body text `#212121`;
  slate bg `#242424`, slate body text `#c3bfbf`.

## What the output looks like

- Static HTML site in `site/` directory
- Built via `uv run mkdocs build`