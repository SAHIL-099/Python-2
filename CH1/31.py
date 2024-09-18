# Consider the following autompg dataset:
# https://raw.githubusercontent.com/Jovita7/Data-Analysis-and-Visualization/main/auto-mpg.csv
# Write Python code to convert it to a DataFrame and remove mpg and cylinders columns from it

import pandas as pd

data=pd.read_csv("files/auto-mpg.csv")

df=pd.DataFrame(data)
print(df.info())
df=df.drop(columns=['mpg','cylinders'])
print(df)