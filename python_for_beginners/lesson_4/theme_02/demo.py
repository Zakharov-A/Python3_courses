hour = int(input())


if hour >= 9 and hour <= 11:
    discount = 0.05
elif hour >= 12 and hour <= 13:
    discount = 0.20
elif hour >= 20 and hour <= 21:
    discount = 0.15
print(discount)

