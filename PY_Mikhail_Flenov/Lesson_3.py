


# ----
# d = 1; index = 20

# if d > 0 and index == 20 or index == 30:
#     print("wow")
# ----

# ----
# s1 = 'это строка'
# s2 = "Это тоже строка"
# i = str(10)
# n = 9

# s = s = s1 + str(n)
# print(s)

# print(s1[2:9])

# for ch in s1:
#     print(ch)
# ----

# ----
# s1 = 'это строка'
# s2 = "Это тоже строка"
# i = 10
# print('This is a string ' + s1 + ' and ' + s2)
# print(f'This is a string {s1} and {s2}')
# print(f'This is a string {i + 4}')
# print('This is a string {m1} and {m2}'.format(m1 = s1, m2 = s2))
# ----

# ----

for i in range(0, 9):
    str = ''
    for j in range(0, 9):
        str += f'{i}{j} '
    print(str)    