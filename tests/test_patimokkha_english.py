"""Tests for the Bhikkhu Pātimokkha English translation export."""

import re
import sys
from pathlib import Path

import pandas as pd
import pytest
from docx import Document

from scripts.extract_patimokkha_english import (
    SECTION_NAMES,
    build_markdown,
    main,
)
from scripts.generate_patimokkha import Page, get_pages, load_data

REPO = Path(__file__).resolve().parent.parent
TSV = REPO / "data" / "patimokkha_word_by_word.tsv"
DOCS = REPO / "docs" / "6-pali-class" / "bhikkhu-patimokkha"

LABEL = re.compile(r"^[A-Z]{2,3} [0-9]+\.")


@pytest.fixture(scope="module")
def rendered() -> tuple[list[Page], list[str]]:
    """Return the pages and the Markdown blocks, built once for the whole module."""
    df = load_data(TSV)
    pages = get_pages(df)
    blocks = [block.strip() for block in build_markdown(df, pages).split("\n\n")]
    return pages, [block for block in blocks if block]


def paragraphs(blocks: list[str]) -> list[str]:
    return [block for block in blocks if not block.startswith("#")]


def body(paragraph: str) -> str:
    """Drop the rule label and the space after it from a numbered paragraph."""
    return re.sub(r"^[A-Z]{2,3} [0-9]+\. ", "", paragraph)


def label_of(paragraph: str) -> str:
    """Return the rule code a numbered paragraph starts with."""
    match = LABEL.match(paragraph)
    if match is None:
        raise AssertionError(f"Not a labelled paragraph: {paragraph[:40]}")
    return match.group(0)[:-1]


def test_headings_are_the_nine_sections_in_order(
    rendered: tuple[list[Page], list[str]],
) -> None:
    _, blocks = rendered
    headings = [block[3:] for block in blocks if block.startswith("## ")]
    assert headings == list(SECTION_NAMES.values())


def test_every_page_is_one_paragraph(rendered: tuple[list[Page], list[str]]) -> None:
    pages, blocks = rendered
    assert len(paragraphs(blocks)) == len(pages) == 236


def test_only_numbered_rules_are_labelled(
    rendered: tuple[list[Page], list[str]],
) -> None:
    pages, blocks = rendered
    labelled = [paragraph for paragraph in paragraphs(blocks) if LABEL.match(paragraph)]
    expected = [
        page["abbrev"]
        for page in pages
        if page["run_of_rule"] == 0 and " " in page["abbrev"]
    ]
    assert len(labelled) == len(expected) == 220
    assert [label_of(paragraph) for paragraph in labelled] == expected


def test_section_intros_and_closings_carry_no_label(
    rendered: tuple[list[Page], list[str]],
) -> None:
    _, blocks = rendered
    pārājika = blocks.index("## Pārājika")
    intro = blocks[pārājika + 1]
    assert intro.startswith("Therein these four cases")
    assert not LABEL.match(intro)
    closing = blocks[blocks.index("## Saṅghādisesa") - 1]
    assert closing.startswith("Venerables, the four cases")
    assert not LABEL.match(closing)


def test_paragraphs_match_the_website_pages(
    rendered: tuple[list[Page], list[str]],
) -> None:
    pages, blocks = rendered
    mismatched: list[str] = []
    for page, paragraph in zip(pages, paragraphs(blocks), strict=True):
        bold = [
            line[2:-2]
            for line in (DOCS / page["filename"])
            .read_text(encoding="utf-8")
            .splitlines()
            if line.startswith("**") and line.endswith("**") and len(line) > 4
        ]
        if body(paragraph) != " ".join(bold):
            mismatched.append(page["filename"])
    assert mismatched == []


def test_unknown_section_abbrev_raises_key_error() -> None:
    df = pd.DataFrame(
        [["text", "", "a sentence", 0]], columns=["pali", "pos", "sentence", "run"]
    )
    pages: list[Page] = [
        {
            "run": 0,
            "abbrev": "XX",
            "source": "unknown",
            "run_of_rule": 0,
            "filename": "001-xx.md",
        }
    ]
    with pytest.raises(KeyError):
        build_markdown(df, pages)


def test_main_writes_the_markdown_and_the_docx(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["extract_patimokkha_english.py", str(TSV), "--output-dir", str(tmp_path)],
    )
    main()

    md_path = tmp_path / "patimokkha_english.md"
    docx_path = tmp_path / "patimokkha_english.docx"
    assert md_path.exists()
    assert docx_path.exists()

    texts = [paragraph.text for paragraph in Document(str(docx_path)).paragraphs]
    assert "Pārājika" in texts
    assert any(text.startswith("PA 1. ") for text in texts)


def test_docx_text_matches_the_markdown(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["extract_patimokkha_english.py", str(TSV), "--output-dir", str(tmp_path)],
    )
    main()

    markdown = (tmp_path / "patimokkha_english.md").read_text(encoding="utf-8")
    expected = [
        re.sub(r"^#{1,6}\s+", "", block.strip())
        for block in markdown.split("\n\n")
        if block.strip()
    ]
    docx = Document(str(tmp_path / "patimokkha_english.docx"))
    assert [paragraph.text for paragraph in docx.paragraphs] == expected
