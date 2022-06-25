import requests
from bs4 import BeautifulSoup

print('Scrape wiktionary for IPA')

search_term = input('Search for Thai word: ')
language = 'Thai'
ipa_url = f'https://en.wiktionary.org/wiki/{search_term}#{language}'
trans_url = 'https://learngaelic.scot/dictionary/index.jsp?abairt=test&slang=both&wholeword=false'

r_ipa = requests.get(ipa_url)
r_trans = requests.get(trans_url)

soup_ipa = BeautifulSoup(r_ipa.content, 'lxml')
soup_trans = BeautifulSoup(r_trans.content, 'lxml')

ipa = soup_ipa.findAll('span', class_='IPA')
trans = soup_trans.findAll('span', class_='Q4iAWc')

if ipa:
    print(ipa[0].text)
else:
    print('no ipa found')


print(soup_trans.prettify())