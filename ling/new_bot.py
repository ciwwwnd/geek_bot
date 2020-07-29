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


# Делаем из вопроса список лемм
def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords
              and token != " "
              and token.strip() not in punctuation]
    return tokens


def find_synonyms(words):
    with open('new_dict.txt', encoding='utf-8') as file:
        words_synonyms = []
        for line in file:
            line = line.replace('\n', '')
            synonyms = line.split(' ')
            for word in words:
                if word in synonyms:
                    synonyms.remove(word)
                    words_synonyms.extend(synonyms)
    return words_synonyms


def find_quotes(words, filename):
    with open(filename, encoding='utf-8') as file1:
        reader = csv.DictReader(file1)
        quotes = []  # Сюда кидаем все цитаты из корпуса
        needed = {}  # Делаем словарь по типу (цитата: число совпадений лемм)
        for line in reader:
            quotes.append(line['line'])
            common = 0  # Счетчик для общих лемм
            for lemma in words:
                if lemma in line['lemmas']:
                    common += 1
            if common > 0:
                needed[line['line']] = common
        return needed, quotes


def ask_for_help(words):
    with open('help_words.txt', encoding='utf-8') as file:
        question = ' '.join(words)
        for line in file:
            line = line.replace('\n', '')
            if line in question:  # смотрим, есть ли словаря из этого корпуса в вопросе
                return True
        return False


def add_vvod(answer):
    with open('vvodnie.txt', encoding='utf-8') as file:
        phrases = []
        for line in file:
            line = line.replace('\n', '')
            phrases.append(line)
        phrase = random.choice(phrases)
        print(f'Albert: {phrase} {answer}')


def ask_question():
    question = preprocess_text(input('You: '))
    if ask_for_help(question):  # сначала проверяем на призыв о помощи
        print('\info')
    else:
        needed_quotes, all_quotes = find_quotes(question, 'lemmas.csv')
        if needed_quotes:
            answer = collections.Counter(needed_quotes).most_common(1)  # Выбираем цитату, в которой
            # самое больше совпадение лемм
            add_vvod(answer[0][0])
        else:
            synonyms = find_synonyms(question)
            needed_quotes, all_quotes = find_quotes(synonyms, 'lemmas.csv')
            if needed_quotes:
                answer = collections.Counter(needed_quotes).most_common(1)
                print(f'Albert: {answer[0][0]}')
            else:
                print(f'Albert: Я вас плохо понял, но: {random.choice(all_quotes)}')
                # Если вообще не найдены цитаты с такими же леммами, то выбираем рандомную


if __name__ == '__main__':
    ask_question()
