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

# Задача 1

# lst = list('hello world!')
#
# voc = dict(h='х', e='е', l='л', o='о', w='в', r='р', d='д')
#
#
#
# a = map(lambda x: voc.get(x) if voc.get(x) is not None else x, lst)
#
# print(''.join(a))


# Задача 2

a="""Куда ты скачешь, гордый конь 

И где опустишь ты копыта? 

О мощный властелин судьбы! 

Не так ли ты над самой бездной, 

На высоте, уздой железной 

Россию поднял на дыбы?"""



a=a.split()



b=list(a[x] for x in range(len(a)) if  x%2!=0)

print(b)

# Задание 3

n=int(input("Введите целое число: "))

b=[i for i in range(1,n+1) if n%i==0]; print(b)
