# Телеграм-бот для игры в крестики-нолики
## Установка и настройка
### Тoken
Для создания бота необходимо получить токен с помощью телеграм-бота [@BotFather](https://t.me/BotFather).
Процедура проходит в 3 этапа:
1) `/newbot` - команда для регистрации бота в телеграм.
2) выбор имени бота, например `tic-tac-toe_bot`.
3) выбор username бота, то есть ссылки, по которой он будет доступен, например `@ttt_pythonBot`.
Если все действия были выполнены успешно, то [@BotFather](https://t.me/BotFather) предоставит токен для работы бота:
`Use this token to access the HTTP API: <токен для работы бота>`
Полученный токен необходимо вставить в строку `application = Application.builder().token("TOKEN").build()` функции main модуля bot.
### Библиотеки
При создании бота использовалась библиотека [python-telegram-bot](https://python-telegram-bot.org/). Для установки воспользуйтесь командой:
```
pip install python-telegram-bot --pre
```
или установите зависимости:
```
python -m pip install -r requirements.txt
```
### Запуск бота
```
git clone https://github.com/Tosya1/ttt-tg-bot.git
cd ttt-tg-bot
python -m pip install -r requirements.txt
python bot.py
```
## Доступные команды:
* `/start` - начать работу с ботом.
* `/new_game` - начать новую игру.
* `/close` - завершить игру.
* `/help` - помощь.
## Правила игры
1) Программа в рандомном порядке определяет, кто из игроков будет играть "Х", а кто "О", а также кто из игроков начинает игру.
2) Игрок ставит свою метку ("Х" или "О") в выбранную ячейку.
3) После успешного хода одного игрока наступает ход другого игрока. Нельзя поставить метку в уже занятую ячейку.
4) Если один из игроков поставил три метки в ряд, игра заканчивается победой этого игрока. В противном случае игра заканчивается вничью.
## Модули:
### processing
Содержит вспомогательные функции: проверка результата игры (победа/ ничья), функции рандомного выбора игрока и метки, разметка игровой доски (кнопок бота), 
получение ходов Бота (рандомно)и.т.д
### bot_commands 
Содержит функции, которые описывают основные команды бота.
### bot
Отвечает за обработку команд из модуля bot_commands и обеспечивает запуск программы.
