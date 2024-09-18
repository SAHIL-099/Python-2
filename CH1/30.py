# Consider the following data:
# data = {
#  "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
#  "B": [50, 40, 40, 30, 50],
#  "C": [True, False, False, False, True]
# }
# Convert this to a Pandas DataFrame and remove duplicate rows from it. Reset index values

import pandas as pd
data = {
 "A": ["TeamA", "TeamB", "TeamB", "TeamC", "TeamA"],
 "B": [50, 40, 40, 30, 50],
 "C": [True, False, False, False, True]
}

df=pd.DataFrame(data)

ds=df.drop_duplicates()
print(ds)

ds=ds.reset_index()
print(ds)