# For the given RealEstate csv, write a python program satisfying following tasks to demonstrate application of machine learning through 
# multiple linear regression as follows – 
# Given: - 
# Dataset RealEstate.csv
# ML Library to be used scikit-learn 
# Dependent variable 'Y house price of unit area'
# Independent variables 'X1 transaction date', 'X2 house age', 'X3 distance to the nearest MRT station', 'X4 number of convenience stores', 'X5 
# latitude' and 'X6 longitude'
# 1. Import required libraries.
# 2. Load RealEstate dataset, create a dataframe and check datatypes of its attributes using appropriate method.
# 3. Remove ‘No’ column from the dataframe.
# 4. Check for any null values in features using appropriate method.
# 5. Create feature variables x and y as given above. 
# 6. Create training and testing sets of feature variables with 70% of data for training and with random state of 110.
# 7. Create and fit regression model using appropriate method.
# 8. Use testing set created in step 6 to find and print the prediction of the outcome.
# 9. Find and print coefficient and mean squared error of the regression model.



# 1. Import required libraries.

import pandas as pd
# 2. Load RealEstate dataset, create a dataframe and check datatypes of its attributes using appropriate method.
df=pd.read_csv("RealEstate.csv")
print(df.dtypes)
# 3. Remove ‘No’ column from the dataframe.
df.drop('No',axis=1,inplace=True)
# 4. Check for any null values in features using appropriate method.
print(df.isnull().sum())
# 5. Create feature variables x and y as given above. 
y=df['Y house price of unit area']
x=df.drop('Y house price of unit area',axis=1)
# 6. Create training and testing sets of feature variables with 70% of data for training and with random state of 110.
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=110)



# 7. Create and fit regression model using appropriate method.
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)

# 8. Use testing set created in step 6 to find and print the prediction of the outcome.
y_pred=model.predict(x_test)
print("prediction",y_pred)
# 9. Find and print coefficient and mean squared error of the regression model
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_pred,y_test)
print(model.coef_)
print("mse",mse)
