# # 74.You have been given a dataset of house prices and their respective lot size and square footage. Your task is to create a scatter plot 
# to determine if there is any correlation between these variables.
#  Dataset:
#  The dataset, named "house_data.csv":
# https://raw.githubusercontent.com/kavit88/Data-Sets/main/house_data.csv

import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset into a DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/kavit88/Data-Sets/main/house_data.csv')
# Create scatter plots
# Scatter plot between HousePrice and LotSize
plt.subplot(1, 2, 1)
plt.scatter(df['LotSize'], df['Price'], color='blue', alpha=0.5)
plt.title('HousePrice vs LotSize')
plt.xlabel('LotSize')
plt.ylabel('HousePrice')
# Scatter plot between HousePrice and SquareFootage
plt.subplot(1, 2, 2)
plt.scatter(df['SqFt'], df['Price'], color='green', alpha=0.5)
plt.title('HousePrice vs SquareFootage')
plt.xlabel('SquareFootage')
plt.ylabel('HousePrice')
plt.tight_layout()
plt.show()