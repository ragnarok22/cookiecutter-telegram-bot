import constants


def greetings_callback(update, context):
    query = update.callback_query
    query.answer()

    query.reply_text(
        text='¿Cómo te llamas?'
    )
    return constants.GREETINGS
