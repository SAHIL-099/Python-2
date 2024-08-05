# Find the first paragraph on the page and print its text. url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'


from bs4 import BeautifulSoup
import requests

req_url="https://en.wikipedia.org/wiki/Python_(programming_language)"
data=requests.get(req_url)
data=data.text
soup=BeautifulSoup(data,"html.parser")
p_tag=soup.find('p')
print(p_tag.text.strip())