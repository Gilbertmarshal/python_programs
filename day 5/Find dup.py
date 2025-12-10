lst = [1,2,3,2,4,3,3)
seen=set()
dublicates = set()
for x in lst:
  if x in seen:
    duplicates.add(x)
  else:
    seen.add(x)
print(list(duplicates))
