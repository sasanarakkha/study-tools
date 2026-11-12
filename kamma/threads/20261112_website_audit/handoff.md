# Handoff — 20261112_website_audit (Issue #19)

**State:** Phases 1 and 2 are done except the owner gate: tasks 1.0–1.4 and 2.1–2.3 are `[x]`, and **2.4 (owner approval) is `[~]`**, waiting for the owner. Next: when the owner says the review is done, mark 2.4 `[x]` (check that the report still has at least one finding, or that the owner said nothing is approved). Then start **Phase 3, task 3.1**, on the **Fast** model.

## Phase 2 result
- Report: `kamma/audit/site-audit/site-audit.md`, with 85 numbered findings. 1–69 are Prose (1–2 are decisions: American English; no blanket Pāli/Pāḷi change), 70–85 are Site, plus Follow-ups and a triage summary. 
- Findings marked **⚠ data/URL**: 74 (`git mv` the Tamil page to drop " copy" from its name; the URL changes) and 77 (delete 3 empty `## Maintenance` headings). Findings marked **Pāḷi** (they change Pāḷi spelling): 8, 15, 32, 57.
- Finding 73 (dead BPS link) needs the owner to write in a replacement URL. Don't apply it without one.
- Finding 70 means *insert a blank line after* each listed line. Findings 76 and 81 are lists of `file:line` edits.

## Evidence and scripts (all in `temp/site-audit/`, git-ignored)
- `languagetool.tsv` (689 rows), `triage.tsv` (a disposition for every row: 38 accepted, 651 dropped; `triage.py` rebuilds it).
- `find_unseparated_lists.py <files.txt>`: lists that render as plain text (finding 70).
- `check_links.py <files.txt>`: internal links and anchors (none missing; only the empty links in `sbs-per-ex.md`).
- `suspect-urls.txt` / `suspect-urls-status.txt`: HTTP status of 55 release-download and DPD links (7 return 404).
- `verify_quotes.py`: checks that every quoted "Current" text exists in its file. (It also checks for approve boxes; they were removed on 2026-11-12, so that check no longer applies.) The last run reported 85 findings, 0 problems.

## Things Phase 3 must know
- **Generated files:** `docs/index.md` and the folder `index.md` files are rebuilt from `.header.md` by `scripts/generate_indexes.py`, and the `mkdocs.yaml` nav from first headings by `scripts/generate_mkdocs_yaml.py`. Edit the source file named in the finding; `bash scripts/web_preprocessing.sh` (task 3.3) regenerates the rest. A note about this has been added to plan task 3.3.
- **Spec correction (DRIFT GATE):** the site uses directory URLs (`1-pre-pali-study/`), not `.html`; `mkdocs.yaml` does not set `use_directory_urls`. `spec.md` Constraints has been corrected.
- Findings that name several files (e.g. 21, 24, 34, 60–64) apply the same edit in each named file.

## Commands that worked (for the guide, task 4.1)
- Everything listed in the Phase 1 handoff (file list, `--report` run, mkdocs build), plus:
- `uv run python temp/site-audit/find_unseparated_lists.py temp/site-audit/files.txt`
- `uv run python temp/site-audit/check_links.py temp/site-audit/files.txt`
- `uv run python temp/site-audit/triage.py`
- `uv run python temp/site-audit/verify_quotes.py`

## Lessons for the guide (task 4.1)
- LanguageTool false positives here were mostly Pāḷi words (299), product and proper names (131), file names/URLs (103) and Buddhist loanwords (43). Only 38 of 689 rows were real errors; most real problems were grammar that LanguageTool doesn't catch.
- Python-Markdown needs a blank line before a list; without it the items render as text with literal `- `. Check this by script; LanguageTool can't see it.
- `../../index.md` from a sub-sub-folder points at the site home page, not the section index; link checks that test only "file exists" miss this.
- The DPD site moved to directory URLs (`features/`, `install/`), and the old `.html` pages return 404.

## Files touched in Phase 2
`kamma/audit/site-audit/site-audit.md` (new), `kamma/threads/20261112_website_audit/{plan.md,spec.md,handoff.md}`, `temp/site-audit/*` (scratch). No change to `docs/`, `mkdocs.yaml` or `scripts/`.

## Validation
- `uv run pytest tests/test_grammar_check.py -q`: 4 passed (baseline at session start).
- `verify_quotes.py`: 85 findings, 0 problems. `triage.py`: 689 of 689 rows assigned.
- `git status --short docs/ mkdocs.yaml`: clean.

## Not done / known issues
- Nothing committed. The Phase 1 renames and script change, plus the Phase 2 report, are ready for the owner to commit.
- `NOTICED — NOT TOUCHING`: the orphaned pages, HTML comments, chant-translation questions and Russian typos are listed under Follow-ups in the report, not as findings.

## Next
1. The owner reviews `kamma/audit/site-audit/site-audit.md` and ticks the findings to apply.
2. A fresh session on the **Fast** model runs `/kamma:2-do 20261112_website_audit`. It marks 2.4 `[x]` after confirming the owner's approval, then starts 3.1.
