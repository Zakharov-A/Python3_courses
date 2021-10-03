#A=[]
#N=10
#for x in range(N):
    #A.append(x**2)

#print(A)


#N=10

#A = [x**2 for x in range(N)]

#print(A)


#A = []
#N=10

#for x in range(N):
    #if x%2 == 0:
        #A.append(x**2)
        
#print(A)

#A = []
#N=10

#A = [x**2 for x in range(N) if x%2 == 0]

#print(A)

#cities = ["Москва", "Тверь", "Рязань", "Ярославль", "Владимир"]
#A = [city for city in cities if len(city) < 7]
#print(A)

#x = int(input("Введите целое положительное число:  "))
#digs = []
#while x:
    #digs.append(x%10) #берем последнюю цифру числа
    #digs = [x%10] + digs
    #x = x//10         # отбрасываем последнюю цифру цисла
#print(digs)


# программа reverse
#N = 11
#A = list(range(N))
#print(A)

#for i in range(N//2):
    #A[i], A[N-i-1] = A[N-i-1], A[i]

#print(A)

# сортировка методом выбора

A = [2, 2, -1, -5, 55, 34, 0, 10]
N = len(A)
for i in range(N-1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

print(A)




