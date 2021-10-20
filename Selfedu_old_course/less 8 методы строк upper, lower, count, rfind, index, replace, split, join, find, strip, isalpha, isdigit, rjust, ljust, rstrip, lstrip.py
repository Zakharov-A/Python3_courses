#Метод строки count

#msg = "abrakadabra"
#co = msg.count("ra")
#print(co)

#Метод строки replace

#msg = "abrakadabra"
#co = msg.replace("ab", "")
#print(co)

#a = "2+3+6.7+82+5.7+1"
#d = a.replace("+", "-")
#print(d)

#Метод строки count

#msg = "anananalala"
#sdf = msg.count('na')
#ert = msg.find('la')
#print(sdf, ert)

#Метод строки isgigit

#dig = input("Введите число: ")
#if(dig.isdigit()):
    #dig = int(dig)
    #print(dig)
#else:
    #print("Число введено неверно")

#Задания:


# Задание №1

#x = input('Введите телефонный номер в формате x(xxx)xxxxxxx:   ')
#print('Номер корректен!'if len(x) == 13 and x[0].isdigit()and x[1] == '('and x[2:5].isdigit()and x[5] == ')' and x[6:].isdigit() else 'Номер не корректен!')

# Задание №2

#print("2+3+6.7 + 82 + 5.7 +1".replace(' ','').replace('+', '-'))

# Задание №3

print("0; -100; 5.6; -3".replace(';', '\n'))


