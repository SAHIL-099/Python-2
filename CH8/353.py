# Find all the citation needed tags on the page.url = 'https://en.wikipedia.org/wiki/Python_(programming_language)' using Beautiful soup.

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

citation_needed_tags = soup.find_all('span', string='citation needed')

for tag in citation_needed_tags:
    print(tag.find_parent('p').text)