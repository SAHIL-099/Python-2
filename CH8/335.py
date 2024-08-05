# Write a program of web scrapping using BeautifulSoup to scrape the given data from the following link.
# https://editorial.rottentomatoes.com/guide/popular-movies/
# On the above link, you’ll find 30 Popular movies. Scrape the Movie Title and Rating of that particular movie and make a Dataframe of the 
# same

from bs4 import BeautifulSoup
import requests
import pandas as pd
req_url="https://editorial.rottentomatoes.com/guide/popular-movies/"
data=requests.get(req_url)
data=data.text
soup=BeautifulSoup(data,"html.parser")
movie_containers = soup.find_all("div", class_="row countdown-item")
# Initialize lists to store movie titles and ratings
titles = []
ratings = []
# Extract the movie titles and ratings from the movie containers
for container in movie_containers:
 title = container.h2.text.strip()
 rating = container.find("span", class_="tMeterScore").text.strip()
 #print(rating)
 titles.append(title)
 ratings.append(rating)
# Create a DataFrame from the extracted data
data = {"Movie Title": titles, "Rating": ratings}
df = pd.DataFrame(data)
# Print the DataFrame
print(df)
