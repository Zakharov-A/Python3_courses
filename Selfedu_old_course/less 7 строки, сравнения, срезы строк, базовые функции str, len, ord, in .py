#Первый пример

#psw = "pass"
#in_psw = ""
#while psw != in_psw:
    #in_psw = input("Введите пароль: ")
#print("Вход в систему разрешен")

#Задания к уроку

# задача №1
#print('abrakadabra'.count('a'))


# задача №2
#print('abrakadabra'.replace('ab', ''))

# задача №3
#x = input('Введи слово: ')
#print('Это слово-палиндром!' if x.lower() == x[::-1].lower() else 'Обычное слово.')

# Задача №4
#print('abrakadabra'.count('ra'))

# Задача №5
#print(input('Введи предложение через пробел: ').replace(' ', '\n'))


#Примеры к заданию 1
print('Руководство по выживанию для создателей нейрочипов'.count('о'))
print('Руководство по выживанию для создателей нейрочипов'.count('ов'))

#Примеры к заданию 2

print('Руководство по выживанию для создателей нейрочипов'.replace('для', '').replace('Ру', 'Ка'))


#Примеры к заданию 3

x = input('Enter a word:  ')
print('This word is palindrome!' if x.lower() == x[::-1].lower() else 'Common word.')
