"""Tests for the Bhikkhu Pātimokkha word-by-word page generator."""

import re
from pathlib import Path
from typing import Any, cast

import pandas as pd
import pytest

from scripts.fix_pali_tables import process_file
from scripts.generate_patimokkha import (
    assign_orphan_sentences,
    file_name,
    generate_index,
    generate_rule_page,
    get_sources,
    load_data,
)

REPO = Path(__file__).resolve().parent.parent
XLSX = REPO / "temp" / "patimokkha.xlsx"
DOCS = REPO / "docs" / "6-pali-class" / "bhikkhu-patimokkha"

SEPARATOR = re.compile(r"^\|[\s:|-]*\|$")
LABEL = re.compile(r"^[A-Z]{2,3}(?: \d+)?$")

needs_xlsx = pytest.mark.skipif(
    not XLSX.exists(), reason="temp/patimokkha.xlsx not downloaded"
)


def frame(rows: list[list[str]]) -> pd.DataFrame:
    """Build a minimal sheet slice: pali, pos, grammar, sentence, source."""
    return pd.DataFrame(rows, columns=["pali", "pos", "grammar", "sentence", "source"])


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def pages() -> list[Path]:
    return sorted(p for p in DOCS.glob("*.md") if p.name != "index.md")


def data_rows(path: Path) -> list[str]:
    return [
        line
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("|") and not SEPARATOR.match(line)
    ]


# --- assign_orphan_sentences -------------------------------------------------


def test_translation_row_inherits_the_preceding_sentence() -> None:
    df = frame(
        [
            ["yo", "pron", "masc", "yo pana bhikkhu", "rule"],
            ["Yo, whoever", "", "", "", "rule"],
        ]
    )
    assert assign_orphan_sentences(df)["sentence"].tolist() == [
        "yo pana bhikkhu",
        "yo pana bhikkhu",
    ]


def test_section_labels_stay_ungrouped() -> None:
    df = frame(
        [
            ["yo", "pron", "masc", "yo pana bhikkhu", "rule"],
            ["PC 42", "", "", "", "rule"],
            ["Yo, whoever", "", "", "", "rule"],
        ]
    )
    assert assign_orphan_sentences(df)["sentence"].tolist() == [
        "yo pana bhikkhu",
        "",
        "yo pana bhikkhu",
    ]


def test_section_label_with_a_sentence_stays_ungrouped() -> None:
    """Some label rows carry the rule's sentence; they are still labels."""
    df = frame(
        [
            [
                "SE 49",
                "",
                "",
                "na jivhānicchārakaṃ bhuñjissāmī'ti sikkhā karaṇīyā.",
                "rule",
            ],
            [
                "na",
                "ind",
                "neg",
                "na jivhānicchārakaṃ bhuñjissāmī'ti sikkhā karaṇīyā.",
                "rule",
            ],
        ]
    )
    assert assign_orphan_sentences(df)["sentence"].tolist() == [
        "",
        "na jivhānicchārakaṃ bhuñjissāmī'ti sikkhā karaṇīyā.",
    ]


def test_row_repeating_a_pali_sentence_stays_ungrouped() -> None:
    """The next rule's heading is placed inside the previous rule's block."""
    df = frame(
        [
            ["yo", "pron", "masc", "yo pana bhikkhu", "rule"],
            ["so bhikkhu", "", "", "", "rule"],
            ["so", "pron", "masc", "so bhikkhu", "next rule"],
        ]
    )
    assert assign_orphan_sentences(df)["sentence"].tolist() == [
        "yo pana bhikkhu",
        "",
        "so bhikkhu",
    ]


def test_inheritance_does_not_cross_a_rule_boundary() -> None:
    df = frame(
        [
            ["yo", "pron", "masc", "yo pana bhikkhu", "rule"],
            ["stray translation", "", "", "", "next rule"],
            ["so", "pron", "masc", "so bhikkhu", "next rule"],
        ]
    )
    assert assign_orphan_sentences(df)["sentence"].tolist() == [
        "yo pana bhikkhu",
        "",
        "so bhikkhu",
    ]


def test_word_rows_keep_their_own_sentence() -> None:
    df = frame(
        [
            ["yo", "pron", "masc", "sentence one", "rule"],
            ["so", "pron", "masc", "sentence two", "rule"],
        ]
    )
    assert assign_orphan_sentences(df)["sentence"].tolist() == [
        "sentence one",
        "sentence two",
    ]


# --- generation from the spreadsheet ----------------------------------------


@needs_xlsx
def test_every_orphan_row_of_the_sheet_is_accounted_for() -> None:
    """No row may remain ungrouped unless it is a label or a Pāḷi heading."""
    df = load_data(XLSX)
    sentences = {
        word.strip()
        for word in cast(list[str], df["sentence"].astype(str).tolist())
        if word.strip()
    }
    ungrouped = df[df["sentence"].astype(str).str.strip() == ""]
    leftover = [
        word
        for word in cast(list[str], ungrouped["pali"].astype(str).tolist())
        if word.strip()
        and not LABEL.match(word.strip())
        and word.strip() not in sentences
    ]
    assert leftover == []


@needs_xlsx
def test_every_translation_from_the_sheet_is_published() -> None:
    df = load_data(XLSX)
    pos = df["pos"].astype(str).str.strip()
    grouped = df["sentence"].astype(str).str.strip().ne("")
    pali = df["pali"].astype(str)
    missing: list[tuple[str, str]] = []
    for source in cast(pd.Series, df["source"]).drop_duplicates():
        if not str(source).strip():
            continue
        page = DOCS / f"{file_name(str(source))}.md"
        published = set(page.read_text(encoding="utf-8").splitlines())
        rows = df[(df["source"] == source) & pos.eq("") & grouped]
        for text in pali[rows.index].tolist():
            published_text = text.replace("\n", "<br>").strip()
            if published_text.strip() and f"**{published_text}**" not in published:
                missing.append((str(source), published_text[:60]))
    assert missing == []


@needs_xlsx
def test_generated_pages_match_the_repository(tmp_path: Path) -> None:
    """Regenerating from the workbook must reproduce the committed pages."""
    df = load_data(XLSX)
    sources = get_sources(df)
    generate_index(sources, tmp_path)
    for idx, source in enumerate(sources):
        generate_rule_page(source, df, tmp_path, sources, idx)
    for path in tmp_path.glob("*.md"):
        process_file(str(path))

    generated = sorted(p.name for p in tmp_path.glob("*.md"))
    committed = sorted(p.name for p in DOCS.glob("*.md"))
    assert generated == committed

    differing = [
        name
        for name in committed
        if (tmp_path / name).read_text(encoding="utf-8")
        != (DOCS / name).read_text(encoding="utf-8")
    ]
    assert differing == []


# --- structural invariants of the committed pages ---------------------------


def test_pages_exist() -> None:
    assert len(pages()) == 217


def test_every_table_row_has_eleven_columns() -> None:
    bad: list[Any] = [
        (path.name, line)
        for path in pages()
        for line in data_rows(path)
        if len(cells(line)) != 11
    ]
    assert bad == []


def test_section_labels_are_not_rendered() -> None:
    bad = [
        (path.name, cells(line)[0])
        for path in pages()
        for line in data_rows(path)
        if LABEL.match(cells(line)[0])
    ]
    assert bad == []


def test_translations_are_not_inside_tables() -> None:
    """No table row may hold only the translation: it is squeezed to column one."""
    bad = [
        (path.name, line)
        for path in pages()
        for line in data_rows(path)
        if len([c for c in cells(line) if c]) == 1
    ]
    assert bad == []


def test_every_page_shows_a_translation() -> None:
    missing = [
        path.name
        for path in pages()
        if not any(
            line.startswith("**") and line.endswith("**") and len(line) > 4
            for line in path.read_text(encoding="utf-8").splitlines()
        )
    ]
    assert missing == []


def test_index_lists_exactly_the_existing_pages() -> None:
    index = (DOCS / "index.md").read_text(encoding="utf-8")
    linked = re.findall(r"\]\(([^)]+)\)", index)
    assert sorted(linked) == sorted(path.name for path in pages())
