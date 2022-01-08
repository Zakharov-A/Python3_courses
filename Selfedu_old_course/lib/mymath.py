PI = 3.1415

def max2(a,b):
    return a if(a > b) else b

def max3(a, b, c):
        return max2(a, max2(b,c))

def sum(*vals):
    print("lib")
    print("mysum")
    s = 0
    for x in vals:
        s += x
    return s
