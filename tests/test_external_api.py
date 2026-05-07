from src.external_api import amout_rur
from unittest.mock import patch
import os
from dotenv import load_dotenv
import requests
import requests.exceptions

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
    'id': 441966776,
    'state': 'EXECUTED',
    'date': '2019-08-26T10:50:58.294041',
    'operationAmount': {'amount': '17367.34', 'currency': {'name': 'RUB.', 'code': 'RUB'}},
    'description': 'Перевод организации',
    'from': 'Maestro 1596837868705199',
    'to': 'Счет 64686473678894779589'
}

trans_action3 = {
    'id': 441945776,
    'state': 'EXECUTED',
    'date': '2019-08-26T10:50:58.294041',
    'operationAmount': {'amount': '28836.74', 'currency': {'name': 'USD.', 'code': 'USD'}},
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
    mock_response.text = '{"result": 17367.34}'

    # Вызываем тестируемую функцию
    result = amout_rur(trans_action2)

    # Проверяем результат
    assert result == 17367.34

    # Запрос не проверяем, конвертации to=RUB&from=RUB нет
    # expected_url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=RUB&amount=17367.34"
    # mock_request.assert_called_once_with(
    #     "GET",
    #     expected_url,
    #     headers={"apikey": api_token},
    #     data={}
    # )


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


@patch('src.external_api.requests.request')
def test_amout_rur5(mock_request):
    # Настраиваем заглушку — мокаем Response.text
    mock_request.side_effect = requests.exceptions.Timeout

    # Вызываем тестируемую функцию
    result = amout_rur(trans_action3)

    # Проверяем результат
    assert result == "Превышено время ожидания..."


@patch('src.external_api.requests.request')
def test_amout_rur6(mock_request):
    # Настраиваем заглушку — мокаем Response.text
    mock_request.side_effect = requests.exceptions.TooManyRedirects

    # Вызываем тестируемую функцию
    result = amout_rur(trans_action3)

    # Проверяем результат
    assert result == "Количество перенаправлений превысило предел"


@patch('src.external_api.requests.request')
def test_amout_rur7(mock_request):
    # Настраиваем заглушку — мокаем Response.text
    mock_request.side_effect = requests.exceptions.RequestException

    # Вызываем тестируемую функцию
    result = amout_rur(trans_action3)

    # Проверяем результат
    assert result == "Ошибка в обращении к сервису. Попробуйте позже."
