#!/usr/bin/env bash
# Download the Pātimokkha Word by Word spreadsheet from Google Sheets.
set -euo pipefail

XLSX_URL="https://docs.google.com/spreadsheets/d/1rS-IlX4DvKmnBO58KON37eVnOZqwfkG-ot-zIjCuzH4/export?format=xlsx"
OUT_DIR="$(dirname "$0")/../temp"
OUT_FILE="$OUT_DIR/patimokkha.xlsx"

mkdir -p "$OUT_DIR"

echo "Downloading Pātimokkha XLSX..."
curl -L -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
    "$XLSX_URL" -o "$OUT_FILE"

if [ ! -f "$OUT_FILE" ]; then
    echo "Error: download failed." >&2
    exit 1
fi

file_info=$(file "$OUT_FILE")
if [[ "$file_info" != *"Zip archive data"* ]] && [[ "$file_info" != *"Microsoft Excel 2007+"* ]]; then
    echo "Error: Downloaded file is not a valid Excel file." >&2
    echo "It appears to be: $file_info" >&2
    exit 1
fi

echo "Saved to $OUT_FILE"
