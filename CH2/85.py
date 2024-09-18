# Consider the following numpy arrays:
# Time=np.arange(12)
# income=np.array([5,9,6,6,10,7,6,4,4,5,6,4])
# expense=np.array([6,6,8,3,6,9,7,8,6,6,4,8])
# Use Time array for X-axis and create two separate lines in the same graph with income & expense on Y-axis. Give Appropriate labels. Create an
# area fill graph between the two lines in such a way that where income is more than expense, are filled with Green and areas where expense is
# more than income are filled with red.

import numpy as np
import matplotlib.pyplot as plt

Time = np.arange(12)
income = np.array([5, 9, 6, 6, 10, 7, 6, 4, 4, 5, 6, 4])
expense = np.array([6, 6, 8, 3, 6, 9, 7, 8, 6, 6, 4, 8])

plt.fill_between(Time, income, expense, where=income >
                 expense, color='green',label="positive", interpolate=True)
plt.fill_between(Time, expense, income, where=income <
                 expense, color='red', label="negative",interpolate=True)

plt.xlabel("month")
plt.ylabel("income/expense")
plt.legend()
plt.show()
