# Given the credit card transaction dataset, the objective is to build a kNN classification model that accurately predicts whether a transaction is 
# fraudulent or non-fraudulent based on the transaction features provided. The model should be trained on historical transaction data and 
# evaluated on another portion of the dataset to assess its performance. The ultimate goal is to create a reliable classifier that can automatically 
# detect fraudulent transactions and prevent financial losses for credit card companies and cardholders. Use card_transdata.csv for dataset.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix

data = pd.read_csv("card_transdata.csv")
print(data)


data = pd.read_csv("card_transdata.csv")
# Assuming the target variable is named 'Class'
x= data.drop('fraud', axis=1)
y = data['fraud']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3,
random_state=41)
# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


knn = KNeighborsClassifier(n_neighbors=5)

# Train the kNN classifier
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))