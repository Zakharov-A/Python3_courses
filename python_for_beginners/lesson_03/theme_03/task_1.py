x = int(input())

if x < 80:
    res = 'xs'
elif x < 100:
    res = 's'
elif x < 150:
    res = 'm'
elif x < 180:
    res = 'l'
else:
    res = 'xl'
print(res)
