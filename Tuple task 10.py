#Calculate Average Age
group=[("hema",26),("sudha",40),("latha",45)]
total=0
count=0
for name,age in group:
    total+=age
    count+=1
Average=total/count
print("Average:",Average)
