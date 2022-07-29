# Removing duplicated words

This work is based on the [DPD](https://digitalpalidictionary.github.io/) dictionary which is a work in progress and being updated regularly. Because of this, from time to time may an updated may be done of selected words (this will show itself like this; for example: the word 'pada' will become 'pada 1', and variations of meanings of 'pada' will be added as 'pada 2', 'pada 3' etc.). 

From this follows that from time to time duplicated words (the original 'pada' is now duplicated as 'pada 1', need to be removed. For this, the field called **"Test"** is used.

After you updated the downloaded Anki Deck (same way, just by double-clicking on the latest downloaded file). Choose your Deck and in the **Browse** add:

`-test:`{number}

It will show all cards which do not have a number in field "Test". And you can easily delate all of this old words, by selecting all (**Ctrl + A**) and deleting (**Ctrl + Delete**). 

Now you are up-to-date.

With every update, this {number} will be different. Please see the random number for Test in Anki
 [here](https://github.com/sasanarakkha/study-tools/releases/latest)
