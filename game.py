import bot

game = True
game_field = []
count_x = 0


def new_game():
    """
    Функция-старт новой игры, на поле очищаются все клетки,
    переменные game и cross_x устанавливаются в начальное положение.
    """
    global game
    game = True
    global count_x
    count_x = 0
    for row in range(3):
        for col in range(3):
            game_field[row][col]['text'] = ' '
            game_field[row][col]['background'] = 'lavender'


def click(row: int, col: int):
    """
    Функция вызывается при попытке поставить крестик. Проверяет возможность его поставить
    и вызывает функцию победы, либо продолжается игра, либо прекращается.
    :param row: номер строки
    :param col: номер столбца
    """
    global count_x
    global game
    if game and game_field[row][col]['text'] == ' ':
        game_field[row][col]['text'] = 'X'
        count_x += 1
        check_win('X')
        if game or count_x < 5:
            bot.bot_move()
            check_win('O')


def check_win(symbol: str):
    """
    Функция проверяет находится ли один и тот же символ в строке, столбце или в диагонале.
    :param symbol: крестик или нолик, котрый находится в проверяемой клетке
    """
    def check_line(x1, x2, x3):
        global game
        if x1['text'] == x2['text'] == x3['text'] == 'X':
            x1['background'] = x2['background'] = x3['background'] = 'green'
            game = False
            return game
        elif x1['text'] == x2['text'] == x3['text'] == 'O':
            x1['background'] = x2['background'] = x3['background'] = 'red'
            game = False
            return game

    check_line(game_field[0][0], game_field[1][1], game_field[2][2])
    check_line(game_field[0][2], game_field[1][1], game_field[2][0])
    for i in range(3):
        check_line(game_field[i][0], game_field[i][1], game_field[i][2])
        check_line(game_field[0][i], game_field[1][i], game_field[2][i])



