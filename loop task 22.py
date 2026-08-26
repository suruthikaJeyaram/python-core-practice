#Check Whether a Number is Prime or Not.
a=120
if a>1:
    for i in range(2,a):
        if a%i==0:
            print("Not a Prime Number")
            break
        else:
            print("Prime Number")
else:
    print("Not a prime number")
