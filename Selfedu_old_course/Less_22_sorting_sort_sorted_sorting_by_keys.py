# def funcSort(x):
#     return x%2
#
# a=[1,4,3,6,5,2]
# print( sorted(a, key=funcSort))

# a=[1,2,4,-1,-4,-2,6,50,10,102]
# a = sorted(a, reverse=True)
# print(a)

# def funcSort(x):
#     return x%2
#
# a=[1,4,3,6,5,2]
# print( sorted(a, key=funcSort) )

# def funcSort(x):
#     if x%2 ==0:
#         return x
#     else:
#         return x+100
#
# a=[1,4,3,6,5,2]
# print( sorted(a, key=funcSort) )

# a=[1,4,3,6,5,2]
# print( sorted(a, key=lambda  x: x%2) )

# lst = ["Москва", "Тверь", "Смоленск", "Псков", "Рязань"]
# # print( sorted(lst, key=len ))
# print( sorted(lst, key=lambda x: x[-1] ) )
# print( sorted(lst, key=lambda x: x[0] ) )

# books = {
#     ("Увгений Онегин", "Пушкин А.С.", 200),
#     ("Муму", "Тургенев И.С.", 250),
#     ("Мастер и Маргарита", "Булгаков М.А.", 500),
#     ("Мертвые души", "Гоголь Н.В.", 190)
# }
# print( sorted(books, key=lambda x: x[2]) )

#Задания

# 1 задача


#
# a = [1, 2, -5, 0, 5, 10]
#
# print((sorted(a))[:3]) # [-5, 0, 1]

# 2 Задача
# digs=[-10,0,7,-2,3,6,-8]
#
# print(sorted(digs,key=lambda x:x>0))

# 3 задача

numb = {'+7': 2345678901, '+4': 3456789012, '+5': 5678901234, '+12': 78901234}
keys = sorted(numb, key = lambda x: int(x[:]))
for key in keys:
  print(key,numb.get(key))
