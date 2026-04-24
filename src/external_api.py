import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
token = os.getenv('API_KEY')
load_dotenv()


def amout_rur (trans_action):
    '''
    функция, которая принимает на вход одну (словарь)транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float
    Пример операции:
    {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount':
    {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации',
    'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}
    :return:
    '''


    rest = trans_action['operationAmount']['currency']['code']
    turn = trans_action['operationAmount']['amount']


    if rest == 'RUB':

        return float(turn)

    if rest == 'USD':
        # load_dotenv()
        # token = os.getenv('API_KEY')
        # load_dotenv()
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={turn}"
        payload = {}
        headers = {
            "apikey": f"{token}"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        dura = response.text
        dura = json.loads(dura)

        return float(dura['result'])
    if rest == 'EUR':
        # load_dotenv()
        # token = os.getenv('API_KEY')
        # load_dotenv()
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={turn}"

        payload = {}
        headers = {
            "apikey": f"{token}"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        dura = response.text
        dura = json.loads(dura)

        return float(dura['result'])

    return ()
