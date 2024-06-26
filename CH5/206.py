# Write a program to create a Model using linear regression to predict the price of house using the csv file provided named 
# “Housing.csv”. Do the required process in the data before making a model. Find predicted values, co-efficients, intercept and mean 
# squared error.
# https://github.com/pdsinroza/python2/blob/39b36bf2f0121910fd1207952aa0ec20b2d77cfb/housing.csv


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
df=pd.read_csv("HousingData.csv")
df=df.dropna()
# Linear Regression
# Let's use multiple features to predict the housing prices (MEDV)
x= df.drop('MEDV', axis=1)
y = df['MEDV']
# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,
random_state=42)
# Create and train the linear regression model
model = LinearRegression()
model.fit(x_train, y_train)
# Make predictions
y_pred = model.predict(x_test)

mse=mean_squared_error(y_pred,y_test)
r2=r2_score(y_pred,y_test)

print("coef:",model.coef_)
print("intercept",model.intercept_)
print("R-squared:",r2 )
print("mse",mse)
print("predict value:",y_pred)



