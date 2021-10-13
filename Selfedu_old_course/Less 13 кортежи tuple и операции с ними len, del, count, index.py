

    
#print(dict([[i, int(i)**2] for i in input('Введи числа через пробел: ').split() if int(i) % 2 == 0]))




#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#for elem in a:
    #if elem < 5:
        #print(elem)
#print([elem for elem in a if elem < 5])

#Решение задачи 1 урока 12
#Задача 1
#d = {}
#for n in input("Введите числa через запятую: ").replace(","," ").split():
    #n = int(n)
    #if n%2 == 0:
        #d.setdefault(n, n**2)

#print(d)

#Задача 2


#a='int=целое число, dict=словарь,  list=список, str=строка, bool=булевый тип'
#lst=a.split(',')
#print (a)
#lst2=[]
#for e in lst:
    #lst2.append(e.split('='))
#d=dict(lst2)
#print(d)


#Задача 3

d = {}
n = int(input("Сколько слов будете переводить:"))
for i in range(n):
    d.setdefault(
        input(f"Введите {i+1} слово на англ:"),
        input("Введите все возможные переводы через запятую:").split(","))
print(d)




#Решение задачи 1 урока 13
#p=("+792345678", "+792345478", "+92345478", "+592345678", "+392345678", "+7923456558")
#print([x for x in p if x.find('+7') == 0])

#решение задачи 2 урока 13

#a = "Оценки: 5, 4, 3, 4, 2, 4, 5, 4"
#b = a.split(": ")[1].split(', ')
#d = []
#c = tuple(b)
#for i in c:
    #d.append(int(i))
#f = tuple(d)

#print(f)

 # Решение задачи 3 урока 13
 
#a = ((1,2,3),(4,5,6),(7,8,9))
#for i in range(len(a)):
    #z = a[i]
    #print(z[0],'-',z[1],'-',z[2])
    
