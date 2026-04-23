"""Comparison tool to identify changes between current Pāḷi study Markdown files and a past Git commit."""
import os
import subprocess
import re
import argparse
import difflib
from tools.printer import printer as pr

def get_tokens(text):
    """
    Normalizes text and extracts a list of words.
    Removes markdown formatting, HTML tags, and punctuation.
    """
    # Remove markdown links/images URLs but keep the alt/link text
    text = re.sub(r'\[([^\]]*)\]\([^\)]+\)', r'\1', text)
    # Remove markdown formatting characters
    text = re.sub(r'[*_~`]', '', text)
    # Remove HTML tags
    text = re.sub(r'<[a-zA-Z/][^>]*>', ' ', text)
    # Remove punctuation that might be attached to words differently
    # Include hyphens and other standard punctuation in removal to focus strictly on words
    text = re.sub(r'[#\[\]\(\)>|\\.,;!?\'"/\-:]', ' ', text)
    # Split into words and convert to lowercase
    words = re.split(r'\s+', text.strip().lower())
    # Normalize grammar abbreviations: treat 'sg' as 's' for comparison
    return [w if w != 'sg' else 's' for w in words if w]

def get_old_content(file_path, commit):
    cmd = ["git", "show", f"{commit}:{file_path}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return None
    return result.stdout

def main():
    parser = argparse.ArgumentParser(description="Compare current .md files with an older version using word sequence logic.")
    parser.add_argument("--commit", default="71c840b", help="Git commit to compare against")
    parser.add_argument("--dir", default="docs/6-pali-class", help="Directory to search for .md files")
    parser.add_argument("--verbose", action="store_true", help="Show the actual differences found")
    
    args = parser.parse_args()

    md_files = []
    if os.path.isfile(args.dir):
        if args.dir.endswith(".md"):
            md_files.append(args.dir)
    else:
        for root, dirs, files in os.walk(args.dir):
            for file in files:
                if file.endswith(".md"):
                    md_files.append(os.path.join(root, file))

    if not md_files:
        pr.warning(f"No .md files found in {args.dir}")
        return

    pr.green(f"Comparing {len(md_files)} files vs {args.commit[:8]}")
    files_with_losses = 0

    for file_path in md_files:
        old_content = get_old_content(file_path, args.commit)
        if old_content is None:
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                new_content = f.read()
        except Exception as e:
            pr.warning(f"Error reading {file_path}: {e}")
            continue

        old_tokens = get_tokens(old_content)
        new_tokens = get_tokens(new_content)

        # Count frequencies of each token
        from collections import Counter
        old_counts = Counter(old_tokens)
        new_counts = Counter(new_tokens)

        missing_words = []
        added_words = []

        # Check for missing words
        for word, count in old_counts.items():
            if new_counts[word] < count:
                diff = count - new_counts[word]
                missing_words.append(f"{word} (missing {diff})")

        # Check for added words
        for word, count in new_counts.items():
            if word not in old_counts:
                added_words.append(f"{word} (new word)")
            elif count > old_counts[word]:
                diff = count - old_counts[word]
                added_words.append(f"{word} (added {diff})")

        if missing_words or added_words:
            files_with_losses += 1
            if missing_words:
                pr.warning(f"[DATA LOSS] {file_path}: {len(missing_words)} words missing")
                for mw in missing_words[:5]: pr.warning(f"  '{mw}'")
            if added_words:
                pr.warning(f"[DATA GAIN] {file_path}: {len(added_words)} words added")
                for aw in added_words[:5]: pr.warning(f"  '{aw}'")

    if files_with_losses == 0:
        pr.yes("ok")
    else:
        pr.no(f"{files_with_losses} files with data loss")

if __name__ == "__main__":
    main()
