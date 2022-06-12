from math import ceil as cail
amount = int(float(input()))

if amount <= 100:
    discount = 0.02
elif amount <= 500:
    discount = 0.05
elif amount <= 1000:
    discount = 0.08
elif amount <= 5000:
    discount = 0.10
else:
    discount = 0.15
discount_amount = cail(amount * discount)

print(amount)
print(discount_amount)
print(amount - discount_amount)

