'''Write a Python program to check that a string contains only a certain set of
characters (in this case a-z, A-Z and 0-9).'''
import re
a='The rain is Spain 3456'
if re.fullmatch('[a-zA-Z0-9]+',a):
    print("String contains only a-z, A-Z and 0-9")
else:
    print("invalid string")