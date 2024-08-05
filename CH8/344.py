# Find all the link tags and list the first ten from the webpage python.org

from bs4 import BeautifulSoup
import requests

req_url="https://www.python.org/"
data=requests.get(req_url)
data=data.text
soup=BeautifulSoup(data,"html.parser")


# Find all <a> tags on the webpage
a_tags = soup.find_all('a')


ten= []
for i in a_tags:
    if i and i.has_attr('href'):
        ten.append(i['href'])


c=0
for i in ten:
    if(c==10):
        break
    print(i)
    c=c+1
   
    
    
        
    