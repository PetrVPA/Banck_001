from src.utils import json_operation
from unittest.mock import patch


answer_json_string_01 = [
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "5221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
]

answer_json_string_02 = [
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "18321.39",
      "currency": {
        "name": "RUB",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
]

answer_json_string_03 = [
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "1351.79",
      "currency": {
        "name": "EUR",
        "code": "EUR"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
]

answer_json_string_04 = [{}]

answer_json_string_05 = [
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "1351.79",
      "currency": {
        "name": "AUD",
        "code": "AUD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
]


def test_utils1():
    stend1 = json_operation("../Banck_001/data/json_string_01.json")
    assert stend1 == answer_json_string_01


def test_utils2():
    stend2 = json_operation("../Banck_001/data/json_string_02.json")
    assert stend2 == answer_json_string_02


def test_utils3():
    stend3 = json_operation("../Banck_001/data/json_string_03.json")
    assert stend3 == answer_json_string_03


def test_utils4():
    stend4 = json_operation("../Banck_001/data/json_string_04.json")
    assert stend4 == answer_json_string_04


def test_utils5():
    stend5 = json_operation("../Banck_001/data/json_string_05.json")
    assert stend5 == answer_json_string_05


def test_utils6():
    stend6 = json_operation("../Banck_001/data/json_string_xx.json")
    assert stend6 == 'Файл не найден ../Banck_001/data/json_string_xx.json'


@patch('src.utils.json.load')
def test_utils7(mock_utils):
    # Настраиваем заглушку — мокаем
    mock_utils.side_effect = FileNotFoundError('Файл не найден json_string_xx.json')

    stend7 = json_operation("../Banck_001/data/json_string_xx.json")

    assert stend7 == 'Файл не найден ../Banck_001/data/json_string_xx.json'
