text = input()
symbols_x = input()

if symbols_x in text:
    print(f'The text "{symbols_x}" was found in the text "{text}".')
else:
    print(f'The text "{symbols_x}" was not found in "{text}".')
