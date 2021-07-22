import logging
import os

from dotenv import load_dotenv
from telegram.ext import CommandHandler, CallbackQueryHandler, Filters, MessageHandler, Updater

import callbacks
import constants
import conversations
import handlers as handlers_module

# load environment file
load_dotenv()

# settings logging config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('{{cookiecutter.project_slug}}')

updater = Updater(token=os.getenv('TELEGRAM_TOKEN'), use_context=True)
dp = updater.dispatcher

# commands handlers
handlers = [
    {
        'command': 'start',
        'handler': handlers_module.start_handler
    },
]
conversations = [
    {
        'entry_points': [
            CommandHandler('greetings', handlers_module.greetings_handler),
            CallbackQueryHandler(pattern='greetings', callback=callbacks.greetings_callback)
        ],
        'states': {
            constants.GREETINGS: [MessageHandler(Filters.text, conversations.greetings_conversation)]
        },
        'fallbacks': []
    },
]
