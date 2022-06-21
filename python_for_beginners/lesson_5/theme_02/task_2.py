text = input()
repetitions = int(input())
first = int(input())
last = int(input())
if last < 0:
    last -= 1
else:
    last += 1
step = int(input())

line = ''
for _ in range(repetitions):
    line += text

for i in range(first, last, step):
    print(f'{i}_{line}')

