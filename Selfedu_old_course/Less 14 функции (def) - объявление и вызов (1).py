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
    #print(x)
    #return x

#print( myAbs(-5) )
#print( myAbs(15) )
#a = 100
#print( myAbs(a) )

#--------------


#def sayHello(msg, end="!", sep=": "):
    #print("Message"+sep+msg+end)
    
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
    #sx = 1
    #while n >0:
        #sx *= x
        #n -= 1
    #return sx

#def sayHello():
    #print("hello")

#def sayHello():
    #print("-----hello-----")

#def sayHello(msg):
    #print(msg)    


#sayHello("redred")

#---------------
# Следующий пример

#TYPE_FUNC = False

#if TYPE_FUNC:
    #def sayHello():
        #print("hello")
#else:
    #def sayHello(msg):
        #print(msg)
        
#sayHello("Ha ha ha")

def max2(a, b):
    if a>b:
        return a
    else:
        return b
def max3(a, b, c):
    return max2(a, max2(b, c))
    
print( max3(2, -3, 5) )
print( max3("ab", "cd", "abc"))


 



