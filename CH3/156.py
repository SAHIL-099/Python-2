# Write a Python program to remove lowercase substrings from a given string

import re
str1 = 'KDeoALOklOOHserfLoAJSIskdsf'
print("Original string:")
print(str1)
print("After removing lowercase letters, above string becomes:")
remove_lower = re.sub('[a-z]', '', str1)
print(remove_lower)