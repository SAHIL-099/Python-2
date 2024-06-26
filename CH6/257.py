# Using the Iris dataset 
# (https://raw.githubusercontent.com/pdsinroza/python2/main/Iris.csv?token=GHSAT0AAAAAACQ7ZNWMQ3U6FOFL37O2JIPAZQ5CWZA), 
# write Python code to perform the following tasks:
# Split the dataset into features (X) and labels (y).
# Split the features and labels into training and testing sets with a test size of 0.2 and a random state of 42.
# Initialize a kNN classifier with 3 neighbors.
# Train the classifier on the training set.
# Make predictions on the test set.
# Calculate and print the accuracy score of the classifier.

import pandas as pd

df=pd.read_csv("iris.csv")
df.drop('Id',axis=1,inplace=True)
df=pd.get_dummies(df,drop_first=True)

y=df['Species_Iris-versicolor']
x=df.drop('Species_Iris-versicolor',axis=1)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier(n_neighbors=3)

knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)


from sklearn.metrics import accuracy_score


ac=accuracy_score(y_test,y_pred)
print(ac)
