text = input()
symbols = input()

new_text = text.replace(symbols, '_' * len(symbols))
print(new_text)
