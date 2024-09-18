# Write a Python program that starts each string with a specific number using regular expressions

import re
def match_num(string):
    text = re.search(r"^5",string)
    if text:
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))