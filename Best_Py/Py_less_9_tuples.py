# data = (4, 6, 7, 5, 11, True, 7.9, "Reider")
# # data[1] = 5 # - no
# print(data[1:4])
#
# # print(data.count(6))
# print(len(data))
# print(data)

# data = 5, 7, True # Варианты создания кортежа
# print(data)

data = (4, 6, 7, 5, 11, True, 7.9, "Reider")

for el in data:
    print(el)
nums = [4, 5, 6]

new_data = tuple(nums)
word = tuple('Hello world')
print(word)