# Create a Pandas DataFrame from the following table and write code to drop all columns containing NaN

import pandas as pd
import numpy as np
data = [
["wilim",np.nan,50000.0,4200.0],
["Emma", "North", 50000.0, 43000],
["Sofia", "East", np.nan, np.nan],
["Marku", np.nan, np.nan, np.nan],
["Edward", "West", 49.0, 42.0],
["Thomas", "South", 72000.0,39000.0],
[ np.nan, np.nan, np.nan, np.nan],
["Arun", "West", 67000.0, 39000.0],
["Anika", "East", 65000.0, 45000.0],
["Paulo", "South", 67000.0,45000.0]]    

df=pd.DataFrame(data)
df=df.dropna(how='any',axis=1)
print(df)