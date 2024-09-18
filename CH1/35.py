# 1. Load the dataset into a pandas DataFrame (data_result.csv) and answer the following questions.
# 2. View the first few rows of the dataset 
# 3. Check the shape of the dataset 
# 4. View the first last rows of the dataset
# 5. Get summary statistics of numerical columns 
# 6. Get summary statistics of numerical columns with 0.58 and 0.87 percentiles 
# 7. Get summary statistics of all types of columns 
# 8. Information of all columns 
# 9. Check for missing values 
# 10. Removing duplicates if duplicates
# 11. List out female students who have greater than 7 spi in all semesters. 
# 12. Find number of students those who have greater than 8 spi in all 5 semesters


import pandas as pd


# 1. Load the dataset into a pandas DataFrame (data_result.csv) and answer the following questions.

df=pd.read_csv("files/data_result.csv")

# 2. View the first few rows of the dataset 
print(df.head())

# 3. Check the shape of the dataset 
print(df.shape)

# 4. View the first last rows of the dataset
print(df.iloc[0])
print(df.iloc[-1])

# 5. Get summary statistics of numerical columns 
print(df.describe(include="number"))

# 6. Get summary statistics of numerical columns with 0.58 and 0.87 percentiles
print(df.describe(percentiles=[0.58,0.87]))

# 7. Get summary statistics of all types of columns 
print(df.describe(include="all"))

# 8. Information of all columns 
print(df.info())

# 9. Check for missing values 
print(df.isna().sum())
# 10. Removing duplicates if duplicates
df=df.drop_duplicates()

# 11. List out female students who have greater than 7 spi in all semesters. 

print(df[(df["1st"] > 7)&(df["2nd"] > 7)&(df["3rd"] > 7)&(df["4th"] > 7)&(df["5th"] > 7)&(df.Gender == "Female")])

# 12. Find number of students those who have greater than 8 spi in all 5 semesters

print(df[(df["1st"] > 8)&(df["2nd"] > 8)&(df["3rd"] > 7)&(df["4th"] > 8)&(df["5th"] > 8)].shape[0])