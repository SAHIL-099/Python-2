# se the file movies.csv which contains 1629 rows and 18 columns. Read this csv file and display the basic information like memory and data 
# types for this data frame. 
# Write python code for the following cases:
# 1.List out Movies Released in Year 2019.
# 2.How Many Movies are having IMDB RaƟng > 7 (Display Number of Movies).
# 3.List out the Movies with ‘Ɵtle’ and ‘story’ whose IMDB Votes > 20000.
# 4.List out Movies Released in Year 2018, Display only Movie Title with Release Date of Year 2018 Movies.
# 5.Display only Movie Title with its Wikipedia Link

import  pandas as pd

df=pd.read_csv("files/movies.csv")
print(df.info())

# 1.List out Movies Released in Year 2019.
print(df[df["year_of_release"]==2019].title_x)

# 2.How Many Movies are having IMDB RaƟng > 7 (Display Number of Movies).
print(df[df["imdb_rating"]>7].shape[0])

# 3.List out the Movies with ‘title’ and ‘story’ whose IMDB Votes > 20000.

print(df[df["imdb_votes"]>20000][["title_x","story"]])
# 4.List out Movies Released in Year 2018, Display only Movie Title with Release Date of Year 2018 Movies.

print(df[df["year_of_release"]==2018][["title_x","year_of_release"]])

# 5.Display only Movie Title with its Wikipedia Link

print(df[["title_x","wiki_link"]])

