# Part-1: (4 marks)
# Write a python code to scrape data from the file ‘imdb.html’, the file contains the list of upcoming movies to be released in India in year 2023 
# and 2024. Scrape the data to get the movie name and year. Create a DataFrame having columns containing movie name and year.
# # Expected Outcome:
# art-2 (5 marks)
# The dataset provided in ‘kc_house_data.csv’ contains house sale prices for King County, which includes Seattle. It includes homes sold 
# between May 2014 and May 2015Perform the following tasks : 
# 1) Load the csv to a dataframe named ‘house_survey’.
# 2) Display the first 5 rows of the dataframe.
# 3) Drop the columns "id" and "Unnamed: 0"
# 4) Check all the null values present in all the columns of the dataframe.
# 5) Fill the missing values of the column 'bedrooms' with the mean of the column.
# 6) Fill the missing values of the column 'bathrooms' with the mean of the column.
# 7) Use the Pandas method corr() to find the feature other than price that is most correlated with price and mention your answer as a 
# comment.
# 8) Fit a linear regression model to predict the 'price' using the list of features:
# ["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15" ,"sqft_above","grade","sqft_living"]
# 9) Consider 30% testing samples and use random state 10.
# 10) Find the Mean Squared Error

from bs4 import BeautifulSoup
import pandas as pd


data=open('top250.html','r',encoding='utf-8')
soup=BeautifulSoup(data,'html.parser')

# print(soup.prettify())
m=soup.find_all("td",class_="titleColumn")
y=soup.find_all("span",class_="secondaryInfo")
movie=[]
year=[]
for i in m:
    movie.append(i.text[16:])
    
for i in y:
    year.append(i.text)


for j in movie:
    print(j)
data={"movie_name":movie,"year":year}

df=pd.DataFrame(data)

print(df)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the csv to a dataframe named 'house_survey'
house_survey = pd.read_csv('kc_house_data.csv')

# Display the first 5 rows of the dataframe
print(house_survey.head())

# Drop the columns "id" and "Unnamed: 0"
house_survey = house_survey.drop(['id', 'Unnamed: 0'], axis=1)

# Check all the null values present in all the columns of the dataframe
print(house_survey.isnull().sum())

# Fill the missing values of the column 'bedrooms' with the mean of the column
house_survey['bedrooms'] = house_survey['bedrooms'].fillna(house_survey['bedrooms'].mean())

# Fill the missing values of the column 'bathrooms' with the mean of the column
house_survey['bathrooms'] = house_survey['bathrooms'].fillna(house_survey['bathrooms'].mean())

# Use the Pandas method corr() to find the feature other than price that is most correlated with price
corr_matrix = house_survey.corr()
print(corr_matrix['price'].sort_values(ascending=False))

# Fit a linear regression model to predict the 'price' using the list of features
X = house_survey[["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15" ,"sqft_above","grade","sqft_living"]]
y = house_survey['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

model = LinearRegression()
model.fit(X_train, y_train)

# Find the Mea n Squared Error
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(mse)