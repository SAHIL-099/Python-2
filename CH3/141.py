# Write a Python program to remove leading zeros from an IP address using regular expression
import re
ip = "016.08.094.196"
if re.findall("^0",ip):
    ip = re.sub('^0', '', ip)
string = re.sub('\.[0]*', '.', ip)
print(string)