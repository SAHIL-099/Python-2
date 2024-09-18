# Use the file data.csv which contains 169 rows and 4 columns. 
# 1. Convert this file into pandas Data Frame and Display basic statistics like mean, std, quartiles, etc. for this data frame.
# 2. Create a correlation table for the data frame and comment about what kind of correlation is there between Duration and Calories?
# 3. Find whether there any null or NA values, drop all such rows if found in the data frame and print the shape of the data frame after dropping. 
# 4. Prepare a scatter matrix for the following data frame and prepare a parallel coordinates for Duration v/s Pulse, Maxpulse and Calories (all 3 
# other columns). 
# 5. Do Maxpulse have any outliers? Find using function. 
# 6. Show the outliers using box plot for Maxpulse, width of box plot should be 0.75 and notch should be True.
# 7. Create a scatter plot for Duration (x-axis) and then Pulse, Maxpulse and Calories (y-axis) with different colors. For each there should be 
# different color and marker.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

# 1. Convert this file into pandas Data Frame and Display basic statistics like mean, std, quartiles, etc. for this data frame.
df=pd.read_csv("files/data.csv")
print(df.info())

# 2. Create a correlation table for the data frame and comment about what kind of correlation is there between Duration and Calories?
cr=df.corr(numeric_only=True)
print(cr)
dc=cr.loc['Duration','Calories']
if(dc>0):
    print("postive corr")
elif(dc<0):
    print("negative corr")
else:
    print("no corr")
# 3. Find whether there any null or NA values, drop all such rows if found in the data frame and print the shape of the data frame after dropping. 
print(df.isna().sum())
df.dropna(inplace=True)
print("5 in calories in case of data loss")
print(df.isna().sum())

# 4. Prepare a scatter matrix for the following data frame and prepare a parallel coordinates for Duration v/s Pulse, Maxpulse and Calories (all 3 
# other columns). 

pd.plotting.scatter_matrix(df)
pd.plotting.parallel_coordinates(df,"Duration",cols=["Pulse","Maxpulse","Calories"])
plt.show()
# 5. Do Maxpulse have any outliers? Find using function.

def findOutliers(data):
    Q1= data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    series = data[(data<lower) |(data>upper)]
    return series

s = findOutliers(df.Maxpulse)
print(s) 

# 6. Show the outliers using box plot for Maxpulse, width of box plot should be 0.75 and notch should be True.
sn.boxplot(df.Maxpulse,notch=True,width=0.75)
plt.show()
# 7. Create a scatter plot for Duration (x-axis) and then Pulse, Maxpulse and Calories (y-axis) with different colors. For each there should be 
# different color and marker.

plt.scatter(df['Duration'], df['Pulse'], color='blue', marker='*', label='Pulse')
plt.scatter(df['Duration'], df['Maxpulse'], color='red', marker='H', label='Maxpulse')
plt.scatter(df['Duration'], df['Calories'], color='green', marker='s', label='Calories')
plt.xlabel('Duration')
plt.ylabel('Values')
plt.title('Scatter Plot of Duration vs Pulse, Maxpulse, and Calories')
plt.legend()
plt.show()
