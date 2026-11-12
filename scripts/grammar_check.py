#!/usr/bin/env python3
"""
Grammar and spelling check for markdown files using LanguageTool, with Pāḷi awareness.

Usage:
    uv run scripts/grammar_check.py <file_or_folder>
    uv run scripts/grammar_check.py --report <out.tsv> <file_or_folder> [...]

Without --report the check is interactive and can edit files. With --report it runs
without prompts, never edits the sources, and writes every filtered match to a TSV.
"""

import argparse
import csv
import json
import re
import sys
import tty
import termios
from pathlib import Path
import language_tool_python
from tools.printer import printer as pr

# Constants
PALI_ASCII_TERMS = [
    "Sutta",
    "Nibbana",
    "Dhamma",
    "Vinaya",
    "Nikaya",
    "Bhikkhu",
    "Pali",
    "SBS",
    "Majjhima",
]
EXCEPTIONS_FILE = Path("temp/grammar_exceptions.json")
REPORT_COLUMNS = [
    "file",
    "line",
    "rule_id",
    "message",
    "matched",
    "replacement",
    "context",
]


def load_exceptions() -> set[str]:
    """Load ignored rule-word combinations from disk."""
    if EXCEPTIONS_FILE.exists():
        try:
            return set(json.loads(EXCEPTIONS_FILE.read_text()))
        except Exception as e:
            pr.amber(f"Failed to load exceptions: {e}")
            return set()
    return set()


def save_exception(exceptions: set, rule_id: str, matched_text: str):
    """Save a new rule-word combination to the ignore list."""
    key = f"{rule_id}::{matched_text}"
    exceptions.add(key)
    EXCEPTIONS_FILE.parent.mkdir(parents=True, exist_ok=True)
    EXCEPTIONS_FILE.write_text(json.dumps(sorted(list(exceptions)), indent=2))


def extract_pali_words(text: str) -> list[str]:
    """Find all words containing Pāḷi diacritics."""
    # This regex matches words containing at least one non-ASCII character (Pāḷi diacritics)
    diacritic_words = re.findall(r"\b\w*[^\x00-\x7F]\w*\b", text)
    return list(set(diacritic_words + PALI_ASCII_TERMS))


def get_key() -> str:
    """Read a single keypress from stdin."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def split_into_chunks_lossless(text: str) -> list[dict]:
    """Split markdown text into chunks (paragraphs, headings, code blocks) losslessly."""
    chunks = []
    lines = text.splitlines(keepends=True)
    in_code_block = False
    current_prose = []

    for line in lines:
        stripped = line.strip()

        # Markdown triple backtick code blocks
        if stripped.startswith("```"):
            if in_code_block:
                # Ending code block
                chunks.append({"text": line, "type": "skip"})
                in_code_block = False
            else:
                # Starting code block
                if current_prose:
                    chunks.append({"text": "".join(current_prose), "type": "prose"})
                    current_prose = []
                chunks.append({"text": line, "type": "skip"})
                in_code_block = True
            continue

        if in_code_block:
            chunks.append({"text": line, "type": "skip"})
            continue

        # Headings, empty lines, or indented code blocks (4 spaces)
        if stripped.startswith("#") or not stripped or line.startswith("    "):
            if current_prose:
                chunks.append({"text": "".join(current_prose), "type": "prose"})
                current_prose = []
            chunks.append({"text": line, "type": "skip"})
        else:
            current_prose.append(line)

    if current_prose:
        chunks.append({"text": "".join(current_prose), "type": "prose"})

    return chunks


def check_paragraph(tool, text: str, exceptions: set) -> list:
    """Check a paragraph for errors, filtering out Pāḷi and exceptions."""
    matches = tool.check(text)
    filtered_matches = []

    pali_words = extract_pali_words(text)

    # Pre-calculate spans for Pāḷi words in this text (case-insensitive for ASCII terms)
    pali_spans = []
    for word in pali_words:
        # Use re.IGNORECASE for ASCII terms, but be careful with diacritics
        # Actually, let's just use re.IGNORECASE for everything in pali_words for safety
        for m in re.finditer(re.escape(word), text, re.IGNORECASE):
            pali_spans.append((m.start(), m.end()))

    for match in matches:
        # Rule 1: Must have replacements
        if not match.replacements:
            continue

        matched_text = text[match.offset : match.offset + match.error_length]

        # Rule 2: Must not be a Pāḷi word
        is_pali = False
        for start, end in pali_spans:
            if match.offset >= start and (match.offset + match.error_length) <= end:
                is_pali = True
                break
        if is_pali:
            continue

        # Rule 3: Must not be in exceptions
        exception_key = f"{match.rule_id}::{matched_text}"
        if exception_key in exceptions:
            continue

        filtered_matches.append(match)

    return filtered_matches


def apply_fix(text: str, match) -> str:
    """Apply the first suggested fix to the text."""
    return (
        text[: match.offset]
        + match.replacements[0]
        + text[match.offset + match.error_length :]
    )


def process_file(path: Path, tool, exceptions: set):
    """Interactively process a single markdown file for grammar/spelling errors."""
    pr.cyan_tmr(f"Checking {path}")
    try:
        content = path.read_text()
    except Exception as e:
        pr.red(f"Could not read {path}: {e}")
        return

    chunks = split_into_chunks_lossless(content)
    session_skips: set[str] = set()

    for chunk in chunks:
        if chunk["type"] != "prose":
            continue

        # We need to loop because applying a fix changes offsets for subsequent matches
        while True:
            all_ignored = exceptions | session_skips
            matches = check_paragraph(tool, chunk["text"], all_ignored)
            if not matches:
                break

            # Process one match at a time
            match = matches[0]
            matched_text = chunk["text"][
                match.offset : match.offset + match.error_length
            ]

            # Show context
            before = chunk["text"][max(0, match.offset - 40) : match.offset].replace(
                "\n", " "
            )
            after = chunk["text"][
                match.offset + match.error_length : match.offset
                + match.error_length
                + 40
            ].replace("\n", " ")

            print(f"\n  Rule:    {match.rule_id}")
            print(f"  Message: {match.message}")
            print(f"  Context: ...{before}[{matched_text}]{after}...")
            print(f"  Fix:     '{matched_text}' -> '{match.replacements[0]}'")
            print()

            while True:
                print(
                    "[enter] accept  [e]xception  [q]uit  [s]kip: ", end="", flush=True
                )
                key = get_key()
                if key == "\r":
                    print("accept")
                    chunk["text"] = apply_fix(chunk["text"], match)
                    path.write_text("".join(c["text"] for c in chunks))
                    pr.yes("fix applied")
                    break
                elif key.lower() == "e":
                    print("exception")
                    save_exception(exceptions, match.rule_id, matched_text)
                    pr.yes(f"added to exception: {match.rule_id}::{matched_text}")
                    break
                elif key.lower() == "q":
                    print("quit")
                    pr.amber("Quit — file saved with changes so far.")
                    return
                elif key.lower() == "s":
                    print("skip")
                    session_skips.add(f"{match.rule_id}::{matched_text}")
                    break
                else:
                    print("\r" + " " * 40 + "\r", end="", flush=True)


def _one_line(text: str) -> str:
    """Collapse newlines and tabs so the text fits in one TSV cell."""
    return text.replace("\t", " ").replace("\r", " ").replace("\n", " ")


def report_file(path: Path, tool, exceptions: set) -> list[list[str]]:
    """Return one report row per filtered match in a file, without editing it."""
    content = path.read_text()
    rows: list[list[str]] = []
    lines_before = 0

    for chunk in split_into_chunks_lossless(content):
        text = chunk["text"]
        if chunk["type"] == "prose":
            for match in check_paragraph(tool, text, exceptions):
                end = match.offset + match.error_length
                line = lines_before + text.count("\n", 0, match.offset) + 1
                rows.append(
                    [
                        str(path),
                        str(line),
                        match.rule_id,
                        _one_line(match.message),
                        _one_line(text[match.offset : end]),
                        _one_line(match.replacements[0]),
                        _one_line(
                            f"{text[max(0, match.offset - 40) : match.offset]}"
                            f"[{text[match.offset : end]}]"
                            f"{text[end : end + 40]}"
                        ),
                    ]
                )
        lines_before += text.count("\n")

    return rows


def write_report(out_path: Path, rows: list[list[str]]) -> None:
    """Write report rows to a TSV with a header row."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow(REPORT_COLUMNS)
        writer.writerows(rows)


def collect_files(targets: list[Path]) -> list[Path]:
    """Expand files and folders into a list of markdown files."""
    files: list[Path] = []
    for target in targets:
        if target.is_file():
            files.append(target)
        elif target.is_dir():
            files.extend(sorted(target.rglob("*.md")))
        else:
            pr.red(f"Target not found: {target}")
            sys.exit(1)
    return files


def main():
    parser = argparse.ArgumentParser(
        description="Grammar and spelling check for markdown files (Pāḷi-aware)."
    )
    parser.add_argument("targets", nargs="+", type=Path, help="file or folder")
    parser.add_argument(
        "--report",
        type=Path,
        metavar="OUT.tsv",
        help="non-interactive: write all matches to this TSV, edit nothing",
    )
    args = parser.parse_args()

    files = collect_files(args.targets)
    exceptions = load_exceptions()

    pr.green("Initializing LanguageTool (en-US)...")
    try:
        tool = language_tool_python.LanguageTool("en-US")
    except Exception as e:
        pr.red(f"Failed to initialize LanguageTool: {e}")
        sys.exit(1)

    if args.report:
        pr.bip()
        rows: list[list[str]] = []
        for file in files:
            rows.extend(report_file(file, tool, exceptions))
        write_report(args.report, rows)
        pr.yes(f"{len(rows)} matches in {len(files)} files -> {args.report}")
        return

    for file in files:
        process_file(file, tool, exceptions)


if __name__ == "__main__":
    main()
