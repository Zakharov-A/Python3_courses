import random

N, M = (5, 10) # размер игрового поля NxN и число мин M

def getTotalMines(PM, i, j):
    n = 0
    for k in range(-1,2):
        for l in range(-1,2):
            x = i+k
            y = j+1
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            if PM[x*N+y] < 0:
                n += 1
    return n                
            
     
def createGame(PM):
    """Создание игрового поля: расположение мин
       и посчет числа мин вокруг клеток без мин
    """
    rng = random.Random()
    
    n = M
    while n > 0:
        i = rng.randrange(N) # случайное целое [0; N]
        j = rng.randrange(N)
        if PM[i*N+j] != 0:
            continue
        PM[i*N+j] = -1
        n -= 1
        
    # вычисляем количество мин вокруг клетки
    for i in range(N):
        for j in range(N):
           if PM[i*N+j] == 0:
                PM[i*N+j] = getTotalMines(PM, i, j)
        
def show(pole):
    """Функция отображениясостояния текущего
       игрового поля 
    """
    for i in range(N):
        for j in range(N):
            print( str(pole[i*N+j]).rjust(3), end="" )
        print()

def goPlayer():
    """Функция отображения состояния
    текущего игрового поля 
    """
    flLoopInput = True
    while flLoopInput:
        x, y = input("Введите через пробел 2 координаты: ").split()
        if not x.isdigit() or not y.isdigit():
            print("Координаты введены не верно")
            continue

        x = int(x)-1
        y = int(y)-1

        if x < 0 or x >= N or y < 0 or y >= N:
            print("Координаты выходят за приделы поля ")
            continue

        flLoopInput = False
    return(x,y)            
        
def isFinish(PM, P):
    """Определение  текущего состояния игры:
       выиграли, проиграли, игра продолжается 
    """
    for i in range(N*N):
        if P[i] != -2 and PM[i] < 0: return -1

    for i in range(N*N):    
        if P[i] == -2 and PM[i] >= 0: return 1
    return -2    
        
def startGame():
    """Функция запуска игры: отображает игровое поле,
       игрок открывает любую клетку, результат проверяется на
       наличие мины или выиграшной ситуации
    """
    P = [-2]*N*N
    PM = [0]*N*N
    
    createGame(PM)
    
    finishState = isFinish(PM, P)
    while isFinish(PM, P) > 0:
        show(P)
        x,y = goPlayer()
        P[x*N+y] = PM[x*N+y]
        finishState = isFinish(PM, P)
        
    return finishState

res = startGame()
if res == -1:
    print("Вы проиграли")
else:
    print("Вы выиграли")
    
print("Игра завершена")

    
    

        



