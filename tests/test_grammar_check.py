"""Tests for the non-interactive --report mode of scripts/grammar_check.py."""

import csv
from dataclasses import dataclass, field
from pathlib import Path

from scripts.grammar_check import REPORT_COLUMNS, report_file, write_report


@dataclass
class FakeMatch:
    offset: int
    error_length: int
    rule_id: str
    message: str
    replacements: list[str] = field(default_factory=list)


class FakeTool:
    """Flags every occurrence of the configured words, like LanguageTool would."""

    def __init__(self, flagged: dict[str, str]) -> None:
        self.flagged = flagged

    def check(self, text: str) -> list[FakeMatch]:
        matches = []
        for word, replacement in self.flagged.items():
            start = text.find(word)
            while start != -1:
                matches.append(
                    FakeMatch(
                        start, len(word), "FAKE_RULE", "fake message", [replacement]
                    )
                )
                start = text.find(word, start + 1)
        return matches


SAMPLE = (
    "# Title\n"
    "\n"
    "First paragraph is fine.\n"
    "\n"
    "Second paragraph has a mistaek here.\n"
    "and a second line with teh typo.\n"
    "\n"
    "```\n"
    "mistaek inside code\n"
    "```\n"
    "\n"
    "The Dhammā is mistaek-free.\n"
)


def _write_sample(tmp_path: Path) -> Path:
    path = tmp_path / "sample.md"
    path.write_text(SAMPLE)
    return path


def test_report_has_one_row_per_filtered_match(tmp_path: Path) -> None:
    path = _write_sample(tmp_path)
    tool = FakeTool({"mistaek": "mistake", "teh": "the"})
    rows = report_file(path, tool, set())
    out = tmp_path / "report.tsv"
    write_report(out, rows)

    with out.open(newline="") as fh:
        parsed = list(csv.reader(fh, delimiter="\t"))
    assert parsed[0] == REPORT_COLUMNS
    assert [r[REPORT_COLUMNS.index("matched")] for r in parsed[1:]] == [
        "mistaek",
        "teh",
        "mistaek",
    ]
    first = dict(zip(REPORT_COLUMNS, parsed[1]))
    assert first["file"] == str(path)
    assert first["rule_id"] == "FAKE_RULE"
    assert first["message"] == "fake message"
    assert first["replacement"] == "mistake"
    assert "[mistaek] here" in first["context"]


def test_pali_word_match_is_not_reported(tmp_path: Path) -> None:
    path = _write_sample(tmp_path)
    tool = FakeTool({"Dhammā": "Dhamma"})
    assert report_file(path, tool, set()) == []


def test_report_mode_never_changes_the_source(tmp_path: Path) -> None:
    path = _write_sample(tmp_path)
    before = path.read_bytes()
    report_file(path, FakeTool({"mistaek": "mistake"}), set())
    assert path.read_bytes() == before


def test_line_numbers_are_real_one_based_file_lines(tmp_path: Path) -> None:
    path = _write_sample(tmp_path)
    rows = report_file(path, FakeTool({"mistaek": "mistake", "teh": "the"}), set())
    lines = {r[REPORT_COLUMNS.index("matched")]: [] for r in rows}
    for r in rows:
        lines[r[REPORT_COLUMNS.index("matched")]].append(
            r[REPORT_COLUMNS.index("line")]
        )
    # "mistaek" in line 5 and line 12 (the code block one on line 9 is skipped),
    # "teh" on line 6.
    assert lines["mistaek"] == ["5", "12"]
    assert lines["teh"] == ["6"]
