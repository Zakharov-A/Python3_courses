
#Задача 1


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
 

#Задача на вывод чисел из списка.
 
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for DD in a:
    #if DD < 5:
        #print(DD)
        
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for DD in a:
    #if DD > 5:
        #print(DD)

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#print(list(filter(lambda elem: elem > 5, a)))

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#print([elem for elem in a if elem > 5])

#Вернуть список, который состоит из элементов, общих для этих двух списков.
 
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];

#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55, 12, 13]

#result = list(filter(lambda elem: elem in b, a)) 
#print(result)

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55, 12, 13]
#result = [elem for elem in a if elem in b]
#print(result)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x > 5:
        print(x, end = ",")

 
