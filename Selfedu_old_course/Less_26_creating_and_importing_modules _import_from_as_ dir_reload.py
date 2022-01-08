#!/usr/bin/python
# coding=utf-8
# import math, random, time
#
# res = math.cos(0.7)
# print(res)

#--------------------

# import mymath
#
# m = mymath.sum(1,2,3)
# print(m)
#
# print(mymath.PI)

#-------------------

# from lib.mymath import PI, sum as my_sum
#
# m = my_sum(1,2,3)
# print(m)
#
# print(PI)

#--------------------

# import mymath
#
# mymath.PI = 3
#
# from importlib import reload
# reload(mymath)
#
# print(mymath.PI)

#---------------------

# import mymath
#
# mymath.PI = 3
#
# import importlib
# importlib.reload(mymath)
#
# print(mymath.PI)

#--------------------

# from mymath import PI
#
# import mymath
#
# PI = 3
#
# print(PI, mymath.PI)

#---------------------

# from mymath import  ar
# import  mymath
#
# ar += (10,)
#
# print(ar, mymath.ar, sep="\n")

#-----------------------

# import  mymath
# print( dir(mymath) )

#-----------------
#--Tasks----------

#--Task-1----

# import module
#
# try:
#
# 	x, y = map(float,input("Введите через пробел длины cторон прямоугольника: ").split())
#
# 	print("Периметр прямоугольника: %f"% module.perim(x, y))
#
# 	print("Площадь прямоугольника: %f"%  module.square(x, y))
#
# except ValueError:
#
# 	print("Числа введены в неправильном формате")

#----Task-2---

# from module2 import *
#
#
#
# while True:
#
#     print('************************')
#
#     print('* 1: Перевести слово   *')
#
#     print('* 2: Добавить слово    *')
#
#     print('* 3: Удалить слово     *')
#
#     print('* 4: Завершить работу  *')
#
#     print('************************')
#
#
#
#     x = int(input('Выбери пункт меню: '))
#
#     if x == 1:
#
#         translate_word()
#
#     elif x == 2:
#
#         add_word()
#
#     elif x == 3:
#
#         delete_word()
#
#     elif x == 4:
#
#         print('Конец программы..')
#
#         break

#----Task-3---не работает

from module3 import *



while True:

    print('************************')

    print('* 1: Перевести слово   *')

    print('* 2: Добавить слово    *')

    print('* 3: Удалить слово     *')

    print('* 4: Завершить работу  *')

    print('************************')



    x = int(input('Выбери пункт меню: '))

    if x == 1:

        translate_word()

    elif x == 2:

        add_word()

    elif x == 3:

        delete_word()

    elif x == 4:

        save_file()

        print('Конец программы..')

        break