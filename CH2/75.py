# 75 Use the file heights_weights.csv which contains 10000 non-null values for heights and weights. The Male column shows 1 if the person is a 
# Male and 0 if the person is a Female. Take file of dataset from: 
# https://raw.githubusercontent.com/kavit88/Data-Sets/main/heights_weights.csv
#  1. Convert this file into a pandas Data Frame. 
#  2. Display basic information like memory and data types for this data frame. 
#  3. Display basic statistics like mean, std, quartiles, etc. for this data frame. 
#  4. Create a correlation table for the data frame and comment about what kind ofcorrelation is there between Height and Weight.
#  5. Do Height and Weight contain any outliers? Answer by creating boxplots for both.
#  6. Finally, create a scatter plot of Weight v/s Height with the following specifications: 
#  (i) use + sign, colour green and size 50 for markers.
#  (ii) Label X Axis as Weight and Y Axis as Height.
#  (iii) Display title on top as Weight vs Height


import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
df=pd.read_csv("https://raw.githubusercontent.com/kavit88/Data-Sets/main/heights_weights.csv")
print(df.info)
print(df.describe())

hv_corr=df.corr(numeric_only=True)
print(hv_corr)


plt.scatter(df['Weight'], df['Height'], marker='+', color='green', s=50)
plt.title('Weight vs Height')
plt.xlabel('Weight')
plt.ylabel('Height')
plt.show()
