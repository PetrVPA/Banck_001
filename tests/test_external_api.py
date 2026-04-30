from src.external_api import amout_rur
from unittest.mock import patch
import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv('API_KEY')

trans_action1 = {
    'id': 441945886,
    'state': 'EXECUTED',
    'date': '2019-08-26T10:50:58.294041',
    'operationAmount': {'amount': '31957.58', 'currency': {'name': 'EUR.', 'code': 'EUR'}},
    'description': 'Перевод организации',
    'from': 'Maestro 1596837868705199',
    'to': 'Счет 64686473678894779589'
}

trans_action2 = {
    'id': 441945116,
    'state': 'EXECUTED',
    'date': '2019-08-26T10:50:58.294041',
    'operationAmount': {'amount': '46012.31', 'currency': {'name': 'USD.', 'code': 'USD'}},
    'description': 'Перевод организации',
    'from': 'Maestro 1596837868705199',
    'to': 'Счет 64686473678894779589'
}

trans_action3 = {
    'id': 441945776,
    'state': 'EXECUTED',
    'date': '2019-08-26T10:50:58.294041',
    'operationAmount': {'amount': '28836.74', 'currency': {'name': 'RUB.', 'code': 'RUB'}},
    'description': 'Перевод организации',
    'from': 'Maestro 1596837868705199',
    'to': 'Счет 64686473678894779589'
}

trans_action4 = {
    'id': 441945336,
    'state': 'EXECUTED',
    'date': '2019-08-26T10:50:58.294041',
    'operationAmount': {'amount': '123867.54', 'currency': {'name': 'CNH.', 'code': 'CNH'}},
    'description': 'Перевод организации',
    'from': 'Maestro 1596837868705199',
    'to': 'Счет 64686473678894779589'
}


@patch('requests.request')
def test_amout_rur1(mock_request):
    # Настраиваем заглушку — мокаем Response.text
    mock_response = mock_request.return_value
    mock_response.text = '{"result": 31957.58}'

    # Вызываем тестируемую функцию
    result = amout_rur(trans_action1)

    # Проверяем результат
    assert result == 31957.58

    # Проверяем, что запрос был сделан с правильными параметрами
    expected_url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=31957.58"
    mock_request.assert_called_once_with(
        "GET",
        expected_url,
        headers={"apikey": api_token},
        data={}
    )


@patch('requests.request')
def test_amout_rur2(mock_request):
    # Настраиваем заглушку — мокаем Response.text
    mock_response = mock_request.return_value
    mock_response.text = '{"result": 46012.31}'

    # Вызываем тестируемую функцию
    result = amout_rur(trans_action2)

    # Проверяем результат
    assert result == 46012.31

    # Проверяем, что запрос был сделан с правильными параметрами
    expected_url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=46012.31"
    mock_request.assert_called_once_with(
        "GET",
        expected_url,
        headers={"apikey": api_token},
        data={}
    )


@patch('requests.request')
def test_amout_rur3(mock_request):
    # Настраиваем заглушку — мокаем Response.text
    mock_response = mock_request.return_value
    mock_response.text = '{"result": 28836.74}'

    # Вызываем тестируемую функцию
    result = amout_rur(trans_action3)

    # Проверяем результат
    assert result == 28836.74


@patch('requests.request')
def test_amout_rur4(mock_request):
    # Настраиваем заглушку — мокаем Response.text
    mock_response = mock_request.return_value
    mock_response.text = '{"result": 0}'

    # Вызываем тестируемую функцию
    result = amout_rur(trans_action4)

    # Проверяем результат
    assert result == 0
