lst =[1,2,2,3,3,3,4,4,4,4]
freq={}
for i in lst:
  if i in lst:
    freq[i]+=1
  else:
    freq[i]=1
print(freq)
