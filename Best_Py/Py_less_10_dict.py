# country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# country = dict (code='RU', name='Russian')
# print(country['code'])

#----Создание и вывод словаря----
# country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# print(country)

#----Перебор словаря с помощью функций----
# country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# print(country.items())

#
# for key, value in country.items():
#     print(key, " - ", value)

#----Функции в словарях----

# country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# print(country['code'])
# print(country.get('name'))
# country.clear()
# country.pop('name')
# country.popitem()

# print(country.keys())
# print(country.values())
# print(country.items())
# country['code'] = 'None'
# print(country.items())

#----Описание объекта с помощью словарей----

person = {
    'user_1': {
        'first_name': 'John',
        'last_name': 'Stoun',
        'age': 45,
        'address': ['moscow city', 'meat street', '33'],
        'grades': {'math': 5, 'physics': 3}
    },
    'user_2': {

    }
}

print(person['user_1']['address'][1])