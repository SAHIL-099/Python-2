# For the given dataset – iris.csv, perform following exploratory data analysis using python - 
# Use comment feature to answer appropriate questions – 
# a) Load dataset into jupyter notebook using appropriate libraries. Check the datatypes of the dataset attributes. Does the data contain any 
# missing /null values?
# b) Extract head and tail of the dataset using appropriate methods.
# c) Summarize statistical figures (i.e. mean, median, percentiles) in one table using appropriate method.
# d) Create correlation table of all variables. What can you infer about relation between petal length and sepal length?
# e) Create parallel coordinate plot of iris dataset. What can you infer about petal length and petal width?
# f) Create box plot of sepal width. Visualizing the plot, answer whether the sepal width data contains any outliers.
# g) Create cross tabulation of sepal length and petal width attributes. What does the table represent?
# h) Create scatter matrix of the dataset.
# i) Create a new column called ‘SepalLengthSize’ which contains “High” if sepal length ≥ 5 or “Low” if sepal length < 5.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv("files/iris.csv")
print(df.dtypes)
print(df.isna().sum())
# b) Extract head and tail of the dataset using appropriate methods.
print(df.head())
print(df.tail())
# c) Summarize statistical figures (i.e. mean, median, percentiles) in one table using appropriate method.
print(df.describe)
# d) Create correlation table of all variables. What can you infer about relation between petal length and sepal length?
print(df.corr(numeric_only=True))
# e) Create parallel coordinate plot of iris dataset. What can you infer about petal length and petal width?
pd.plotting.parallel_coordinates(df,"Species",cols=["PetalWidthCm","PetalLengthCm"])
plt.show()
# f) Create box plot of sepal width. Visualizing the plot, answer whether the sepal width data contains any outliers.
sn.boxplot(data=df.SepalWidthCm)
# g) Create cross tabulation of sepal length and petal width attributes. What does the table represent?
print(pd.crosstab(df.SepalLengthCm,df.PetalWidthCm))
# h) Create scatter matrix of the dataset.
pd.plotting.scatter_matrix(df,figsize=(20,20))
plt.show()
# i) Create a new column called ‘SepalLengthSize’ which contains “High” if sepal length ≥ 5 or “Low” if sepal length < 5.
df["SepalLengthSize"] = ["High" if length >= 5 else "Low" for length in df['SepalLengthCm']]
df