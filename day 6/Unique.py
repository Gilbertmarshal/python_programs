lst = [1,2,2,2,2,3,3,44,44,44,6,6]
unique=[]
for i in lst:
    if lst.count(i)==1:
        unique.append(i)
print(unique)
