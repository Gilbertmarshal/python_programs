n=int(input("Enter the number:")) 
if n>=1:
    for i in range(2,n):
        if n % i ==0:
            print(f"{n} not a prime number")
            break
    else:
            print(f"{n} prime number")
else:
    print("The number is less than 1")

"""n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a Prime Number")
            break
    else:
        print(f"{n} is a Prime Number")
else:
    print("Number should be greater than 1")"""


