nums = input().split(',')
for i, num in enumerate(nums):
    nums[i] = int(num)

multiply = nums[0] * nums[1]
amount = nums[0] + nums[1]

for i, num in enumerate(nums):
    print(num)
    if i >= 2:
        amount += num
        if amount > multiply:
            break

