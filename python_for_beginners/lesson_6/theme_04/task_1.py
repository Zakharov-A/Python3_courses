text = input()
new_text = ''
for idx, symbol in enumerate(text):
    if (idx + 1) % 2 == 0:
        new_text += symbol

print(new_text)

