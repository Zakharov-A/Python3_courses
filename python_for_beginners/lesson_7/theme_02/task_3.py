text = input()

words = text.split()

is_not_found = True
for word in words:
    if 'a' in word or 'o' in word:
        is_not_found = False
        print(word, end=', ')

if is_not_found:
    print('Item not found')


