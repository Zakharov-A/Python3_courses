

total_seconds = int(input())
total_hours = total_seconds // 3600
hh = total_hours % 24
total_minutes = total_seconds // 60
mm = total_minutes % 60
ss = total_seconds % 60

print(f'The time is {hh:02d}:{mm:02d}:{ss:02d}.')
