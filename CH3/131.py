# Write a Python program using regular expressions that matches a string that has an a followed by zero or more b's.

import re
def match_a_followed_by_zero_or_more_bs(text):
    return bool(re.findall(r'b*', text))
# Example usage
print(match_a_followed_by_zero_or_more_bs("a"))
print(match_a_followed_by_zero_or_more_bs("abbb"))
print(match_a_followed_by_zero_or_more_bs("ac"))