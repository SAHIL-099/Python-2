# For x = np.array([5, 15, 25, 35, 45, 55]) and y = np.array([5, 20, 14, 32, 22, 38]), apply simple linear regression using scikit learn library and 
# calculate calculate R squared, coeficient and intercept. Predict the y values for x = np.arange(5). (Don't split data for training/testing)

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
x = np.array([5, 15, 25, 35, 45, 55]).reshape(-1, 1)
y = np.array([5, 20, 14, 32, 22, 38])

model = LinearRegression()
model.fit(x, y)

x_pred = np.arange(5).reshape(-1, 1)
y_pred = model.predict(x_pred)

print("r square:",model.score(x,y))
print("coef:",model.coef_)
print("intercept",model.intercept_)
print(y_pred)