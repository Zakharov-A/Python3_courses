day = input()
fruit = input()
weight = float(input())

if day == "Monday":
    day_type = "workday"
elif day == "Tuesday":
    day_type = "workday"
elif day == "Wednesday":
    day_type = "workday"
elif day == "Thursday":
    day_type = "workday"
elif day == "Friday":
    day_type = "workday"
elif day == "Saturday":
    day_type = "weekend"
elif day == "Sunday":
    day_type = "weekend"

if fruit == 'Apple':
    if day_type == 'workday':
        price = 0.9
    else:
        price = 1.1
elif fruit == 'Banana':
    if day_type == 'workday':
        price = 1.5
    else:
        price = 1.9
elif fruit == 'Kiwi':
    if day_type == 'workday':
        price = 3.5
    else:
        price = 4.1
elif fruit == 'Orange':
    if day_type == 'workday':
        price = 1.5
    else:
        price = 1.7

amount = weight * price
print(f'{amount:.2f}')
