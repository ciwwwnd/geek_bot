import collections
import csv
import random
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation


mystem = Mystem()
russian_stopwords = stopwords.words("russian")


# Делаем из вопроса строку из лемм
def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords
              and token != " "
              and token.strip() not in punctuation]

    text = " ".join(tokens)
    return text


question = preprocess_text(input('You: '))
with open('lemmas.csv', encoding='utf-8') as file1:
    reader = csv.DictReader(file1)
    quotes = []  # Сюда кидаем все цитаты из корпуса
    needed = {}  # Делаем словарь по типу (цитата: число совпадений лемм)
    for line in reader:
        quotes.append(line['line'])
        common = 0  # Счетчик для общих лемм
        for lemma in question:
            if lemma in line['lemmas']:
                common += 1
        if common > 0:
            needed[line['line']] = common
    if quotes:
        answer = collections.Counter(needed).most_common(1)  # Выбираем цитату, в которой
        # самое больше совпадение лемм
        print(f'Albert: {answer[0][0]}')
    else:
        print(f'Albert: {random.choice(quotes)}')  # Если вообще не найдены цитаты с такими
        # же леммами, то выбираем рандомную
