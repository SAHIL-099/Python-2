# You are given a dataset containing customer reviews of a restaurant. Your task is to create a wordcloud of the most frequent words 
# used in the reviews after removing the stopwords.
# https://raw.githubusercontent.com/kavit88/Data-Sets/main/restaurant_reviews.csv

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

f=open("files/res.csv")
data=f.read()
stop=set(STOPWORDS)
data_wc=WordCloud(background_color='green',stopwords=stop)
data_wc.generate(data)
plt.imshow(data_wc)
plt.show()