# For x = np.arange(0, 30) and y = np.array([3, 4, 5, 7, 10, 8, 9, 10, 10, 23, 27, 44, 50, 63, 67, 60, 62, 70, 75, 88, 81, 87, 95, 100, 108, 135, 151, 160, 
# 169, 179]), apply polynomial regression using scikit learn library and calculate R squared, coeficient and intercept. Predict the y values for x = 
# np.arange(5). (Don't split data for training/testing)

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


# Define the data
x = np.arange(0, 30)
y = np.array([3, 4, 5, 7, 10, 8, 9, 10, 10, 23, 27, 44, 50, 63, 67, 60, 62, 70, 75, 88, 81, 87, 95, 100, 108, 135, 151, 160, 169, 179])

# Create a polynomial feature matrix
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(x.reshape(-1, 1))

# Perform linear regression on the polynomial features
model = LinearRegression()
model.fit(X_poly, y)

print("r square:",model.score(X_poly,y))
print("coef:",model.coef_)
print("intercept",model.intercept_)

# Predict y values for x = np.arange(5)
x_pred = np.arange(5)
X_poly_pred = poly.transform(x_pred.reshape(-1, 1))
y_pred = model.predict(X_poly_pred)
print(f"Predicted y values: {y_pred}")

