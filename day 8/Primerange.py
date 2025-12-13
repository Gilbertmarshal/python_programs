start,end=10,50
for num in range(start,end+1):
    if num>1:
        for i in range(2,int(num**0.5+1)):
            if num%i==0:
                break
        else:
            print(num,end=" ")
    else:
        print("The number is wrong")
