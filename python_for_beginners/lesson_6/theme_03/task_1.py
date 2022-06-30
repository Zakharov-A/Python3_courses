CODE_A = 65
CODE_Z = 98
CODE_a = 97
CODE_z = 122
DELTA = CODE_a - CODE_A

text = input()
new_text = ''
for symbol in text:
    symbol_code = ord(symbol)
    if CODE_a <= symbol_code <= CODE_z:
        new_symbol = chr(symbol_code - DELTA)
        new_text += new_symbol
    else:
        new_text += symbol
print(new_text)




