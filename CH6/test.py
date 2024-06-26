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

print(y_pred)

newdata=pd.DataFrame({"outlook_rainy":[True],"outlook_sunny":[False],"outlook_overcast":[False],"temp_hot":[False],"temp_mild":[True],"temp_cool":[False],"humidity_high":[False],"humidity_normal":[True],"windy":[False]})

pred=dt.predict(newdata)
print(pred)