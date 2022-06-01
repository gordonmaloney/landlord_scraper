import requests
from bs4 import BeautifulSoup

search_term = input('Input search term: ')
url = f'https://www.housingandpropertychamber.scot/apply-tribunal/other-private-tenancy-applications/other-private-tenancy-applications-decisions?field_tribunal_rule_other_value=All&name_of_party={search_term}'
page = 0


def search_page(full_url, page):
    r = requests.get(full_url)

    soup = BeautifulSoup(r.content, 'lxml')

    for match in soup.findAll('tr', {'class': ['odd', 'even']}):
        print('\nCase reference: ' + match.a.text)
        print('Rule: ' + match.find('td', class_='views-field-field-tribunal-rule-other').text)
        print('Applicant: ' + match.find('td', class_='views-field-field-applicant-other').text)
        print('Respondent: ' + match.find('td', class_='views-field-field-respondent-other').text)

        link = match.findAll('a', href=True)

        print('Link to decision: ' + link[1]['href'])

    # Check for next page
    next_page = soup.find('li', class_="pager__item pager__item--next")
    if next_page:
        page += 1
        search_page(url + f'&page={str(page)}', page)
    else:
        print('\n\n Finished Searching')


search_page(url, page)
