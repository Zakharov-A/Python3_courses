FINE = 333

auto = input()
speed = int(input())
is_rental = True
if input() == 'no':
    is_rental = False

if auto == 'motorcycle':
    max_speed = 110
elif auto == 'car':
    max_speed = 130
elif auto == 'minibus':
    max_speed = 120
elif auto == 'truck':
    max_speed = 90

delta_speed = speed - max_speed

delta_fine = 0
if delta_speed >= 80:
    delta_fine = 1800
elif delta_speed >= 60:
    delta_fine = 800
elif delta_speed >= 40:
    delta_fine = 200
elif delta_speed >= 20:
    delta_fine = 50

value = 0
if delta_speed > 0:
    value = FINE + delta_fine

if is_rental:
    if auto == 'car' or auto == 'minibus':
        value += FINE * 0.3

print(f'{value:.2f}')

