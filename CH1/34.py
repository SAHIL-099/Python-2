#  Use the file spotify.csv 
# 1.Convert this file into a pandas Data Frame. (0.5 marks)
# 2.Display basic informaƟon like memory and data types for this data frame. 
# (0.5 marks)
# 3.Display basic staƟsƟcs like mean, std, quarƟles, etc. for this data frame. 
# (0.5 marks)
# 4.Create a correlaƟon table for the data frame and comment about what kind of correlaƟon is there between danceability and energy (0.5 
# marks)
# 5.Display first five rows for this data frame.(0.5 marks)
# 6.Display last five rows for this data frame. (0.5 marks)
# 7.Display the rows between 15 to 39 for this data frame. (0.5 marks)
# 8.Display the data only for last five rows and last five columns for this data frame. (0.5 marks)
# 9.Display the shape for this data frame. (0.5 marks)
# 10.Display the sum of NULL values for all the columns. (0.5 marks)
# 11.Remove first 3 columns from this Data Frame. (0.5 marks)
# 12.Remove first 10 rows from this Data Frame. (0.5 marks)
# 13..After  removing first 3 columns and first 10 rows from this data frame find outliers for the column popularity. (1 marks)
# 14..After  removing first 3 columns and first 10 rows from this data frame remove outliers for the column energy then display the data frame. 
# (1 marks)
# 15.Display cross tabulaƟon between time_signature and track_genre for actual Data Frame. (1 marks)

import pandas as pd

# 1.Convert this file into a pandas Data Frame. (0.5 marks)
data=pd.read_csv("files/spotify.csv")
df=pd.DataFrame(data)

# 2.Display basic informaƟon like memory and data types for this data frame. 
# # (0.5 marks)

print(df.info())


# 3.Display basic staƟsƟcs like mean, std, quarƟles, etc. for this data frame. 
# # (0.5 marks)
print(df.describe())

# 4.Create a correlaƟon table for the data frame and comment about what kind of correlaƟon is there between danceability and energy

data_corr=df.corr(numeric_only=True)
print(data_corr)
dance_enerygy=data_corr.loc['danceability','energy']

if(dance_enerygy>0):
    print("postive correlation")
elif(dance_enerygy<0):
    print("negarive corr")
    
else:
    print("no correlation")
    
# 5.Display first five rows for this data frame.(0.5 marks)

print(df.head())

# # 6.Display last five rows for this data frame. (0.5 marks)

print(df.tail())

# # 7.Display the rows between 15 to 39 for this data frame. (0.5 marks)
print(df.iloc[15:39])
# print(df[(df.index>15)& (df.index <39)])

# 8.Display the data only for last five rows and last five columns for this data frame. (0.5 marks)
print(df.tail().iloc[:,-5:])

# 9.Display the shape for this data frame. (0.5 marks)

print(df.shape)

# 10.Display the sum of NULL values for all the columns. (0.5 marks)

print(df.isna().sum())

# 11.Remove first 3 columns from this Data Frame. (0.5 marks)
df = df.drop(df.columns[:3], axis=1)

# 12.Remove first 10 rows from this Data Frame. (0.5 marks)

print(df.drop(df.index[:10]))

# 13.After removing first 3 columns and first 10 rows from this data frame find outliers for the column popularity. (1 marks)
# 14..After  removing first 3 columns and first 10 rows from this data frame remove outliers for the column energy then display the data frame. 
# (1 marks)
# 15.Display cross tabulaƟon between time_signature and track_genre for actual Data Frame. (1 marks)
pd.crosstab(df['time_signature'],df["track_genre"])
