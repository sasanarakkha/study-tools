#!/usr/bin/env python3
"""Normalize Pāḷi study markdown tables and fix grammar abbreviations."""

import re
import glob
import os
import argparse
from tools.printer import printer as pr

def normalize_cell_padding(line: str) -> str:
    """Strip excessive whitespace, single-space padding in table cells."""
    if not line.startswith("|"):
        return line
    parts = line.split("|")
    new_parts = []
    for i, part in enumerate(parts):
        if i == 0 or i == len(parts) - 1:
            if part.strip() == "":
                new_parts.append("")
                continue
        
        stripped = part.strip()
        if stripped == "":
            new_parts.append(" ")
        else:
            new_parts.append(f" {stripped} ")
    return "|".join(new_parts)

def normalize_separator_row(line: str) -> str:
    """Normalize |---| to | --- |."""
    if not line.startswith("|"):
        return line
    # A separator row contains only |, -, :, and whitespace
    if not re.match(r'^\|[\s\-:|]*\|$', line):
        return line
    parts = line.split("|")
    new_parts = []
    for i, part in enumerate(parts):
        if i == 0 or i == len(parts) - 1:
            if part.strip() == "":
                new_parts.append("")
                continue
        stripped = part.strip()
        if re.match(r'^:?-+:?$', stripped):
            new_parts.append(f" {stripped} ")
        else:
            new_parts.append(f" {stripped} ")
    return "|".join(new_parts)

def strip_bold_footnote_defs(line: str) -> str:
    """Strip bold from **[^N]: ...**."""
    return re.sub(r'\*\*(\[\^[0-9]+\]:.*?)\*\*', r'\1', line)

def fix_grammar_abbreviations(line: str) -> str:
    """Replace .s singular abbreviation with .sg in the grammar column only."""
    if not line.startswith("|"):
        return line
    parts = line.split("|")
    if len(parts) < 5:  # need at least |Pali|POS|Grammar|English|
        return line
    # Grammar column is parts[3] (0="", 1=Pali, 2=POS, 3=Grammar, 4=English)
    parts[3] = re.sub(r'\.s\b(?!g)', '.sg', parts[3])
    return "|".join(parts)

def remove_blank_lead_col(line: str) -> str:
    """Drop the blank first column from a table row."""
    if not line.startswith("|"):
        return line
    parts = line.split("|")
    # parts[0]="", parts[1]=lead col, parts[2+]=content
    if len(parts) >= 4 and parts[1].strip() == "":
        return "|" + "|".join(parts[2:])
    return line

def remove_blank_headings(line: str) -> str:
    """Remove heading lines that have no title text (e.g. '## ' with trailing space only)."""
    if re.match(r'^#{1,6}\s*$', line):
        return ""
    return line

def add_missing_headers(content: str) -> str:
    """Insert | Pāli | POS | Grammar | English | before the first word-analysis
    row of each table that lacks a header. A word-analysis row is detected by
    having non-empty content in cols 2 (POS) and 3 (Grammar), where those
    cells contain known POS tags (noun, verb, adj, ind, pron, pp, prp, etc.)."""
    POS_TAGS = {"noun", "verb", "adj", "ind", "pron", "pp", "prp", "sandhi",
                "adv", "num", "prefix", "suffix", "conj", "part", "neg"}
    lines = content.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if (line.startswith("|")
                and not re.match(r"^\|[\s:]*-", line)   # not separator
                and "Pāli" not in line                   # not already a header
                and "POS" not in line):
            parts = line.split("|")
            # Check col 2 (POS) contains a known POS tag
            pos_cell = parts[2].strip().lower() if len(parts) > 2 else ""
            grammar_cell = parts[3].strip() if len(parts) > 3 else ""
            is_word_row = pos_cell in POS_TAGS and grammar_cell != ""
            if is_word_row:
                # Only insert header if previous non-empty line is not a table row
                prev = ""
                for r in reversed(result):
                    if r.strip():
                        prev = r
                        break
                if not prev.startswith("|"):
                    cols = len(parts) - 2
                    headers = ["Pāli", "POS", "Grammar", "English",
                               "Construction"][:cols]
                    result.append("| " + " | ".join(headers) + " |")
                    result.append("| " + " | ".join(["---"] * cols) + " |")
        result.append(line)
        i += 1
    return "\n".join(result)

def sync_separator_columns(content: str) -> str:
    """Make separator rows match the column count of their preceding header row.

    When remove_blank_lead_col strips the first col from data rows but not from
    separator rows (which have '---' not blank), Python-Markdown fails to parse
    the table. This pass re-aligns separator cols to match the header.
    """
    lines = content.split("\n")
    result = []
    last_data_col_count = None

    for line in lines:
        if not line.startswith("|"):
            result.append(line)
            last_data_col_count = None
            continue

        is_sep = bool(re.match(r'^\|[\s\-:|]*\|$', line))
        if is_sep:
            if last_data_col_count is not None:
                parts = line.split("|")
                sep_col_count = len(parts) - 2
                while sep_col_count > last_data_col_count and len(parts) >= 4:
                    if re.match(r'^\s*:?-+:?\s*$', parts[1]):
                        parts = [""] + parts[2:]
                        sep_col_count -= 1
                    else:
                        break
                line = "|".join(parts)
        else:
            parts = line.split("|")
            last_data_col_count = len(parts) - 2

        result.append(line)

    return "\n".join(result)


def process_file(filepath: str, remove_lead_col: bool = False,
                 add_headers: bool = False) -> bool:
    with open(filepath, "r", encoding="utf-8") as f:
        original = f.read()

    lines = original.split("\n")
    new_lines = []
    for line in lines:
        if remove_lead_col:
            line = remove_blank_lead_col(line)
        line = normalize_cell_padding(line)
        line = normalize_separator_row(line)
        line = strip_bold_footnote_defs(line)
        line = fix_grammar_abbreviations(line)
        line = remove_blank_headings(line)
        new_lines.append(line)

    result = "\n".join(new_lines)

    if remove_lead_col:
        result = sync_separator_columns(result)

    if add_headers:
        result = add_missing_headers(result)

    if result != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(result)
        return True
    return False

def main() -> None:
    """Normalize Pāḷi study markdown tables and fix grammar abbreviations."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", default="docs/6-pali-class",
                        help="Directory or single .md file to process")
    parser.add_argument("--remove-lead-col", action="store_true",
                        help="Drop blank leading column from table rows")
    parser.add_argument("--add-headers", action="store_true",
                        help="Insert column headers before tables that lack them")
    args = parser.parse_args()

    if os.path.isfile(args.dir):
        files = [args.dir]
    else:
        files = sorted(glob.glob(f"{args.dir}/**/*.md", recursive=True))

    pr.green("Fixing tables")
    count = 0
    for filepath in files:
        if process_file(filepath,
                        remove_lead_col=args.remove_lead_col,
                        add_headers=args.add_headers):
            count += 1
            pr.warning(filepath)

    if count > 0:
        pr.yes(f"{count} files")
    else:
        pr.yes("ok")

if __name__ == "__main__":
    main()
