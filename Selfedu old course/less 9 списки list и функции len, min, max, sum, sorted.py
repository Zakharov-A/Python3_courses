#lst = ["Москва", "Санк-Петербург", "Тверь", "Казань"]
#for city in lst:
    #print(city, type(city))
    #city = "новое значение"
#print(lst)
#digs = [-1, 0, 5, 3, 2, 6]
#for x in range(len(digs)):
    #digs[x] **= 2 #digs[x] = digs[x]**2
#print(digs)

digs = [0]*100
N = 0; x = 0
while x >= 0:
    x = int(input("Введите целое число: "))
    digs[N] = x
    if x >= 0: N += 1
    
s = 0
for x in range(N):
    s += digs[x]
s = s/N;

print("s = %f, N = %d"%(s,N))


    
    
