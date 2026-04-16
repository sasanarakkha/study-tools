# plan.md - Thread: 20260413_header-identity

---

## Phase 1 - Confirm the reference behavior and local target files

- [ ] Inspect the current SBS identity setup in `mkdocs.yaml` and `identity/sbs.css`.
  - identify where the current header height, font stack, and extra assets are defined
  - confirm whether the site already loads any JS for the header
  → verify: notes from inspection identify the exact files and selectors that control the current header and typography

- [ ] Inspect the reference files in `/Users/deva/Documents/dpd-pali-courses/` that define the behavior to mirror.
  - read `/Users/deva/Documents/dpd-pali-courses/mkdocs.yaml`
  - read `/Users/deva/Documents/dpd-pali-courses/identity/extra.css`
  - read `/Users/deva/Documents/dpd-pali-courses/identity/dpd.css`
  - read `/Users/deva/Documents/dpd-pali-courses/identity/footnotes.js`
  - extract only the header-height, font-size, font-family, and title-link logic relevant to this thread
  → verify: the reference selectors and rules are identified in the thread notes before any implementation begins

- [ ] Decide the smallest SBS-side implementation that reproduces the requested behavior.
  - keep the plan focused on CSS plus one small JS hook if needed
  - avoid copying unrelated DPD identity behavior
  → verify: the chosen approach is simple enough to fit in one identity update and does not require content changes

- [ ] Phase 1 verification.
  → verify: the reference behavior is clearly mapped to local files and the implementation approach is fixed

## Phase 2 - Apply the identity update

- [ ] Update `mkdocs.yaml` so the site loads the needed identity assets for this thread.
  - keep the SBS site name and navigation intact
  - add only the CSS and JS assets required for the new header and typography behavior
  → verify: `uv run mkdocs build` reads the updated config without errors

- [ ] Update `identity/sbs.css` to make the header narrower and the reading text larger.
  - mirror the compact header treatment from the reference CSS
  - increase the base readable text size
  - keep SBS colors and branding unless the request requires a change
  → verify: a local build shows the narrower header and larger text behavior on standard content pages

- [ ] Add or update a small identity JS file so the visible header title text becomes a homepage link.
  - use the reference title-link behavior as the model
  - make the title words themselves clickable, not only the logo
  → verify: in a local browser, clicking the header title text returns to the homepage

- [ ] Phase 2 verification.
  → verify: `uv run mkdocs build` completes successfully and the new assets are present in the built site

## Phase 3 - Verify the rendered site

- [ ] Run `uv run mkdocs build` and fix any config or asset regressions.
  → verify: the build exits 0 with no errors

- [ ] Run `uv run mkdocs serve` and inspect the rendered site in a browser.
  - open the homepage
  - open at least one content page
  - confirm the header is narrower
  - confirm the text is larger
  - confirm the title text is clickable and returns home
  → verify: the rendered site matches all requested behaviors on both the homepage and an internal page

- [ ] Record the result in `kamma/threads/20260413_header-identity/handoff.md`.
  - list files changed
  - list verification commands run
  - state whether the thread is ready for review
  → verify: `handoff.md` contains the final implementation summary and verification notes

- [ ] Phase 3 verification.
  → verify: the site behavior is confirmed manually and the handoff is complete
