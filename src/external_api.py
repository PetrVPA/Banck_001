import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_token = os.getenv('API_KEY')


def amout_rur(trans_action: dict) -> float:
    '''
    функция, которая принимает на вход одну (словарь)транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float
    Пример операции:
    {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount':
    {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации',
    'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}
    :return:возвращает сумму операции в рублях в пересчете по курсу валюты float.
    '''
    current_currency = trans_action['operationAmount']['currency']['code'].upper()
    quantity_many = trans_action['operationAmount']['amount']

    if current_currency == 'RUB':

        return float(quantity_many)

    if current_currency == 'USD':

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={quantity_many}"
        payload: dict[str, float] = {}
        headers = {
            "apikey": f"{api_token}"
        }
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            output = response.text
        except requests.exceptions.Timeout:
            print("Превышено время ожидания...")
        except requests.exceptions.TooManyRedirects:
            print("Количество перенаправлений превысило предел")
        except requests.exceptions.RequestException:
            print("Ошибка в обращении к сервису. Попробуйте позже.")
        else:
            output_value = json.loads(output)
            return float(output_value['result'])
    if current_currency == 'EUR':

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={quantity_many}"

        payload = {}
        headers = {
            "apikey": f"{api_token}"
        }
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            output = response.text
        except requests.exceptions.Timeout:
            print("Превышено время ожидания...")
        except requests.exceptions.TooManyRedirects:
            print("Количество перенаправлений превысило предел")
        except requests.exceptions.RequestException:
            print("Ошибка в обращении к сервису. Попробуйте позже.")
        else:
            output_value = json.loads(output)
            return float(output_value['result'])

    return 0
