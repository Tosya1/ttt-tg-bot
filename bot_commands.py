
from telegram import InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from processing import *

global board
global mark
global player
global keyboard
global keys
global game_on

marks = ['❌', '⭕']
mark = toss_mark(marks)
game_on = True

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global game_on
    
    kb = [[KeyboardButton('Новая игра')],[KeyboardButton('Завершить игру')],
    [KeyboardButton('Помощь')]]
    reply_kb = ReplyKeyboardMarkup(kb, resize_keyboard=True, one_time_keyboard=True)
    if update.message.text == 'Новая игра' or update.message.text == '/new_game':
        await new_game(update, context)
    elif update.message.text == 'Помощь' or update.message.text == '/help':
        await help(update, context)
    elif update.message.text == '/start':
        await update.message.reply_text(f'{update.effective_user.first_name}, Вас приветствует игра "Крестики-нолики 👋"',reply_markup=reply_kb)
    elif update.message.text == 'Завершить игру'or update.message.text == '/close':
        await update.message.reply_text(f'{update.effective_user.first_name} выходит из игры 💔\nИспользуйте /new_game, чтобы начать новую игру.')
        game_on = False
    else:
        await update.message.reply_text('Используйте /new_game, чтобы начать новую игру или выберите нужную команду из меню.')

async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global player
    global players
    global mark 
    global board
    global keyboard
    global keys
    global game_on
    game_on = True
    players = [update.effective_user.first_name, 'Bot']
    player = toss_player(players)
    board = get_board()
    keys = get_keys_text(board, marks)
    keyboard = draw_board(board, keys)
    reply_markup = InlineKeyboardMarkup(keyboard)
    if player == 'Bot':
        await bot(update, context)
    else:
        await update.message.reply_text(f'{player}, выберите ячейку, чтобы проставить {mark}', reply_markup=reply_markup)

async def bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global player
    global players
    global mark 
    global board
    global keyboard
    global keys
    global game_on
    
    strike = bot_strike(board, marks)
    board = update_board(board, strike, mark)
    keys = get_keys_text(board, marks)
    keyboard = draw_board(board, keys)
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.effective_chat.send_message(f'{player} проставляет {mark} ячейку: {strike}', reply_markup=reply_markup)
    if check_win(board) == True:
        await update.effective_chat.send_message(text=f"Побеждает {player}! 🏆")
        await update.effective_chat.send_message("Используйте /new_game, чтобы начать новую игру.")
        game_on = False
    elif check_draw(board, marks) != True:
        await update.effective_chat.send_message(text=f"Ничья! 🤝")
        await update.effective_chat.send_message("Используйте /new_game, чтобы начать новую игру.")
        game_on = False
    mark =  marks[marks.index(mark) -1]
    player =  players[players.index(player) -1]


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global mark
    global player
    global players
    global board
    global keyboard
    global keys
    global game_on

    if game_on == True:
        strike = update.callback_query.data
        board = update_board(board, strike, mark)
        keys = get_keys_text(board, marks)
        keyboard = draw_board(board, keys)
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.callback_query.answer()
        await update.effective_chat.send_message(text=f"{player} проставляет {mark} в ячейку: {strike}", reply_markup=reply_markup)
        if check_win(board) == True:
            await update.effective_chat.send_message(text=f"Побеждает {player}! 🏆" )
            await update.effective_chat.send_message("Используйте /new_game, чтобы начать новую игру.")
            game_on = False
        elif check_draw(board, marks) != True:
            await update.effective_chat.send_message(text=f"Ничья! 🤝")
            await update.effective_chat.send_message("Используйте /new_game, чтобы начать новую игру.")
            game_on = False
        else:
            mark =  marks[marks.index(mark) -1]
            player =  players[players.index(player) -1]
            await bot(update, context)
    else:
        await update.callback_query.answer(text = 'Игра завершена. Используйте /new_game, чтобы начать новую игру.')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("✍️Правила игры.\n1. Программа в рандомном порядке определяет, кто из игроков будет играть ❌, а кто ⭕, а также кто из игроков начинает игру.\n2. Игрок ставит свою метку (❌ или ⭕) в выбранную ячейку.\n3. После успешного хода одного игрока наступает ход другого игрока. Нельзя поставить метку в уже занятую ячейку.\n4. Если один из игроков поставил три метки в ряд, игра заканчивается победой этого игрока. В противном случае игра заканчивается вничью.\nИспользуте /new_game, чтобы начать игру.")