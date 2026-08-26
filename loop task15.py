#check Armstrong number
a=9474
b=len(str(a))
total=0
temp=a
while temp>0:
    digit=temp%10
    total+=digit**b
    temp//=10
if total==a:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
