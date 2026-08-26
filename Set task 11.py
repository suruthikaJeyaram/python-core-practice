#Find Common Elements
a={"cricket","football","Hockey","Biriyani"}
b={"Biriyani","chicken","mutton","cricket"}
common=set()
for items in a:
     if items in b:
       common.add(items)
print(common)