import random


def choice():
    '''
    Функция выбора чем играет игрок Х или О
    '''
    is_true = True
    player_ch = None
    while is_true:
        player_ch = input('Выбирете Х или О: ').upper()
        if player_ch != 'X' and player_ch != 'O':
            print('Не верный ввод, выбирете Х или О:')
            continue
        is_true = False

    if player_ch == 'X':
        computer_ch = 'O'
    else:
        computer_ch = 'X'

    return player_ch, computer_ch


def show_gird(gird):
    '''
    Функция отображения игрового поля
    '''
    print(gird[7] + '|' + gird[8] + '|' + gird[9])
    print('-+-+-')
    print(gird[4] + '|' + gird[5] + '|' + gird[6])
    print('-+-+-')
    print(gird[1] + '|' + gird[2] + '|' + gird[3])


def player_go(gird):
    '''
    Функция для ввода координат игроком
    '''
    if_loop_input = True
    x = None
    while if_loop_input:
        x = int(input('Введите цифру от 1 до 9: '))
        if not gird[x].isdigit():
            print('Координаты введены не верно')
            continue
        if_loop_input = False
    return x


def computer_go(gird):
    '''
    Функция для ввода координат компютером
    '''
    if_loop_input = True
    x = None
    while if_loop_input:
        x = random.randint(1, 9)
        if not gird[x].isdigit():
            continue
        if_loop_input = False
    return x


def game_stage(gird, mark=''):
    '''
    Функция проверяет: заполнение символов по одной линии,
    и возвращает Х или О в случае совпадения
    '''

    if ((gird[7] == mark and gird[8] == mark and gird[9] == mark) or
            (gird[4] == mark and gird[5] == mark and gird[6] == mark) or
            (gird[1] == mark and gird[2] == mark and gird[3] == mark) or
            (gird[7] == mark and gird[4] == mark and gird[1] == mark) or
            (gird[8] == mark and gird[5] == mark and gird[2] == mark) or
            (gird[9] == mark and gird[6] == mark and gird[3] == mark) or
            (gird[7] == mark and gird[5] == mark and gird[3] == mark) or
            (gird[9] == mark and gird[5] == mark and gird[1] == mark)):
        return mark


def play_game():
    '''
    Функция запуска игры: отображается игровое поле,
       игрок выбирает крестик или нолик,
       игрок или компьютер заполняет свободную клетку,
       результат проверяется на заполнение клеток по одной линии и
       и кто выиграл
    '''
    gird = ['', '1', '2', '3',
                '4', '5', '6',
                '7', '8', '9'
            ]

    p_ch, c_ch = choice()
    show_gird(gird)
    while True:
        i = player_go(gird)
        gird[i] = p_ch
        if game_stage(gird, mark=p_ch) == p_ch:
            show_gird(gird)
            print('Вы выиграли!')
            break
        j = computer_go(gird)
        gird[j] = c_ch
        if game_stage(gird, mark=c_ch) == c_ch:
            show_gird(gird)
            print('Компьютер выиграл!')
            break
        show_gird(gird)


play_game()
print('Игра завершена')


