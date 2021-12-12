# exercise 1
def u(q, w):
    if q<w:
        q, w= w, q
    if q%w==0:
        return w
    else:
        return u(q,q%w)

print(u(24, 8))

# exercise 2
#нахождение максимального числа
def u(s):
    if len(s) == 1:
        return print('макс',s[0])
    elif s[0] > s[1]:
        s[0], s[1] = s[1], s[0]

    return u(s[1:])
d = [901, 17, 5, 3, 103, 5, 9, 7, 99, 170]

u(d)

# exercise 3
#нахождение минимального числа
def u(s):
    if len(s) == 1:
        return print('мин',s[0])
    elif s[0]< s[1]:
        s[0], s[1] = s[1], s[0]

    return u(s[1:])

d = [945, 17, 5, 3, 999, 5, 9, 7, 99, 170]
u(d)
ответ :3
