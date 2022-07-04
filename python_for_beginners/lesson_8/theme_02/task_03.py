words = input().split(',')

text = ''
for word in words:
    if not word.isalpha():
        continue
    text += word

print(text)
