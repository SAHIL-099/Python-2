# Consider variables x and y created from a pandas dataframe “car.csv” .
# Create new column named “Age_car” (Age_car=2023-year)
#  For multiple linear regression problem, x contains the independent variables ( Age_car , Driven_kms , Fuel_Type , Selling_type , Transmission ) 
# and y contains the dependent (Selling_Price) variable which is to be predicted.
#  Write a Python program to spilt x and y into training and testing datasets with a 20% split. Then create a multiple linear regression model 
# using the training data and print its coefficients ,intercept and mean squared error.


import pandas as pd

df=pd.read_csv("car.csv")
df['Age_car']=2023-df['Year']

y=df['Selling_Price']
x=df[['Age_car', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission']]

x=pd.get_dummies(x,drop_first=True)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


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