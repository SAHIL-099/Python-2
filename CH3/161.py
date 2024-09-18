# Write a Python Program to find all URLs from a given text. Consider URLs to be of only this format.
# http://github.com
# https://github.com
# Can Start with either http or https followed by :// domain name dot com
# Example:
# Text="Hello all Students must visit at my website https://www.pandasrockstar.com for more information. Also, check out 
# http://www.google.com"
# Output:
# Found URLs:
# https://www.pandasrockstar.com
# http://www.google.com


import re
def find_urls(text):
    urls = re.findall(r'https?://[^\s]+', text)
    return urls
# Example usage
text = "Hello all Students must visit at my website https://www.pandasrockstar.com for more information. Also, check out http://www.google.com"
print(find_urls(text))
