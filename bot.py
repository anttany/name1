from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import re
from database import get_db_connection

# pip install python-telegram-bot==13.15

API_TOKEN = '7183115873:AAGsfeV2XA-QeeURJsWu1IyylJ1a5yCOJkM'
clicked_button = None
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Кнопка 1", callback_data='button1'),
            InlineKeyboardButton("Кнопка 2", callback_data='button2'),
        ],
        [
            InlineKeyboardButton("Кнопка 3", callback_data='button3'),
            InlineKeyboardButton("Кнопка 4", callback_data='button4'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    original_message_text = query.message.text + '\n\nОжидайте ответа пользователя.'
    user_id = original_message_text[1:8]
    ip_address_match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', original_message_text)
    if ip_address_match:
        ip_address = ip_address_match.group(0)
    else:
        ip_address = None
    print(ip_address)
    if query.data == 'button-ban' and ip_address:
        print('nazal')
        # Записываем IP-адрес в файл ban.txt
        with open('ban.txt', 'a') as f:
            f.write(ip_address + '\n')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO button_state (user_id, button) VALUES (?, ?)', (user_id, query.data))
    conn.commit()
    conn.close()

    query.edit_message_text(text=original_message_text)

def main() -> None:
    
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
