# Write a Python Program to find all five-character words in a string.
# For example:
# Input : text = 'The quick brown fox jumps over the lazy dog.'
# Output : ['quick', 'brown', 'jumps']

import re
def find_five(string):
    five=re.findall(r'\w{5}',string)
    return five


text="The quick brown fox jumps over the lazy dog."  
print(find_five(text))  
    