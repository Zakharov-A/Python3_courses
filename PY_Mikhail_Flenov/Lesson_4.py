# elist = []

# elist = [21, 421, 873, 6783, 87, 12]

# for n in elist:
#     print(n)
# ----

# workdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# for t in workdays:
#     print(t)

# print('______\n')

# workdays.append(123)
# workdays.insert(3, 'in')
# for n in workdays:
#     print(n)

# ----


dict = {'cat' : 'Кошка', 'dog' : 'Собака', 'duck' : 'Утка' }
dict['table'] = 'Стол'
dict['cat'] = 'Кот'
# print(dict['cat'])

for key in dict:
    print(f'{key} это {dict[key]}')