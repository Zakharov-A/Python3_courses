hh_1 = int(input())
mm_1 = int(input())
ss_1 = int(input())
hh_2 = int(input())
mm_2 = int(input())
ss_2 = int(input())

total_seconds = (hh_1 + hh_2) * 3600 + (mm_1 + mm_2) * 60 + ss_1 + ss_2
total_hours = total_seconds // 3600
hh = total_hours % 24
total_minutes = total_seconds // 60
mm = total_minutes % 60
ss = total_seconds % 60

print(f'{hh:02d}:{mm:02d}:{ss:02d}')