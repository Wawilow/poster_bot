telegram_bot_token = "1998961866:AAHLsq-XgXfpgUsS3b1lAZjwgSZI8EreRMA"


import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    # Send a message when the command /start is issued
    update.message.reply_text('Hi!')


def help(update, context):
    # Send a message when the command /help is issued
    update.message.reply_text('Help!')


def echo(update, context):
    # Echo the user message
    update.message.reply_text(update.message.text)


def error(update, context):
    # Log Errors caused by Updates
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    print("""Start the bot.""")
    updater = Updater(f"{telegram_bot_token}", use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
