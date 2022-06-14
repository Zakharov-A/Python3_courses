amount = int(float(input()))
hour = int(input())
if hour < 6:
    discount = -50 / 100
elif hour < 8:
    discount = 0 / 100
elif hour < 12:
    discount = 20 / 100
elif hour < 15:
    discount = -20 / 100
elif hour < 12:
    discount = 20 / 100
else:
    discount = 50 / 100
discount_amount = round(amount * discount)

print(amount)
print(discount_amount)
print( amount + discount_amount)

