# x = input("x: ")
# y = input("y: ")
#
# try:
#     x = int(x)
#     y = int(y)
#
#     res = x/y
# except ZeroDivisionError :
#     res = "деление на ноль"
# except ValueError:
#     res = "не числовое значение"
#
# print(res)

#-----------------------------

# x = input("x: ")
# y = input("y: ")
#
# try:
#     x = int(x)
#     y = int(y)
#
#     res = x/y
# except ZeroDivisionError as z:
#     res = z
# except ValueError as v:
#     res = v
# else:
#     print("Исключений не обнаружено")
# finally:
#     print("Всегда выполняемая часть!")
#
# print(res)

#----------------------------------------

# def getValues():
#     x = input("x: ")
#     y = input("y: ")
#     try:
#         x = int(x)
#         y = int(y)
#         return x,y
#     except ValueError as v:
#         print(v)
#         return 0,0
#     finally:
#         print("finally выполняется до return")
#
# x,y = getValues()
# print(x,y)

#---------------------------------------------


x = input("x: ")
y = input("y: ")
try:
    x = int(x)
    y = int(y)

    res = x/y
except:
    print("Произошло исключение")
else:
    print("Исключений не произошло")
finally:
    print("finally выполняется всегда")

print(res)

#------------------------------------------
#-----------Tasks--------------


