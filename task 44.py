'''Write a Python program to find numbers divisible by nineteen or thirteen from a list
of numbers using Lambda'''
numbers=[114,121,152,190,228,104,117,130]
result=list(filter(lambda x:x%13==0 or x%19==0,numbers))
print(result)