# x = input()
# w = float(x)
# print(w)
# print(type(w))


# x = input()
# w = int(float(x))
# print(w)
# print(type(w))

# n = float(input())
# n_str = str(n) + "="
# n_str_3 = n_str * 3
# print(n_str_3)

# a = 8
# b = 3
#
# # sign = '+'
# # sign = '/'
# # sign = '//'
# # sign = '//'
# sign = '%'
#
# result = f'{a}{sign}{b}'
# print(f'{a} {sign} {b} = ', eval(result))

# #Even
# a = 4 % 2 #0
# #Odd
# a = 3 % 2 #1

#Operation priority

# a = 2 + 3 * 2 ** 2
# print(a)
# a = ((2 + 3) * 2) ** 2
# print(a)

#What time is it?
#1

# total_sec = int(input())
# total_hours = total_sec // 3600
# hh = total_hours % 24
# # print('total_hours=', total_hours) # 25
# # print('hh =', hh) #1
# total_min = total_sec // 60
# mm = total_min % 60
# # print('total_min = ', total_min)
# # print('mm = ', mm)
# ss = total_sec % 60
# # print('ss = ', ss)
# print(f'The time is {hh:02d}:{mm:02d}:{ss:02d}.')

hh = int(input())
mm = int(input())
ss = int(input())
print(f'The time is {hh:02d}:{mm:02d}:{ss:02d}.')






