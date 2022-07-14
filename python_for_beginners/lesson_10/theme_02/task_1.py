nums = input().split()
i_max = int(nums[0])
digit = nums[1]

for x in range(i_max+1):
    if str(x)[-1] == digit:
        print(x, end=',')
