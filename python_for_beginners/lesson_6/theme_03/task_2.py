CODE_0 = 48
CODE_9 = 57
CODE_A = 65
CODE_Z = 90
CODE_a = 97
CODE_z = 122

text = input()
shift = int(input())

new_text = ''
for symbol in text:
    if symbol.isalnum():
        code = ord(symbol)

        for _ in range(shift):
            if code == CODE_9:
                code = CODE_A
            elif code == CODE_Z:
                code = CODE_a
            elif code == CODE_z:
                code = CODE_0
            else:
                code += 1

        new_text += chr(code)

    else:
        new_text += symbol

print(new_text)

