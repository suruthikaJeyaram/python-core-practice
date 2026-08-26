#check palindrome number
num=1331
a=num
reverse=0
while a>0:
    digit=a%10
    reverse=reverse*10+digit
    a=a//10
if num==reverse:
    print("Palindrome number")
else:
    print("Not an palindrome number")