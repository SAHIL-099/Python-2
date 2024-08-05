# # Write a program for web scrapping using BeautifulSoup to scrape the following details from the given link and make a data frame using that 
# # scraped data from
# # the page in a given link.
# # Link: https://www.politifact.com/factchecks
# # You will find 30 news articles with fact checks on this page. You need to scrape the following details from all the articles and store that in a 
# # data frame. Statement of News, Date of News, Source of News


# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# pagesToGet= 3
# upperframe=[] 
# for page in range(1,pagesToGet+1):
#     print('processing page :', page)
#     url = 'https://www.politifact.com/factchecks/?page='+str(page)
#     print(url)
 
#  #an exception might be thrown, so the code should be in a try-except block
#     try:
#  #use the browser to get the url. This is suspicious command that might blow up.
#         page=requests.get(url) # this might throw an exception if something goes wrong.
 
#     except Exception as e: # this describes what to do if an exception is thrown
#         error_type, error_obj, error_info = sys.exc_info()# get the exception information
#         print ('ERROR FOR LINK:',url) #print the link that cause the problem
#         print (error_type, 'Line:', error_info.tb_lineno)#print error info and line that threw the e
#         continue #ignore this page. Abandon this and go back.
 
#     soup=BeautifulSoup(page.text,'html.parser')
#     frame=[]
#     links=soup.find_all('li',attrs={'class':'o-listicle__item'})
#     print(len(links))
#  #filename="NEWS.csv"
#  #f=open(filename,"w", encoding = 'utf-8')
#  #eaders="Statement,Link,Date, Source, Label\n"
#  #f.write(headers)
 
#     for j in links:
#         Statement = j.find("div",attrs={'class':'m-statement__quote'})
#         .text.strip()
#         Link = "https://www.politifact.com"
#         Link += j.find("div",attrs={'class':'m-statement__quote'})
#         .find('a')['href'].strip()
#         Date = j.find('div',attrs={'class':'m-statement__body'})
#         .find('footer').text[-14:-1].strip()
#         Source = j.find('div', attrs={'class':'m-statement__meta'})
#         .find('a').text.strip()
#         Label = j.find('div', attrs ={'class':'m-statement__content'})
#         .find('img',attrs={'class':'c-image__original'})
#         .get('alt').strip()
#         frame.append((Statement,Link,Date,Source,Label))
#  #f.write(Statement.replace(",","^")+","+Link+","+Date.replace(",","^")+","+Source.replace(",
#         upperframe.extend(frame)
# data=pd.DataFrame(upperframe, columns=['Statement','Link','Date','Source','Label'])
# print(data)