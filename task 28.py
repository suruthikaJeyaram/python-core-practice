"""Write a Python program to remove duplicates from a list while preserving the
order of elements"""
a=[14,15,16,14,13,12,15]
b=list(dict.fromkeys(a))
print(b)