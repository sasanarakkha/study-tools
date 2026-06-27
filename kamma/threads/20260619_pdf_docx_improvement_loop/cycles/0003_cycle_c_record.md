# Cycle C: Table Column Mismatch Fix (COMPLETED)

> Cycle C of the PDF/DOCX improvement loop: fixed table rendering issues across several sutta files by resolving mismatched column counts between table headers and data/separator rows in `scripts/fix_pali_tables.py`.

## Report

* **Root Issue:** Tables in several suttas (such as `sn-35/35-70.md`, `sn-35/35-247.md`, and `sn-22/22-82.md`) failed to render as tables, displaying instead as raw markdown.
* **Cause:** The markdown headers for these tables define 6 columns:
  `| ID | Pāli | POS | Grammar | English | Construction |`
  However, the separator and all data rows contain 7 columns due to an extra trailing pipe at the end of the line (e.g., `| --- | --- | --- | --- | --- | --- | --- |` and `| | kathaṃ | ind | adv | how | | |`). Python-Markdown rejects tables where the column count differs between the header and the data/separator rows, rendering them as raw text.

## Analysis & Proposed Fix

* **Detector:** We wrote a scanner script that confirmed the 7th column in these tables was entirely empty across all separator and data rows, containing no real data.
* **Normalizer Function:** We implemented `fix_mismatched_columns(content: str) -> str` in `scripts/fix_pali_tables.py` to automatically detect tables where the header has fewer columns than the subsequent separator/data rows. If the extra trailing columns are entirely empty, they are truncated to match the header column count.
* **Pipeline Integration:** Integrated this function into `process_file()` in `scripts/fix_pali_tables.py` to run automatically.

## Implementation

We added the following helper and integration to [scripts/fix_pali_tables.py](file:///Users/deva/Documents/sasanarakkha/study-tools/scripts/fix_pali_tables.py):

```python
def fix_mismatched_columns(content: str) -> str:
    """Fix tables where header and separator/data rows have mismatched column count.

    If the extra columns at the end are entirely empty, they are stripped.
    """
    lines = content.split("\n")
    result: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("|"):
            # Gather whole table
            table_lines: list[str] = []
            while i < len(lines) and lines[i].startswith("|"):
                table_lines.append(lines[i])
                i += 1

            # Process table
            if len(table_lines) >= 2:
                header = table_lines[0]
                sep = table_lines[1]
                if re.match(r"^\|[\s\-:|]*\|$", sep):
                    header_cells = [c.strip() for c in header.strip()[1:-1].split("|")]
                    header_len = len(header_cells)

                    # Analyze if subsequent rows have mismatches and check if extra cols are empty
                    mismatch = False
                    max_cols = header_len
                    table_rows_cells: list[list[str]] = []
                    for t_line in table_lines:
                        cells = [c.strip() for c in t_line.strip()[1:-1].split("|")]
                        table_rows_cells.append(cells)
                        if len(cells) != header_len:
                            mismatch = True
                        if len(cells) > max_cols:
                            max_cols = len(cells)

                    if mismatch and max_cols > header_len:
                        # Check if columns from header_len to max_cols-1 are empty in all data rows
                        # and empty/sep in separator
                        extra_cols_empty = True
                        for col_idx in range(header_len, max_cols):
                            # Check separator (row 1)
                            sep_cell = (
                                table_rows_cells[1][col_idx]
                                if col_idx < len(table_rows_cells[1])
                                else ""
                            )
                            if sep_cell != "" and not re.match(r"^:?-+:?$", sep_cell):
                                extra_cols_empty = False
                                break
                            # Check data rows (rows 2+)
                            for row_idx in range(2, len(table_rows_cells)):
                                row_cells = table_rows_cells[row_idx]
                                cell_val = (
                                    row_cells[col_idx]
                                    if col_idx < len(row_cells)
                                    else ""
                                )
                                if cell_val != "":
                                    extra_cols_empty = False
                                    break
                            if not extra_cols_empty:
                                break

                        if extra_cols_empty:
                            # We can truncate all rows to header_len columns
                            new_table_lines: list[str] = []
                            for t_line in table_lines:
                                parts = t_line.split("|")
                                truncated_parts = parts[: header_len + 1] + [""]
                                new_table_lines.append("|".join(truncated_parts))
                            table_lines = new_table_lines

            result.extend(table_lines)
        else:
            result.append(line)
            i += 1

    return "\n".join(result)
```

And registered it inside `process_file()` right before header-adding:
```python
    result = fix_mismatched_columns(result)
```

## Validation

1. **Local Checks:** Ran the project's formatting and type-checking suite on the modified Python file:
   * ✓ Ruff formatting/checking: Passed with no issues.
   * ✓ Pyright static analysis: 0 errors, 0 warnings.
   * ✓ Pyrefly check: 0 errors.
2. **Execution:** Ran `uv run python scripts/fix_pali_tables.py`. It correctly modified 3 files in the repository:
   * [docs/6-pali-class/suttas/sn-22/22-82.md](file:///Users/deva/Documents/sasanarakkha/study-tools/docs/6-pali-class/suttas/sn-22/22-82.md)
   * [docs/6-pali-class/suttas/sn-35/35-247.md](file:///Users/deva/Documents/sasanarakkha/study-tools/docs/6-pali-class/suttas/sn-35/35-247.md)
   * [docs/6-pali-class/suttas/sn-35/35-70.md](file:///Users/deva/Documents/sasanarakkha/study-tools/docs/6-pali-class/suttas/sn-35/35-70.md)
3. **Verification:**
   * Ran the mismatch scan script again; it confirmed 0 remaining table mismatches.
   * Regenerated affected files:
     * ✓ `suttas.docx` generated successfully in 3.5s.
     * ✓ `suttas.pdf` generated successfully in 47.5s.
