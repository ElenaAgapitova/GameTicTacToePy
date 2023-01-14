import game
import random


def bot_move():
    """
    Функция определяет клетку, в которую бот сделает ход с учетом возможности победы и препятствия
    выигрыша для игрока.
    """
    for sym in ['O', 'X']:
        for i in range(3):
            if game.game_field[i][0]['text'] == game.game_field[i][1]['text'] == sym and \
                    game.game_field[i][2]['text'] == ' ':
                game.game_field[i][2]['text'] = 'O'
                return
            elif game.game_field[i][0]['text'] == game.game_field[i][2]['text'] == sym and \
                    game.game_field[i][1]['text'] == ' ':
                game.game_field[i][1]['text'] = 'O'
                return
            elif game.game_field[i][1]['text'] == game.game_field[i][2]['text'] == sym and \
                    game.game_field[i][0]['text'] == ' ':
                game.game_field[i][0]['text'] = 'O'
                return
            elif game.game_field[0][i]['text'] == game.game_field[1][i]['text'] == sym and \
                    game.game_field[2][i]['text'] == ' ':
                game.game_field[2][i]['text'] = 'O'
                return
            elif game.game_field[2][i]['text'] == game.game_field[1][i]['text'] == sym and \
                    game.game_field[0][i]['text'] == ' ':
                game.game_field[0][i]['text'] = 'O'
                return
            elif game.game_field[0][i]['text'] == game.game_field[2][i]['text'] == sym and \
                    game.game_field[1][i]['text'] == ' ':
                game.game_field[1][i]['text'] = 'O'
                return

        if game.game_field[0][0]['text'] == game.game_field[1][1]['text'] == sym and \
                game.game_field[2][2]['text'] == ' ':
            game.game_field[2][2]['text'] = 'O'
            return
        elif game.game_field[2][2]['text'] == game.game_field[1][1]['text'] == sym and \
                game.game_field[0][0]['text'] == ' ':
            game.game_field[0][0]['text'] = 'O'
            return
        elif game.game_field[2][2]['text'] == game.game_field[0][0]['text'] == sym and \
                game.game_field[1][1]['text'] == ' ':
            game.game_field[1][1]['text'] = 'O'
            return
        elif game.game_field[2][0]['text'] == game.game_field[1][1]['text'] == sym and \
                game.game_field[0][2]['text'] == ' ':
            game.game_field[0][2]['text'] = 'O'
            return
        elif game.game_field[0][2]['text'] == game.game_field[1][1]['text'] == sym and \
                game.game_field[2][0]['text'] == ' ':
            game.game_field[2][0]['text'] = 'O'
            return
        elif game.game_field[0][2]['text'] == game.game_field[2][0]['text'] == sym and \
                game.game_field[1][1]['text'] == ' ':
            game.game_field[1][1]['text'] = 'O'
            return

    while True:
        i, j = random.randint(0, 1), random.randint(0, 1)
        if game.game_field[i][j]['text'] == ' ':
            game.game_field[i][j]['text'] = 'O'
            break
