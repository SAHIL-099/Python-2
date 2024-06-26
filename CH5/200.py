# Given a dataset with 'SAT' scores as independent variables and 'GPA' as the dependent variable, calculate R squared, coeficient and intercept 
# using linear regression and scikitlearn library. (Don't split data for training/testing) 

import pandas as pd

df=pd.read_csv('SATGPA.csv')
y=df['GPA']
x=df.drop('GPA',axis=1)

from sklearn.linear_model import LinearRegression

lr=LinearRegression()
model=lr.fit(x,y)
y_pred=model.predict(x)
print("r square:",model.score(x,y))
print("coef:",model.coef_)
print("intercept",model.intercept_)
print("prediction",y_pred)