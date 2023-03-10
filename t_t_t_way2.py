import random

position = [str(i + 1) for i in range(9)]
player = 'X'
bot = 'O'
game = False


def draw_game_field(position: list):
    for i in range(3):
        print('-' * 13)
        print('| ' + position[0 + i * 3] + ' | ' + position[1 + i * 3] + ' | ' + position[2 + i * 3] + ' |')
    print('-' * 13)


def player_move():
    while True:
        try:
            pos = int(input(f'Куда поставим {player}? Введите позицию (число от 1 до 9): '))
        except:
            print('Некорректный ввод. Введите число от 1 до 9!')
            continue

        if 1 <= pos <= 9:
            if position[pos - 1] not in "XO":
                position[pos - 1] = player
                print('Ход игрока:')
                draw_game_field(position)
                break
            else:
                print("Это клетка уже занята!")
        else:
            print('Hекорректный ввод! Введите число от 1 до 9!')


def lucky_move(x1, x2, x3, sym):
    res = False
    if position[x1] == position[x2] == sym and position[x3] not in 'XO':
        print('Ход бота:')
        position[x3] = 'O'
        draw_game_field(position)
        res = True
    elif position[x1] == position[x3] == sym and position[x2] not in 'XO':
        print('Ход бота:')
        position[x2] = 'O'
        draw_game_field(position)
        res = True
    elif position[x2] == position[x3] == sym and position[x1] not in 'XO':
        print('Ход бота:')
        position[x1] = 'O'
        draw_game_field(position)
        res = True
    return res


def bot_move():
    if lucky_move(0, 4, 8, 'O'):
        return
    elif lucky_move(6, 4, 2, 'O'):
        return
    elif lucky_move(0, 1, 2, 'O') or \
            lucky_move(3, 4, 5, "O") or \
            lucky_move(6, 7, 8, "O"):
        return
    elif lucky_move(0, 3, 6, 'O') or \
            lucky_move(1, 4, 7, "O") or \
            lucky_move(2, 5, 8, "O"):
        return
    elif lucky_move(0, 4, 8, 'X'):
        return
    elif lucky_move(6, 4, 2, 'X'):
        return
    elif lucky_move(0, 1, 2, 'X') or \
            lucky_move(3, 4, 5, "X") or \
            lucky_move(6, 7, 8, "X"):
        return
    elif lucky_move(0, 3, 6, 'X') or \
            lucky_move(1, 4, 7, "X") or \
            lucky_move(2, 5, 8, "X"):
        return
    else:
        while True:
            pos = random.randint(1, 9)
            if position[pos - 1] not in 'XO':
                print('Ход бота:')
                position[pos - 1] = bot
                draw_game_field(position)
                break
            else:
                continue


def check_win(position):
    def check_line(x1, x2, x3):
        global game
        sym = ''
        if x1 == x2 == x3 == 'X':
            sym = "X"
            game = False
        elif x1 == x2 == x3 == 'O':
            sym = "O"
            game = False
        if sym == "X":
            print('Игра окончена! Победил игрок!')
        elif sym == "O":
            print('Игра окончена! Победил бот!')
        return game

    check_line(position[0], position[4], position[8])
    check_line(position[6], position[4], position[2])

    check_line(position[0], position[3], position[6])
    check_line(position[1], position[4], position[7])
    check_line(position[2], position[5], position[8])

    check_line(position[0], position[1], position[2])
    check_line(position[3], position[4], position[5])
    check_line(position[6], position[7], position[8])


def new_game():
    global game
    game = True
    print('*' * 4 + " Игра 'Крестики-нолики' " + '*' * 4)
    draw_game_field(position)
    count_x = 0
    while game and count_x < 5:
        player_move()
        count_x += 1
        check_win(position)
        if not game:
            return
        bot_move()
        check_win(position)
        if not game:
            return
        if count_x == 4:
            game = False
            print("Игра окончена! Ничья!")
            return


new_game()
