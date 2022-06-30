# ABCAB
word = input()
length = len(word)
half_len = length // 2

is_palindrome = True
for i in range(half_len):
    if word[i] != word[length - 1 - i]:
        is_palindrome =False
        break
if is_palindrome:
    print(f'The text "{word}" is palindrome.')
else:
    print(f'The text "{word}" is not palindrome.')


