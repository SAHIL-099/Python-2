# 76. The file "sales.csv" contains the monthly sales data for a store over a year. Each row contains the month (in the format "yyyy-mm"), 
# the total sales for that month, and the number of items sold. Create a pandas DataFrame from this data and plot the monthly sales 
# using an area plot. Take the dataset from below:
# https://raw.githubusercontent.com/kavit88/Data-Sets/main/sales.csv

import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset into a DataFrame
url = 'https://raw.githubusercontent.com/kavit88/Data-Sets/main/sales.csv'
df = pd.read_csv(url)
## Convert the month column to datetime format
df['Month'] = pd.to_datetime(df['Month'])
# Plot the monthly sales using an area plot
plt.figure(figsize=(10, 5))
plt.fill_between(df['Month'], df['Total Sales'], color="skyblue", alpha=0.4)
plt.plot(df['Month'], df['Total Sales'], color="Slateblue", alpha=0.6, linewidth=2)
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()