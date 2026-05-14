from src.counter_transaction import bank_counter
from src.counter_transaction import bank_discr_operation
import pytest


@pytest.fixture
def test_bank_counter1(question_transactions_z):
    search_name = 'CANCELED'
    list_data = [{
        "id": 593027,
        "state": "CANCELED",
        "date": "2023-07-22T05:02:01Z",
        "amount": 30368,
        "currency_name": "EUR",
        "currency_code": "EUR",
        "from": "Visa 1959232722494097",
        "to": "Visa 6804119550473710",
        "description": "Перевод с карты на карту"
    },
        {
            "id": 5380041,
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "amount": 23789,
            "currency_name": "EUR",
            "currency_code": "EUR",
            "from": "null",
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада"
        }
    ]
    assert bank_counter(question_transactions_z, search_name) == list_data


@pytest.fixture
def test_bank_counter2(question_transactions_z):
    search_name = 'EXECUTED'
    list_data = [{
        "id": 650703,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210,
        "currency_name": "USD",
        "currency_code": "USD",
        "from": "Счет 68856226464168431377",
        "to": "Счет 64009673148302301520",
        "description": "Перевод со счета на счет"
    },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740,
            "currency_name": "RUB",
            "currency_code": "RUB",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту"
        },
        {
            "id": 366176,
            "state": "EXECUTED",
            "date": "2020-08-02T09:35:18Z",
            "amount": 29482,
            "currency_name": "RUB",
            "currency_code": "RUB",
            "from": "Discover 0325955596714937",
            "to": "Visa 3820488829287420",
            "description": "Перевод с карты на карту"
        }
    ]
    assert bank_counter(question_transactions_z, search_name) == list_data


@pytest.fixture
def test_bank_counter3(question_transactions_z):
    search_name = 'PENDING'
    list_data = [
        {"id": 1962667,
         "state": "PENDING",
         "date": "2023-10-22T09:43:32Z",
         "amount": 18588,
         "currency_name": "USD",
         "currency_code": "USD",
         "from": "Discover 5448680041474638",
         "to": "Счет 81509213611289630443",
         "description": "Перевод организации"},
        {"id": 5294458, "state": "PENDING", "date": "2022-06-20T18:08:20Z", "amount": 16836, "currency_name": "RUB",
         "currency_code": "RUB", "from": "Visa 2759011965877198", "to": "Счет 38287443300766991082",
         "description": "Перевод с карты на карту"}]
    assert bank_counter(question_transactions_z, search_name) == list_data


@pytest.fixture
def test_bank_counter4(question_transactions_z):
    search_name = ''
    list_data = []
    assert bank_counter(question_transactions_z, search_name) == list_data


@pytest.fixture
def test_bank_counter5(question_transactions_z):
    search_name = 'TEST'
    list_data = []
    assert bank_counter(question_transactions_z, search_name) == list_data


@pytest.fixture
def test_bank_discr_operation1(question_transactions_z):
    list_data = ['Перевод организации', 'Перевод со счета на счет']
    assert bank_discr_operation(question_transactions_z, list_data) == {'Перевод организации': 1,
                                                                        'Перевод со счета на счет': 1}


@pytest.fixture
def test_bank_discr_operation2(question_transactions_z):
    list_data = ['Перевод с карты на карту', 'Открытие вклада']
    assert bank_discr_operation(question_transactions_z, list_data) == {'Перевод с карты на карту': 4,
                                                                        'Открытие вклада': 1}


@pytest.fixture
def test_bank_discr_operation3(question_transactions_z):
    list_data = ['Перевод с карты на карту', 'Открытие вклада', 'Перевод организации', 'Перевод со счета на счет']
    assert bank_discr_operation(question_transactions_z, list_data) == {'Перевод с карты на карту': 4,
                                                                        'Открытие вклада': 1, 'Перевод организации': 1,
                                                                        'Перевод со счета на счет': 1}
