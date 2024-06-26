# imagine that you are a medical researcher compiling data for a study. You have collected data about a set of patients, all of whom suffered 
# from the same illness. During their course of treatment, each patient responded to one of 5 medications, Drug A, Drug B, Drug c, Drug x and y.
# Part of your job is to build a model to find out which drug might be appropriate for a future patient with the same illness. The feature sets of 
# this dataset are Age, Sex, Blood Pressure, and Cholesterol of patients, and the target is the drug that each patient responded to.
# It is a sample of multiclass classifier, and you can use the training part of the dataset to build a decision tree, and then use it to predict the class 
# of a unknown patient, or to prescribe it to a new patient. Use drug200.csv for dataset.

import pandas as pd
df=pd.read_csv("drug200.csv")
print(df.info())
df = pd.get_dummies(df, drop_first=True)
print(df)
y = df['Drug_drugB']
x = df.drop('Drug_drugB', axis=1)



from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(criterion='entropy',max_depth=None)
dt.fit(x_train,y_train)
y_pred=dt.predict(x_test)


from sklearn.metrics import accuracy_score,confusion_matrix
cm=confusion_matrix(y_test,y_pred)
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

new_data=pd.DataFrame({"Age":[23],"Na_to_K":[25.355],"Sex_M":[False],"BP_LOW":[False],"BP_NORMAL":[False],"Cholesterol_NORMAL":[False],"Drug_drugC":[False],"Drug_drugX":[False],"Drug_drugY":[True]})

pred=dt.predict(new_data)
print(pred[0])


