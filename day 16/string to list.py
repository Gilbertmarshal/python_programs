s = "I am Learning Python"
words=[]
word=""
for ch in s:
  if ch!=" ":
    word +=ch
  else:
    words.append(word)
    word =""
words.append(word)
print(words)
