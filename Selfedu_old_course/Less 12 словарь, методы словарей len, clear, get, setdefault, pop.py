#d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
#for x in d.values():
    #print(x)

d = {True: 1, False: "Ложь", "list": [1,2,3], 5: 5}
for x in d.items():
    print(x[0], x[1])

