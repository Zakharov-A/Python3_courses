text = input()
symbol_x = input()
is_found = False
for symbol in text:
    if symbol == symbol_x:
        is_found = True
        break

if is_found:
    print(f'The "{symbol_x}" character was found in "{text}".')
else:
    print(f'The "{symbol_x}" character was not found in "{text}".')
