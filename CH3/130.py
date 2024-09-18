# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9) using regular expressions

import re
def contains_only_allowed_chars(text):
    return bool(re.findall(r'[a-zA-Z0-9]*', text))
# Example usage
print(contains_only_allowed_chars("Hello123"))
print(contains_only_allowed_chars("Hello 123"))