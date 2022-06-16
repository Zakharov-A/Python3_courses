 #по чётным дням скидка 5%, а по нечётным - 7%. Кроме этого,
 #если дата, в которую сделана покупка, кратна 3, то скидка увеличивается ещё на 3 %.

date = int(input())
amount = float(input())

discount = 7
if date % 2 == 0:
    discount = 5
if date % 3 == 0:
    discount += 3

amount -= amount * discount / 100
print(f'{amount:.2f}')

