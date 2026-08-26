'''Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Task 41'''
original_list=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
original_list.sort(key=lambda x: x[1])
print(original_list)
   