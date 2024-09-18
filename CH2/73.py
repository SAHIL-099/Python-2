# 73. You have been given a dataset of car prices and their respective horsepower, mileage, and weight. You have been tasked to 
# analyze the relationship between these variables and create a scatter plot to visualize the patterns.
#  Dataset:
#  The dataset, named "car_data.csv" : 
# https://raw.githubusercontent.com/kavit88/Data-Sets/main/car_data.csv

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("https://raw.githubusercontent.com/kavit88/Data-Sets/main/car_data.csv")

# Create scatter plots
plt.figure(figsize=(15, 5))
# Scatter plot between CarPrice and Horsepower
plt.subplot(1, 3, 1)
plt.scatter(df['Horsepower'], df['Price'], color='blue', alpha=0.5)
plt.title('CarPrice vs Horsepower')
plt.xlabel('Horsepower')
plt.ylabel('CarPrice')
# Scatter plot between CarPrice and Mileage
plt.subplot(1, 3, 2)
plt.scatter(df['Mileage'], df['Price'], color='green', alpha=0.5)
plt.title('CarPrice vs Mileage')
plt.xlabel('Mileage')
plt.ylabel('CarPrice')
# Scatter plot between CarPrice and Weight
plt.subplot(1, 3, 3)
plt.scatter(df['Weight'], df['Price'], color='red', alpha=0.5)
plt.title('CarPrice vs Weight')
plt.xlabel('Weight')
plt.ylabel('CarPrice')
plt.tight_layout()
plt.show()

