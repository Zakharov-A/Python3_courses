# # data = set('hello')
# data = {5, 7, 4, 3, 5}
#
# data.add(32)
# data.update(['32', True, 4, 6, 5])
# data.remove(True)
# print(data)
# data.pop()

nums = [2, 3, 4, 6, 6, 3, 3]
print(nums)
new_nums = set(nums)

print(new_nums)

new_data = frozenset([2, 3, 4, 6, 6, 3, 3, '32', True, 4, 6, 5])

# new_data.add(4)
print(new_data)