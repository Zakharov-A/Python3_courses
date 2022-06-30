from math import ceil as ceil
a = float(input())
b = float(input())
c = float(input())
car = float(input())

volume = a * b * c
count_cars = ceil(volume / car)
print(count_cars)

