# Find all the headings on the page and print their text. url = 'https://en.wikipedia.org/wiki/Python_(programming_language)


from bs4 import BeautifulSoup
import requests

req_url="https://en.wikipedia.org/wiki/Python_(programming_language)"
data=requests.get(req_url)
data=data.text
soup=BeautifulSoup(data,"html.parser")

heading_tag=soup.find_all(['h1','h2','h3','h4','h5','h6'])

for i in heading_tag:
    print(i.text.strip())