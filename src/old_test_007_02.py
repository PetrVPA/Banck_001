import requests
#from src.external_api import amout_rur
from src.exter import amout_rur


trans_action = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
        'operationAmount':{'amount': '31957.58', 'currency': {'name': 'USD.', 'code': 'USD'}},
        'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}


if __name__ == '__main__':
    zed = amout_rur(trans_action)
    print (zed)
    print (type(zed))
