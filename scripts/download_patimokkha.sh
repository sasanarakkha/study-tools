#!/usr/bin/env bash
# Download the Pātimokkha Word by Word spreadsheet from Google Sheets.
set -euo pipefail

XLSX_URL="https://docs.google.com/spreadsheets/d/1rS-IlX4DvKmnBO58KON37eVnOZqwfkG-ot-zIjCuzH4/export?format=xlsx"
OUT_DIR="$(dirname "$0")/../temp"
OUT_FILE="$OUT_DIR/patimokkha.xlsx"

mkdir -p "$OUT_DIR"

if ! ping -c 1 google.com &>/dev/null; then
    echo "Error: no internet connection." >&2
    exit 1
fi

echo "Downloading Pātimokkha XLSX..."
curl -L "$XLSX_URL" -o "$OUT_FILE"

if [ ! -f "$OUT_FILE" ]; then
    echo "Error: download failed." >&2
    exit 1
fi

echo "Saved to $OUT_FILE"
