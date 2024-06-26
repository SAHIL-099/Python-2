# Write Python code to train a decision tree classifier with entropy as the criterion using the following steps:
# Initialize a Decision Tree classifier with entropy as the criterion.
# Train the classifier on the training set.
# Make predictions on the test set.
# Calculate and print the confusion matrix for the classifier.

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


from sklearn.metrics import confusion_matrix

cm=confusion_matrix(y_test,y_pred)

print(cm)