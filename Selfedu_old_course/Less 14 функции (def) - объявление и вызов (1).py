#def sayHello():
    #print("hello")
#sayHello()
#print("----------------")
#sayHello()

#--------------------------------------    
#def sayHello():
    #print("hello")

#def myAbs(x):
    #x = -x if(x<0) else x
    #return x
#print( myAbs(-5) )
#print( myAbs(15) )
#a = 100
#print( myAbs(a) )


#val = myAbs(-5.8)
#print(val)

#def isPositive(x):
#    if x >= 0:
#        return x >= 0
#p = []
#for a in range(-5, 11):
#    if isPositive(a):
#        p.append(a)
#print(p)

#def sayHello(msg, end="!", sep=": "):
#    print("Message"+sep+msg+end)
    
#def getSquare(w, h):
#        return 2*(w+h)
#p = getSquare(10, 5.5)        
#print(p)
#sayHello("Hello", sep=" ")

#def perAndSq(w, h):
#    return 2*(w+h), w*h
#per, sq = perAndSq(2.3, 5)
#print(per, sq)

    
#def myAbs(x):
    #x = -x if(x<0) else x
    #return x
#def isPositive(x):
    #return x >= 0
#def perAndSq(w, h):
    #return 2*(w+h), w*h

#per, sq = perAndSq(2.3, 5)
#print(per, sq)
#---------------
# Следующий пример

#def myPow(x, n):
#    sx = 1
#    while n >0:
#        sx *= x
#        n -= 1
#    return sx
#p = myPow(3, 5)
#print(p)


#def sayHello():
#    print("hello")

#def sayHello():
#    print("-----hello-----")
#sayHello()    

#def sayHello(msg):
#    print(msg)    
#sayHello("qwerty")  

#sayHello("redred")

#---------------
# Следующий пример

#TYPE_FUNC = False

#if TYPE_FUNC:
#    def sayHello():
#        print("hello")
#else:
#    def sayHello(msg):
#        print(msg)
        
#sayHello(123)

# Следующий пример
#def max2(a, b):
#   if a>b:
 #       return a
  # else:
   #     return b

#print( max2(2, -3) )



#def max2(a, b):
#    if a>b:
#        return a
#    else:
#        return b
#def max3(a, b, c):
#    return max2(a, max2(b, c))
    
#print( max3(22, -3, 5) )
#print( max3("ab", "cdb", "abc"))

#Задания:
#Вывод чисел из списка:
#пример 1
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 
#for x in a:
#    if x > 8:
#        print(x, end = ",")
#пример 2
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#print(list(filter(lambda el: el > 8, a)))

#пример 3
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#print([el for el in a if el > 8])

#Вернуть общие значения из 2-х списков
#Вариант 1
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];

#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55, 12, 13]
#res = list(filter(lambda el: el in b, a))
#print(res)


#Вариант 2
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];

#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55, 12, 13]

#result = [elem for elem in a if elem in b]
#print(result)


#Вариант 3

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];

#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#result = list(set(a) & set(b))
#print(result)

#Задать и вызвать функцию, которая вычисляет площядь прямоугольника
#def Myfun(a, b):
#    c = (a*b)
#    return c
#d = Myfun(5, 4)
#print(d)

#Вычислить или площадь или периметр прямоугольника

# Необходимо создать функцию, которая в зависимости от значения формального параметра type будет вычислять

# или площадь или периметр прямоугольника



#Не выполнил

