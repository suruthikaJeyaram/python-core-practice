"""Create a Python program that takes two lists and returns a new list containing
elements that are common in both input lists."""
a=["Apple","Orange","Mango","Lemon"]
b=["Pomagranate","Watermelon","Lemon","Orange"]
common=[]
for items in a:
    if items in b:
      common.append(items)
print(common)    