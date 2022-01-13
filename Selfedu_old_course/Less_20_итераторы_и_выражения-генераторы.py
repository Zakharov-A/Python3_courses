# lst = (x for x in range(1000000000))
# for i in lst:
#      print(i, end=" ")
#      if i > 100: break
#
# print("\nnew \nloop")
#
# for i in lst:
#      print(i, end=" ")
#      if i > 200: break


#---------


def getAllAverage(N):
     count = 0
     S = 0
     for i in range(1,N+1):
          count += 1
          S += i
          yield S/count
it = getAllAverage(10)
print( next(it) )
print( next(it) )
print( next(it) )
print( next(it) )
print( next(it) )
print( next(it) )
print( next(it) )


# def f ():
#      for x in range(10):
#           yield x
# s = f()
# print( s )
# print( next(s) )
# print( next(s) )
# print( next(s) )
