from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from processing import *

global board
global mark
global player

marks = ['X', 'O']
mark = toss_mark(marks)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global player
    global players
    global mark 
    global board

    board = get_board()
    keyboard = draw_board(board)
    players = [update.effective_user.first_name, 'Bot']
    player = toss_player(players)
    reply_markup = InlineKeyboardMarkup(keyboard)
    if player == 'Bot':
        await update.message.reply_text(f'Вас приветствует игра "Крестики-нолики"!')
        await bot(update, context)
    else:
        await update.message.reply_text(f'Вас приветствует игра "Крестики-нолики"!\n{player}, выберите ячейку, чтобы проставить {mark}', reply_markup=reply_markup)


async def bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global player
    global players
    global mark 
    global board
    global board
    strike = bot_strike(board)

    for i in board:
        for j in i:
            if j == strike:
                i[i.index(j)] = mark
    keyboard = draw_board(board)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.effective_chat.send_message(f'{player} проставляет {mark} ячейку: {strike}', reply_markup=reply_markup)
    if check_win(board) == True:
        await update.effective_chat.send_message(text=f"Побеждает {player}!")
        await update.effective_chat.send_message("Используйте /start, чтобы начать новую игру.")
    elif check_draw(board, marks) != True:
        await update.effective_chat.send_message(text=f"Ничья!")
        await update.effective_chat.send_message("Используйте /start, чтобы начать новую игру.")
    mark =  marks[marks.index(mark) -1]
    player =  players[players.index(player) -1]


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global mark
    global player
    global players
    global query
    global board

    query = update.callback_query 
    for i in board:
        for j in i:
            if j == int(query.data):
                i[i.index(j)] = mark
    keyboard = draw_board(board)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.answer()
    await query.edit_message_text(text=f"{player} проставляет {mark} в ячейку: {query.data}", reply_markup=reply_markup)
    if check_win(board) == True:
        #await query.edit_message_text(text=f"{player} проставляет {mark} в ячейку: {query.data}", reply_markup=reply_markup)
        await update.effective_chat.send_message(text=f"Побеждает {player}!" )
        await update.effective_chat.send_message("Используйте /start, чтобы начать новую игру.")
    elif check_draw(board, marks) != True:
        await query.edit_message_text(text=f"Ничья!")
        await update.effective_chat.send_message("Используйте /start, чтобы начать новую игру.")
    else:
        mark =  marks[marks.index(mark) -1]
        player =  players[players.index(player) -1]
        await bot(update, context)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Используй /start, чтобы начать игру.")