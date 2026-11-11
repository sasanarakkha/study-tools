"""One-time export: turn dpd-db's xlsx2csv Pātimokkha CSV into the local data/patimokkha_word_by_word.tsv (issue #55)."""

import csv
import sys
from pathlib import Path

from tools.printer import printer as pr

SRC = Path.home() / "Documents/dpd-db/temp/patimokkha_word_by_word.csv"
OUT = Path("data/patimokkha_word_by_word.tsv")
N_COLS = 21  # header minus the dropped "#" column


def main() -> None:
    pr.bip()
    csv.field_size_limit(sys.maxsize)
    with SRC.open(newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f, delimiter="\t"))

    header = rows[0][1 : 1 + N_COLS]
    if header[0] != "x" or header[-1] != "comments":
        pr.no(f"unexpected header: {header}")
        sys.exit(1)

    out_rows: list[list[str]] = [header]
    for row in rows[1:]:
        cells = row[1 : 1 + N_COLS]
        cells += [""] * (N_COLS - len(cells))
        out_rows.append(cells)

    while len(out_rows) > 1 and not any(out_rows[-1]):
        out_rows.pop()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f, delimiter="\t", lineterminator="\n").writerows(out_rows)

    pr.green_title("export patimokkha tsv")
    pr.yes(len(out_rows) - 1)
    pr.green(str(OUT))


if __name__ == "__main__":
    main()
