# def test_func(red):
#     print(red, end="")
#     print("!")
#
#
#
# test_func("Hi")
# test_func(6)
# test_func(6)

# def summa(a, b):
#         return a + b
#
# res = summa(5.5, 7.5)
# print(res)
# print(summa("Hi ", "Dendy"))


#----Код без Функции----

# nums_1 = [5, 6, 2, 7, 9, 4]
#
# min = nums_1[0]
# for el in nums_1:
#     if el < min:
#         min = el
#
# print(min)
#
# nums_1 = [5, 6, 2, 7, 9, 5.3, 4]
#
# min2 = nums_1[0]
# for el in nums_1:
#     if el < min2:
#         min2 = el
#
# print(min2)

#----Код с функцией----
#
# def minlist(lis):
#     min_num = lis[0]
#     for el in lis:
#         if el < min_num:
#             min_num = el
#     print(min_num)
#
# nums_1 = [5, 6, 2, 7, 9, 4]
# minlist(nums_1)
#
# nums_2 = [5, 6, 2, 1, 7, 9, 5.3, 4]
# minlist(nums_2)

#----Код с функцией и переменной----
#
# def minlist(lis):
#     min_num = lis[0]
#     for el in lis:
#         if el < min_num:
#             min_num = el
#     return min_num
#
# nums_1 = [5, 6, 2, 7, 9, 4, -12]
# mi1 = minlist(nums_1)
#
# nums_2 = [5, 6, 2, 1, 7, 9, 5.3, 4]
# mi2 = minlist(nums_2)
#
# print(mi1 + mi2)
# if mi1 < mi2:
#     print(mi1)
# else:
#     print(mi2)

#----lambda функция----
func = lambda x, y: x * y
rere = func(5, 3)
print(rere)