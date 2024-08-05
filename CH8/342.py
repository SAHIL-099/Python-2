# Write a Python program to extract all the URLs from the webpage python.org that are nested within <li> tags from. 

from bs4 import BeautifulSoup
import requests

req_url="https://www.python.org/"
data=requests.get(req_url)
data=data.text
soup=BeautifulSoup(data,"html.parser")
print(soup.prettify())

# Find all <li> tags on the webpage
li_tags = soup.find_all('li')

# Extract URLs from <li> tags
urls = []
for li in li_tags:
    a_tag = li.find('a')
    if a_tag and a_tag.has_attr('href'):
        urls.append(a_tag['href'])

# Print the extracted URLs
for url in urls:
    print(url)