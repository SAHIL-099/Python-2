# Find all the links on the page and print their URLs. url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'


from bs4 import BeautifulSoup
import requests

req_url="https://en.wikipedia.org/wiki/Python_(programming_language)"
data=requests.get(req_url)
data=data.text
soup=BeautifulSoup(data,"html.parser")
a_tags=soup.find_all('a')
link=[]
for i in a_tags:
    if i and i.has_attr('href'):
        link.append(i['href'])
        
for i in link:
    print(i)
    
        