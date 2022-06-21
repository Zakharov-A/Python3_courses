text = input()
repetitions = int(input())
rows = int(input())

line = ''
for _ in range(repetitions):
    line += text

for _ in range(rows):
    print(line)


