# Spec: Website English & Site Audit (Issue #19)

**GitHub issue:** [#19 — gramma check for the website](https://github.com/sasanarakkha/study-tools/issues/19)

## Overview

Audit the published website (https://sasanarakkha.github.io/study-tools/, sources in `docs/`) for English grammar, spelling, clarity and site-level defects, then fix what the owner approves. The work is split by model tier: an advanced (Pro) model audits and proposes corrections; the owner approves or rejects each one; a Fast model applies only the approved ones. Finally, the procedure is written up as a reusable guide.

Also, every audit (the existing ones and the new one) moves from `kamma/draft/` to `kamma/audit/`, and the GitHub issues that link to the old paths are corrected.

## What it should do

0. **Move all audits into `kamma/audit/`.** `git mv` each subfolder: `kamma/draft/{pat-audit,sbs-per-audit,sutta-audit}/` → `kamma/audit/{same names}/`. Update the path references inside the moved files (verified: only `kamma/draft/pat-audit/pat-audit-tsv.md:3`). Remove the empty `kamma/draft/`. No content changes beyond the path references.
1. **Make `scripts/grammar_check.py` usable by an agent.** Add a `--report <path>` option that runs LanguageTool over the target without prompts and writes every filtered match (file, line, rule ID, message, matched text, first replacement, context) to a TSV. The interactive mode stays as is. `scripts/rewrite_english.py` is not used or changed (the Pro audit covers its job, with no OpenRouter cost).
2. **Collect mechanical evidence (Fast):** the LanguageTool report and the `uv run mkdocs build` warnings for the in-scope files, saved under `temp/site-audit/`.
3. **Audit (Pro, review only, no edits to `docs/`):** read every in-scope file in full, triage the LanguageTool report (drop false positives such as Pāḷi words and intended usage), and add findings LanguageTool can't catch. Write `kamma/audit/site-audit/site-audit.md` with numbered findings, each giving `file:line`, category, current text, proposed text, and confidence. Categories:
   - **Prose:** grammar, spelling, punctuation, unclear wording, consistent English spelling variety (the audit finds which variety the site mostly uses and proposes it).
   - **Site:** broken or wrong internal/external links, nav entries vs files, build warnings, stray or duplicate files (e.g. `docs/4-dictionaries/3-ta-pali-dictionary copy.md`), heading or title inconsistencies, raw HTML or `&nbsp;` in sources (forbidden by project rules).
   There are no approve boxes: the owner deletes the findings they reject, and every finding left counts as approved. (Changed 2026-11-12.)
4. **Owner approval gate:** the owner ticks or rejects each finding in the report. Nothing in `docs/` changes before this.
5. **Implement (Fast):** apply exactly the approved findings, nothing else, then verify that the diff contains only those changes, that Pāḷi text is unchanged, and that the site builds.
6. **Write the guide:** `kamma/audit/audit-guide.md` — how to rerun this audit cycle later (scope rules, commands, the Pro-audit / approval / Fast-implement split, report format, lessons from this run, and the rule that when an audit moves, the GitHub issues linking to it must be updated). Update `README.md` for the new `--report` option and point to the guide.
7. **Fix the issue references.** After the move is on `main`, edit the bodies of issues #22, #23 and #24, replacing `kamma/draft/<name>-audit/` with `kamma/audit/<name>-audit/`. Change nothing else in the bodies.

## Scope

**In scope:** all `.md` files under `docs/` (90 files, about 13,000 words), **except**:

- `docs/6-pali-class/bhikkhu-patimokkha/`, `docs/6-pali-class/sbs-per-analysis/`, `docs/6-pali-class/suttas/` — already audited (see the existing audits, moving to `kamma/audit/*-audit/`).
- `docs/6-pali-class/advanced/` — unpublished draft (comment on issue #19).
- `docs/6-pali-class/draft-advanced-pali-course.md` — ~19,000-word draft, marked "still being edited" (owner decision).

Also in scope: the `mkdocs.yaml` nav, where it relates to in-scope pages; the 5 tracked files in `kamma/draft/`; the bodies of issues #22, #23 and #24.

## Assumptions & uncertainties

**Verified this session (2026-11-12):**

- Both scripts are interactive (raw-terminal keypress loop); `grammar_check.py` has no non-interactive mode. Its `check_paragraph()` already filters Pāḷi words and saved exceptions (`temp/grammar_exceptions.json`), and `split_into_chunks_lossless()` splits the prose, so a report mode can reuse both.
- `grammar_check.py` uses LanguageTool `en-US`; Java is installed (`/usr/bin/java`).
- In-scope file count (90) and word count (~13,000) were measured with `find`/`wc`. The exclusion list was read from the comment on issue #19.
- `mkdocs.yaml` sets `validation.nav.omitted_files: ignore`, so pages left out of the nav give no warning — the audit must compare nav against files itself.
- There are no existing tests for `grammar_check.py` (`tests/` has two unrelated test files).
- `kamma/draft/` holds 5 tracked files in 3 subfolders, and neither `kamma/draft` nor `kamma/audit` is git-ignored. A repo-wide grep (excluding the git-ignored `kamma/archive/`) finds one reference to `kamma/draft`: `kamma/draft/pat-audit/pat-audit-tsv.md:3`.
- `kamma/draft/pat-audit/pat-audit-tsv.md` had uncommitted changes from outside this thread when this was planned.
- A sweep of all issues and PRs (bodies and comments, open and closed) found `kamma/draft` only in the bodies of #22, #23 and #24, line 3 of each, all written by the owner.

**Assumptions:**

- `en-US` LanguageTool will flag British spellings if the site uses them; the Pro audit treats spelling variety as one decision and doesn't take each flag on its own.
- `.header.md` files and `docs/5-anki/templates/*.md` (35 files, mostly card template code) count as in scope. The audit checks only their English prose and leaves template code alone.
- External link checking means the Pro model verifies links that look wrong or suspect; a full HTTP crawl of every link is not included.

## Constraints

- **Data preservation (project rule):** never remove data from `docs/`. A deletion finding (e.g. a duplicate file) must show that the content exists elsewhere, and needs the owner's explicit approval.
- Pāḷi text, Pāḷi terms, and diacritics must stay byte-identical.
- Clean Markdown: no raw HTML or `&nbsp;` introduced.
- Keep the existing page URLs; don't rename published pages unless approved. (Corrected 2026-11-12, Phase 2: `mkdocs.yaml` does not set `use_directory_urls`, so the default directory URLs apply, e.g. `1-pre-pali-study/`, not `.html`.)
- File moves use `git mv` to keep history.
- Don't edit the GitHub issues until the move is on `main` and the owner confirms.
- Python changes pass ruff, ruff format, pyright, pyrefly, and pytest (project pre-completion rule).
- Pro phases only analyse; Fast phases do all edits and commands.

## How we'll know it's done

- `kamma/draft/` no longer exists; `git status` shows the 5 files as renames; `grep -rn 'kamma/draft'` (excluding `kamma/archive/`) finds nothing.
- `uv run scripts/grammar_check.py --report temp/site-audit/languagetool.tsv <target>` runs with no prompts and writes the TSV; a new `tests/test_grammar_check.py` passes.
- `kamma/audit/site-audit/site-audit.md` exists, covers every in-scope file (a coverage list), and every finding has location, current text, proposed text, and an approval box.
- Every approved finding is applied and no unapproved change is in the `docs/` diff (checked finding by finding).
- `uv run mkdocs build` succeeds with no new warnings.
- `kamma/audit/audit-guide.md` exists, and `README.md` documents `--report` and points to the guide.
- `gh issue view N --json body` for 22, 23 and 24 shows `kamma/audit/…` and no `kamma/draft`. A repeat of the issue/PR sweep finds no `kamma/draft` anywhere.

## What's not included

- The excluded folders and the draft course file.
- Changing or running `scripts/rewrite_english.py`.
- Any new Claude skill or slash command (the guide replaces it).
- Visual/CSS changes. If the audit finds styling problems, it lists them as follow-ups only.
- Translating content, or changing the Pāḷi analysis.
- Changing the content of the existing audits (only their location and path references).
- Updating references in the git-ignored `kamma/archive/`.
