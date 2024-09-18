# Write a Python program to split a string into uppercase letters using regular expressions

import re
text = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', text))
