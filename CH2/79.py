# The file "student_scores.csv" contains the marks scored by a group of students in three subjects: Maths, Science, and English. 
# Each row contains the name of the student, their score in Maths, Science, and English. Create a pandas DataFrame from this data 
# and create a heatmap to visualize the correlations between the scores in these three subjects. Take Dataset from below:
# https://raw.githubusercontent.com/kavit88/Data-Sets/main/student_scores.csv

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset into a DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/kavit88/Data-Sets/main/student_scores.csv')
# Compute the correlation matrix
correlation_matrix = df[['Maths', 'Science', 'English']].corr()
# Visualize the correlations using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation between Maths, Science, and English Scores')
plt.show()
