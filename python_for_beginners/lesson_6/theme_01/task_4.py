text = input()
symbol_x = input()
symbol_y = input()
new_text = ''

for symbol in text:
    if symbol != symbol_x:
        new_text += symbol
    else:
        new_text += symbol_y

print(new_text)

