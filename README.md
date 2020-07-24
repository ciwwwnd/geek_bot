# GEEK PICNIC 2020

**Дедлайн**: 3-4 августа. Так у нас будет один-два дня, чтобы вычитать код, протестировать его, исправить все возможные ошибки. Чем раньше мы все закончим, тем будет лучше!

## Лингвистическая часть

У нас есть замечательная [гугл-папка](https://drive.google.com/drive/folders/1XHisyJyqv859x64v9aqljhHr4RqszalS?usp=sharing). В ней вы можете хранить свои цитаты, прочий рабочий стафф, состоящий из эмоционально-окрашенных кусков текста. Когда вы закончите собирать тексты в своих гугл-файлах, прогоните его через свои регулярки, а потом залейте сюда в папку [corpora](https://github.com/ciwwwnd/geek_bot/tree/master/corpora). На выходе у вас будет .txt в кодировке UTF-8 с цитатами (1 тип вопроса — 1 .txt файл, если вопрос не общий и не тупой). 

Мы сегодня говорили о том, что интересные цитаты, которые можно использовать как ответ на посредственный вопрос, можно размечать как-нибудь, но пока просто держите их в отдельном файле (хотя бы в другом гугл-доке).

**Про стек технологий:**

+ [pymorphy2](https://pymorphy2.readthedocs.io/en/latest/) для лемматизации и прочего. Если вам не хватит каких-то функций и фич, попробуйте пользоваться обычным pymorphy, но учтите, что он медленнее работает и ему придется тяжко.

**Что еще может пригодиться?**
+ [nltk](https://www.kaggle.com/alxmamaev/how-to-easy-preprocess-russian-text) —— он нам нужен для стоп-слов типа *который*, *все*, *некоторые* и проч.
+ [MyStem](https://yandex.ru/dev/mystem/) –– MyStem умеет строить гипотетические разборы для множества слов — включая те слова, которых нет в словаре. Но она консольная!
+ [Tesuck](https://nlpub.ru/Tesuck) —— Извлекает ключевые слова и словосочетания из текстов. Но он для некоммерческого использования, так что тут надо уточнить у организаторов.

## Нелингвистическая часть

Ждем вопросов для research. Эта часть будет дорабатываться.

## Прочее
Давайте договоримся пользоваться [Issues](https://github.com/ciwwwnd/geek_bot/issues). Вы нажимаете на New issue, пишете в начале в большом окошке @ciwwwnd (или никнейм любого другого человека, который может помочь вам). Альтернатива: добавить ciwwwnd сразу в Assignees. А затем рассказываете, что пошло не так. (Можно прикладывать скриншоты и делать многое другое. Опционально – добавьте к вопросу Labels.) После того, как мы найдем решение, issue сохранится и будет доступна [здесь](https://github.com/ciwwwnd/geek_bot/issues?q=is%3Aissue+is%3Aclosed). Так другие участники проекта смогут ознакомиться со встретившимися проблемами и, возможно, найти нужное решение.

Кроме того, давайте называть переменные понятно. Лучше три слова через нижний слеш, чем тратить два часа, чтобы понять, что вы имели в виду. Так вам будет проще разбираться со своим кодом, а остальным —— читать ваш. Пожалуйста, никаких i, n, item, k, l, data, info, object, не называйте словарь словарем —— это все упростит нам дальнейшую отладку и работу уже с цельным кодом. Помните, что для названия функций используются глаголы, а для всего остального — существительные. 

Старайтесь комментировать большие функции, эти комментарии нужны другим (и их не будет, когда мы будем совмещать все наши штуки в одну). И если уж вы беретесь за написание комментария, напишите его хорошо. Не пишите сумбурно. Не объясняйте очевидное. Будьте лаконичны. 


## Q&A

+ Мне нужно загружать промежуточные результаты своей работы?
    * Да. Так мы будем знать, с какой скоростью работаем, и, если что, сможем скорректировать задачи, перераспределить их или еще как-нибудь помочь друг другу. 

+ А что если у меня сырой код или там много костылей? 
    * Все в порядке. Главное, чтобы он работал. Я надеюсь, что у нас будет время, чтобы привести все в порядок. 

+ Есть ли стайлгайд? 
    * Для питона есть стандарт написания кода —— это PEP 8. Если в вашей программе много нарушений PEP 8 – она выглядит неряшливо. Для упрощения жизни существует модуль pep8. Это модуль, позволяющий проверять, соответствует ли код стандарту PEP 8. Сперва её надо установить (```pip install pep8```), поле этого запустить, указав путь до файла или папки с кодом: ```pep8 ./2_wallie_how_are_you/wallie.py```. Программа выдаст все нарушения PEP 8. Остаётся их только поправить.

+ Отладочные принты надо оставлять? 
    * Не надо. Отладочные принты нужны только для вас, чтобы вы понимали, что все работает в процессе написания или запуска программы. Если хотите, используйте модуль logging. 

+ Куда мне заливать свои файлы? 
    * Если это txt c текстами, то в папку [corpora](https://github.com/ciwwwnd/geek_bot/tree/master/corpora). Если что-то связанное с API и вебом, то в папку [web](https://github.com/ciwwwnd/geek_bot/tree/master/web). Папка [ling](https://github.com/ciwwwnd/geek_bot/tree/master/ling) для всей NLP части. 
!(https://raw.githubusercontent.com/ciwwwnd/geek_bot/master/пфп.jpg?token=ANIMGCRBTDA34VDGRR7LWM27DIV2O[true])
