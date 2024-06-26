# Given a real estate price size year dataset, implement multiple linear regression using scikitlearn library. Using the model, make a prediction 
# about an apartment price with size 750 sq.ft. for 2009.Also Calculate R squared, coeficient and intercept. (Don't split data for training/testing


import pandas as pd

df=pd.read_csv('real_estate.csv')
y=df['price']
x=df.drop('price',axis=1)

from sklearn.linear_model import LinearRegression

lr=LinearRegression()
model=lr.fit(x,y)
y_pred=model.predict([[750,2009]])
print("r square:",model.score(x,y))
print("coef:",model.coef_)
print("intercept",model.intercept_)
print("for 750 sq and year 2009",y_pred)