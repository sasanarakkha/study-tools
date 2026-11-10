"""Tests for the Bhikkhu Pātimokkha word-by-word page generator."""

import re
from pathlib import Path
from typing import Any

import pandas as pd
import pytest

from scripts.fix_pali_tables import process_file
from scripts.generate_patimokkha import (
    Page,
    assign_orphan_sentences,
    generate_index,
    generate_rule_page,
    get_pages,
    load_data,
    normalize_cell,
    page_filename,
    strip_anki_number,
)

REPO = Path(__file__).resolve().parent.parent
XLSX = REPO / "temp" / "patimokkha.xlsx"
DOCS = REPO / "docs" / "6-pali-class" / "bhikkhu-patimokkha"

SEPARATOR = re.compile(r"^\|[\s:|-]*\|$")
LABEL = re.compile(r"^[A-Z]{2,3}(?: \d+)?$")
PAGE_NAME = re.compile(r"^\d{3}-")

needs_xlsx = pytest.mark.skipif(
    not XLSX.exists(), reason="temp/patimokkha.xlsx not downloaded"
)


def frame(rows: list[list[str]]) -> pd.DataFrame:
    """Build a minimal sheet slice: pali, pos, grammar, sentence, source, abbrev."""
    return pd.DataFrame(
        rows, columns=["pali", "pos", "grammar", "sentence", "source", "abbrev"]
    )


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def pages() -> list[Path]:
    return sorted(p for p in DOCS.glob("*.md") if PAGE_NAME.match(p.name))


def data_rows(path: Path) -> list[str]:
    return [
        line
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("|") and not SEPARATOR.match(line)
    ]


def headings(path: Path) -> list[str]:
    return [
        line[3:]
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("## ")
    ]


def load_sheet() -> tuple[pd.DataFrame, list[Page]]:
    df = load_data(XLSX)
    return df, get_pages(df)


# --- assign_orphan_sentences -------------------------------------------------


def test_translation_row_inherits_the_preceding_sentence() -> None:
    df = frame(
        [
            ["yo", "pron", "masc", "yo pana bhikkhu", "rule", "PC 1"],
            ["Yo, whoever", "", "", "", "rule", "PC 1"],
        ]
    )
    assert assign_orphan_sentences(df)["sentence"].tolist() == [
        "yo pana bhikkhu",
        "yo pana bhikkhu",
    ]


def test_section_labels_stay_ungrouped() -> None:
    df = frame(
        [
            ["yo", "pron", "masc", "yo pana bhikkhu", "rule", "PC 1"],
            ["PC 42", "", "", "", "rule", "PC 1"],
            ["Yo, whoever", "", "", "", "rule", "PC 1"],
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
                "SE 49",
            ],
            [
                "na",
                "ind",
                "neg",
                "na jivhānicchārakaṃ bhuñjissāmī'ti sikkhā karaṇīyā.",
                "rule",
                "SE 49",
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
            ["yo", "pron", "masc", "yo pana bhikkhu", "rule", "PC 1"],
            ["so bhikkhu", "", "", "", "rule", "PC 1"],
            ["so", "pron", "masc", "so bhikkhu", "next rule", "PC 2"],
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
            ["yo", "pron", "masc", "yo pana bhikkhu", "rule", "PC 1"],
            ["stray translation", "", "", "", "next rule", "PC 2"],
            ["so", "pron", "masc", "so bhikkhu", "next rule", "PC 2"],
        ]
    )
    assert assign_orphan_sentences(df)["sentence"].tolist() == [
        "yo pana bhikkhu",
        "",
        "so bhikkhu",
    ]


def test_inheritance_does_not_cross_a_rule_with_the_same_name() -> None:
    """Two rules can share a name; the code, not the name, ends the block."""
    df = frame(
        [
            ["na", "ind", "neg", "na oguṇṭhito antaraghare", "rule", "SE 23"],
            ["stray translation", "", "", "", "rule", "SE 24"],
            ["na", "ind", "neg", "na oguṇṭhito nisīdissāmi", "rule", "SE 24"],
        ]
    )
    assert assign_orphan_sentences(df)["sentence"].tolist() == [
        "na oguṇṭhito antaraghare",
        "",
        "na oguṇṭhito nisīdissāmi",
    ]


def test_word_rows_keep_their_own_sentence() -> None:
    df = frame(
        [
            ["yo", "pron", "masc", "sentence one", "rule", "PC 1"],
            ["so", "pron", "masc", "sentence two", "rule", "PC 1"],
        ]
    )
    assert assign_orphan_sentences(df)["sentence"].tolist() == [
        "sentence one",
        "sentence two",
    ]


# --- filenames ---------------------------------------------------------------


def test_page_filename_uses_position_and_rule_code() -> None:
    assert page_filename(1, "NI", 0) == "001-ni.md"
    assert page_filename(3, "PA 1", 0) == "003-pa-1.md"
    assert page_filename(60, "PC 01", 0) == "060-pc-01.md"
    assert page_filename(7, "PA", 1) == "007-pa-end.md"


def test_two_runs_of_a_section_become_two_pages() -> None:
    df = frame(
        [
            ["namo", "ind", "", "namo tassa", "nidānuddeso", "NI"],
            ["tatrime", "comp", "", "tatr'ime cattāro", "pārājikuddeso", "PA"],
            ["yo", "pron", "", "yo pana bhikkhu", "methunadhamma", "PA 1"],
            ["uddiṭṭhā", "pp", "", "uddiṭṭhā kho", "pārājikuddeso", "PA"],
        ]
    )
    assigned = assign_orphan_sentences(df)
    found = get_pages(assigned)
    assert [(p["abbrev"], p["filename"]) for p in found] == [
        ("NI", "001-ni.md"),
        ("PA", "002-pa.md"),
        ("PA 1", "003-pa-1.md"),
        ("PA", "004-pa-end.md"),
    ]
    assert [p["source"] for p in found][1] == "pārājikuddeso"


# --- cell normalisation ------------------------------------------------------


def test_cell_line_breaks_become_plain_text() -> None:
    assert (
        normalize_cell("vinassa + iti\n(or) vinassā + iti")
        == "vinassa + iti (or) vinassā + iti"
    )
    assert normalize_cell("√rāj + a + āno\nrāja + āno") == "√rāj + a + āno / rāja + āno"
    assert (
        normalize_cell("patta + kāla > kalla (or)\npatta + kalla")
        == "patta + kāla > kalla (or) patta + kalla"
    )
    assert (
        normalize_cell("nt dat sg of aggaḷaṭṭhapanāya\n, comp")
        == "nt dat sg of aggaḷaṭṭhapanāya, comp"
    )
    assert normalize_cell("  text \n") == "text"


def test_anki_numbers_are_removed_from_words() -> None:
    assert strip_anki_number("kallaṃ 2") == "kallaṃ"
    assert strip_anki_number("- patta 1") == "- patta"
    assert strip_anki_number("te 4") == "te"
    assert strip_anki_number("bhikkhu") == "bhikkhu"


# --- generation from the spreadsheet ----------------------------------------


@needs_xlsx
def test_every_page_has_a_unique_filename() -> None:
    _, page_list = load_sheet()
    names = [p["filename"] for p in page_list]
    assert len(set(names)) == len(names)


@needs_xlsx
def test_page_count_and_codes() -> None:
    _, page_list = load_sheet()
    assert len(page_list) == 236
    assert len({p["abbrev"] for p in page_list}) == 229


@needs_xlsx
def test_sections_are_split_into_opening_and_closing_pages() -> None:
    _, page_list = load_sheet()
    for abbrev in ["PA", "SA", "AN", "NP", "PC", "PD", "SE"]:
        matching = [p for p in page_list if p["abbrev"] == abbrev]
        assert len(matching) == 2, abbrev
        opening, closing = matching
        assert opening["filename"].endswith(f"-{abbrev.lower()}.md")
        assert closing["filename"].endswith(f"-{abbrev.lower()}-end.md")
        assert headings(DOCS / closing["filename"])[0].startswith(
            "uddiṭṭhā kho āyasmanto"
        )


@needs_xlsx
def test_rules_that_share_a_name_still_get_their_own_page() -> None:
    df, page_list = load_sheet()
    by_code = {p["abbrev"]: p for p in page_list}
    for abbrev in ["SE 23", "SE 24", "SE 67"]:
        page = by_code[abbrev]
        assert page["filename"].endswith(f"-{abbrev.replace(' ', '-').lower()}.md")
        assert len(df[df["abbrev"] == abbrev]) > 0
        title = (DOCS / page["filename"]).read_text(encoding="utf-8").splitlines()[0]
        assert title == f"# {abbrev} {page['source']}"
    assert len({by_code[a]["filename"] for a in ["SE 23", "SE 24", "SE 67"]}) == 3


@needs_xlsx
def test_no_page_title_ends_with_a_number() -> None:
    _, page_list = load_sheet()
    bad = [
        p["filename"]
        for p in page_list
        if re.search(r"\s\d+$", f"{p['abbrev']} {p['source']}")
    ]
    assert bad == []


@needs_xlsx
def test_index_follows_the_recitation_order() -> None:
    _, page_list = load_sheet()
    index = (DOCS / "index.md").read_text(encoding="utf-8")
    linked = re.findall(r"\]\(([^)]+)\)", index)
    assert linked == [p["filename"] for p in page_list]


@needs_xlsx
def test_every_row_of_the_sheet_is_published() -> None:
    df, page_list = load_sheet()
    missing: list[tuple[str, str]] = []
    for page in page_list:
        text = (DOCS / page["filename"]).read_text(encoding="utf-8")
        first_cells = {cells(line)[0] for line in data_rows(DOCS / page["filename"])}
        for _, row in df[df["run"] == page["run"]].iterrows():
            word = str(row["pali"]).strip()
            if not word or LABEL.match(word):
                continue
            if str(row["pos"]).strip():
                if strip_anki_number(normalize_cell(word)) not in first_cells:
                    missing.append((page["filename"], word[:60]))
            elif str(row["sentence"]).strip():
                if f"**{strip_anki_number(normalize_cell(word))}**" not in text:
                    missing.append((page["filename"], word[:60]))
    assert missing == []


@needs_xlsx
def test_generated_pages_match_the_repository(tmp_path: Path) -> None:
    """Regenerating from the workbook must reproduce the committed pages."""
    df, page_list = load_sheet()
    generate_index(page_list, tmp_path)
    for idx, page in enumerate(page_list):
        generate_rule_page(page, df, tmp_path, page_list, idx)
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
    assert len(pages()) == 236


def test_every_table_row_has_eleven_columns() -> None:
    bad: list[Any] = [
        (path.name, line)
        for path in pages()
        for line in data_rows(path)
        if len(cells(line)) != 11
    ]
    assert bad == []


def test_word_cells_keep_no_anki_numbers() -> None:
    bad = [
        (path.name, cells(line)[0])
        for path in pages()
        for line in data_rows(path)
        if re.search(r"\s\d+$", cells(line)[0])
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


def test_pages_contain_no_html() -> None:
    bad = [
        (path.name, match.group(0))
        for path in pages()
        for match in re.finditer(r"</?[A-Za-z][^>]*>", path.read_text(encoding="utf-8"))
    ]
    assert bad == []


def test_index_lists_exactly_the_existing_pages() -> None:
    index = (DOCS / "index.md").read_text(encoding="utf-8")
    linked = re.findall(r"\]\(([^)]+)\)", index)
    assert sorted(linked) == sorted(path.name for path in pages())
