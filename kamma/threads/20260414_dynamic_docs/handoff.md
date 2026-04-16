### Handoff: Dynamic Site Architecture & Asset Localization

#### **What has been done**
1.  **Digit-First Automation System:**
    *   Implemented `scripts/generate_indexes.py`: Automatically generates `index.md` files for directories starting with a digit. It prepends `.header.md` content and sorts items numerically (e.g., `1-` before `4-`).
    *   Implemented `scripts/generate_mkdocs_yaml.py`: Dynamically updates `mkdocs.yaml` navigation to match the directory structure. It follows the same numeric sorting and digit-only inclusion rules.
    *   **Promotion Logic:** If a directory contains only one digit-prefixed child, the system "promotes" that child, linking directly to it from the parent menu/index to avoid redundant submenus (applied to `4-dictionaries`, `1-sbs`, etc.).

2.  **Asset Localization & Contextual Renaming:**
    *   Created `scripts/localize_assets.py`: Scans for GitHub-hosted images (`user-attachments`, `user-images`, etc.), downloads them to `docs/assets/images/`, and renames them based on alt-text or nearest headings (e.g., `add-on-special-fields.png`).
    *   Updated all markdown files to use local relative paths.

3.  **Universal Link Repair & Cleanup:**
    *   Created `scripts/fix_links.py`: Uses fuzzy matching (ignoring digits) and normalization (underscores to dashes) to repair broken internal relative links.
    *   Integrated `scripts/clean_dead_links.py`: Automatically removes list items in indices that point to deleted or moved `.md` files.
    *   Integrated `scripts/fix_heading_hierarchy.py`: Normalizes markdown structure by converting bold first lines to H1 and fixing skipped heading levels.

4.  **Pipeline Integration:**
    *   Consolidated all steps into `scripts/web_preprocessing.sh`.
    *   Integrated the pipeline into `scripts/cl/sbs-build-website` and the GitHub deployment workflow.
    *   Standardized output using `tools/printer.py` (requires `rich`).

---

#### **Errors, Issues, and Repeated Mistakes**

*   **Logic Errors (Promotion & Root):**
    *   **Repeatedly neglected the root `index.md`:** Initially skipped root generation to "protect" the homepage, which left it in a broken/manual state. It required a special `is_root` flag to ensure it also followed digit-sorting and header-prepending.
    *   **Submenu nesting in YAML:** In the promotion logic, directories with one child were initially being returned as single-key dictionaries instead of unwrapped strings in `mkdocs.yaml`, causing nested menu items (e.g., `Dictionaries > Dictionary Name` instead of just `Dictionary Name`).
    *   **Header Exclusion:** Incorrectly assumed `.header.md` presence should block promotion. This led to redundant submenus until the logic was adjusted to allow promotion regardless of header presence in the target folder.

*   **Link Mapping Faults:**
    *   **Greedy Fuzzy Matching:** `fix_links.py` suffered from overly aggressive matching, mapping generic folder names (like `Anki`) to the first available `index.md` found, which was often `5-anki/templates/index.md`. I had to implement a strict exclusion for the `templates` folder during auto-resolution.

*   **Environment & Execution Issues:**
    *   **`PYTHONPATH` Oversight:** Multiple script failures occurred because `tools/` was not in the Python path when running from subdirectories. This required explicit `export PYTHONPATH` additions to the shell scripts.
    *   **Dependency Management:** Failed to verify the presence of the `rich` library before integrating the new `tools/printer.py`, resulting in a `ModuleNotFoundError` during the first pipeline run.
    *   **Script Typos:** Small errors (e.g., `hashlib.mdsafe` instead of `hashlib.md5`) caused crashes during high-volume operations (asset localization).

---

#### **Critical Findings for Future Sessions**
*   **Navigation:** The `nav` in `mkdocs.yaml` is now 100% managed by `generate_mkdocs_yaml.py`. Manual changes will be overwritten. To control order, simply prefix folders/files with `Number-`.
*   **Headers:** To add introductory text to any auto-generated index, create a `.header.md` in that folder. It will automatically appear at the top of the local `index.md` and (if it's the root) the Home page.
