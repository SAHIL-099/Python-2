# Write a Python program to replace all occurrences of a space, comma, or dot with a colon using regular expressions
import re
text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", text))
