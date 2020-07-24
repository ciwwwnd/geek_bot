from bs4 import BeautifulSoup
import requests
import re

url_id_counter = '1'

for urls in range(14):
    url_template = 'https://ru.citaty.net/avtory/albert-einshtein/?page=' + url_id_counter
    url = requests.get(url_template).text
    soup = BeautifulSoup(url, 'html.parser')

    finding_quote = soup.find_all('div', attrs={'class': 'blockquote'})
    finding_more_quotes = soup.find_all(
        'h3', attrs={'class': 'blockquote-text'})
    for i in range(17):
        text = finding_more_quotes[i].text
        with open("corpora.txt", "a", encoding='utf-8') as file:
            for j in text[0]:
                cleanr = '<.+>'
                cleantext = re.sub(cleanr, '', text)
                print(cleantext, file=file)
                print(text)
    url_id_counter = str(int(url_id_counter) + 1)
