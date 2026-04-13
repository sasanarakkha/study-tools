# Advanced CSV Update

For those who have trouble updating the Anki deck by simply clicking on the `.apkg` file, there is a reliable method using CSV imports. This is especially useful for users with very old versions of the deck.

1. Download the latest `.csv` file from the [Releases page](https://github.com/sasanarakkha/study-tools/releases/latest).
2. In Anki, go to **Tools > Manage Note Types** and ensure your field list matches the current standard.
3. Go to **File > Import** and select the downloaded `.csv`.
4. Set: **Existing notes:** Update, **Match scope:** Notetype.
5. Map the fields correctly (ensure `marks` maps to the last column, and `Tags` is left unmapped).
6. Click **Import**.
