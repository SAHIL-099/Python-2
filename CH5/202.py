# Predict salary based on job position of 6.5 using polynomial regression with a degree of 3 and scikit learn library for the given 
# 'Position_Salaries.csv' dataset. (Don't split data for training/testing) 


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Load the dataset
df = pd.read_csv('Position_Salaries.csv')
df.drop('Position', axis=1, inplace=True)

# Extract the features and target variable
y = df['Salary']
x = df[['Level']]

# Create a PolynomialFeatures object with degree 3
poly = PolynomialFeatures(degree=3)

# Transform the features using the PolynomialFeatures object
x_poly = poly.fit_transform(x)

# Create a LinearRegression model
model = LinearRegression()

# Fit the model to the polynomial features and target variable
model.fit(x_poly, y)

# Create a new data point with Level 6.5
new_data = pd.DataFrame({"Level": [6.5]})

# Transform the new data point using the PolynomialFeatures object
new_data_poly = poly.transform(new_data)

# Predict the salary for the new data point
predicted_salary = model.predict(new_data_poly)

print("Predicted salary:", predicted_salary)