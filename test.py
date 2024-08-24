import requests
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

print(get_country_by_ip('8.8.8.8'))
