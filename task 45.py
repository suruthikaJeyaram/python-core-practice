'''Write a Python program to calculate the sum of the positive and negative numbers
of a given list of numbers using the lambda function.'''

original_list=[4,5,6,7,-4,-5,-6,-7]
positive=sum(filter(lambda x:x>0,original_list))
negative=sum(filter(lambda x:x<0,original_list))

print("positive sum:",positive)
print("negative sum",negative)
