# The task involves building a Decision Tree classifier to predict whether to play tennis based on weather conditions. The dataset used for this 
# task is the PlayTennis dataset, which contains information about various weather attributes such as outlook, temperature, humidity, and wind, 
# along with the corresponding decision to play tennis or not. Use PlayTennis.csv for dataset.

import pandas as pd

df=pd.read_csv("PlayTennis.csv")

df.info()
df=pd.get_dummies(df,drop_first=True)
print(df)

y=df['play_yes']
x=df.drop('play_yes',axis=1)

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(criterion='entropy',max_depth=None)
dt.fit(x,y)
y_pred=dt.predict(x)


from sklearn.metrics import accuracy_score,confusion_matrix
cm=confusion_matrix(y,y_pred)
tn=cm[0][0]
fp=cm[0][1]
fn=cm[1][0]
tp=cm[1][1]
acc=((tn+tp)/(tn+tp+fp+fn))
print("acc",acc)

sensi=((tn)/(tn+fp))
print("sensi",sensi)


speci=((tn)/(tn+fp))
print("speci",speci)

print(y_pred)

newdata=pd.DataFrame({"windy":[False],"outlook_rainy":True,"outlook_sunny":[False],"temp_hot":[False],"temp_mild":[True],"humidity_normal":[True]})

pred=dt.predict(newdata)
print(pred[0])


