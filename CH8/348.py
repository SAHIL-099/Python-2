# Find the title of the webpage. url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

from bs4 import BeautifulSoup
import requests

req_url="https://en.wikipedia.org/wiki/Python_(programming_language)"
data=requests.get(req_url)
data=data.text
soup=BeautifulSoup(data,"html.parser")
title=soup.find("title")
print(title.text)