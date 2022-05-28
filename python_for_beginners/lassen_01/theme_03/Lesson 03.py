# f-string Function

# userN = 'Max'
# greeting = f'Hello {userN:1}!'
# print(greeting)

# value = 22.5678
# print(f"Area of a circle is {value:.2f}")

# sec = 9
# print(f"0{sec}")


# hours = 7
# minutes = 50
#
# print(f"{hours:02d}:{minutes:02d}")

# name = input()
# surname = input()
# domain = input()
#
# # John.Smith@my-site.com
#
# result = f'{name}.{surname}@{domain}'
# print(result)

# Name: Clint ; Surname: Eastwood ; Age: 090

# name = input('Enter:\n Name, Surname, Age\n')
# surname = input()
# age = int(input())
#
# result = f'Name: {name:6}; Surname: {surname:10}; Age: {age:03d}'
# print(result)

#
# Isotope mass of Uranium-235 is 235.0439 u.

# name = input()
# weight = float(input())
# result = f'Isotope mass of {name} is {weight:.4f} u.'
# print(result)

# The time is 01:15:09.

# hh = int(input())
# mm = int(input())
# ss = int(input())
#
# print(f'The time is {hh:02d}:{mm:02d}:{ss:02d}.')

# The time is 1:15: 9.

hh = int(input())
mm = int(input())
ss = int(input())

print(f'The time is {hh:2d}:{mm:2d}:{ss:2d}.')
