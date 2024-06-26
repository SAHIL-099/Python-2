# The objective is to perform classification on the Iris dataset using the k-Nearest Neighbors (kNN) algorithm. The Iris dataset contains 
# measurements of various iris flowers, including features such as sepal length, sepal width, petal length, and petal width, along with the 
# corresponding species label. The problem involves two main tasks:
# Build a kNN classification model to predict the species of iris flowers based on their feature measurements.
# Train the model on a portion of the dataset and evaluate its performance on another portion to assess its accuracy.
# Experiment with different values of k and choose the optimal value that maximizes the model's performance.
# Use appropriate evaluation confusion matrix to evaluate the model's performance. Also calcualte accuracy, sensitivity and specificity.
# Use iris.csv file for dataset


import pandas as pd

df=pd.read_csv("iris.csv")
df.drop('Id',axis=1,inplace=True)
df=pd.get_dummies(df,drop_first=True)

y=df['Species_Iris-versicolor']
x=df.drop('Species_Iris-versicolor',axis=1)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

k=[]
for i in range(1,80):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train,y_train)
    y_pred=knn.predict(x_test)
    ac=accuracy_score(y_test,y_pred)
    k.append(ac)
    
    
best = k.count(1)  
print(best)

knn=KNeighborsClassifier(n_neighbors=best)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)

cm=confusion_matrix(y_test,y_pred)
tp=cm[0][0]
fp=cm[0][1]
fn=cm[1][0]
tn=cm[1][1]
ac=accuracy_score(y_test,y_pred)
print("accuracy",ac)

sensi=(tp)/(tp+fn)
speci=(tn)/(tn+fp)

print("sensitivity:",sensi)
print("specificity:",speci)



    

    

