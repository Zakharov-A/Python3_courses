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


# x = input("x: ")
# y = input("y: ")
# try:
#     x = int(x)
#     y = int(y)
#
#     res = x/y
# except:
#     print("Произошло исключение")
# else:
#     print("Исключений не произошло")
# finally:
#     print("finally выполняется всегда")
#
# print(res)

#------------------------------------------
#-----------Tasks--------------

#  Задание 1

# try:
#
#     lst = list(map(int, input("Введите числа через запятую:  ").replace(",", '').split()))
#
#     print(lst)
#
# except ValueError:
#
#     print("Невозможно преобразовать нечисловое значение в int")
#
# finally:
#
#     print("Задание 1 успешно.")

#--------------------------------------------------

# Задание 2 (среднее арифметическое)



# lst = input("Введите числа через пробел или запятую:  ").replace(",", " ").split()
#
# def aver(x):
#
#     try:
#
#         return sum(map(int, lst))/len(lst)
#
#     except ZeroDivisionError as z:
#
#         return z
#
#     except ValueError as v:
#
#         return v
#
#     except:
#
#         print("Произошло неизвестное исключение")
# print("Средним арифметическим является: ")
# print(aver(lst))
#---------------------------------------------------


# task 3
def func(x):

    for i in range(len(x)):

        yield x.pop()

s = {4, 2, 5, 8, 9, 6, 4, 5, 7}

print(s)



it = func(s)

while True:

    try:

        print(next(it))



    except StopIteration:

        print("множество закончилось")

        break
