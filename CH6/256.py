# Write Python code to evaluate the performance of a classification model using the following steps:
# Import the necessary functions from sklearn.metrics.
# Calculate and print the classification report for the true labels and predicted labels.
# Calculate and print the accuracy score of the classifier.


from sklearn.datasets import load_wine

wine=load_wine()
x=wine.data
y=wine.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)

from sklearn.tree import DecisionTreeClassifier

dt=DecisionTreeClassifier(criterion="entropy",max_depth=None)

dt.fit(x_train,y_train)
y_pred=dt.predict(x_test)


from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

cm=confusion_matrix(y_test,y_pred)
cr=classification_report(y_test,y_test)
ac=accuracy_score(y_test,y_pred)
print(cm)
print(cr)
print(ac)