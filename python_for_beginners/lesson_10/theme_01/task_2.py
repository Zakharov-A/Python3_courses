first_symbol_code = int(input())
last_symbol_code = int(input())

word = ''
for code in range(first_symbol_code, last_symbol_code+1):
    word += chr(code)

print(f'{word}: ', end='')
for a in word:
    for b in word:
        for c in word:
            print(f'{a}{b}{c}', end=',')

