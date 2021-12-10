from random import randint



PATTERN = [str(i) for i in range(1, 10)]



def select():

    """Выбираем Х или 0"""

    symbol_user = input('Выберите (X) или (0): ').strip().upper()

    while symbol_user not in ('X', '0'):

        print('Не верно!')

        symbol_user = input('Выберите (Х) или (0): ').strip().upper()

    return symbol_user



def show_box(box):

    """Показываем поле"""

    print(f'-------------\n'

          f'| {box[6]} | {box[7]} | {box[8]} |\n'

          f'-------------\n'

          f'| {box[3]} | {box[4]} | {box[5]} |\n'

          f'-------------\n'

          f'| {box[0]} | {box[1]} | {box[2]} |\n'

          f'-------------')



def not_empty(box):

    """Ничья, если все клетки заняты"""

    cnt = 0

    for i in range(9):

        for j in PATTERN:

            if j in box[i]:

                cnt += 1

    return cnt == 0



def get_user_position(box):

    """Ввод позиции пользователем"""

    real_coordinats = 0

    while True:

        coordinats = input('Введите координаты 1-9: ')

        if coordinats not in PATTERN:

            print('Недопустимые координаты!')

            continue

        real_coordinats = int(coordinats) - 1

        if box[real_coordinats] in PATTERN:

            break

        else:

            print('Занято')

    return real_coordinats



def get_computer_position(box):

    """Случайный ввод позиции компьютером"""

    x0 = randint(0, 8)

    while box[x0] not in PATTERN:

        x0 = randint(0, 8)

    return x0



def inside_out(symbol):

    """Указываем противоположный символ компьютеру"""

    return '0' if symbol == 'X' else 'X'



def eight_victory(x0, box):

    """Ищем одну из 8 побед"""

    if x0 == box[0] == box[1] == box[2]\
    or x0 == box[3] == box[4] == box[5]\
    or x0 == box[6] == box[7] == box[8]\
    or x0 == box[0] == box[3] == box[6]\
    or x0 == box[1] == box[4] == box[7]\
    or x0 == box[2] == box[5] == box[8]\
    or x0 == box[0] == box[4] == box[8]\
    or x0 == box[2] == box[4] == box[6]:

        return x0



box = [str(i) for i in list(range(1, 10))]



smbl_usr = select()

smbl_comp = inside_out(smbl_usr)



while True:

    show_box(box)

    if not_empty(box):

        print('Ничья!')

        break



    pos = get_user_position(box)

    box[pos] = smbl_usr

    if eight_victory(smbl_usr, box):

        print('Вы победили!')

        show_box(box)

        break



    pos = get_computer_position(box)

    box[pos] = smbl_comp

    if eight_victory(smbl_comp, box):

        print('Вы проиграли(:')

        show_box(box)

        break

