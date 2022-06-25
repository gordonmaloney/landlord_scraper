import requests
from bs4 import BeautifulSoup


f = 'index.html'

with open('index.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    matches = soup.findAll('div', class_="_2Saup")


    for index, match in enumerate(matches):
        if index == 4:
            level = str(match.findAll('p')[1].text)
            for j in match.findAll('div', class_="_3Odbm"):
                words = j.text.split(', ')
                for word in words:
                    wikiUrl = f'https://en.wiktionary.org/wiki/{word}#Polish'
                    r = requests.get(wikiUrl)
                    wikiSoup = BeautifulSoup(r.content, 'xml')

                    #check if there's a Polish entry on Wiktionary:
                    if '<span class="mw-headline" id="Polish">' in str(wikiSoup):
                        #strip everything before polish entry
                        polishSoup = BeautifulSoup(str(wikiSoup).split('<span class="mw-headline" id="Polish">')[1], 'lxml')
                        ipa = polishSoup.findAll('span', class_='IPA')[0].text
                        trans = polishSoup.findAll('ol')[0]
                        translation1 = trans.findAll('li')[0].text
                        print(word + '	' + level + '	' + translation1.split('\n')[0].split('Coordinate')[0].split('Synonyms')[0] + '	' + ipa)
                    else:
                        print(word + '	' + level + '	')