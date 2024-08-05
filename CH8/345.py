# Write a Python program to a list of all the h1, h2, h3 tags from the webpage python.org.


from bs4 import BeautifulSoup
import requests

req_url="https://www.python.org/"
data=requests.get(req_url)
data=data.text
soup=BeautifulSoup(data,"html.parser")


h1_tags=soup.find_all('h1')
h2_tags=soup.find_all('h2')
h3_tags=soup.find_all('h3')


for i in h1_tags:
    print(i.text.strip())
    
for i in h2_tags:
    print(i.text.strip())
    
for i in h3_tags:
    print(i.text.strip())
    
        
    