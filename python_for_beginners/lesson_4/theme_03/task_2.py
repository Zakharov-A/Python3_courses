from math import pi as pi
from math import sqrt as sqrt

figure = input()
param = input()
radius = float(input())
if figure == 'rectangle' or figure == 'right triangle':
    side = float(input())
if figure == 'square':
    if param == 'area':
        value = radius ** 2
    else:
        value = 4 * radius
elif figure == 'circle':
    if param == 'area':
        value = pi * radius ** 2
    else:
        value = 2 * pi * radius

elif figure == 'rectangle':
    if param == 'area':
        value = radius * side
    else:
        value = 2 * radius + 2 * side

elif figure == 'right triangle':
    if param == 'area':
        value = radius * side / 2
    else:
        value = radius + side + sqrt(radius ** 2 + side ** 2)

print(f'The {param} of the {figure} is {value:.2f}.')


