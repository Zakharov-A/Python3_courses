text = input()

new_text_1 = ''
new_text_2 = ''

for idx, symbol in enumerate(text):
    if idx % 2 == 0:
        new_text_2 += symbol
    else:
        new_text_1 += symbol

print(new_text_1)
print(new_text_2)


