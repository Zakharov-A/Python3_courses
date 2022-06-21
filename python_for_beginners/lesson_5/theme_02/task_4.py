n = int(input())

for _ in range(n):
    num = int(input())
    if num % 2 == 1 and num > 0:
        print(num)
    else:
        print(f'The number {num} is invalid.')

