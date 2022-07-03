text = input()
keyword = input()

words = text.split()
found_word = None

for word in words:
    if keyword in word:
        found_word = word

if found_word is None:
    print("Item not found")
else:
    print(found_word)

