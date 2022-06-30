# task 1

# total_seconds = int(input()) #91089
# total_hours = total_seconds // 3600
# hh = total_hours % 24
# total_minutes = total_seconds // 60
# mm = total_minutes % 60
# ss = total_seconds % 60
#
# print(f'The time is {hh:02d}:{mm:02d}:{ss:02d}.')

# task 2

hours = int(input())
minutes = int(input())
seconds = int(input())

total_seconds_before = hours * 3600 + minutes * 60 + seconds


total_seconds = total_seconds_before + 5
total_hours = total_seconds // 3600
hh = total_hours % 24
total_minutes = total_seconds // 60
mm = total_minutes % 60
ss = total_seconds % 60

print(f'The time is {hh:02d}:{mm:02d}:{ss:02d}.')




