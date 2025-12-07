#Sum of numbers in a iteration

"""num= int(input("Enter the number: "))
count=0
for i in range(1,num+1):
    count+=i
print(count)"""

#Sum of digits in a number

num=12345
total=0
while num >0:
    digit = num%10
    total=total+digit
    num//=10
print(total)




