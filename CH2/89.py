# The dataset provided in ‘kc_house_data.csv’ contains house sale prices for King County, which includes Seattle. It includes homes sold 
# between May 2014 and May 2015.
# Perform the following tasks : 
# 1) Load the csv to a dataframe named ‘house_survey’.
# 2) Display the first 5 rows of the dataframe.
# 3) Display the data types of each column.
# 4) Obtain a statistical summary of the dataframe.
# 5) Drop the columns "id" and "Unnamed: 0"
# 6) Check all the null values present in all the columns of the dataframe.
# 7) Replace the missing values of the column 'bedrooms' with the mean of the column.
# 8) Replace the missing values of the column 'bathrooms' with the mean of the column.
# 9) Count the number of houses with unique floor values.
# 10) Using boxplot determine whether houses with a waterfront view or without a waterfront view have more price outliers. (Mention your 
# answer as comment in the next cell)
# 11) Use the function regplot in the seaborn library to determine if the feature sqft_above is negatively or positively correlated with price. 
# (Mention your answer as comment in the next cell).
# 12) Find the feature other than price that is most correlated with price. (Mention your answer as comment in the next cell)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn


# 1) Load the csv to a dataframe named ‘house_survey’.
house_survey = pd.read_csv("files/kc_house_data.csv")
# 2) Display the first 5 rows of the dataframe.
print(house_survey.head())
# 3) Display the data types of each column.
print(house_survey.dtypes)
# 4) Obtain a statistical summary of the dataframe.
print(house_survey.describe())
# 5) Drop the columns "id" and "Unnamed: 0"
print(house_survey.columns)
house_survey.drop(house_survey.columns[0],axis=1,inplace=True)
house_survey.drop(house_survey.columns[0],axis=1,inplace=True)
print(house_survey)
# 6) Check all the null values present in all the columns of the dataframe.
print(house_survey.isnull().sum())
# 7) Replace the missing values of the column 'bedrooms' with the mean of the column.
house_survey.bedrooms.fillna(house_survey.bedrooms.mean(),inplace=True)
# 8) Replace the missing values of the column 'bathrooms' with the mean of the column.
house_survey.bathrooms.fillna(house_survey.bathrooms.mean(),inplace=True)
print(house_survey.isnull().sum())

# 9) Count the number of houses with unique floor values.
print(house_survey.floors.value_counts())
# 10) Using boxplot determine whether houses with a waterfront view or without a waterfront view have more price outliers. (Mention your
# answer as comment in the next cell)
sn.boxplot(x="waterfront",y="price",data=house_survey)
plt.show()
# without
# 11) Use the function regplot in the seaborn library to determine if the feature sqft_above is negatively or positively correlated with price.
# (Mention your answer as comment in the next cell).
sn.regplot(x="sqft_above",y="price",data=house_survey)
plt.show()
# 12) Find the feature other than price that is most correlated with price. (Mention your answer as comment in the next cell)
print(house_survey.corr(numeric_only=True))