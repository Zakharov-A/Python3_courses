num: str = (input())
count = 0
while count < 5:
    if '.' in num:
        break
    print(num)
    num: str = input()
    count += 1
