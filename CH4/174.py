# You've been given a dataset with apartment area and price information. There's a noticeable non-linear relationship between area and price.
# To address this you intend to categorize them into 'High', 'Medium', and 'Low' groups. Prices above $3,000,000 are 'High', below $2,000,000
# are 'Low', and between $2,000,000 and $3,000,000 are 'Medium'. Write a code to achieve this assuming that dataset has two columns named
# area and price


import pandas as pd
import numpy as np
data = {
    'area': [500, 750, 1000, 1200, 1500],
    'price': [1500000, 2500000, 3000000, 3500000, 1800000]
}
df = pd.DataFrame(data)

df['category']=np.where(df.price>3000000,'high',np.where(df.price<2000000,'low','medium'))


print(df)