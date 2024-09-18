# Write a Python program that checks whether a word starts and ends with a vowel in a given string. Return true if a word matches the 
# condition; otherwise, return false.
#  Sample Data:
#  ("Red Orange White") -> True
#  ("Red White Black") -> False
#  ("abcd dkise eosksu") -> True

import re
def test(text):
    return bool(re.findall('[/^[aeiou]$|^([aeiou]).*\1$/', text))
text ="Red Orange White"
print("Original string:", text)
print("Check beginning and end of a word in the said string with a vowel:")
print(test(text))
text ="Red White Black"
print("\nOriginal string:", text)
print("Check beginning and end of a word in the said string with a vowel:")
print(test(text))
text ="abcd dkise eosksu"
print("\nOriginal string:", text)
print("Check beginning and end of a word in the said string with a vowel:")
print(test(text))