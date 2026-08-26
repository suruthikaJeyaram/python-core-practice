#Write a Python program to create Fibonacci series up to n using Lambda.
n=20
a=0
b=1
fib=lambda x,y:x+y
print(a,b,end=" ")
for i in range(n-2):
    c=fib(a,b)
    print(c,end=" ")
    a=b
    b=c
