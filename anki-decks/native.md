## Native cloumn

If English is not your first language, it’s recommended to translate words into your native language. For this, in almost all SBS Anki decks there is an empty field called "native" that you can fill in.

We are delighted to provide additional data for Russian at the moment, and we may potentially expand our language support to include other languages in the future. Artificial intelligence has made significant strides in automatic language translation, achieving quite good quality. For more information on language support, please [contact us](mailto:studytools@sasanarakkha.org). 


Download the CSV files below and import them into most SBS decks. Note that the deck must have a "native" field:

- [sbs_russian.csv](https://github.com/sasanarakkha/study-tools/releases/latest/download/sbs-rus.csv)

For Pāli Class decks:
- [ru_common_roots.csv](https://github.com/sasanarakkha/study-tools/releases/latest/download/ru-common-roots.csv) (Grammar Deck; Grammar Note Type)
- [ru_grammar_pali_class_gramm.csv](https://github.com/sasanarakkha/study-tools/releases/latest/download/ru-grammar-pali-class-gramm.csv) (Common Roots Deck)

--- 

__! Important !__ Before doing anything, synchronize your collection across all your Anki devices. Go to **Tools > Preferences > Syncing** and enable "*On next sync force changes in one direction*". This will provide a secure backup on the Anki cloud in case of any issues.

The update process is slightly different since these CSV files contain all words related to all SBS decks in a single file. Let’s describe the process for sbs_russian.csv in detail. (The process for other CSV files related to the Pāli class is similar, except for the last part of removing irrelevant cards.)

- in Anki, click on **File > Import**

![image](https://user-images.githubusercontent.com/39419221/187018280-c295e071-c130-4f42-8518-a3a5e0326124.png)

- Select the downloaded CSV file.

- Choose the Notetype and Deck you wish to update.

- Scroll down to the beginning of the **Field Mapping** section and switch the positions of *pali* and *native*, so that *native* maps to the second column in the CSV file, while *pali* remains unmapped (Nothing).
  
![2024-10-25_16-36](https://github.com/user-attachments/assets/5c813ea8-0596-42e7-af26-fff725b8aa20)

- Double-check everything with the image above, then click  **import**

- In the window **Overview**, you’ll see that along with updated existing cards, many new notes have been imported. We need to remove these. Click on **Show** to display the new notes.
  
![2024-10-25_16-38](https://github.com/user-attachments/assets/3949078d-2ebe-4e2d-b5cc-8eb202ccf3cc)

- In the window **Browse**, you’ll see all these new notes. Select them all (**Ctrl + A**) and delete (**Ctrl + del**).
  
![2024-10-25_16-40](https://github.com/user-attachments/assets/b957699f-b0a7-478a-9eeb-fbe61fbde6cf)

- Now you have the latest native meaning.

