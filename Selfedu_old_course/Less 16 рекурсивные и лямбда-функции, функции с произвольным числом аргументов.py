#def pow(x, n):
#    if n == 0:
#        return 1
#    else:
 #       return x*pow(x, n-1)

#print( pow(2, 5) )

#a = [-5, 6]
#for x in range(*a):
#    print(x, end=" ")

#def myFunc(*args):
 #   for arg in args:
  #      print(arg)
#myFunc(1,3,"Helo")        

#def myFunc(x, y, *lst, sep="sep", end="end", **args):
#    print(sep, end)
#    for name, value in args.items():
#        print(name, value)


#def myFunc(*ist, sep="sep", end="end", **args):
#    print(sep, end)
#    for name, value in args.items():
#        print(name, value)
    
#def mySum(*args):
#    s = 0
#    for arg in args:
 #       s += arg
 #   return s

#myFunc(1,2,3, sep="&", arg1=1, arg2=2, arg3=3)


def showElements(lst, func):
    for x in lst:
        if func(x):
            print(x)

def __odd(x):
    return True if x%2 != 0 else False

a = [1,2,3,4,5,6,7]
showElements(a, lambda x: True if x%2==0 else False)

#showElements(a, __odd)



