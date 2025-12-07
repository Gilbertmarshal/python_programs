# reverse a string with slicing
name = input("Enter the name: ")
print(name[::-1])

# reverse a string without slicing

name = input("Enter the name: ")
rev=""
for i in name:
    if i in name:
        rev=i+rev
print(rev)
