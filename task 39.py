#Write a program to create a custom iterator that iterates from 1 to 10 in 0.5 intervals
number=[x/2 for x in range(2,21)]
result=iter(number)
for values in result:
    print(values)