#  Write a Python program to check for a number at the end of a string using regular expressions.

import re
def end_num(string):
    return bool(re.findall(r"\d$",string))
print(end_num('abcdef'))
print(end_num('abcdef6'))