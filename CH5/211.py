# Write a program to create a Model using linear regression to predict the charges of insurance using the csv file provided named 
# “insurance.csv”. Do the required process in the data before making a model. Find predicted values, co-efficients, intercept and mean squared 
# error


import pandas as pd

df=pd.read_csv("insurance.csv")
df.drop(columns=['children','region'])
df = pd.get_dummies(df, drop_first=True)
y=df['expenses']
x=df.drop('expenses',axis=1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)


from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

from sklearn.metrics import mean_squared_error

mse=mean_squared_error(y_pred,y_test)

print("coef:",model.coef_)
print("intercept",model.intercept_)
print("mse",mse)
print("predict value:",y_pred)