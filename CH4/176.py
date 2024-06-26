# In a customer dataset, you have a column representing customer incomes. You want to categorize incomes into 'Low', 'Medium', and 'High' 
# groups. Incomes below 30000 are 'Low', incomes between 30000 and 70000 are 'Medium', and incomes above 70000 are 'High'. Write a code 
# to achieve this assuming the dataset has a column named 'income'.


import pandas as pd 
import numpy as np


data={"income":[25000,28000,35000,40000,50000,75000,80000]}
df=pd.DataFrame(data)

df['category']=np.where(df.income<30000,'low',np.where(df.income>70000,'high','medium'))
print(df)