lst=[1,2,3,4,2,2,2,4]
target=2
remove=[]
for i in lst:
    if i!=target:
        remove.append(i)
print(remove)
