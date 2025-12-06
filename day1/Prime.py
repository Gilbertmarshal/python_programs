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
