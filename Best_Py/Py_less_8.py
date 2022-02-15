# word = 'riddick'
# print(word[1])
# print(word.count('i'))   # количество символов в word
# print((word.upper()))    # word заглавными
# print(word.isupper())    # word в нижнем ригистре
# print(word.capitalize())  # с заглавной
# print(word.find('d'))  # Найти по значению
#
# list = 'football, basketball, skate'
# print(list.split(', '))      # делит на список по символу
#
# hobby = list.split(', ')
# print(hobby[2])
#
#
# for el in range(len(hobby)):
#     hobby[el] = hobby[el].capitalize()

# print(hobby)

# result = "| ".join(hobby)
#
# print(result)

#----Срезы(slices)----

# slice = 'Football'
# print(slice[0:4])              #
# print(slice[4:])
# print(slice[2:-2])
# print(slice[1:-1:2])           # добавляет шаг через одну
# print(slice[1::3])

lis = [6, 7, 10, "faka", True, 10.34, [2, 3, 4]]
print(lis[2:])
print(lis[2:5:2])
print(lis[::-1])
print(lis[::2])