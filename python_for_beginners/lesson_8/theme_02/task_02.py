nums = input().split(',')

amount = 0
for num in nums:
    if num.isalpha():
        continue
    amount += float(num)

print(f'{amount:.1f}')

