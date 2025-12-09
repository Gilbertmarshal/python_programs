lst=[10,20,30,55,65,70]
first=second=float("-inf")
for num in lst:
    if num>first:
        second = first
        first = num
    elif num>second and num!=first:
        second = num
print(second)
