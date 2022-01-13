import pickle

with open('dict.bin', 'rb') as file:
    dictonary = pickle.load(file)

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

    print(dictonary)



def delete_word():

    k = input('Введи английское слово: ')

    if k in dictonary.keys():

        del dictonary[k]

        print('Удалено')

    else:

        print('Нет такого слова')



def save_file():

    with open('dict.bin', 'wb') as file:

        pickle.dump(dictonary, file)