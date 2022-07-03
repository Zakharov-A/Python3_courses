text = input()
nums = text.split(', ')

sum_even = 0
sum_odd = 0
for i, num in enumerate(nums):
    num = int(num)
    if i % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print(f'The even sum is "{sum_even}", and odd sum "{sum_odd}".')







