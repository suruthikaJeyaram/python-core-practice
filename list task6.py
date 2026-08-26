#Remove Duplicates from a List
a=['Horlics', 'boost', 'tea', 'coffee','tea','coffee']
result=[]
for items in a:
    if items not in result:
           result.append(items)
print(result)
