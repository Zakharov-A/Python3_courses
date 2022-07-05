while True:
    text = input()
    if text == "STOP":
        break

    formula = text.replace('_', ' ')
    print(f'{formula} = {eval(formula)}')
