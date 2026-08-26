'''Write a program to create an iterator to print English alphabets from A to Z'''
alphabets=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
my_list=iter(alphabets)
for letter in my_list:
    print(letter)