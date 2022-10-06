import logging
from bot_commands import *
from processing import *
from token import *
from telegram import __version__ as TG_VER


try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

with open("token.txt", "r") as file:
    for line in file:
        token = line

def main() -> None:
    application = Application.builder().token(token).build()

    application.add_handler(MessageHandler(filters.TEXT, start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("new_game", new_game))
    application.run_polling()

if __name__ == "__main__":
    main()
