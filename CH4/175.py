# In a survey dataset, you have a column representing participants' ages. You want to categorize ages into 'Young', 'Middle-aged', and 'Elderly' 
# groups. Ages below 30 are 'Young', ages between 30 and 60 are 'Middle-aged', and ages above 60 are 'Elderly'. Write a code to achieve this 
# assuming the dataset has a column named 'age'

import pandas as pd 
import numpy as np  


data={"age":[25,35,45,55,65,75,85]}

df=pd.DataFrame(data)

df['age_group']=np.where(df.age<30,'Young',np.where(df.age>60,'Elderly','Middle-aged'))

print(df)