# You are given a text file named "speech.txt" which contains the transcript of a speech. You need to create a Word Cloud for the 
# most frequent words used in the speech.

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
f=open("files/speech.txt")
speech=f.read()
plt.figure(figsize=(20, 5))
speech_wc=WordCloud(background_color='black')
speech_wc.generate(speech)
plt.imshow(speech_wc)
plt.axis('off')
plt.show()