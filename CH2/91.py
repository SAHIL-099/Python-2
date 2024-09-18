# To upload the ‘diabetes_unclean.csv’ to your working folder
# First import the following libraries
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# 1.Make a data frame with the variable name df 
# 2.To display the specific staƟsƟcs or measures that are relevant for object-type columns
# 3.To display the specific staƟsƟcs or measures that are relevant for numerical-type columns
# 4.How many rows and columns are in a given dataset
# 5.To check the missing values
# 6.To replace the missing values in the column "HbA1c" with their mean value
# 7.Dropping the missing values of other columns
# 8.Display the correlaƟon between variables
# 9. Checking the outliers in the dataset for the following parameters: 'AGE', 'Urea', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI' using box plot 
# with labels and title
# 10.Visualized the "Urea", "HbA1c", "TG" and "BMI" parameters for different ages using parallel_coordinates with labels and Ɵtle
# 11.Remove the rows whose gender column has an “f” value and give the frequency count of the “F” and “M” values in different CLASS values
# 12.Remove the outliers in the "HbA1c" columns and print the shape of the data frame
# Note: all task output with specific question numbers and follow the sequence 
# Example: print(“Ans-1”)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

# 1.Make a data frame with the variable name df 
df=pd.read_csv("files/diabetes_unclean.csv")
# 2.To display the specific statstics or measures that are relevant for object-type columns
print(df.describe(include=['object']))
# 3.To display the specific statstics  or measures that are relevant for numerical-type columns

print(df.describe(include=['number']))

# 4.How many rows and columns are in a given dataset
print(f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.")

# 5.To check the missing values
print(df.isnull().sum())

# 6.To replace the missing values in the column "HbA1c" with their mean value

df.HbA1c.fillna(df.HbA1c.mean(),inplace=True)


# 7.Dropping the missing values of other columns
df = df.dropna(subset=['AGE', 'Urea', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI'])

# 8.Display the correlation between variables
print(df.corr(numeric_only=True))

# 9. Checking the outliers in the dataset for the following parameters: 'AGE', 'Urea', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI' using box plot 
# with labels and title
plt.figure(figsize=(12, 8))
sn.boxplot(data=df[['AGE', 'Urea', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI']])
plt.title('Outliers in the dataset')
plt.xlabel('Parameters')
plt.ylabel('Values')
plt.show()
# 10.Visualized the "Urea", "HbA1c", "TG" and "BMI" parameters for different ages using parallel_coordinates with labels and title

plt.figure(figsize=(12, 8))
pd.plotting.parallel_coordinates(df, 'AGE', cols=['Urea', 'HbA1c', 'TG', 'BMI'])
plt.title('Urea, HbA1c, TG and BMI parameters for different ages')
plt.xlabel('Age')
plt.ylabel('Values')
plt.show()
# 11.Remove the rows whose gender column has an “f” value and give the frequency count of the “F” and “M” values in different CLASS values

# Remove the rows whose gender column has an “f” value
df = df[df['Gender']!= 'f']

# Give the frequency count of the “F” and “M” values in different CLASS values
print(df['Gender'].value_counts())

# 12.Remove the outliers in the "HbA1c" columns and print the shape of the data frame

# Remove the outliers in the "HbA1c" columns
Q1 = df['HbA1c'].quantile(0.25)
Q3 = df['HbA1c'].quantile(0.75)
IQR = Q3 - Q1
df = df[((df['HbA1c'] >= (Q1 - 1.5 * IQR)) &(df['HbA1c'] <= (Q3 + 1.5 * IQR)))]

# Print the shape of the data frame
print(df.shape)