# Handoff: restyle the study-tools website (issue #25)

**GitHub issue:** [sasanarakkha/study-tools#25](https://github.com/sasanarakkha/study-tools/issues/25)
**Status:** proposals drafted and prototyped on 2026-11-13. Nothing in `docs/`, `identity/`, `tools/`, `tests/` or `mkdocs.yaml` has been changed. No thread exists yet.
**Next step:** the owner picks a proposal (section 4), then a thread is planned from section 6.

Issue text, verbatim:

> The original SBS site is available at https://sasanarakkha.org/. The sbs-study-tools site should resemble it while remaining distinct. Its logo must also be similar yet different, so users can tell them apart in a browser while recognizing a shared family.

---

## 1. What is in this folder

| Path | What it is |
|---|---|
| `handoff.md` | This file. |
| `01-overview.png` | Reference site, today's site and the three proposals side by side (home, inner page, dark mode). Start here. |
| `02-reference-design-language.png` | What was extracted from sasanarakkha.org: palette, type, components, identity. |
| `03-proposal-1-family-colours.png` | Proposal 1 board. |
| `04-proposal-2-sanctuary-sibling.png` | Proposal 2 board (recommended). |
| `05-proposal-3-reading-room.png` | Proposal 3 board. |
| `06-logo-and-favicon.png` | Logo mark, four favicon candidates, browser-tab tell-apart test, lockups. |
| `07-tokens-and-components.png` | Colour tokens with contrast ratios, header options, component close-ups. |
| `screens/` | 42 raw 1440px screenshots: `current_*` (today), `p1_*`, `p2_*`, `p3_*`, each for home / anki / patimokkha / book in light and dark, plus phone-width shots and the slate-header variant. These are the target look for visual verification. |
| `prototype/identity/sbs.p1.css`, `sbs.p2.css`, `sbs.p3.css` | Complete, working replacement stylesheets for `identity/sbs.css`, one per proposal. |
| `prototype/identity/*.svg`, `*.png` | Logo mark, ghost mark, favicons (SVG plus PNG at 32/48/180/192/512), roundel, lockups. |
| `prototype/tools/home_hook.py` | Working MkDocs hook that turns the home page into hero + cards (proposals 2 and 3). |
| `prototype/build.sh` | Rebuilds any proposal into `temp/restyle/<p1\|p2\|p3>/site` without touching the real site files. |

The boards are composites of real builds: every screenshot is the current `docs/` built by MkDocs with the prototype stylesheet. They are not mock-ups.

To see a proposal live (run from the repo root):

```
bash kamma/draft/restyle/prototype/build.sh p2
cd temp/restyle/p2/site && python3 -m http.server 8765
```

Then open `http://127.0.0.1:8765/`. Use `p1` or `p3` for the others. `temp/` is gitignored.

---

## 2. Current state of the site (read from source, 2026-11-13)

- MkDocs 1.6.1 with Material 9.7.6. Config: `mkdocs.yaml`. Theme overrides live in `identity/` (`custom_dir`), so every file in `identity/` is copied to the site root.
- `identity/sbs.css` (176 lines) is the only web stylesheet. `identity/sbs.js` makes the header title a link to the home page. The `sbs-pdf*.css` files and `identity/fonts/` belong to the PDF pipeline and are out of scope.
- Palette is `primary: brown`, `accent: orange`, with brown header `#593e26` forced by `!important` rules. Page background is Material's default white (light) and bluish slate (dark).
- Header is compressed to 26px and **the logo is hidden** (`.md-header__button.md-logo { display: none }`). There is no favicon or logo configured.
- Home page (`docs/index.md`) is a heading, three paragraphs, a rule, two paragraphs and a list of seven section links.
- Body text is enlarged to `1rem` (20px). Body links are bold with no underline; the bold weight is the deliberate non-colour cue for WCAG 1.4.1 (documented in `kamma/tech.md`, "Website Styling").
- `body { font-family: "Inter", … }` names Inter but no `@font-face` loads it for the web, so visitors only see Inter if it is installed on their device. The screenshots here were taken on a machine that has Inter.
- `tools/patimokkha_hook.py` is the existing pattern for build hooks: an `on_post_page` function that edits rendered HTML with BeautifulSoup.
- `scripts/generate_mkdocs_yaml.py` rewrites `mkdocs.yaml` on every preprocessing run. It loads the whole file with `yaml.safe_load`, replaces only `nav`, and dumps with `allow_unicode=True, sort_keys=False`. Other keys survive; **YAML comments do not**, so do not rely on comments in `mkdocs.yaml`.
- Deploy: `.github/workflows/deploy_site.yaml` runs on pushes to `main` that touch `docs/**`, `mkdocs.yaml`, `identity/**`. A change to `tools/**` alone does not trigger a deploy.

---

## 3. The design language of sasanarakkha.org

Read from the live site's HTML and Elementor stylesheets and sampled from screenshots on 2026-11-13. See `02-reference-design-language.png`.

| Element | Value | Source |
|---|---|---|
| Header bar | `#191718` at 81% opacity; renders as `#141313` | header stylesheet, pixel sample |
| Dark tiles | `#1E1D1C` | pixel sample |
| Slate tile ("Teachings") | `#353740` | pixel sample |
| Page background, logo colour | `#EFE8DE` | global colour, pixel sample |
| Accent copper | `#B6825E` (nav active, links, favicon, footer icons) | global colour |
| Button copper | `#BE895F` | button rule |
| Body text | `#666666` / `#3A3A3A`; headings near-black, bold | stylesheets |
| Body font | system stack: `-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, …` | theme stylesheet |
| Nav font | Open Sans 600, 14px, cream at 88% | header stylesheet |
| Buttons | Lato 900, 13px, uppercase, `letter-spacing: 3px`, 2px copper border, square corners, transparent fill, fills on focus | button rule |
| Logo | cream line-drawn monk + three-line wordmark in wide-tracked bold capitals | `SBS_Icon_beidge.png` |
| Favicon | copper outlined lotus, transparent background | `cropped-lotusb6825e.512px` |

The family signature is: ink + cream + copper, small bold wide-tracked capitals, outlined square buttons, raised cream cards with a soft shadow, a dark header and footer.

The body font of the main site is the same system stack study-tools already declares, so **no new font is needed**.

---

## 4. The three proposals

All three share one token set (section 5). Each builds on the previous one, so choosing a smaller option now does not block a larger one later.

### Proposal 1: Family Colours (simplest)

Board: `03-proposal-1-family-colours.png`. Stylesheet: `prototype/identity/sbs.p1.css`.

- Recolour only. Cream page, warm ink dark mode, ink header, copper active tab, accessible copper links, new favicon.
- Keeps today's 26px header, hidden logo, thin grey headings and plain home list.
- Touches `identity/sbs.css`, `mkdocs.yaml` (palette + favicon), favicon files. No hook, no tests.
- Weakness: only the colours say "SBS". It reads as a recoloured docs site.

### Proposal 2: Sanctuary Sibling (recommended)

Board: `04-proposal-2-sanctuary-sibling.png`. Stylesheet: `prototype/identity/sbs.p2.css`.

Everything in Proposal 1, plus:

- **Header:** logo mark (lotus over an open book) and the site name in tracked capitals; 3px copper rule on top; header and tabs share one ink bar; the active tab is copper with a copper underline. Header returns to Material's standard height (2.4rem) instead of 26px.
- **Home page:** full-width ink hero band (heading, intro, large faint mark) and one card per section with a number and an outlined "Open" label. Built at build time by a hook from the existing link list; `docs/index.md` is not edited.
- **Headings:** bold and dark like the main site; `h2` gets a thin rule.
- **Download buttons:** any link whose URL contains `/releases/latest/download/` is drawn as the main site's outlined copper button. CSS selector only, no markdown change. There are 21 pages with such links.
- **Tables and images:** raised-card treatment (border, soft shadow); table heads use a sunken tone with a copper rule.
- **Footer:** SBS name, link back to sasanarakkha.org, licence, and three icon links (main site, GitHub, contact).
- Touches `identity/sbs.css`, logo/favicon files, new `tools/home_hook.py` + test, `mkdocs.yaml`, `README.md`, `kamma/tech.md`.

It is distinct from the main site through the mark's subject (book, not monk), the filled-tile favicon and the documentation layout, not through colour.

### Proposal 3: Reading Room (most distinct)

Board: `05-proposal-3-reading-room.png`. Stylesheet: `prototype/identity/sbs.p3.css` (Proposal 2 plus one 40-line block at the end).

- Light scheme: cream header with ink text and a copper active tab. Hero and footer use slate `#353740`, the colour of the main site's "Teachings" tile.
- Dark scheme: ink header as in Proposal 2, slate-tinted hero and footer.
- Tells the two sites apart at a glance, but gives up the dark header, which is the main site's strongest signature.

### Variant: slate header

Shown in `07-tokens-and-components.png` and `screens/p2_slate_variant_*.png`. Proposal 2 with header, hero and footer in slate `#353740`. It is a four-variable change on top of `sbs.p2.css`:

```css
[data-md-color-scheme] {
    --md-primary-fg-color: #353740;
    --sbs-hero-bg: #353740;
    --md-footer-bg-color: #353740;
    --md-footer-bg-color--dark: #2b2d35;
}
```

This block was only tested in the light scheme.

### Recommendation

Proposal 2 with favicon candidate A (copper tile). Confidence 8/10 that it is the best fit for the issue's wording. The remaining doubt is taste, which only the owner can settle.

### Decisions the owner must make before planning

| # | Decision | Default if the owner has no preference |
|---|---|---|
| 1 | Which proposal: 1, 2, 3, or 2 with the slate header | 2 |
| 2 | Favicon candidate A (copper tile), B (ink tile), C (outline), D (roundel). See `06-logo-and-favicon.png` | A |
| 3 | Accept the lotus-over-book mark, or ask for changes | accept |
| 4 | Header height: standard 2.4rem with logo (as prototyped), or keep the 26px compact header the owner chose earlier | standard |
| 5 | Footer content: is the wording and are the three icon links right? | as prototyped |
| 6 | Lockup wording "SBS / STUDY / TOOLS". The site name "SBS DhammaVinaya Learning Tools" is unchanged; the lockup is only for README/social use | keep, do not use on the site |
| 7 | Automatic button styling of release-download links: wanted on all 21 pages? | yes |

---

## 5. Colour tokens (final, contrast-checked)

Ratios computed with the WCAG 2 formula. AA for normal text is 4.5:1.

**Light scheme**

| Role | Hex | Contrast |
|---|---|---|
| Page | `#EFE8DE` | |
| Raised surface (cards, tables) | `#F7F3EC` | |
| Sunken surface (table heads, code) | `#E6DDD0` | |
| Body text | `#2B2826` | 12.0:1 on page |
| Muted text | `#5F5A55` | 5.6:1 on page |
| Link and button text | `#7D4C29` | 5.9:1 on page, 6.5:1 on raised, 5.3:1 on sunken |
| Hover / focus (`--md-accent-fg-color`) | `#5E3618` | 8.6:1 on page |
| Copper, decoration only | `#B6825E` | 2.7:1 on page: **never use for text on cream** |

**Dark scheme**

| Role | Hex | Contrast |
|---|---|---|
| Page | `#1E1D1C` | |
| Raised / sunken surface | `#2A2826` | |
| Body text | `#D9D1C5` | 11.1:1 on page |
| Muted text | `#A39C93` | 6.2:1 on page |
| Link and button text | `#D9A77F` | 7.8:1 on page, 6.8:1 on raised |
| Hover / focus | `#F0C9A6` | 10.9:1 on page |

**Header, tabs, footer (both schemes in proposals 1 and 2)**

| Role | Hex | Contrast |
|---|---|---|
| Header and tabs | `#191718` | |
| Header text | `#EFE8DE` | 13.8:1 on ink |
| Active tab | `#D9A77F` | passes on ink |
| Footer | `#1E1D1C` / `#141313` | footer text `#A39C93` is 6.8:1 on `#141313` |
| Slate (Proposal 3, variant) | `#353740` | cream text 9.8:1, `#D9A77F` 5.5:1 |

The main site's own footer grey `#726E6D` is 3.7:1 on its footer and was deliberately not copied.

---

## 6. Implementation guide for Proposal 2

Written so a thread's `spec.md` and `plan.md` can be lifted from it. If the owner picks Proposal 1, do only steps 6.1 (using `sbs.p1.css`), 6.2 (favicon only), 6.4 (palette and favicon keys only), 6.6 and 6.7. If Proposal 3, use `sbs.p3.css` in step 6.1; everything else is identical to Proposal 2.

### Spec points

- Keep the issue reference `#25` at the top of `spec.md` and `plan.md` (project workflow rule).
- No file in `docs/` is edited, added or removed. Markdown sources stay free of HTML.
- No new dependencies and no new fonts. `beautifulsoup4` is already used by the existing hook.
- All text/background pairs keep WCAG AA; links stay bold.
- Light and dark schemes both supported; the scheme toggle stays.
- Phone layout must not scroll sideways and the header title must not collide with the icons.
- The owner must confirm the look before the thread is finalized (project rule "Visual Changes").

### 6.1 Replace the stylesheet

Copy `kamma/draft/restyle/prototype/identity/sbs.p2.css` over `identity/sbs.css`.

Then tidy comment wording only: the section banners mention "proposals 2 and 3" and "Proposal"; reword them to describe the section without referring to proposals. Do not change any rule.

What the new file does differently from the old one, so a reviewer knows these are intentional:

- Removed: the brown `--md-primary-*` colours and all `!important` colour overrides; the 26px compact header block; the rule hiding the logo; the separate `.md-tabs` background.
- Kept unchanged: the system font stacks, the `body { font-family: "Inter", … }` rule, `font-size: 1rem` for body and tables, bold links, the whole Pātimokkha table block.
- Added: tokens, header/tab styling, headings, sidebar captions, download buttons, table and image treatment, footer, home page (hero, cards, closing note), small-screen block.

The file is organised as: 1 tokens, 2 components, 3 home page, 4 Pātimokkha tables.

### 6.2 Add logo and favicon files

Copy from `kamma/draft/restyle/prototype/identity/` to `identity/`:

- `sbs-mark.svg` (header logo; also the base of the hero decoration)
- `sbs-mark-ghost.svg` (faint version used by the hero background; referenced from the CSS as `url("sbs-mark-ghost.svg")`, which resolves because both files land in the site root)
- `sbs-favicon-48.png` (favicon)
- `sbs-favicon.svg` (source of the favicon, kept beside it)

For favicon candidate B use `sbs-favicon-ink.svg` and export PNGs from it; only candidate A has PNG exports here. For C use `sbs-mark.svg`, for D `sbs-roundel.svg`.

Do not copy the lockup SVGs into `identity/` unless they are used: everything in `identity/` is published. The lockups use live text in Helvetica/Arial; convert the text to outlines before using them outside a browser.

The mark was drawn from scratch for this proposal (five stroked paths for the lotus, two for the book, 512 viewBox, stroke width 34, round caps). It imitates the weight and style of the main site's favicon but copies no file from it.

### 6.3 Add the home page hook

Copy `kamma/draft/restyle/prototype/tools/home_hook.py` to `tools/home_hook.py`.

What it does, only for `index.md`:

1. Adds class `sbs-home` to `<body>` (the CSS uses it to hide the empty sidebars on the home page).
2. Wraps the `h1` and everything before the first `<hr>` in `<div class="sbs-hero">`.
3. Adds class `sbs-cards` to the last top-level `<ul>` and moves it directly after the hero.
4. Wraps what is left (the rule and closing paragraphs) in `<div class="sbs-home-foot">`.

If the page has no top-level `h1`, `hr` or `ul`, it returns the HTML unchanged. Nothing is deleted. Verified on the prototype build: the home article has the same 18 text strings and 11 links before and after the hook.

Write `tests/test_home_hook.py` against `restructure_home(output: str) -> str`. Each test must fail for its own reason:

- A fixture page with `h1`, two `p`, `hr`, one `p`, and a `ul` of three links: every link `href` and every text string is still present afterwards.
- The `ul` has class `sbs-cards` and is the element immediately after `.sbs-hero`.
- `.sbs-hero` contains the `h1` and exactly the paragraphs that came before the rule.
- `.sbs-home-foot` contains the `hr` and the paragraph that came after it.
- `<body>` has class `sbs-home`.
- A page without `<hr>` is returned byte-for-byte unchanged.
- `on_post_page` returns the input unchanged when `page.file.src_path` is not `index.md`.

The fixture must include `<body>` and `<article class="md-content__inner">`, because the hook looks for both.

### 6.4 Edit `mkdocs.yaml`

Change the `theme` block and add `hooks`, `copyright` and `extra.social`. Final values:

```yaml
theme:
  name: material
  language: en
  custom_dir: identity
  logo: sbs-mark.svg
  favicon: sbs-favicon-48.png
  font:
    text: false
    code: false
  palette:
    - media: '(prefers-color-scheme: light)'
      scheme: default
      primary: custom
      accent: custom
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - media: '(prefers-color-scheme: dark)'
      scheme: slate
      primary: custom
      accent: custom
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:          # unchanged
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.top
    - navigation.indexes
    - content.code.copy
hooks:
  - tools/patimokkha_hook.py
  - tools/home_hook.py
copyright: 'Sāsanārakkha Buddhist Sanctuary · <a href="https://sasanarakkha.org/">sasanarakkha.org</a> · <a href="http://creativecommons.org/licenses/by-nc/4.0/">CC BY-NC 4.0</a>'
extra:
  generator: false
  social:
    - icon: fontawesome/solid/house
      link: https://sasanarakkha.org/
      name: Sāsanārakkha Buddhist Sanctuary
    - icon: fontawesome/brands/github
      link: https://github.com/sasanarakkha/study-tools
      name: Source on GitHub
    - icon: fontawesome/solid/envelope
      link: mailto:studytools@sasanarakkha.org
      name: Contact us
```

Notes:

- `primary: custom` / `accent: custom` is what lets the stylesheet set colours without `!important`.
- `logo` and `favicon` paths are relative to the site root; they resolve because the files are in `custom_dir`. Confirmed in the prototype build (`<img src="../sbs-mark.svg">`, `<link rel="icon" href="../sbs-favicon-48.png">`).
- The licence URL and contact address are the ones already used in `docs/index.md`.
- After editing, run `bash scripts/web_preprocessing.sh` once and check with `git diff mkdocs.yaml` that the generator kept the new keys and changed nothing else. This round trip was not tested in this session.

### 6.5 `identity/sbs.js`

No change. It still wraps the header title in a link to the home page; the new CSS styles that link (`.md-header__topic a`). Confirmed working in the prototype.

### 6.6 Documentation

- `kamma/tech.md`, section "Website Styling": rewrite to the new tokens. It currently states light background `#ffffff`, slate background `#242424`, slate text `#c3bfbf`; these become `#EFE8DE`, `#1E1D1C`, `#D9D1C5`. Keep the three rules that still hold: the slate block must come after the light block (equal specificity), links stay bold as the non-colour cue, `--md-accent-fg-color` is functional. Add: copper `#B6825E` is decoration-only on cream; the hero must not be positioned (see 6.8).
- `README.md`: the line describing `identity/` and the list of hooks/tools should mention the logo files and `tools/home_hook.py`.

### 6.7 Verification

Python checks for the new hook and test (all mandatory in this project):

```
uv run ruff check --fix tools/home_hook.py tests/test_home_hook.py
uv run ruff format tools/home_hook.py tests/test_home_hook.py
uv run pyright tools/home_hook.py tests/test_home_hook.py
uv run --with pyrefly pyrefly check --min-severity warn tools/home_hook.py tests/test_home_hook.py
uv run pytest tests/test_home_hook.py -v
```

Never run bare `uv run pytest` in this repo. The prototype hook has not been run through ruff, pyright or pyrefly yet; expect to adjust typing (the existing `tools/patimokkha_hook.py` shows the style that passes).

Build and look:

```
bash scripts/web_preprocessing.sh
uv run mkdocs build
```

Compare these pages against `screens/p2_*.png`, in light and dark, at desktop and phone width:

- `index.html` (hero, 7 cards in rows of 4 + 3, closing note, footer)
- `5-anki/1-sbs/1-sbs-vocab/` (sidebar, headings, download button)
- `2-sbs-book/` (row of four small buttons, footer)
- `6-pali-class/bhikkhu-patimokkha/002-pa/` (table head, horizontal scroll)

Screenshot recipe used for this handoff (macOS, Chrome installed):

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1440,1000 --virtual-time-budget=4000 --screenshot=temp/shot.png http://127.0.0.1:8765/index.html
```

- Serve the built site over HTTP (`python3 -m http.server`), not `file://`.
- Headless Chrome follows the system colour scheme. To force one, screenshot a copy of the page with `<script>document.body.setAttribute("data-md-color-scheme","slate")</script>` (or `"default"`) inserted before `</body>`.
- Headless Chrome will not go narrower than 500px, so phone shots here are 500px wide.

Then ask the owner to confirm the look. Screenshots inspected by an agent are evidence, not sign-off.

### 6.8 Gotchas found while prototyping

1. **Do not give `.sbs-hero` a `position`.** Material decides when to swap the header title for the page title by reading the `h1`'s `offsetTop`. A positioned hero becomes the offset parent, the value drops to about zero, and the header shows "Home" instead of the site name. This is why the faint mark is a background image and not a positioned pseudo-element.
2. **Copper `#B6825E` fails contrast as text on cream (2.7:1).** Use `--sbs-copper-dark` for text in the light scheme. Copper is fine for text on ink (5.1:1).
3. **Order of scheme blocks matters.** `[data-md-color-scheme="default"]` and `[data-md-color-scheme="slate"]` have equal specificity; the slate block must come second. In Proposal 3 the light-header block is appended after both and is scoped to `default`.
4. **Full-width hero** uses `box-shadow: 0 0 0 100vmax` with `clip-path: inset(0 -100vmax)` so it bleeds to the window edges while its content stays in the text column. It needs no change to Material's templates.
5. **Cards use flex, not grid,** with `flex: 1 1 13rem`, so seven cards fall as 4 + 3 with the second row stretched. If a section is added or removed the rows rebalance on their own.
6. **The download-button selector is `a[href*="/releases/latest/download/"]`.** Links to a releases page (not a file) stay ordinary links. Extension-based selectors were rejected because they would also restyle PDF links inside running prose.
7. **The Light-header search box** (Proposal 3) needs its own background and text colour; Material assumes a dark header.
8. **Wide-tracked header title overflows on phones.** The small-screen block reduces its size and tracking; keep it.

---

## 7. Review items: not verified

- `.md-typeset img` now gets a border and shadow on every image. Only the pages listed in 6.7 were looked at. Check a page with many screenshots (the Anki guides under `docs/5-anki/general/`) and any small inline images.
- `.md-typeset h4` becomes small tracked capitals. No `####` headings exist in `docs/` today, so this is untested on real content.
- Only four page types were screenshotted per proposal. Not checked: search results overlay, the 404 page, the mobile navigation drawer, print styles, and pages in Russian or Tamil.
- Favicon: the boards show the SVG favicons; the PNG exports were checked for correct pixels and for the `<link rel="icon">` output, not in a real browser tab.
- Hover and focus states are defined in the CSS but cannot be seen in static screenshots.
- No browser other than Chrome was used.
- The `mkdocs.yaml` round trip through `scripts/generate_mkdocs_yaml.py` (step 6.4) was not run.

## 8. Explicitly out of scope

- Any edit to `docs/`.
- The PDF/DOCX pipeline and its stylesheets (`identity/sbs-pdf*.css`, `identity/fonts/`).
- Loading Inter (or any font) as a web font. If wanted later: `identity/fonts/` already holds Inter TTFs, but that is a separate decision with a page-weight cost.
- Photography or imagery from the main site.
- Changing `site_name` or any URL.

## 9. Approaches considered and dropped

- **Serif headings for a "manuscript" feel.** Dropped: system serif fonts on Windows lack some Pāḷi diacritics, and bundling a font was not justified.
- **Uppercase, tracked navigation tabs.** Dropped: the tab labels are long and would overflow; the main site's own navigation is sentence case.
- **Per-card descriptions on the home page.** Dropped: the text would have to be invented or scraped from each page.
- **Front matter (`template:` or `hide:`) on `index.md`** to restyle the home page. Dropped in favour of the hook so the markdown source stays untouched.
- **Positioned pseudo-element for the hero mark.** Dropped because of gotcha 1.
- **Reusing the main site's monk figure in the logo.** Not attempted: the issue asks for a different logo, and only a small PNG of the figure is available.

## 10. Repo state at handoff

- New, untracked: `kamma/draft/restyle/` (this folder). Nothing else was created or modified in the repository.
- `temp/restyle/p1`, `p2`, `p3` hold leftover prototype builds (gitignored, safe to delete).
- Pre-existing and not touched by this work: deleted `kamma/audit/owner-decisions.md` and untracked `kamma/threads/20261113_audit_recheck/` in the working tree.
- Nothing was committed or pushed, and no comment was posted on issue #25.
