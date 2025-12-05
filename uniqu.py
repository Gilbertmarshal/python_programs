lst = list(map(int, input("Enter numbers separated by space: ").split()))
unique_list = []
for num in lst:
    if num not in unique_list:
        unique_list.append(num)
print("List after removing duplicates:", unique_list)
