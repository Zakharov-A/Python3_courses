#s=0; i=10
#while i < 100 :
    #if i == 0: break
    #s += 1/i
    #i=i+1
#else:
    #print("Сумма вычеслена корректно")
#print(s)


# break - досрочное завершение цыкла (любого)
# continue - пропуск последующих операторов тела цикла и
# переход к следующей итерации

# целые числа от -4 до 4 (кроме 0)
#s=0; i=-5
#while i < 4 :
    #i=i+1
    #if i == 0: continue
    #print(i)
    #s +=1/i
#print(s)


#for x in 1,5,2,4:
    #print(x**2)

#for x in range(5,0,-1):
    #print(x)


 # range(start, stop, step)

#s=0
#for i in range(1, 1001, 1):
    #s += 1/i
#print(s)

#k = 0.5; b = 2
#lst = [0, 0.1, 0.2, 0.3, 0.4, 0.5,]
#for x in lst:
    #print(x*k+b)

#msg = "Hello World"
#for x in msg:
    #print(x)

#A = [ [1,2,3], [4,5,6] ]
#N=2; M=3
#for i in range(N):
    #for j in range(M):
        #print(A[i][j], end='')
    #print()

S=0; M=10; N=5
for i in range(1,N+1):
    for j in range(1,M+1):
        S += i*j
print(S)








    

