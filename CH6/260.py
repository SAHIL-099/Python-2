# Given the Breast Cancer Wisconsin (Diagnostic) dataset, the objective is to build a kNN classification model that accurately predicts whether a 
# tumor is benign or malignant based on the diagnostic features provided. The model should be trained on a portion of the dataset and 
# evaluated on another portion to assess its performance. The ultimate goal is to create a reliable classifier that can assist healthcare 
# professionals in diagnosing breast cancer accurately and early. Use cancer.csv file for dataset.


import pandas as pd

df=pd.read_csv("cancer.csv")
df.drop('Unnamed: 32',axis=1,inplace=True)
df=pd.get_dummies(df,drop_first=True)
print(df.info())
y=df['diagnosis_M']
x=df.drop('diagnosis_M',axis=1)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix


knn=KNeighborsClassifier(n_neighbors=5)
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



    

    

