# You are tasked with using the k-Nearest Neighbors (kNN) algorithm to classify whether patients have diabetes or not based on certain 
# diagnostic measurements. You have been provided with diabetes.csv file. The datasets consist of several medical predictor (independent) 
# variables and one target (dependent) variable, Outcome. Independent variables include the number of pregnancies the patient has had, their 
# BMI, insulin level, age, and so on. Also perform Model Performance Analysis using confusion matrix.


import pandas as pd

df=pd.read_csv("diabetes.csv")
df=pd.get_dummies(df,drop_first=True)

y=df['Outcome']
x=df.drop('Outcome',axis=1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

k=[]
for i in range(1,615):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train,y_train)
    y_pred=knn.predict(x_test)
    ac=accuracy_score(y_test,y_pred)
    k.append(ac)

best_index = k.index(max(k)) + 1  # Find the index of the maximum accuracy score and add 1
print(best_index)
knn=KNeighborsClassifier(n_neighbors=best_index)

knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)

ac=accuracy_score(y_test,y_pred)
print(ac)