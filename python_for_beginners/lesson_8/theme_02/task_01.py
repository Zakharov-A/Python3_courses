nums = input().split(',')

for num in nums:
    if num.isalpha() or '-' in num:
        continue
    print(num)
