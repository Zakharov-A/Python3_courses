# def sq(x):
#     return x, x**2
#
# lst = [1,-2,3,-4,-5]
#
# b = map(sq, lst)
# a = list(b)
# print(a)

# def sq(x):
#     return x, x**2
#
# lst = ["Москва", "Рязань", "Смоленск", "Тверь", "Томск"]
#
# b = map(len, lst)
# a = list(b)
# print(a)

# def sq(x):
#     return x, x**2
#
# lst = ["Москва", "Рязань", "Смоленск", "Тверь", "Томск"]
#
# b = map(str.upper, lst)
# a = list(b)
# print(a)


# def sq(x):
#     return x, x**2
#
# lst = ["Москва", "Рязань", "Смоленск", "Тверь", "Томск"]
#
# b = map(lambda x: x[::-1], lst)
# a = list(b)
# print(a)

# def sq(x):
#     return x, x**2
#
# lst = ["Москва", "Рязань", "Смоленск", "Тверь", "Томск"]
#
# b = map(lambda x: x.replace("а", "А"), lst)
# a = list(b)
# print(a)

# def sq(x):
#     return x, x**2
#
# lst = ["Москва", "Рязань", "Смоленск", "Тверь", "Томск"]
#
# b = map(lambda x: x.replace("а", "А"), lst)
# c = map(sorted, b)
# a = list(c)
# print(a)

# a = list(map(int, input().split(";")))
# print( a )

# def odd(x):
#     return x%2
# a=[1,2,3,4,5,6,7,8,9,10]
#
# b = filter(odd, a)
# print(b)
# for x in b:
#     print(x, end=" ")

#
# def odd(x):
#     return x%2
# a=[1,2,3,4,5,6,7,8,9,10]
#
# b = list(filter(odd, a))
# print(b)



# a=[1,2,3,4,5,6,7,8,9,10]
#
# b = list(filter(lambda x: x%2, a))
# print(b)

# a=[1,2,3,4,5,6,7,8,9,10]
#
# b = list(filter(lambda x: not x%2, a))
# print(b)

# lst = ["Москва", "Рязань1", "Смоленск", "Тверь2", "Томск"]
#
# b = list(filter(str.isalpha, lst))
# print(b)

# a = [1,2,3,4]
# b = [5,6,7,8]
#
# it = zip(a, b)
# print( list(it ) )

# a = [1,2,3,4]
# b = [5,6,7,8]
# c ="abracadabra"
#
# it = zip(a, b, c)
# print( list(it ) )

# Tasks