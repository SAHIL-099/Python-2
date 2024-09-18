# Write a Python program that matches a string that has an 'a' followed by three 'b' using regular expressions

import re
def match_a_followed_by_three_bs(text):
    return bool(re.findall(r'ab{3}', text))
# Example usage
print(match_a_followed_by_three_bs("ab"))
print(match_a_followed_by_three_bs("abbb"))
print(match_a_followed_by_three_bs("abbbb"))