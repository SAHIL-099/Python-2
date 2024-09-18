#71
# Create a boxplot of the distribution of temperatures in different cities. Take data from 'temperatures.csv' from below:
# https://raw.githubusercontent.com/kavit88/Data-Sets/main/temperatures.csv


import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

data=pd.read_csv("https://raw.githubusercontent.com/kavit88/Data-Sets/main/temperatures.csv")

sn.boxplot(data)
plt.show()