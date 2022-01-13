#d = {"house": "дом", "car": "машина",
     #"tree": "дерево", "river": "река",
     #"road": "дорога"}
#print(d)
#print(d["house"])


#d2 = dict(house = "дом", car = "машина",
          #tree = "дерево", road = "дорога",
          #river = "река")
#print(d2)

#a = dict.fromkeys(["+7", "+6", "+5", "+4"], "Code of the country")
#print(a)


#d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
#for x in d:
 #print(x, d[x])


#d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
#d.setdefault(3, "three")
#print(d)
#d2 = d.pop(3)
#print(d2)

#d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
#for x in d.items():
    #print(x[0], x[1])


#d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
#for x in d.keys():
 #print(x, d[x])

#d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
#for x in d.values():
 #print(x)


#d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
#for x in d.items():
 #print(x[0], x[1])

#d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
#for key, value in d.items():
 #print(key, value)

#Задания
# Задание №1 
#print(dict([[i, int(i)**2] for i in input('Введи числа через пробел: ').split() if int(i) % 2 == 0]))

#Задание №2

#s = 'int=целое число, dict=словарь, list=список, str=строка, bool=булевый тип'

#d = [i.split('=') for i in s.split(',')]

#q = dict(d)

#print(q.keys())

#Задание №3

d={} # Создаём пустой словарь
A=int(input("Введите кол-во английских слов для перевода:  "))
B=int(input("Введите кол-во переводов для каждого английского слова: "))
for x in range (A):
 aword=input("Введите английчкое слово:  ")
 value=[]#Создаём пустой список переводов в конце каждого цикла ввода английских слов
 for j in range(B):
  Translation=input("Введите перевод:  ")
  value=value+[Translation];# Формируем список переводов для каждого английского слова
  d[aword]=value;# Создаём словaрь в котором ключ=английское слово, а значение этого ключа = список переводов
print(d)




  


