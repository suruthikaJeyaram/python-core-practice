'''Write a Python program to square and cube every number in a given list of integers
using Lambda'''
original_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x=list(map(lambda a:a**2, original_list))
y=list(map(lambda a:a**3, original_list))
print('square:',x)
print('cube:',y)