import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import constants


def start_handler(update, context):
    logging.info(update.message.chat)

    about_authors = InlineKeyboardButton(
        text='Saludos',
        callback_data='greetings'
    )
    update.message.reply_text(
        text='Hola {0}. Este es {{cookiecutter.project_name}}.'.format(
            update.message.chat.first_name),
        reply_markup=InlineKeyboardMarkup([
            [about_authors],
        ])
    )


def greetings_handler(update, context):
    update.message.reply_text('¿Cómo te llamas?')
    return constants.GREETINGS
