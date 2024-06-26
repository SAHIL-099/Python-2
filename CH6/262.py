# The task involves building a k-Nearest Neighbors (kNN) regression model to predict the Air Quality Index (AQI) based on the latitude and 
# longitude coordinates of various countries. The dataset used for this task contains information about the AQI levels and geographic locations 
# (latitude and longitude) of different countries. The AQI serves as an indicator of air quality, with higher values indicating poorer air quality and 
# vice versa. Use AQI and Lat Long of Countries.csv for dataset.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the data
df = pd.read_csv("Countries.csv")
print(df.info())

# Select the features and target variable
x = df[['lat', 'lng']]
y = df['AQI Value']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create and train a KNeighborsRegressor model
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(x_train, y_train)

# Make predictions on the testing set
y_pred = knn.predict(x_test)

# Evaluate the model using regression metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Example of new latitude and longitude coordinates
new_data = pd.DataFrame([[40.7128, -74.0060],  # New York City
                         [34.0522, -118.2437],  # Los Angeles
                         [51.5074, -0.1278]],  # London
                        columns=['lat', 'lng'])

# Make predictions on the new data
new_predictions = knn.predict(new_data)
print("Predicted AQI for New York City:", new_predictions[0])
print("Predicted AQI for Los Angeles:", new_predictions[1])
print("Predicted AQI for London:", new_predictions[2])