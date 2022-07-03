text = input()
nums = text.split(', ')

max_even = None
max_odd = None

for num in nums:
    num = int(num)
    if num % 2 == 0:
        if max_even is None:
            max_even = num
        else:
            if num > max_even:
                max_even = num
    else:
        if max_odd is None:
            max_odd = num
        else:
            if num > max_odd:
                max_odd = num

print(f'The maximum even number is "{max_even}" and the maximum odd number is "{max_odd}".')
