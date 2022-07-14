start_end = input().split()
first_symbol_code = ord(start_end[0])
last_symbol_code = ord(start_end[1])

for code in range(first_symbol_code, last_symbol_code+1):
    print(chr(code), end='')
