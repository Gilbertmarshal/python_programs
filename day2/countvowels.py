name = input("Enter the name: ")
vowels ="aeiouAEIOU"
count = 0
for i in name:
    if i in vowels:
        count+=1
print(f"There are {count} vowels in the string")

