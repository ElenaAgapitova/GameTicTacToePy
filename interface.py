from tkinter import *
import bot
import game

root = Tk()
root.title('Tic-Tac-Toe')

for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: game.click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    game.game_field.append(line)
    game_button = Button(root, text="NEW GAME", command=game.new_game)
    game_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

