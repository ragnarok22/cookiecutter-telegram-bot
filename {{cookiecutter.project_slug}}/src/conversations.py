from telegram import ChatAction
from telegram.ext import ConversationHandler


def greetings_conversation(update, context):
    name = update.message.text
    chat = update.message.chat

    chat.send_action(
        action=ChatAction.TYPING,
        timeout=None
    )
    update.message.reply_text(f'Hola {name}')
    return ConversationHandler.END
