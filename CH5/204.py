# Write a program to make a model based on linear regression for the following
# dataframe created from a csv file named “Package.csv” of x and y which follows equaation y = a + bx. Write a program which can predict value of y based on any value of
# x, also write code to find value of a and b in above equation

import pandas as pd
from sklearn.linear_model import LinearRegression

df= pd.read_csv("Placement.csv")
y=df['package']
x=df.drop('package',axis=1)


lr=LinearRegression()
model=lr.fit(x,y)


print("coef:",model.coef_)
print("intercept",model.intercept_)


def fun(val):
    data=pd.DataFrame({"cgpa":[val]})
    return data


ans=fun(6.89)
y_pred=model.predict(ans)

print(y_pred)


