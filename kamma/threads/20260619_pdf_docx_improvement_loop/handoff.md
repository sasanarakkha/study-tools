# Handoff: PDF & DOCX Generator Improvement Loop

## Status

**Cycle D COMPLETE** — DOCX generation disabled; release upload fixed; PDF download links added.

### What was done

1. **Disabled DOCX generation** — Commented out the `uv run python scripts/generate_docx.py` step in `.github/workflows/generate_documents.yaml`. The workflow triggers (push + dispatch), PDF generation, and release upload remain fully active. `scripts/generate_docx.py` is untouched.

2. **Fixed release upload step** — Removed `output/docs/*.docx` glob from the upload commands (both `gh release create` and `gh release upload`), and removed `.docx` from the asset existence check. Release now only operates on PDFs.

3. **Added PDF download links** — Inserted download links pointing to GitHub Releases latest assets in 3 class index pages:
   - `2-patimokkha-class.md` — `bhikkhu-patimokkha.pdf`
   - `sbs-per-analysis.md` — `sbs-per-analysis.pdf`
   - `1-pali-class-adv.md` — `suttas.pdf`

### Validation

- ✓ Workflow re-triggered successfully via `workflow_dispatch`
- ✓ No active `.sh`, `.py`, `.yaml`, `.yml` file outside the script itself calls `generate_docx.py`
- ✓ Release upload globs no longer reference `.docx` files

## Next Action

**User action required:**
1. Confirm the latest workflow run completed successfully with PDF-only upload.
2. Verify the download links work from the live site.
3. Run `/kamma:3-review` to review this thread.

## Known Backlog

- `verify_pdf_content.py` / `verify_docx_content.py` not yet implemented
- Leftover `output/pdf/suttas_debug.html` from manual debugging (gitignored, safe to delete)
