# nums = [5, 7, 8, 9, 32, True, "Hello", 6.7, [5, 4, 6]]
#
# nums[0] = 50
# nums[5] = "Hi!"
#
# print(nums[-1][1])

# numb = [5, 3, 7]
# numb[3] = 100 - не верно
# numb.append(100)
# numb.insert(1, True)
#
# b = [9, 6, 3]
# numb.extend(b)
# numb.sort()
# numb.reverse()

# numb.pop(0)
# numb.remove(6)
# numb.clear()

# print(numb.count(True))

# nums = [5, 2, 7, "50", False]
#
# for elem in nums:
#     elem *= 2
#     print(elem)

# Program

n =int(input("Enter length: "))

user_list = []

i = 0
while i < n:
    string = "Enter element #" + str(i + 1) + ": "
    user_list.append(input(string))
    i += 1
print(user_list)


