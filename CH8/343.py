# Write a Python program to find all the h2 tags and list the first four from the webpage python.org.

from bs4 import BeautifulSoup
import requests

req_url="https://www.python.org/"
data=requests.get(req_url)
data=data.text
soup=BeautifulSoup(data,"html.parser")

h2_tag=soup.find_all("h2")
c=0
for i in h2_tag:
    if(c==4):
        break
    print(i.text)
    c=c+1

