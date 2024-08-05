# Find the table on the page and its rows, Extract the data from each row, and print it url = 
# 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'


from bs4 import BeautifulSoup
import requests

req_url="https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
data=requests.get(req_url)
data=data.text
soup=BeautifulSoup(data,"html.parser")

table = soup.find('table', class_='wikitable')
# Find all the rows in the table
rows = table.find_all('tr')
# Iterate over the rows and extract the data from each row
for row in rows:
 # Find all the cells in the row
 cells = row.find_all('td')
 
 # Extract and print the data from each cell
 for cell in cells:
    print(cell.text.strip(), end='\t')
    print() # Print a new line after each r