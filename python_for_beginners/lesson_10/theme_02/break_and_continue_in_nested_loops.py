# ---- break ----
words = ['hello', 'word', 'python']
for word in words:
    for w in word:
        if w == 'o':
            break
        print(w, end="")

    print(end=',')

# ---- continue ----

print()
words1 = ['hello', 'word', 'python']
for word in words1:
    for w in word:
        if w == 'o':
            continue
        print(w, end="")

    print(end=',')

