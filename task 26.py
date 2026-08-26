"""Write a Python program that uses a list comprehension to create a new list that
contains only the uppercase letters in an existing list of strings"""
mylist=["Apple","Banana","Orange"]
newlist=[item.upper() for item in mylist]
print(newlist)