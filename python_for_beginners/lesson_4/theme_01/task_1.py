season = input()
room = input()
days = int(input())

if room == 'Single':
    price = 60
elif room == 'Double':
    price = 85
elif room == 'Triple':
    price = 140


if season == "Winter":
    if room == "Single":
        k = 1
    elif room == "Double":
        k = 1
    elif room == "Triple":
        k= 1
elif season == "Spring":
    if room == "Single":
        k = 1.5
    elif room == "Double":
        k = 1.3
    elif room == "Triple":
        k= 1.2
elif season == "Summer":
    if room == "Single":
        k = 3
    elif room == "Double":
        k = 2.8
    elif room == "Triple":
        k= 2.5
elif season == "Autumn":
    if room == "Single":
        k = 1.8
    elif room == "Double":
        k = 1.5
    elif room == "Triple":
        k = 1.5

total_cost = price * days * k
print(f'{total_cost:.2f}')




