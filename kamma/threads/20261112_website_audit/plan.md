# Plan: Website English & Site Audit (Issue #19)

**GitHub issue:** [#19 — gramma check for the website](https://github.com/sasanarakkha/study-tools/issues/19)
**Spec:** `kamma/threads/20261112_website_audit/spec.md`

## Architecture Decisions

- **All audits live in `kamma/audit/<name>-audit/`** (owner decision). The existing drafts move there with history kept via `git mv`; the guide sits beside them at `kamma/audit/audit-guide.md`.
- **Report mode goes into the existing script.** `--report <path>` is added to `scripts/grammar_check.py`. It reuses `split_into_chunks_lossless()` and `check_paragraph()`, so Pāḷi filtering and exceptions behave exactly as in interactive mode. There is no new script and no shared module, because only this script uses the logic.
- **`rewrite_english.py` is left alone.** The Pro audit does its job.
- **Evidence files go in `temp/site-audit/`** (project temp rule).
- **There is one owner approval gate, between audit and implementation (task 2.4).** `kamma/workflow.md` says no manual gates mid-plan, but the owner asked for this one explicitly. The other STOPs (1.0, 4.4) only protect someone else's uncommitted file and public issue edits.
- **No separate Pro re-check after implementation.** `/kamma:3-review` covers it.
- **Issue edits come last,** after the move is on `main`, so the links never point at a folder that doesn't exist on GitHub.

## Model Strategy

| Phase | Tier | Reason |
|---|---|---|
| 1 — Move audits, report mode, evidence | Fast | File moves, small code change, tests, running commands |
| 2 — Audit | Pro | Judging prose, triaging false positives, site analysis |
| 3 — Apply approved findings | Fast | Mechanical edits from an approved list |
| 4 — Guide, docs, issue links | Fast | Writing up a procedure that is already known; `gh` edits |

## In-scope file list (used by every phase)

Generate with:
`find docs -name '*.md' | grep -v -E '/bhikkhu-patimokkha/|/sbs-per-analysis/|/6-pali-class/suttas/|/6-pali-class/advanced/|draft-advanced-pali-course' | sort > temp/site-audit/files.txt`
Expected: 90 lines.

---

## Phase 1 — Move audits, report mode, evidence — *Fast*

- [x] 1.0 Move the existing audits. First run `git status --short kamma/draft/`. If `pat-audit-tsv.md` still shows ` M`, STOP and ask the owner to commit it or approve moving it as is. Then:
  `git mv kamma/draft/pat-audit kamma/audit/pat-audit`, and do the same for `sbs-per-audit` and `sutta-audit`.
  In `kamma/audit/pat-audit/pat-audit-tsv.md:3`, change `kamma/draft/pat-audit/pat-audit.md` → `kamma/audit/pat-audit/pat-audit.md`. Remove the empty `kamma/draft/`.
  → verify: `git status` shows 5 renames (`R`); `test ! -d kamma/draft`; `grep -rn 'kamma/draft' --exclude-dir=.git --exclude-dir=site --exclude-dir=archive .` returns nothing outside this thread's own spec/plan.
- [x] 1.1 Write `tests/test_grammar_check.py` (test first). Mock the LanguageTool tool object (a fake whose `.check()` returns match-like objects with `offset`, `error_length`, `rule_id`, `message`, `replacements`), so no Java is needed. Tests:
  - (a) report mode writes one TSV row per filtered match with the columns `file, line, rule_id, message, matched, replacement, context`;
  - (b) a match that falls on a Pāḷi word (e.g. `Dhammā`) is not written;
  - (c) report mode never changes the source file (bytes are identical before and after);
  - (d) `line` is the real 1-based line number in the file.
  → verify: `uv run pytest tests/test_grammar_check.py -v` fails, because the report function doesn't exist yet. Paste the failure summary here.
- [x] 1.2 Implement `--report <path>` in `scripts/grammar_check.py`. Add a `report_file(path, tool, exceptions) -> list[row]` function that loops over the prose chunks, calls `check_paragraph()`, and works out the line number from the chunk's offset in the file. In `main()`, if `--report` is given, collect the rows for every target file and write a TSV with a header row; never call `get_key()`. Parse arguments with `argparse` (one or more positional targets, optional `--report`). The interactive path must behave as before. Update the docstring usage.
  → verify: `uv run pytest tests/test_grammar_check.py -v` all pass; then `uv run ruff check --fix scripts/grammar_check.py tests/test_grammar_check.py`, `uv run ruff format scripts/grammar_check.py tests/test_grammar_check.py`, `uv run pyright scripts/grammar_check.py tests/test_grammar_check.py`, `uv run --with pyrefly pyrefly check --min-severity warn scripts/grammar_check.py tests/test_grammar_check.py` all clean.
- [x] 1.3 Generate the evidence. Create `temp/site-audit/files.txt` (command above; check it has 90 lines). Run the report over all in-scope files into one file: `uv run scripts/grammar_check.py --report temp/site-audit/languagetool.tsv $(cat temp/site-audit/files.txt)` (filenames contain a space — `3-ta-pali-dictionary copy.md` — so use a `while read` loop or `xargs -d '\n'`/`tr '\n' '\0' | xargs -0` instead of plain `$(cat …)`). Run `uv run mkdocs build 2>&1 | tee temp/site-audit/build.log`.
  → verify: `languagetool.tsv` exists with a header row and more than 0 data rows, and covers files from all top-level folders; `build.log` ends in a successful build; `git status docs/` shows no changes.
- [x] 1.4 Phase check.
  → verify: rerun the 1.2 checks; confirm `git status` shows only the 5 renames (plus the path fix), `scripts/grammar_check.py` and `tests/test_grammar_check.py`.

## Phase 2 — Audit — *Pro*

⚠️ MODEL SWITCH REQUIRED (Pro tier): judging prose quality and triaging false positives

Review only: **no edits to `docs/`, `mkdocs.yaml`, or scripts in this phase.**

- [x] 2.1 Read every file in `temp/site-audit/files.txt` in full. Decide which English spelling variety the site uses most (count the evidence) and record that as finding #1 (one decision). Triage every row in `languagetool.tsv`: accept it, merge it into a broader finding, or drop it as a false positive. Count the dropped rows by reason. Add the prose problems that LanguageTool missed (wording, clarity, punctuation, consistency of terms and capitalisation).
  → verify: every TSV row has a disposition (an accepted finding number or a dropped reason); the dropped and accepted counts add up to the number of TSV data rows.
- [x] 2.2 Site checks. Compare the `mkdocs.yaml` nav entries against the in-scope files: list orphaned pages and nav entries with no file. Check every internal link and anchor in the in-scope files against real paths and headings. Check the external links that look suspect. Find stray or duplicate files (start with `docs/4-dictionaries/3-ta-pali-dictionary copy.md`; for any deletion proposal, show where the content already exists, e.g. with `diff`). Look for heading and title inconsistencies, raw HTML or `&nbsp;` in sources, and every warning in `build.log`.
  → verify: each site finding cites the command or file evidence behind it (e.g. a nav line, `ls` output, a diff).
- [x] 2.3 Write `kamma/audit/site-audit/site-audit.md`, following the style of `kamma/audit/sutta-audit/sutta-audit.md`:
  - a header with date, scope, exclusions, and "review only";
  - **Coverage:** all 90 files, each marked read in full, or prose-only for template files;
  - **Findings**, numbered and grouped by Prose / Site. Each finding has `file:line`, category, current text (quoted exactly), proposed text, confidence (high/med/low). There are no approve boxes: the owner deletes rejected findings, and what remains is approved. Deletion or rename findings are marked **⚠ data/URL**;
  - **Follow-ups (not to be fixed here):** CSS or visual issues, and anything in the excluded folders;
  - **Triage summary:** LanguageTool rows accepted and dropped, by reason.
  → verify: every quoted "current text" is found by `grep -F` in its file (check all of them with a quick script in `temp/`); `git status docs/` is clean.
- [~] 2.4 **STOP — owner approval.** Tell the owner the report is ready and give its path. The owner deletes the findings they reject; every finding left in the report counts as approved (the owner may also edit the proposed text). Do not start Phase 3 until the owner says the review is done.
  → verify: the owner has confirmed in the conversation; the report still contains at least one finding, or the owner states that nothing is approved.

## Phase 3 — Apply approved findings — *Fast*

⚠️ MODEL SWITCH REQUIRED (Fast tier): mechanical execution resumes

- [ ] 3.1 Before you start, record the current commit with `git rev-parse HEAD`, as the baseline (write it in the report under "Implementation check"). Then apply each remaining (approved) finding exactly as written (use the owner's edited text if they changed it). Change nothing else: no reformatting, no extra fixes. If a finding no longer matches its file, skip it and note it. Any deletion or rename must be marked **⚠ data/URL** and approved; use `git mv`/`git rm` as appropriate. After applying a finding, mark it `applied` (or `skipped: <reason>`) in the report.
  → verify: every approved finding is marked applied or skipped; no unapproved finding is marked applied.
- [ ] 3.2 Diff audit. Check `git diff --word-diff <baseline> -- docs/ mkdocs.yaml` hunk by hunk against the applied findings: every hunk must map to a finding number, and every applied finding must have a hunk. Confirm no Pāḷi changed: extract the words with diacritics from the old and new version of each changed file and compare the multisets, which must match, unless an approved finding was itself a Pāḷi spelling fix. Confirm no raw HTML or `&nbsp;` was introduced.
  → verify: write the hunk→finding map in the report under "Implementation check"; the Pāḷi multiset comparison passes for every changed file.
- [ ] 3.3 Build. Run `bash scripts/web_preprocessing.sh` and then `uv run mkdocs build 2>&1 | tee temp/site-audit/build-after.log`.
  → verify: the build succeeds; `build-after.log` has no warning that `build.log` lacked.
  Note (added in Phase 2): preprocessing rebuilds `docs/index.md`, the folder `index.md` files from their `.header.md`, and the `mkdocs.yaml` nav from first headings. Hunks in those generated files map to the finding on their source (`.header.md` or heading). Preprocessing also runs `clean_dead_links.py`, `fix_heading_hierarchy.py` and `fix_pali_tables.py` over all of `docs/`; any hunk they produce that maps to no approved finding must be reported to the owner, not kept silently.

## Phase 4 — Guide, docs, issue links — *Fast*

- [ ] 4.1 Write `kamma/audit/audit-guide.md`: how to rerun this cycle. Cover:
  - the scope rule and the exclusion command;
  - the evidence commands (`grammar_check.py --report`, the mkdocs build);
  - the Pro-audit brief (what to read, categories, report format, where remaining findings count as approved, review only);
  - the approval step;
  - the Fast implementation rules and the diff/Pāḷi checks;
  - where audits live (`kamma/audit/<name>-audit/`), and the rule that when an audit moves, the GitHub issues linking to it must be updated;
  - lessons from this run (e.g. common LanguageTool false positives, the spelling-variety decision).
  → verify: the file exists; every command in it was run in this thread and is copied exactly.
- [ ] 4.2 Update `README.md`: add the `--report` usage to the `grammar_check.py` entry in the script list, and add a pointer to `kamma/audit/audit-guide.md`.
  → verify: `grep -n -- '--report' README.md` and `grep -n 'audit-guide' README.md` both match.
- [ ] 4.3 Phase check.
  → verify: `uv run pytest tests/test_grammar_check.py -v` passes; `uv run mkdocs build` succeeds; `git status` shows only the expected files: the 5 renames in `kamma/audit/`, `scripts/grammar_check.py`, `tests/test_grammar_check.py`, the approved `docs/` changes, `mkdocs.yaml` if approved, `README.md`, `kamma/audit/audit-guide.md`, `kamma/audit/site-audit/site-audit.md`, and this thread's files.
- [ ] 4.4 Fix the issue references. STOP: ask the owner to confirm (a) the move commit is pushed to `main` and (b) the public issue edits can go ahead. Then for each of N = 22, 23, 24:
  `gh issue view N --repo sasanarakkha/study-tools --json body -q .body > temp/site-audit/issue-N.md`
  In that file, replace `kamma/draft/` with `kamma/audit/`, and check that `diff` against an untouched copy shows only that one line changed. Then:
  `gh issue edit N --repo sasanarakkha/study-tools --body-file temp/site-audit/issue-N.md`
  → verify: rerun the sweep — for every issue (`gh issue list --state all --limit 300`) and PR (`gh pr list --state all`), fetch the body and all comments and grep `kamma/draft` — and confirm it returns nothing.

**Suggested commit:** `docs(site): English and site audit fixes, grammar_check report mode (closes #19)`
