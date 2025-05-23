## Удаление устаревших слов

Эта работа зависит от развивающегося словаря [DPD](https://digitalpalidictionary.github.io/), регулярно обновляемого. Иногда выбранные слова могут изменяться, например, 'pada' может стать 'pada 1', с дополнительными значениями, такими как 'pada 2', 'pada 3' и так далее. Следовательно,устареашие копии (как оригинальное 'pada', продублированное как 'pada 1'), должны быть удалены с помощью поля "Test".

### Как это сделать

После обновления загруженной колоды Anki (дважды щелкнув по последнему загруженному файлу, либо используя CSV). Выберите вашу колоду и в разделе Browse и добавьте:

`-test:{дата}`

Это будет выглядеть примерно так:

`deck:Vocab Pali Class -test:01-03`

Это зависит от названия колоды, которую вы обновляете, и {дня} обновления.

Где {дата} - это дата обновления. Вы можете посмотреть ее на [странице последнего релиза](https://github.com/sasanarakkha/study-tools/releases/latest/). Например, если дата 01.03, вам нужно использовать дату в формате 01-03.

![2024-01-01_15-10](https://github.com/sasanarakkha/study-tools/assets/39419221/7c8aaca3-5db9-48d6-90dc-2ab5e89d47bb)

Используя этот поиск в Anki Browser, вы увидите все слова, у которых нет {дня} в поле "Test". И вы легко можете удалить все эти устаревшие слова, выделив их все (**Ctrl + A**) и удалив (**Ctrl + Del**); или щелкнув правой кнопкой мыши на выбранных словах, **Notes > Delete**.

Теперь ваша колода имеет только самую свежую информацию.

Этот номер будет зависеть от даты релиза с каждым обновлением.