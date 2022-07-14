x_max = int(input())
y_max = int(input())
z = int(input())

is_not_found = True
for x in range(x_max):
    for y in range(y_max):
        if x * x - y == z:
            is_not_found = False
            print(f'Equation solution: {x} * {x} - {y} = {z}')

if is_not_found:
    print('No solution found')
