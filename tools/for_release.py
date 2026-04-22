# Configuration for GitHub releases
# Dynamically generates the release body from docs/5-anki/index.md

import sys
import re
from pathlib import Path

# The single source of truth for assets
ASSETS = [
    "common-roots.apkg",
    "common-roots.csv",
    "dhp-vocab.apkg",
    "dhp-vocab.csv",
    "grammar-pali-class-abbr.csv",
    "grammar-pali-class-gramm.csv",
    "grammar-pali-class-sandhi.csv",
    "grammar-pali-class.apkg",
    "parittas.apkg",
    "parittas.csv",
    "patimokkha-learning.apkg",
    "patimokkha-word-by-word.apkg",
    "patimokkha-word-by-word.csv",
    "phonetic-pali-class.apkg",
    "phonetic-pali-class.csv",
    "roots-pali-class.apkg",
    "roots-pali-class.csv",
    "ru-pali-vocab.apkg",
    "ru-pali-vocab.csv",
    "sbs-daily-chanting.apkg",
    "sbs-pali-english-vocab.apkg",
    "sbs-pd.csv",
    "sbs-rus.csv",
    "suttas-advanced-pali-class.apkg",
    "suttas-advanced-pali-class.csv",
    "vibhanga.apkg",
    "vibhanga.csv",
    "vocab-pali-class.apkg",
    "vocab-pali-class.csv",
    "ru_common_roots.csv",
    "ru_cl_sum_gramm.csv",
]

# Formatting constants
SITE_BASE_URL = "https://sasanarakkha.github.io/study-tools/5-anki/"
IMAGE_BANNER = "![compressed_more](https://github.com/user-attachments/assets/24d4cae6-66b4-48de-a7d0-de1ce5969a77)"
FOOTER = """
----------

If you have any questions or comments related to these study tools, please [email us.](mailto:studytools@sasanarakkha.org)

-----------

These Learning Tools are licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />
"""

def generate_release_body():
    source_path = Path("docs/5-anki/index.md")
    if not source_path.exists():
        return "Automated build artifacts"

    content = source_path.read_text(encoding="utf-8")
    
    # 1. Start with the banner
    body = IMAGE_BANNER + "\n\n"
    
    # 2. Process the content from index.md
    # We replace relative links starting with digits: ](1... -> ](https://.../5-anki/1...
    # And convert .md to / for clean website links
    
    # Regex explains: match ]( followed by a digit. Replace with ](URL + digit
    transformed = re.sub(r'\]\((\d)', rf']({SITE_BASE_URL}\1', content)
    
    # Clean up the .md extensions for the website links we just created
    # We only want to target the links we just made absolute
    transformed = re.sub(rf'({re.escape(SITE_BASE_URL)}[^)]+)\.md', r'\1/', transformed)
    
    # Remove the redundant "release GitHub page" line if it exists
    transformed = re.sub(r'.*release GitHub page.*\n?', '', transformed)
    
    body += transformed
    body += "\n" + FOOTER
    
    # Save a copy for inspection
    temp_dir = Path("temp")
    temp_dir.mkdir(exist_ok=True)
    (temp_dir / "release_body.md").write_text(body, encoding="utf-8")
    
    return body

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "body":
        print(generate_release_body())
    else:
        print(" ".join(ASSETS))
