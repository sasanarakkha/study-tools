# Cycle D: Disable DOCX Generation

## Report

User requested to disable DOCX generation (`scripts/generate_docx.py`) from any active trigger, while keeping everything else (PDF generation, workflow triggers) working normally.

## Analysis

**Root cause:** The CI workflow `.github/workflows/generate_documents.yaml` had an active step running `uv run python scripts/generate_docx.py` as part of the release pipeline. No other scripts or workflows invoke `generate_docx.py`.

**Proposed fix:** Comment out the DOCX step in the workflow YAML. Keep all other steps (PDF generation, release upload) and workflow triggers (push to `docs/6-pali-class/**`, `workflow_dispatch`) unchanged.

## Approval

Approved by user on 2026-06-27.

## Implementation

**Changed files:**
- `.github/workflows/generate_documents.yaml` — commented out lines 41-42 (DOCX generation step)

## Validation

- ✓ Only active reference to `generate_docx` outside the script itself is now commented out in the workflow
- ✓ No other `.sh`, `.py`, `.yaml`, or `.yml` files invoke `generate_docx.py`
- ✓ `scripts/generate_docx.py` itself is untouched (available for future re-enabling)
- ✓ PDF generation step remains active
- ✓ Workflow triggers (push + dispatch) remain active

## Outcome

DOCX generation is fully disabled from any automated or manual trigger. The script remains in the repo for future re-enabling.

## Known Backlog (unchanged)

- Pandoc image warning on `suttas.docx` generation (benign, now moot)
- `verify_pdf_content.py` / `verify_docx_content.py` not yet implemented
- Leftover `output/pdf/suttas_debug.html` from manual debugging (gitignored)
