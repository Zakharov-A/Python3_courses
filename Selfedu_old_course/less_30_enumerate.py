# a = [1, 3, 4, 2, -5, 0, 11]
# i = 0
# for x in a:
#     if x % 2 == 0:
#         a[i] += 1
#         i += 1
#
# print(a)

# -----------------------

# a = [1, 3, 4, 2, -5, 0, 11]
# for i, x in enumerate(a):
#     if x % 2 == 0:
#         a[i] += 1
#
# print(a)

# -------------------------

# a = [1, 3, 4, 2, -5, 0, 11]
# for e in enumerate(a):
#     print(e)

# -------------------------
#
# def enumerate2(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1
#
# a = [1, 3, 4, 2, -5, 0, 11]
# g = enumerate(a)
# print(next(g))
# for e in enumerate2(a, 1):
#     print(e)


# -------------------------

# for i in enumerate(["hello", "world"]):
#     print(i)

#--------------------------

# c = {1: 'a', 2: 'b', 3: 'c'}
# for i in enumerate(c):
#     print(i)
#-------------------------

# s = {1,2,3,4,5,4,4,4}
# for i in enumerate(s):
#     print(i)

#--------------------------

#--feat--1--
# Имеется упорядоченный список

# Перебрать все элементы этого списка с помощью функций enumerate и элементы,

# стоящие на главной диагонали (имеющие равные индексы), превратить в нули.



# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in enumerate(A):
#
#     for j in enumerate(i[1]):
#
#         if j[0] == i[0]:
#
#             A[i[0]][j[0]] = 0
#
# print(A)

#--feat--2--




#--feat--3--


