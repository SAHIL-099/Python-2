# Write a python program to print Phone number from given string using regular expressions

import re
def extract_phone_number(text):
    phone_numbers = re.findall(r'\b\d{10}\b', text)
    return phone_numbers
# Example usage
text = "Contact me at 1234567890 or at 9876543210"
print(extract_phone_number(text))