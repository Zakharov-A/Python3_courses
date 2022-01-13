#lst = ["Москва", "Санк-Петербург", "Тверь", "Казань"]
#for city in lst:
    #print(city, type(city))
    #city = "новое значение"
#print(lst)
#digs = [-1, 0, 5, 3, 2, 6]
#for x in range(len(digs)):
    #digs[x] **= 2 #digs[x] = digs[x]**2
#print(digs)

#digs = [0]*100
#N = 0; x = 0
#while x >= 0:
    #x = int(input("Введите целое число: "))
    #digs[N] = x
    #if x >= 0: N += 1
    
#s = 0
#or x in range(N):
    #s += digs[x]
#s = s/N;

#print("s = %f, N = %d"%(s,N))

#Задания к уроку

#Задание №1

#lst=[-1,0,5,3,2]
#for x in range(len(lst)):
    #lst[x]+=7.2
#print(lst)

#Задание №2

#x = input('Введите числа через пробел :').split()
#lx = []
#for w in x:
    #if w.isdigit():
        #lx.append(int(w)),lx.append(int(w))
    #else:
        #lx.append(w),lx.append(w)

#print(lx)

#Задание №3

#a=[1,2,3,4,5,6]; b=[1,0,0,1,1,1]
#c=[0]*6
#print(a,b,c)
#for x in range(len(c)):
    #c[x]=b[x]+a[x]
#print(c)    
    

#Задание №4

x = int(input("Введите количество элементов списка: "))
lst = [0]*x   #Создаем пустой список с введонной длиной

for i in range(x): #Заполняем список
    lst[i] = input('Введите элемент списка:  ')

print(lst)

if '5' in lst: # Ищем нужное значение в списке
    print('В списке присутствует цифра 5.')
else:
    print('В списке цифры 5 нет.')
   



    
    
