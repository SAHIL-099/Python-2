# How to get the Daily News using Python. url='https://www.bbc.com/news'


# import requests
# from bs4 import BeautifulSoup
 
# url = 'https://www.bbc.com/news'
# response = requests.get(url)
 
# soup = BeautifulSoup(response.text, 'html.parser')
# headlines = soup.find('body').find_all('h3')
# for x in headlines:
#  print(x.text.strip())





from bs4 import BeautifulSoup
import requests
# Creates a header
headers = {'User-agent': 'Mozilla/5.0'}
# Requests the webpage
request = requests.get('https://www.bbc.com/news', headers=headers)
html = request.content
# Create some soup
soup = BeautifulSoup(html, 'html.parser')
# Used to easily read the HTML that we scraped
# print(soup.prettify())
def bbc_news_scraper(keyword):
 news_list = []
 # Finds all the headers in BBC Home
 for h in soup.findAll('h3', class_='gs-c-promo-heading__title'):
    news_title = h.contents[0].lower()
    if news_title not in news_list:
        if 'bbc' not in news_title:
            news_list.append(news_title)
 no_of_news = 0
 keyword_list = []
 # Goes through the list and searches for the keyword
 for i, title in enumerate(news_list):
    text = ''
    if keyword.lower() in title:
        text = ' <------------ KEYWORD'
        no_of_news += 1
        keyword_list.append(title)
    print(i + 1, ':', title, text)
 # Prints the Titles of the articles that contain the keywords
 print(f'\n--------- Total mentions of "{keyword}" = {no_of_news} ---------')
 for i, title in enumerate(keyword_list):
    print(i + 1, ':', title)
    
bbc_news_scraper("daily-news")

