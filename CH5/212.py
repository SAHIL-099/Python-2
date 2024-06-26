# Write a program to create a Model using linear regression to predict the wine quality using the csv file provided named “winequality.csv”. Do 
# the required process in the data before making a model. 
# If you find any null value in “winequality.csv” then replace null value with mean value of respected columns.
# Find co-efficient, intercept and mean squared error.
# also Predict the quality of red wine for the following data: 
# fixed acidity: 8 
# volaƟle acidity: 0.4 
# citric acid: 0.40 
# residual sugar: 15 
# chlorides: 0.048 
# free sulfur dioxide: 40 
# total sulfur dioxide: 150 
# density: 0.99 
# pH: 3 
# sulphates: 0.45 
# alcohol: 10.5

import pandas as pd
df = pd.read_csv("winequality.csv")
df.drop('Id',axis=1,inplace=True)
y = df['quality']
x= df.drop('quality',axis=1) 


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)


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


new_data = pd.DataFrame({
'fixed acidity': [8],
'volatile acidity': [0.4],
'citric acid': [0.40],
'residual sugar': [15],
'chlorides': [0.048],
'free sulfur dioxide': [40],
'total sulfur dioxide': [150],
'density': [0.99],
'pH': [3],
'sulphates': [0.45],
'alcohol': [10.5]
})
predicted_red_wine_quality = model.predict(new_data)
print("Predicted quality of red wine:", predicted_red_wine_quality)