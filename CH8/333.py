# ValueErroWrite a Python program using beautiful soup to scrape all the news headlines in the div class “top news” from https://indianexpress.com

from bs4 import BeautifulSoup
import requests

req_url="https://indianexpress.com"

response=requests.get(req_url)
response=response.text
soup=BeautifulSoup(response,"html.parser")
box=soup.find("div",class_="top-news")
result=box.find_all("a")
for i in result:
 print(i.text)

