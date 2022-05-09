# import math # import the library completely
from math import sqrt, floor # Importing the function from a library


# def pr_line():
#     print('____________________\n')

    # code
# ----
# pr_line() 

# def max(num1, num2):
#     if num1 > num2:
#         return num1

#     if num2 > num1:    
#         return num2
# str = max(10, 15)
# print(str)
# pr_line() 
# print(max(10, 10))       
# ----

# math.sqrt - library.function

# ----

# pr_line()
# str = max(10, 10)
# if str == None:
#     print('They are equal')
# print(str) 
# pr_line()


# print(sqrt(15))
# pr_line()
# print(floor(3.5))



# # ----

# pr_line()

# def max(num1, num2):
#     if num1 > num2:
#         return num1

#     if num2 > num1:    
#         return num2

#     return None


# def print_line_with_ch(ch = '='):        
#     str = ''
#     for index in range(15):
#         str += ch
#     print(str)

# print_line_with_ch('+')
# pr_line()
# print_line_with_ch()   
# pr_line()  

# # ----

# def open_file(filename, access = 'read'):
#     pass

# open_file("test.txt")
# open_file(filename='test.txt', access='write')

#----

def pr_line():
    print('____________________\n')


def max1(num1: int, num2: int) -> int:
    if num1 > num2:
        return num1

    if num2 > num1:    
        return num2

    return None
    
# print(max1('a', 'b'))

# pr_line()