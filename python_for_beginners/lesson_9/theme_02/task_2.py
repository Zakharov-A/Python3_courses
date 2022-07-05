num: str = (input())
count = 0
while count < 5:
    if float(num) < 0:
        break
    print(num)
    num: str = input()
    count += 1



