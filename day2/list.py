# Unique values in list

lst = list(map(int, input("Enter numbers separated by space: ").split()))
unique_list = []
for num in lst:
    if num not in unique_list:
        unique_list.append(num)
print("List after removing duplicates:", unique_list)

#Maximum list in values

lst=[10,22,55,33,67,78]
max_lst=lst[0]
for num in lst:
    if num>max_lst:
        max_lst=num
print(max_lst)

#Minimum number in list

lst=[1,45,25,67,22,11,34,56,90]
min_list=lst[0]
for i in lst:
    if i<min_list:
        min_list=i
print(min_list)
