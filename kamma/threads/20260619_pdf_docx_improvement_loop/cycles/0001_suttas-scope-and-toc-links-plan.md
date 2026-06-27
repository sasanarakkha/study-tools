# Cycle 0001: suttas.pdf/docx scope + TOC + working links (PLAN ONLY — not yet implemented)

## Report

User-reported: `suttas.pdf` contains content outside `docs/6-pali-class/suttas/`. It
should have only that folder's content, in the order listed in
`docs/6-pali-class/1-pali-class-adv.md`, with a relevant Table of Contents (new one
if needed) limited to files actually present in `suttas/`, and all internal links —
"index leads to TOC", TOC leads to content — must work. Same link-correctness
requirement applies to all three generated PDFs.

## Root causes (confirmed)

### Bug 1 — content scope (suttas only)

`get_markdown_files()` in both `scripts/generate_pdfs.py` (line ~413) and
`scripts/generate_docx.py` (line ~211) treats `docs/6-pali-class/1-pali-class-adv.md`
as the suttas index. That file is the *whole* "Advanced Pāli Education" page — it
also links to `sbs-per-analysis.md`, `sbs-per-analysis/pubbakicca-analysis.md`,
`../4-dictionaries/1-sbs-pali-dictionary.md`, and the entire "Advanced Pāli Course"
key-to-exercises set. The suttas branch parses *every* `.md` link on that page
(`parse_md_links(index_content, index_base)`), then recurses into each one,
again with no folder restriction. Reproduced by generating
`output/pdf/suttas_debug.html` — it contains SBS recitation and Anki-workflow
content that doesn't belong.

### Bug 2 — TOC links don't resolve (all three PDFs)

In `build_html_document()` (`generate_pdfs.py`, line ~301), when `root_index_content`
is empty (true for all three folders today — `main()` hardcodes `root_index_content=""`
at line ~485), the TOC is built by:
```python
all_md = ""
for file_path, content in files_data:
    all_md += pre_process_content(clean_markdown_content(content)) + "\n\n"
md.convert(all_md)
toc = getattr(md, "toc", "")
```
This is a **separate** Markdown conversion pass from the one that renders each file's
content (`md.reset()` + `md.convert(...)` per file at line ~347-348).

The `toc` extension's heading-id de-duplication (`used_ids` in
`.venv/.../markdown/extensions/toc.py` line ~367) is scoped to a single `run()` call
— i.e. to whatever is inside one `convert()` call's document tree. Per-file content
conversion never sees other files' headings, so a heading like "Pāli Text" repeated
in 5 different sutta files gets the **same unsuffixed id** in all 5 content divs. The
TOC-building pass converts everything concatenated in one call, so *it* sees all 5
occurrences and correctly suffixes them `_1`.._4. Result: the TOC links to
`#pali-text_1`..`#pali-text_4`, none of which exist in the actual content (only
`#pali-text`, six times over, exists). Reproduced and confirmed with
`sbs-per-analysis_debug.html`: TOC contains `#homage-to-the-triple-gem_1`..`_5`;
content has six identical `id="homage-to-the-triple-gem"` elements and nothing
matching the suffixed ids. This affects **all three** PDFs whenever a heading
repeats across files (very common in this corpus — "Pāli Text", "Translation",
"Grammatical Analysis", section names in the recitation book, etc.).

DOCX has an analogous but distinct issue: `build_manual_toc()`
(`generate_docx.py` line ~103) computes a heading slug per occurrence via
`make_heading_slug()` with **no de-dup tracking at all**, so every repeated heading
gets the *same* href. Pandoc itself auto-assigns ids to headers in the final
document and *does* de-dup duplicates by appending `-1`, `-2`, ... in document
order. So in the DOCX, all of `build_manual_toc`'s entries for a repeated heading
point to the *first* occurrence's id — entries 2+ are simply wrong, not dangling.
(This assumption about Pandoc's own dedup suffix format should be verified with a
quick sample conversion before relying on it — see Step B3.)

## Plan

Two cycles. **Cycle A is self-contained and should be done first** — it fixes the
literal complaint (suttas scope + suttas TOC + suttas links) without touching the
other two PDFs. **Cycle B is a separate, larger architectural fix** for the
TOC-link bug across all three PDFs/DOCX — bigger blast radius, needs its own
review/validation pass, do not bundle into Cycle A.

---

### Cycle A — suttas.pdf / suttas.docx scope + curated TOC

**A1. Fix file discovery (`get_markdown_files`, both scripts).**

Add a containment check and apply it to both the top-level links and the recursive
children in the `suttas` branch:

```python
def _is_within(path: str, base_dir: str) -> bool:
    base_abs = os.path.abspath(base_dir)
    path_abs = os.path.abspath(path)
    return path_abs == base_abs or path_abs.startswith(base_abs + os.sep)
```

```python
if folder_key == "suttas":
    suttas_dir = FOLDER_DIRS["suttas"]
    files: list[str] = []
    for top_file in parse_md_links(index_content, index_base):
        if not _is_within(top_file, suttas_dir):
            continue
        files.append(top_file)
        with open(top_file, "r", encoding="utf-8") as f:
            sub_content = f.read()
        top_base = os.path.dirname(top_file)
        for child in parse_md_links(sub_content, top_base):
            if _is_within(child, suttas_dir) and child not in files:
                files.append(child)
    result[folder_key] = files
```

Order is preserved automatically (link order in `1-pali-class-adv.md` is already
correct; `parse_md_links` is order-preserving).

**A2. Curated TOC source — shared by PDF and DOCX.**

Add a helper (duplicate it into both scripts, matching the existing duplication
pattern of `parse_md_links`/`FOLDER_DIRS`/etc. — do not introduce a shared module
in this cycle, that's an unrelated refactor):

```python
def extract_suttas_toc_source(suttas_files: list[str]) -> str:
    """Curated TOC markdown: the 'Suttas and passages' section of
    1-pali-class-adv.md, limited to links we actually kept."""
    index_path = INDEX_FILES["suttas"]
    index_base = os.path.dirname(os.path.abspath(index_path))
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    m = re.search(r"## \*\*Suttas and passages\*\*\n(.*?)(?=\n## )", content, re.DOTALL)
    section = m.group(1) if m else ""
    kept = {os.path.abspath(p) for p in suttas_files}

    def keep_link(match):
        href = match.group(2)
        if href.startswith("http"):
            return match.group(0)
        abs_path = os.path.normpath(os.path.join(index_base, href))
        return match.group(0) if abs_path in kept else match.group(1)

    return re.sub(r"\[([^\]]+)\]\(([^)#\s]+\.md)\)", keep_link, section)
```

Verify the regex against the live heading text first — confirm
`## **Suttas and passages**` is exactly that string (it is, per
`docs/6-pali-class/1-pali-class-adv.md` read this session) and that the next `##`
heading is `## **Advanced Pāli Course**` (also confirmed) so the non-greedy
`(?=\n## )` lookahead stops in the right place.

**A3. Wire it into the PDF builder.**

In `generate_pdfs.py` `main()` (line ~479), for the `suttas` folder only, pass
`root_index_content=extract_suttas_toc_source(files)` instead of `""`. Leave
`bhikkhu-patimokkha` and `sbs-per-analysis` exactly as they are (`root_index_content=""`)
— do not change their TOC mechanism in this cycle.

This makes `build_html_document()` take the `if root_index_content:` branch
(line ~366-367) for suttas, rendering the curated section as the TOC page. Because
`post_process_html()`'s href-fixup (line ~209-223) converts any `.md` link to
`#{basename}_md` — the same id scheme used for each file's wrapping div
(`file_id = os.path.basename(file_path).replace(".", "_")`, line ~358-359) — and
file-level ids are unique by construction (distinct basenames), this TOC's links
cannot suffer the duplicate-heading-id bug from Bug 2. No further change needed for
suttas's link correctness.

**A4. Wire an equivalent curated TOC into the DOCX builder.**

`generate_docx.py`'s `aggregate_markdown()` (line ~119) currently calls
`build_manual_toc(files_data)` for any folder in `SBS_FOLDERS` (which includes
`suttas`). Replace that call, for `folder == "suttas"` only, with a new function
that builds TOC entries directly from the curated section text using file-level
anchors (matching the `anchor_id = os.path.basename(file_path).replace(".", "_")`
scheme already used at line ~154):

```python
def build_suttas_toc(toc_source: str, suttas_files: list[str]) -> str:
    """File-level-anchor TOC for suttas, built from the curated index section."""
    lines = ["# Table of Contents", ""]
    by_name = {os.path.basename(p): p for p in suttas_files}
    for m in re.finditer(r"\[([^\]]+)\]\(([^)#\s]+\.md)\)", toc_source):
        text, href = m.group(1), m.group(2)
        basename = os.path.basename(href)
        if basename in by_name:
            anchor_id = basename.replace(".", "_")
            lines.append(f"- [{text}](#{anchor_id})")
    lines.append("")
    return "\n".join(lines)
```

Call `extract_suttas_toc_source(files)` (mirrored into this script per A2) and pass
its result into `build_suttas_toc`. Leave `build_manual_toc` untouched and still in
use for `bhikkhu-patimokkha` / `sbs-per-analysis`.

**A5. Validate.**

1. `uv run python scripts/generate_pdfs.py suttas` and
   `uv run python scripts/generate_docx.py --folder suttas`.
2. Confirm `output/pdf/suttas.pdf` / `output/docs/suttas.docx` contain only
   `docs/6-pali-class/suttas/**` content (no SBS recitations, no Advanced Pāli
   Course exercises, no dictionary page).
3. Confirm the TOC order matches the "Suttas and passages" section of
   `1-pali-class-adv.md` (MN 107, then the six SN compilations in listed order).
4. Open both outputs and manually click every TOC entry — confirm each lands on
   the correct section (not just "doesn't crash" — actually verify the target).
5. Run `ruff check --fix`, `ruff format`, `pyright`, `pyrefly check --min-severity warn`
   on both touched files (per CLAUDE.md mandatory gate).
6. Run any existing tests under `tests/` that cover these scripts.

---

### Cycle B — universal TOC/anchor-id consistency fix (all three PDFs + DOCX)

This is **not** included in Cycle A. It's a structural fix to the shared rendering
core in `build_html_document()` and is higher risk — it changes how every PDF
(not just suttas) gets its ids assigned, so it needs its own validation pass across
all three outputs before being considered done. Recommend running it as its own
loop cycle after A is validated and committed.

**B1. The real fix: make content ids and TOC ids come from the same conversion.**

The per-file loop currently does, for each file (`generate_pdfs.py` line ~347-348):
```python
md.reset()
topic_html = md.convert(pre_process_content(c))
```
`md.reset()` does not matter here — `toc`'s `used_ids` set is rebuilt fresh inside
each `run()` (i.e. each `convert()` call) regardless of `reset()`
(`toc.py` line ~367, confirmed by reading the installed `markdown` package
source). The dedup only sees headings within *one* `convert()` call. So simply
removing `md.reset()` between files will **not** fix anything by itself — the fix
has to make all files' headings part of one `convert()` call.

Concrete approach: convert all files' markdown in a single `md.convert()` call
(like the existing — but currently TOC-only — `all_md` accumulation already does),
and recover the per-file HTML boundaries by inserting a sentinel marker between
files' raw markdown before conversion, then splitting the resulting HTML on that
marker afterward to rebuild each file's wrapping `<div class='pdf-topic-page' id=...>`.

Sketch:
```python
SENTINEL = "<!--FILE-BOUNDARY:{idx}-->"

raw_chunks = []
for idx, (file_path, content) in enumerate(files_data):
    c = clean_markdown_content(content)
    c = resolve_image_paths(c, file_path)
    if not is_idx and not folder_type.endswith(("_ex", "_key")):
        c = re.sub(r"^# Class \d+.*?\n", "", c, flags=re.MULTILINE)
    raw_chunks.append(SENTINEL.format(idx=idx) + "\n\n" + pre_process_content(c))

md.reset()
combined_html = md.convert("\n\n".join(raw_chunks))
toc = getattr(md, "toc", "")  # now correctly de-duplicated against ALL headings
# split combined_html on the sentinel comments (markdown/md_in_html passes raw
# HTML comments through untouched — verify this holds for every extension combo
# in use before relying on it) and wrap each piece in its own div using the
# existing file_id / div_class / per-folder-type heading-shift logic.
```

This is a genuine restructure of the content-loop in `build_html_document()`
(lines ~336-376) — every special case currently handled per-file (the `bpc`/`ipc`
heading-level shift at line ~349-354, the `is_idx` div-class switch at line ~355-360,
the `# Class N` stripping) has to be preserved across the split. Budget real time
for this; don't treat it as a one-line change.

**B2. Validate the sentinel-splitting approach carefully** before trusting it:
write a throwaway script in `temp/` that runs the conversion on two small files
with a shared heading name and checks (a) the comment survives conversion
unmolested, and (b) the resulting ids in content match the ids in `md.toc` exactly.

**B3. DOCX equivalent — verify Pandoc's own dedup format first.**

Before changing `build_manual_toc()`, confirm empirically (small throwaway markdown
file with a repeated `## Heading` converted via `pypandoc.convert_text(..., "docx")`,
then inspect the resulting `document.xml` bookmark/anchor names) what suffix format
Pandoc actually uses for duplicate header ids in this Pandoc version. Only once
that's confirmed, make `build_manual_toc()` track `used_slugs` (a `Counter` or
`set`, matching Pandoc's exact suffix scheme) so generated hrefs match Pandoc's
real output instead of assuming no duplicates exist.

**B4. Validate.**

Regenerate all three PDFs and all three DOCX files. For each, manually click every
TOC entry (not just the first few) and confirm it lands on the right heading —
pay particular attention to sections with deliberately repeated heading text
(e.g. "Pāli Text" / "Translation" patterns, "Homage to the Triple Gem" in
sbs-per-analysis). Run the full CLAUDE.md pre-completion gate on both touched
files.

## Status

Plan only. No source files have been changed in this cycle. Next session should
execute Cycle A first (A1-A5), confirm with the user, then decide whether to open
Cycle B as its own loop cycle.
