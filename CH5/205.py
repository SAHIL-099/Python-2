# Write a program to make a model based on linear regression for the following dataframe
#  created from a csv file named “data.csv” of x1 and y which follows equation y = a+bx1. Write a program which can predict value of y based on 
# any value of x, also write code to find value of a and b in above equation. Given Data in csv file:

import pandas as pd
from sklearn.linear_model import LinearRegression

import pandas as pd
import numpy as np
data={"x1":[60,62,67,70,71,72,75,78],
"y":[140,155,159,179,192,200,212,215]}
df=pd.DataFrame(data)
x=df[["x1"]]
y=df["y"]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("coef:",model.coef_)
print("intercept",model.intercept_)

from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test, y_pred))



