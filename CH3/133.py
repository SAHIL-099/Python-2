# Write a Python program that matches a string that has an 'a' followed by zero or one 'b' using regular expressions

import re
def match_a_followed_by_zero_or_one_b(text):
    return bool(re.findall(r'ab?', text))
# Example usage
print(match_a_followed_by_zero_or_one_b("a"))
print(match_a_followed_by_zero_or_one_b("ab"))
print(match_a_followed_by_zero_or_one_b("abb"))