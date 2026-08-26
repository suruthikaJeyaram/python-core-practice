#Write a program to print sum of digits
a=1456
sum=0
while a>0:
    digit=a%10
    sum+=digit
    a//=10
print("sum of digits:",sum)
