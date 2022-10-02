
from random import choice
from telegram import InlineKeyboardButton

def check_win (board):
    for i in board:
        if i[0] == i[1] == i[2]:
            return True

def check_draw(board, marks):
    list1 = [marks[0] in i and marks[1] in i for i in board]
    return False in list1

def get_board ():
    board = [[3*i + 1, 3*i + 2, 3*i + 3] for i in range(3)]
    board.extend([[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]])
    return board

def toss_mark (marks):
        mark = choice(marks)
        return mark 

def toss_player (players):
        player = choice(players)
        return player

def bot_strike (board):
    li = [j for i in board for j in i]
    li = list(filter(lambda x: x != "X" and x != "O", li))
    unic = list(set(li))
    strike = choice(unic)
    return strike

def draw_board(board):
    global keyboard
    keyboard = [
        [
            InlineKeyboardButton(f"{board[0][0]}", callback_data=f"{board[0][0]}"),
            InlineKeyboardButton(f"{board[0][1]}", callback_data=f"{board[0][1]}"),
            InlineKeyboardButton(f"{board[0][2]} ", callback_data=f"{board[0][2]}"),
        ],
        [
            InlineKeyboardButton(f"{board[1][0]}", callback_data=f"{board[1][0]}"),
            InlineKeyboardButton(f"{board[1][1]}", callback_data=f"{board[1][1]}"),
            InlineKeyboardButton(f"{board[1][2]}", callback_data=f"{board[1][2]}"),
        ],
        [
            InlineKeyboardButton(f"{board[2][0]}", callback_data=f"{board[2][0]}"),
            InlineKeyboardButton(f"{board[2][1]}", callback_data=f"{board[2][1]}"),
            InlineKeyboardButton(f"{board[2][2]}", callback_data=f"{board[2][2]}"),
        ],
    ]
    return keyboard
