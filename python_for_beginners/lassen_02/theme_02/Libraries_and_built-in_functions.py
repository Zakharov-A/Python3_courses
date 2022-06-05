# import math


#rounding up and down

# radius = 5
#
# circumference = 2*math.pi*radius #31.41592653589793
# print(circumference)
# print(math.ceil(circumference)) #32
# print(math.floor(circumference)) #31

# ----

#rounding up and down option 2

# from math import pi as pi
# from math import ceil as ceil
# from math import floor as floor
#
# radius = 5
#
# circumference = 2 * pi * radius  #31.41592653589793
# print(circumference)
# print(ceil(circumference)) #32
# print(floor(circumference)) #31

# Built-In Functions in Python eval

# a = 4
# b = 2
#
# sign = '+'
#
# result = f'{a}{sign}{b}'
# print(f'{a}{sign}{b}=', eval(result))

# Built-In Functions in Python round and abs and sqrt

print(round(2.567,2)) #2.57
print(round(2.567,0)) #3.0

print(abs(-555)) #555
print(abs(555)) #555

import math
print(math.sqrt(4))
