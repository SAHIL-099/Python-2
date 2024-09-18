# Write a Python program that takes a string with some words. For two consecutive words in the said string, check whether the first word ends 
# with a vowel and the next word begins with a vowel. If the program meets the condition, return true, otherwise false. Only one space is 
# allowed between the words.
#  Sample Data:
#  ("These exercises can be used for practice.") -> True ("Following exercises should be removed for practice.") -> False ("I use these stories in my 
# classroom.") -> True
import re
def test(text):
    return bool(re.findall('[AEIOUaeiou] [AEIOUaeiou]', text))
text ="These exercises can be used for practice."
print("Original string:", text)
print("Two following words begin and end with a vowel in the said string:")
print(test(text))
text ="Following exercises should be removed for practice."
print("\nOriginal string:", text)
print("Two following words begin and end with a vowel in the said string:")
print(test(text))
text ="I use these stories in my classroom."
print("\nOriginal string:", text)
print("Two following words begin and end with a vowel in the said string:")
print(test(text))