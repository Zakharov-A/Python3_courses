# import time
#
# def getNOD(a, b):
#     while a != b:
#         if a > b: a-= b
#         else: b -= a
#     return a
#
# def testTime(fn):
#     def wrapper(*args):
#         st = time.time()
#         fn(*args)
#         dt = time.time() - st
#         print(f"Время работы: {dt} сек")
#     return wrapper
#
# test1 = testTime(getNOD)
# test1(100000, 2)

#------------

# import time
#
#
# def getNOD(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# def testTime(fn, *args):
#     st = time.time()
#     fn(*args)
#     dt = time.time() - st
#     print(f"Время работы: {dt} сек")
#
#
# testTime(getNOD, 100000, 2)

#--------------------


# import time
#
# def getNOD(a, b):
#     while a != b:
#         if a > b: a-= b
#         else: b -= a
#     return a
#
# def getFastNOD(a, b):
#     if a < b: a,b = b,a
#     while b: a,b = b, a%b
#     return a
#
# def testTime(fn):
#     def wrapper(*args, **kwargs):
#         st = time.time()
#         fn(*args, **kwargs)
#         dt = time.time() - st
#         print(f"Время работы: {dt} сек")
#     return wrapper
#
# test1 = testTime(getNOD)
# test2 = testTime(getFastNOD)
# test1(100000, 2)
# test2(100000, 2)

#------------

# import time
#
# def testTime(fn):
#     def wrapper(*args, **kwargs):
#         st = time.time()
#         res = fn(*args, **kwargs)
#         dt = time.time() - st
#         print(f"Время работы: {dt} сек")
#         return res
#     return wrapper
#
# @testTime
# def getNOD(a, b):
#     while a != b:
#         if a > b: a-= b
#         else: b -= a
#     return a
#
# @testTime
# def getFastNOD(a, b):
#     if a < b: a,b = b,a
#     while b: a,b = b, a%b
#     return a

# getNOD(100000,2)
# getFastNOD(100000, 2)

# res = getNOD(100000,2)
# print(res)

#---Tasks----

#--Task--1--

# import time
#
# s=int(input('введите число: '))
#
# def u(s):
#
#     d=[]
#
#     for i in range(s+1):
#
#         if i%2==0:
#
#             d.append(i)
#
#     return print(d)
#
#
#
# def us(s):
#
#     q=[i for i in range(s+1) if i%2==0]
#
#     return print(q)
#
#
#
# def tim(uss):
#
#     def warpp(*args):
#
#         s=time.time()
#
#         uss(*args)
#
#         d=time.time()-s
#
#         print(f'время работы {d} сек')
#
#
#
#     return warpp
#
#
#
# t=tim(u)
#
# t1=tim(us)
#
# t(s)
#
# t1(s)

#--Task--2--

# def cache(fn):
#
#     d = {}
#
#
#
#     def wrapper(k):
#
#         if d.get(k):
#
#             print(f'Есть {d[k]}')
#
#         else:
#
#             d[k] = fn(k)
#
#             print(f'Нет {d[k]}')
#
#         return d
#
#
#
#     return wrapper
#
#
#
#
#
# @cache
#
# def sq(x):
#
#     return x ** .5
#
#
#
#
#
# print('"stop" для выхода')
#
# x = input('Вычислить корень из числа: ')
#
# while x != 'stop':
#
#     sq(int(x))
#
#     x = input()