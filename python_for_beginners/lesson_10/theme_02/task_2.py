TIME_BEFORE = 530 #8:50
TIME_AFTER = 540 #9:00

lateness = 0
while True:
    line = input()
    if line =='STOP':
        break
    time = line.split(':')
    hh = int(time[0])
    mm = int(time[1])
    minutes = hh * 60 + mm

    if minutes < TIME_BEFORE:
        lateness -= TIME_BEFORE - minutes
    elif minutes > TIME_AFTER:
        lateness += minutes - TIME_AFTER

print(f'total lateness: {lateness} min')
