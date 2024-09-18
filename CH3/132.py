# Write a Python program that matches a string that has an 'a' followed by one or more b's using regular expressions.

import re
def match_a_followed_by_one_or_more_bs(text):
    return bool(re.findall(r'ab+', text))
# Example usage
print(match_a_followed_by_one_or_more_bs("a"))
print(match_a_followed_by_one_or_more_bs("ab"))
print(match_a_followed_by_one_or_more_bs("abbb"))