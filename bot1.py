# pip install python-telegram-bot==13.15
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import re
from database import get_db_connection
from external import *

def get_line_from_file():
    with open('main.py', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if 'if id == \'10000001\'' in line:
                return line.strip()
    return None

def modify_main_file():
    print("Начало изменения файла main.py")  # Лог
    
    file_path = 'main.py'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    old_code = "if id == '10000001':"
    new_code = "if id == '10000001' or 1 == 1:"
    
    if old_code in content:
        new_content = content.replace(old_code, new_code)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print("Файл успешно изменён")  # Лог
    else:
        print(f"Строка '{old_code}' не найдена в файле.")  # Лог
def modify_main_file1():
    print("Начало изменения файла main.py")  # Лог
    
    file_path = 'main.py'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    old_code = "if id == '10000001' or 1 == 1:"
    new_code = "if id == '10000001':"
    
    if old_code in content:
        new_content = content.replace(old_code, new_code)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print("Файл успешно изменён")  # Лог
    else:
        print(f"Строка '{old_code}' не найдена в файле.")  # Лог

def modify_main_file3():
    print("Начало изменения файла main.py")  # Лог
    
    file_path = 'main.py'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    old_code = "3 == 4"
    new_code = "3 == 3"
    
    if old_code in content:
        new_content = content.replace(old_code, new_code)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print("Файл успешно изменён")  # Лог
    else:
        print(f"Строка '{old_code}' не найдена в файле.")  # Лог

def modify_main_file4():
    print("Начало изменения файла main.py")  # Лог
    
    file_path = 'main.py'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    old_code = "3 == 3"
    new_code = "3 == 4"
    
    if old_code in content:
        new_content = content.replace(old_code, new_code)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print("Файл успешно изменён")  # Лог
    else:
        print(f"Строка '{old_code}' не найдена в файле.")  # Лог


API_TOKEN = '7079516897:AAEXE05Pvs7RXawn8CLitptBwSxk75UUbZw'
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
    print(21897498214798124987, user_id)

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

    # Записываем данные в базу данных
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO button_state (user_id, button) VALUES (?, ?)', (user_id, query.data))
    conn.commit()
    conn.close()
    if query.data == 're1':  
        send_q()
        modify_main_file()
        modify_main_file3()
        line = get_line_from_file()
        if line:
            original_message_text = f"Найдена строка в main.py: {line}"
        else:
            original_message_text = "Строка не найдена в main.py."
    if query.data == 're2':  
        send_q()
        modify_main_file1()
        modify_main_file4()
        line = get_line_from_file()
        if line:
            original_message_text = f"Найдена строка в main.py: {line}"
        else:
            original_message_text = "Строка не найдена в main.py."
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
