import time

def getNOD(a, b):
    """Вычисляется НОД для натуральных чисел a и в
        по алгоритму Евклида.
        Возвращает вычисленный НОД.
    """    
    if a<b:
        a,b = b,a
    while b>0:
        a,b = b, a%b
        
    return a

print( getNOD(45, 9) )

def testNOD():
    #--test 1---------
    a=28; b=35
    res = getNOD(a,b)
    if res == 7:
       print("#test1 - ok")
    else:
        print("#test1 - fail")
        
        
     #--test 2---------
    a=100; b=1
    res = getNOD(a,b)
    if res == 1:
        print("test2 - ok")
    else:
        print("#test2 - fail")

    #--test 3---------
    a=2; b=100000000

    st = time.time()
    res = getNOD(a,b)
    et = time.time()
    dt = et-st

    
    if res == 2 and dt <1:
        print("test13 - ok")
    else:
        print("#test13 - fail")
        
testNOD()


        
        
