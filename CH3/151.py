# Write a Python program to remove multiple spaces from a string and store the output in list using regular expression
import re
text1 = 'Python Exercises'
print("Original string:",text1)
output_list=[re.sub(' +',' ',text1)]
print(output_list)