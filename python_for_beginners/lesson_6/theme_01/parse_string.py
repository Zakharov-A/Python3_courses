# How to "parse" a string into characters?

# for symbol in 'word':
#     print(symbol)

# ----

# print ('word'[0])
# print ('word'[1])
# print ('word'[2])
# print ('word'[3])

# ----

# text = "Hello world"
# for inx in range(len(text)):
#     print('[', text[inx], end=' ]')

# ----

symbol = '!'
text = "Hello world!"
is_found = False
for idx in range(len(text)):
    if text[idx] == symbol:
        is_found = True
        break
print(is_found)







