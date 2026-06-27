# Plan: PDF & DOCX Generator Improvement Loop

> **Thread type:** Loop (standing thread)

## Architecture Decisions

- **Standing loop, not a one-shot thread.** The generator pipeline
  (`scripts/generate_pdfs.py`, `scripts/generate_docx.py`, SBS CSS/fonts, the
  release workflow) is stable but will keep surfacing small issues over time
  (rendering edge cases, new Pandoc warnings, workflow flakiness). A loop
  thread avoids re-planning from scratch for each one.
- **No model tiering.** Cycles are small and judgment-heavy (rendering
  fidelity, CLAUDE.md validation gates) — not worth splitting fast/pro models.
- **Hard stop before implementation.** Every fix touches generator code that
  produces user-facing output (PDF/DOCX given to others); no edit happens
  without explicit approval of the proposed fix and its validation plan.
- **Cycle records over a running log.** Each cycle gets its own
  `cycles/NNNN_slug.md` so history is inspectable without bloating the
  context every other cycle has to read.

## Per-Cycle Protocol

1. **Report:** Identify the next issue or task in the domain. Pull from
   `handoff.md`'s Known Backlog, a user-reported issue, or something noticed
   while inspecting generator output. State it in one or two sentences.

2. **Analyze:** Assess the issue (root cause, affected files), propose a fix,
   and define what validation will prove it's resolved (which of the Validation
   Standards in `spec.md` apply, plus anything issue-specific).

3. **Approval (HARD STOP):** Present the analysis and proposed fix. WAIT for
   explicit user approval before touching any source or test file.

4. **Implement:** Apply only the approved fix. No unrelated cleanup.

5. **Validate:** Run the validation defined in step 2 — regenerate affected
   output, run ruff/pyright/pyrefly on touched files, manually open the
   PDF/DOCX and confirm rendering, run relevant tests. Report tested/not
   tested honestly; do not claim success without having actually run it.

6. **Record:** Write the cycle record to `cycles/NNNN_slug.md` — what was
   reported, the approved analysis, what changed, and validation results.

7. **Handoff:** Update `handoff.md` with current state, updated backlog, and
   the next suggested cycle.

8. **Learn:** Curate `learnings.md` — add any new non-obvious discovery from
   this cycle, and prune any lesson that no longer applies (e.g. superseded
   by a later fix).

## Read Contract

A cycle reads only `spec.md`, `plan.md`, `handoff.md`, and `learnings.md`.
Full cycle records under `cycles/` are read only on demand (e.g. when
investigating a regression or referencing prior reasoning).
