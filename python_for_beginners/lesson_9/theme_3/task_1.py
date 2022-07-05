while True:
    word = input()
    if word == 'exit':
        break

    reversed_word = ''
    for i in range(len(word)-1, -1, -1):
        reversed_word += word[i]

    print(f'{word}+{reversed_word}')
