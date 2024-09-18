# Using ‘supermarket_sales.csv’ file do the following operations and give required answer by using proper programming process.
# 1). Load the dataset into a pandas DataFrame and read first 8 rows.
# 2). Check for missing values and fill it by mean values of that particular column if any.
# 3). Find the number of orders which have ‘Quantity’ less than 3 and which have (either ‘Rating’ greater than 8.5 or ‘Total’ greater than 600).
# 4). Find the sum of ‘Total’ purchasing price spent by Member and Normal 'Customer type'.
# 5). Find the percentage of total of ‘gross income’ based on the different ‘Payment’ methods used by customers. (Ewallet, Cash and Credit card)
# 6). Analyze the purchasing behavior of male and female customers using ‘Gender’ column. Find their average purchase prices using ‘Total’ 
# column.
# 7). Create a scatter plot that shows the relationship between total amount spent and rating. (keep ‘+’ marker, with marker size 100 and green 
# color).
# 8). Create a box plot that shows the distribution of ‘Rating’ and ‘Quantity’. And comment about outliers in both columns.
# 9). Visualize with parallel co-ordinates for ‘Unit price’, ‘Total’, ’cogs’ columns’ data with respect to ‘Product line’.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import parallel_coordinates
# 1). Load the dataset into a pandas DataFrame and read first 8 rows.
df=pd.read_csv("files/supermarket_sales.csv")
print(df.head(8))
# 2). Check for missing values and fill it by mean values of that particular column if any.

print(df.isna().sum())
df["cogs"].fillna(df["cogs"].mean(), inplace=True)
df["Rating"].fillna(df["Rating"].mean(), inplace=True)
print(df.isna().sum())

# 3). Find the number of orders which have ‘Quantity’ less than 3 and which have (either ‘Rating’ greater than 8.5 or ‘Total’ greater than 600).
print(df[(df.Quantity < 3) & ((df.Rating > 8.5) | (df.Total)>600)].shape[0])

# 4). Find the sum of ‘Total’ purchasing price spent by Member and Normal 'Customer type'.
print(df[(df["Customer type"] == "Member")]["Total"].sum())
print(df[(df["Customer type"] == "Normal")]["Total"].sum())

# 5). Find the percentage of total of ‘gross income’ based on the different ‘Payment’ methods used by customers. (Ewallet, Cash and Credit card)

payment_counts = df['Payment'].value_counts()
print(payment_counts)
total_income = df['gross income'].sum()
percentage_income_by_payment = (payment_counts / len(df)) * 100
print("Percentage of total gross income by Payment method:")
print(percentage_income_by_payment)

# 6). Analyze the purchasing behavior of male and female customers using ‘Gender’ column. Find their average purchase prices using ‘Total’ 
# column.
print(df[df.Gender == "Male"].Total.mean())
print(df[df.Gender == "Female"].Total.mean())

# 7). Create a scatter plot that shows the relationship between total amount spent and rating. (keep ‘+’ marker, with marker size 100 and green 
# color).

plt.scatter(df.Rating,df.Quantity,marker="+",color="green",s=100)
plt.show()
# 8). Create a box plot that shows the distribution of ‘Rating’ and ‘Quantity’. And comment about outliers in both columns.

sns.boxplot(x='Rating',y='Quantity',data=df)

# 9). Visualize with parallel co-ordinates for ‘Unit price’, ‘Total’, ’cogs’ columns’ data with respect to ‘Product line’.

parallel_coordinates(df,"Product line",cols=["Unit price","Total","cogs"])
plt.show()