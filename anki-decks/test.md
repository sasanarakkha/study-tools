## Removing outdated words

This work relies on the evolving [DPD](https://digitalpalidictionary.github.io/) dictionary, updated regularly. Occasionally, selected words might undergo changes—for instance, 'pada' could become 'pada 1', with additional meanings like 'pada 2', 'pada 3', and so forth. Consequently, duplicates (like the original 'pada' duplicated as 'pada 1') must be removed using the "Test" field.

### How to do it

After you updated the downloaded Anki Deck (by double-clicking on the latest downloaded file, or using CSV). Choose your Deck and in the Browse and add:

`-test:{date}`

It will be something like this:

`deck:Vocab Pali Class -test:01-03-24`

As it depends on the name of the deck you are updating and the {day} of update.

Where {date} is the date of the update. You can look it on the [page of latest release](https://github.com/sasanarakkha/study-tools/releases/latest/). For example if date is 01.03.2024 you need to use {date} in the format 01-03-24.

![2024-01-01_15-10](https://github.com/sasanarakkha/study-tools/assets/39419221/7c8aaca3-5db9-48d6-90dc-2ab5e89d47bb)

Using this search in the Anki Brows you will see all cards which do not have a {day} in field "Test". And you can easily delate all of this old words, by selecting all (**Ctrl + A**) and deleting (**Ctrl + Del**); or right-click on the selected cards, **Notes > Delete**

Now you are up-to-date.

This number will depend on the date of release with every update.
