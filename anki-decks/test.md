## Removing outdated words

The decks are regularly checked, and occasionally certain words no longer fit the deck's requirements. Sometimes, the meanings of words are split between two entries in [DPD](https://digitalpalidictionary.github.io/) or vice versa, and need to be unified. As a result, some words need to be removed from the deck.

### How to do it

After you updated the downloaded Anki Deck (by double-clicking on the latest downloaded file, or using CSV). Choose your Deck and in the Browse and add:

`-test:{date}`

It will be something like this:

`deck:Vocab Pali Class -test:25-11`

As it depends on the name of the deck you are updating and the {day} of update.

Where {date} is the date of the update. You can look it on the [page of latest release](https://github.com/sasanarakkha/study-tools/releases/latest/). For example if date is 25.11 you need to use {date} in the format 25-11.

![2024-12-03_18-33](https://github.com/user-attachments/assets/3ad34c54-73d8-4fe3-b5bc-9e090bfb6380)


Using this search in the Anki Brows you will see all cards which do not have a {day} in field "Test". And you can easily delate all of this old words, by selecting all (**Ctrl + A**) and deleting (**Ctrl + Del**); or right-click on the selected cards, **Notes > Delete**

Now you are up-to-date.

This number will depend on the date of release with every update.

### If it is not regular update

It is possible that one deck has been updated separately after the official update date. For instance, while the latest release for all decks was on 25.11.2024, one deck was updated on 03.12.2024. In this scenario, you should check the dates in Anki and identify which date has fewer cards, then remove them accordingly. In this example, the date 25.11 will have significantly fewer cards than 03.12. The cards with anything but "03-12" in the "test" field need to be removed.

`deck:Vocab Pali Class -test:03-12`
