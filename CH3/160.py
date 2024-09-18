# Write a python program that executes following tasks (strictly using regex module)
# Given text – “ hello welcome to the python exam my email is alice@google.com, world this is bob@meta.com appearing for python exam “
# a) Remove leading and trailing spaces of the given text.
# b) Replace space between words of the given text by ‘$’ symbol 
# c) Extract username and host name (i.e. alice,bob,google, meta ) in a list a/

import re
def process_text(text):
# a) Remove leading and trailing spaces
    text = re.sub(r'^\s+|\s+$', '', text)
    
# b) Replace space between words with '$' symbol
    text_with_dollar = re.sub(r'\s+', '$', text)
    
# c) Extract username and host name from emails
    email_matches = re.findall(r'(\w+)@(\w+)\.\w+', text)
    usernames_hosts = [item for sublist in email_matches for item in sublist]
    return text, text_with_dollar, usernames_hosts


text = " hello welcome to the python exam my email is alice@google.com, world␣this is bob@meta.com appearing for python exam "
cleaned_text, text_with_dollar, usernames_hosts = process_text(text)
print("Cleaned Text:", cleaned_text)
print("Text with Dollar:", text_with_dollar)
print("Usernames and Hosts:", usernames_hosts)