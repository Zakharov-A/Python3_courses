n = int(input())
amount = 0
for i in range(n):
    num = float(input())
    amount += num

average = amount / n
print(f'{average:.2f}')

