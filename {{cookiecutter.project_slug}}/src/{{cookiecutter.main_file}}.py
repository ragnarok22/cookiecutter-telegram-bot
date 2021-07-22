import logging

from telegram.ext import CommandHandler, ConversationHandler

from config import handlers, conversations, dp, updater

if __name__ == '__main__':
    # handlers
    for handler in handlers:
        dp.add_handler(CommandHandler(handler.get('command'), handler.get('handler')))

    # conversations handlers
    for conversation in conversations:
        dp.add_handler(ConversationHandler(
            entry_points=conversation.get('entry_points'),
            states=conversation.get('states'),
            fallbacks=conversation.get('fallbacks', [])
        ))

    updater.start_polling()
    logging.info('Bot is polling')
    updater.idle()
