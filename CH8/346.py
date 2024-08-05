# Write a Python program to extract all the text from a given web page python.org.


from bs4 import BeautifulSoup
import requests

req_url="https://www.python.org/"
data=requests.get(req_url)
data=data.text
soup=BeautifulSoup(data,"html.parser")

page_text=soup.get_text()
print(page_text.strip())