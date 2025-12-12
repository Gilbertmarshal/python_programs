s = "hello world"
freq = {}

for ch in s:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1

print(freq)
