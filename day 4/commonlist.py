lst1=[1,2,5,6,7,4]
lst2=[2,3,4,8,9,7]
cmnlist=[]
for i in lst1:
    if i in lst2:
        cmnlist.append(i)
print(cmnlist)
