#  Write Python code to remove outliers from any given DataFrame.
import pandas as pd
import numpy as np
data = {'Name': ['William', 'Emma', 'Sofia', 'Markus',
'Edward','Thomas','Ethan',np.nan,'Arun','Anika','Paulo'],
'Region': [np.nan,'North','East',np.nan,'West',
'West', 'South',np.nan,'West','East', 'South'],
'Sales': [50000.0, 52000.0, np.nan,np.nan,42000.0,
72000.0,49000.0,np.nan,67000.0,65000.0,67000.0],
'Expenses': [42000.0, 43000.0,np.nan,np.nan, 38000.0,
390000.0,42000.0,np.nan,39000.0,50000.0,45000.0]}
# Create the DataFrame
df = pd.DataFrame(data)
print(df.shape)
def remove_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
# Remove outliers from column Sales using the remove_outliers function
df_no_outliers = remove_outliers(df, 'Sales')
print(df_no_outliers.shape)

print(df_no_outliers)