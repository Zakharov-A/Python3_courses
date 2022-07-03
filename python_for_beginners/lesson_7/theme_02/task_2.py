text = input()
times = text.split()
total_seconds = int(input())
total_hours = total_seconds // 3600
hh = total_hours % 24
total_minutes = total_seconds // 60
mm = total_minutes % 60
ss = total_seconds % 60
time = f'{hh:02d}:{mm:02d}:{ss:02d}.'

index = None
for i, item in enumerate(times):
    if time == item:
        index = i

if index is None:
    print("Item not found")
else:
    print(f'The index of the item is "{index}"')
