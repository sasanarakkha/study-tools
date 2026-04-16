# spec.md - Thread: 20260413_header-identity

**Thread type:** chore

---

## Overview

The SBS DhammaVinaya Learning Tools site needs a small identity refresh so its header and typography match the relevant behavior from `/Users/deva/Documents/dpd-pali-courses/`.

This thread uses that repository as the reference for:

- compact top header height
- larger default reading text
- the visible site title in the header being clickable and linking to the homepage

This is not a request to copy the full `dpd-pali-courses` identity stack. Only the header and font behavior relevant to this site update should be adopted.

Reference files:

- `/Users/deva/Documents/dpd-pali-courses/mkdocs.yaml`
- `/Users/deva/Documents/dpd-pali-courses/identity/extra.css`
- `/Users/deva/Documents/dpd-pali-courses/identity/dpd.css`
- `/Users/deva/Documents/dpd-pali-courses/identity/footnotes.js`

Current SBS files that are likely affected:

- `mkdocs.yaml`
- `identity/sbs.css`
- one small identity JS file if the title-link behavior is implemented there

---

## What It Should Do

- Make the top header bar visually narrower and more compact.
- Increase the base reading font size across the site so body content is easier to read.
- Match the relevant font-family / typography feel from the reference site where practical.
- Make the visible header title text `SBS DhammaVinaya Learning Tools` itself clickable.
- Clicking the title text should go to the homepage, just like the reference site behavior.
- Keep the site name, content, and navigation unchanged.

---

## Assumptions & Uncertainties

- The request is about the live website presentation, not PDFs or export outputs.
- The reference repo is the source of truth for the requested header and font behavior, but only for the specific rules named above.
- It is acceptable to implement the clickable title as a small JS behavior rather than trying to rework MkDocs templates.
- The current site probably does not need the rest of the DPD identity CSS or JS.
- No GitHub issue number was provided.

---

## Constraints

- Do not change Markdown content just to force the visual result.
- Preserve existing SBS branding and navigation structure.
- Preserve existing `.html` URL behavior and MkDocs build flow.
- Do not import unrelated DPD behavior such as footnotes, PDF styling, or search customization.
- Keep the implementation minimal and local to the identity layer.

---

## How We'll Know It's Done

- The site builds successfully with `uv run mkdocs build`.
- The top header is visibly narrower than before.
- Body text is noticeably larger across the site.
- The visible header title text is clickable.
- Clicking the title text returns to the homepage.
- The implementation files clearly show the relevant CSS/JS changes and the use of the reference repo as the source for the behavior.

---

## What's Not Included

- Full visual parity with `dpd-pali-courses`
- New content pages or navigation changes
- Footnote tooltip behavior
- PDF output changes
- Search behavior changes
- Any data removal from `docs/`
