"""Tests for the Pāḷi markdown table normalizer."""

from scripts.fix_pali_tables import normalize_separator_row


def test_long_dash_runs_collapse_to_three() -> None:
    line = "| :--------------------- | :-------- | --- |"
    assert normalize_separator_row(line) == "| :--- | :--- | --- |"


def test_short_dash_runs_are_left_alone() -> None:
    line = "| :--- | --- | :---: |"
    assert normalize_separator_row(line) == "| :--- | --- | :---: |"


def test_data_rows_are_not_touched() -> None:
    line = "| bhikkhu | noun | masc nom sg | | monk |"
    assert normalize_separator_row(line) == line
