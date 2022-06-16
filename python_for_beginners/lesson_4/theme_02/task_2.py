TICKET_PRICE = 10
people = int(input())
days = int(input())

group_discount = 0
if people >= 3:
    group_discount = people * 3

if group_discount > 30:
    group_discount = 30

time_discount = 0
if days >= 4 and days <= 7:
     time_discount = 5
elif days >= 8 and days <= 14:
     time_discount = 10
elif days > 7:
     time_discount = 15

discount = group_discount + time_discount
amount = TICKET_PRICE * people * days
amount2 = TICKET_PRICE * people * days
amount = amount - amount * discount / 100

print(f'Price without discount: {amount2:.2f}')
print(f'Discount: {discount}%')
print(f'Price with discount: {amount:.2f}')





