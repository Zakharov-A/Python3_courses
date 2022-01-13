dictonary ={'apple': 'яблоко',

            'lemon': 'лимон',

            'orange': 'апельсин'}



def translate_word():

    k = input('Введи английское слово: ')

    if k in dictonary.keys():

        print(dictonary[k])

    else:

        print('Нет такого слова')



def add_word():

    k = input('Введи английское слово: ')

    v = input('Введи перевод: ')

    dictonary[k] = v

    print('Добавлено')



def delete_word():

    k = input('Введи английское слово: ')

    if k in dictonary.keys():

        del dictonary[k]

        print('Удалено')

    else:

        print('Нет такого слова')
