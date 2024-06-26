# Write Python code to train a kNN classifier using the following steps:
# Split the dataset X into training and testing sets with a test size of 0.3 and a random state of 42.
# Initialize a kNN classifier with 5 neighbors.
# Train the classifier on the training set.
# Make predictions on the test set.
# Calculate and print the accuracy score of the classifier.


import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
# Load the Wine dataset
wine = load_wine()
x= wine.data
y = wine.target
# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=42)
# Initialize a kNN classifier with 5 neighbors
knn = KNeighborsClassifier(n_neighbors=5)
# Train the classifier on the training set
knn.fit(x_train, y_train)
# Make predictions on the test set
y_pred = knn.predict(x_test)
# Calculate and print the accuracy score of the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy of kNN classifier: {accuracy:.2f}')