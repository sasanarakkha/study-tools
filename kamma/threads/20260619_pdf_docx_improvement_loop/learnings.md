# Learnings: PDF & DOCX Generator Improvement Loop

## Carried over from kamma/threads/20260520_pdf_docx_pali_class

- macOS DYLD_LIBRARY_PATH fix is real and required for WeasyPrint: set
  `os.environ["DYLD_LIBRARY_PATH"]` before `import weasyprint`, since
  `cffi.dlopen()` reads the env var at call time.
- Pandoc's missing-image warning on `suttas.docx` (relative image path
  resolution) is benign — output is valid and usable.
- `cd` inside a background Bash command does not persist to subsequent tool
  calls; always use absolute paths in multi-step shell commands.
- Inline `python -c "..."` is prohibited by project CLAUDE.md; write a
  throwaway script to `temp/` instead for ad-hoc verification.

## Active Lessons

- **File-level-anchor TOC avoids duplicate-heading-id bugs:** When headings repeat
  across files (e.g., "Pāli Text" in 5 suttas), the toc extension's per-file
  dedup fails. Using file-based anchors (`#{basename_without_dot}`) instead of
  heading-text anchors sidesteps the issue entirely. Apply this pattern for any
  folder that has repeated heading names across files.

- **Sentinel-marker splitting fixes PDF heading-id dedup across files:** If you need
  both TOC and content to have consistent heading ids, convert all files' markdown
  in a **single** `md.convert()` call with sentinel markers inserted between files
  (e.g., `<!--FILE-BOUNDARY:{idx}-->`). The markdown toc extension will see all
  headings across all files and dedup them correctly. Sentinels survive conversion
  unmodified, making per-file boundary recovery straightforward via regex splitting.

- **Pandoc uses `-1`, `-2` suffix format for duplicate heading ids:** When generating
  DOCX, Pandoc appends `-1`, `-2`, etc. to duplicate heading ids (e.g.,
  `pāli-text`, `pāli-text-1`, `pāli-text-2`). If you build a manual TOC
  alongside Pandoc conversion, track duplicate slugs and apply the same format
  so TOC links match Pandoc's actual output.

- **Markdown table parser column count strictness:** Python-Markdown and other strict MD
  parsers reject table formatting entirely (rendering it as raw text) if the header
  row has a different column count than the delimiter/separator and data rows. If the
  extra columns are trailing and empty, truncating them to match the header length
  restores proper rendering.

## Pruned / Superseded

(none yet)
