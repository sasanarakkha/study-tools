# Updating Anki Decks

Regular updates ensure your decks stay in sync with the latest DPD improvements and course corrections.

__! Important !__ Before updating, synchronize your collection across all devices. Go to **Tools > Preferences > Syncing** and enable "*On next sync force changes in one direction*". This creates a secure backup on AnkiWeb.

![Anki Sync Settings](../assets/images/anki/sync-settings-b.png)

## Steps to Update

1. Download the latest `.apkg` file for the deck from the [Anki Decks index](5-anki/index.md).
2. Double-click the downloaded file to import it.
3. Ensure your import settings match the image below to preserve your learning statistics.

![Anki Import Settings](../assets/images/anki/import-settings-b.png)

## Removing Outdated Words

Occasionally, words are moved, unified, or removed from the course. These cards need to be manually deleted from your local collection to stay up-to-date.

### How to Find Outdated Words

After importing the latest APKG, go to the **Browse** window in Anki. Use the following search term:

`-test:{date}`

*(Example: `deck:Vocab Pali Class -test:25-11`)*

Replace `{date}` with the release date in `DD-MM` format. You can check the date on the [latest release page](https://github.com/sasanarakkha/study-tools/releases/latest/).

![Anki Search for Outdated Cards](../assets/images/anki/search-test-field-b.png)

### Steps to Delete

1. Perform the search above.
2. Select all matching cards (**Ctrl + A**).
3. Delete them (**Ctrl + Del** or **Right-click > Notes > Delete**).

---

If the standard method fails, see the [Advanced CSV Update](csv-update.md) method.
