time_type = input()
time = int(input())
total_seconds = time
if time_type == 'mm':
    total_seconds = time * 60
elif time_type == 'hh':
    total_seconds = time * 3600

total_hours = total_seconds // 3600
hh = total_hours % 24
total_minutes = total_seconds // 60
mm = total_minutes % 60
ss = total_seconds % 60

print(f'{hh:02d}:{mm:02d}:{ss:02d}')
