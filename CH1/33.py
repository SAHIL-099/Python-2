# Use the file ipl-matches.csv which contains data of all the IPL matches from year 2008 to 2022. Read this csv file and display the basic 
# information like memory and data types for this data frame. Write python code for the following cases:
# 1. List out all matches gone in superover.
# 2. How Many Matches won by Chennai Super Kings at Kolkata.
# 3. In How Many Matches MS Dhoni is Player of Match Vs Mumbai Indians.
# 4. Display list of all matches in which Gujarat Titans won the Toss and Elected to Bat and won the match.
# 5. Display list of all matches won by Gujarat Titans.


import pandas as pd
import numpy as np

ipl=pd.read_csv("files/ipl-matches.csv")
print(ipl.info())

# matches goes to super over
supover=ipl[ipl['SuperOver']=='Y']
print(supover)


# How Many Matches won by Chennai Super Kings at Kolkata.

csk=ipl[(ipl['WinningTeam']=='Chennai Super Kings') & ( ipl['City']=='Kolkata')].shape[0]
print(csk)



# In How Many Matches MS Dhoni is Player of Match Vs Mumbai Indians.

msd=ipl[((ipl['Player_of_Match']=='MS Dhoni') & ((ipl['Team1']=='Mumbai Indians')|(ipl['Team2']=='Mumbai Indians')))].shape[0]
print(msd)


# Display list of all matches in which Gujarat Titans won the Toss and Elected to Bat and won the match.


gt=ipl[(ipl['WinningTeam']=='Gujarat Titans') & (ipl['TossWinner']=='Gujarat Titans') &(ipl['TossDecision']=='bat')].shape[0]
print(gt)

# Display list of all matches won by Gujarat Titans.
gt=ipl[ipl['WinningTeam']=='Gujarat Titans']
print(gt)
