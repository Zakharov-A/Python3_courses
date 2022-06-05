# 30     # 1924.7
# 20
# 5.55
# 578

a = float(input())
b = float(input())
c = float(input())
cost = float(input())

volume = int(a * b * c)
total_cost = volume * cost / 1000
print(f"{total_cost:.1f}")
