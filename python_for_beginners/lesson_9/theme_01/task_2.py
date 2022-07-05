num: str = input()
amount: float = float(num)
while amount <= 100:
    print(num)
    num: str = input()
    amount += float(num)
