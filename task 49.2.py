'''Write a Python program that matches a string that has an a followed by zero or
one 'b'''
import re
a="ab"
if re.fullmatch('ab?',a):
    print("matched")
else:
    print("not matched")