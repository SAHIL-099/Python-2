# Predict salary based on job position of 6.5 using polynomial regression with a degree of 3 and scikit learn library for the given 
# 'Position_Salaries.csv' dataset. (Don't split data for training/testing) 


import pandas as pd

df = pd.read_csv('Position_Salaries.csv')
df.drop('Position', axis=1, inplace=True)
y = df['Salary']
x = df[['Level']]

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)
job_position_poly = poly.transform([[6.5]])

lr = LinearRegression()
model = lr.fit(x_poly, y)
predicted_salary = model.predict(job_position_poly)

print("salary", predicted_salary)