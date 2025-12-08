num = 50
count =0
for i in range(1,num):
    if num%i==0:
        count+=i
if num==count:
    print("Perfect number")
else:
    print("Not perfect number")
