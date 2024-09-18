# The file "survey.csv" contains the results of a survey that asks people how many hours they sleep per night, how much coffee they 
# drink per day, and how many hours they spend exercising per week. Create a pandas DataFrame from this data and plot the 
# relationships between these variables using regression plots. Specifically, create the following plots:
#  1. A regression plot of hours of sleep versus cups of coffee per day, with a regression line and confidence interval.
#  2. A regression plot of hours of sleep versus hours of exercise per week, with a regression line and confidence interval.
#  3. A regression plot of cups of coffee per day versus hours of exercise per week, with a regression line and confidence interval.
#  Label each axis appropriately and give each plot a title. Take Dataset from below:
# https://raw.githubusercontent.com/kavit88/Data-Sets/main/survey.csv



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
survey_df = pd.read_csv("https://raw.githubusercontent.com/kavit88/Data-Sets/main/survey.csv")
# Plot regression of hours of sleep
#versus cups of coffee per day
sns.regplot(x="cups_of_coffee_per_day",
y="hours_of_sleep", data=survey_df)
plt.xlabel("Cups of coffee per day")
plt.ylabel("Hours of sleep per night")
plt.title("Relationship between coffee consumption and sleep")
plt.show()
# Plot regression of hours of sleep
#versus hours of exercise per week
sns.regplot(x="hours_of_exercise_per_week",
y="hours_of_sleep", data=survey_df)
plt.xlabel("Hours of exercise per week")
plt.ylabel("Hours of sleep per night")
plt.title("Relationship between exercise and sleep")
plt.show()
# Plot regression of cups of coffee per day
#versus hours of exercise per week
sns.regplot(x="hours_of_exercise_per_week",
y="cups_of_coffee_per_day", data=survey_df)
plt.xlabel("Hours of exercise per week")
plt.ylabel("Cups of coffee per day")
plt.title("Relationship between coffeeconsumption and exercise")
plt.show()
