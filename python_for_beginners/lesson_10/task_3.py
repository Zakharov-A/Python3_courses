while True:
    word = input()
    if word == "STOP":
        break

    new_word = word[0]
    for i in range(1, len(word)):
        new_word += '-' + word[i]

    print(new_word)

