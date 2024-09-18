# Use the file heights_weights.csv (https://raw.githubusercontent.com/Jovita7/Data-Analysis-and-Visualization/main/heights_weights.csv) 
# which contains 10000 non-null values for heights and weights. The Male column shows 1 if the person is a Male and 0 if the person is a Female. 
# 1. Convert this file into a pandas Data Frame. (0.5 marks)
# 2. Display basic information like memory and data types for this data frame. (0.5 marks)
# 3. Display basic statistics like mean, std, quartiles, etc. for this data frame. (0.5 marks)
# 4. Create a correlation table for the data frame and comment about what kind of correlation is there between Height and Weight. (0.5 
# marks)
# 5. Do Height and Weight contain any outliers? (1 mark)

import pandas as pd

url = 'https://raw.githubusercontent.com/Jovita7/Data-Analysis-and-Visualization/main/heights_weights.csv'

df = pd.read_csv(url)

# Display basic information about the DataFrame
print("\nBasic Information:")
print(df.info())

# Display basic statistics for the DataFrame
print("\nBasic Statistics:")
print(df.describe())

# Create a correlation table
correlation_matrix = df.corr()
# Display the correlation table
print("\nCorrelation Table:")
print(correlation_matrix)


# Comment about the correlation between Height and Weight
height_weight_corr = correlation_matrix.loc['Height', 'Weight']
print(f"\nCorrelation between Height and Weight: {height_weight_corr}")
if height_weight_corr > 0:
    print("There is a positive correlation between Height and Weight.")
elif height_weight_corr < 0:
    print("There is a negative correlation between Height and Weight.")
else:
    print("There is no correlation between Height and Weight.")
    
    
    
 # Function to detect outliers using the IQR method
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers
# Detect outliers in Height
height_outliers = detect_outliers(df, 'Height')
print(f"\nNumber of outliers in Height: {len(height_outliers)}")
# Detect outliers in Weight
weight_outliers = detect_outliers(df, 'Weight')
print(f"Number of outliers in Weight: {len(weight_outliers)}")
# Display some of the outliers if they exist
if not height_outliers.empty:
    print("\nOutliers in Height:")
    print(height_outliers.head())
if not weight_outliers.empty:
    print("\nOutliers in Weight:")
    print(weight_outliers.head())      

