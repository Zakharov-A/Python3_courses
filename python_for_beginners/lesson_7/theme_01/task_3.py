text = input()
words = text.split()

max_len = words[0]
for word in words:
    if len(word) >= len(max_len):
        max_len = word

print(max_len)



