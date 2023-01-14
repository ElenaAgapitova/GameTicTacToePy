import game
import random

def lucky_move(x1, x2, x3, symbol):
    """
    Функция проверяет возможный удачный ход для бота

    :param x1: клетка на игровом поле
    :param x2: клетка на игровом поле
    :param x3: клетка на игровом поле
    :param symbol: крестик или нолик
    :return: False или True
    """
    result = False
    if x1['text'] == x2['text'] == symbol and x3['text'] == ' ':
        x3['text'] == 'O'
        result = True
    if x1['text'] == x3['text'] == symbol and x2['text'] == ' ':
        x2['text'] == 'O'
        result = True
    if x2['text'] == x3['text'] == symbol and x1['text'] == ' ':
        x1['text'] == 'O'
        result = True
    return result

def bot_move():
    """
    Функция определяет клетку, в которую бот сделает ход с учетом возможности победы и препятствия
    выигрыша для игрока.
    """
    for i in range(3):
        if lucky_move(game.game_field[i][0], game.game_field[i][1], game.game_field[i][2], 'O'):
            return
        if lucky_move(game.game_field[0][i], game.game_field[1][i], game.game_field[2][i], 'O'):
            return
    if lucky_move(game.game_field[0][0], game.game_field[1][1], game.game_field[2][2], 'O'):
        return
    if lucky_move(game.game_field[2][0], game.game_field[1][1], game.game_field[2][2], 'O'):
        return

    for i in range(3):
        if lucky_move(game.game_field[i][0], game.game_field[i][1], game.game_field[i][2], 'X'):
            return
        elif lucky_move(game.game_field[0][i], game.game_field[1][i], game.game_field[2][i], 'X'):
            return

    if lucky_move(game.game_field[0][0], game.game_field[1][1], game.game_field[2][2], 'X'):
        return
    elif lucky_move(game.game_field[2][0], game.game_field[1][1], game.game_field[2][2], 'X'):
        return

    while True:
        i, j = random.randint(0, 1), random.randint(0, 1)
        if game.game_field[i][j]['text'] == ' ':
            game.game_field[i][j]['text'] = 'O'
            break
