STARTING_BALANCE = 1000

balance = STARTING_BALANCE
while True:
    text = input()
    if text == 'EXIT':
        break

    tokens = text.split('_')
    command = tokens[0]
    amount = float(tokens[1])

    if command == 'income':
        balance += amount
    else:
        balance -= amount
        if balance < 0:
            print('Budget limit exceeded!')
            break
    comment = ''
    if len(tokens) > 2:
        comment = tokens[2]

    print(f'balance: {balance:.2f} | {command}: {amount:.2f} {comment}')

