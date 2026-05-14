import pytest


@pytest.fixture
def test_data():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture
def off_status_data():
    return 'CANCELED'


@pytest.fixture
def card_name():
    return "Visa Platinum 1234123412341234"


@pytest.fixture
def error_card_name():
    return "Visa Platinum 1234123u12341234"


@pytest.fixture
def account_name():
    return "Счет 12345678901234567890"


@pytest.fixture
def error_account_name():
    return "Счет 123456789u1234567890"


@pytest.fixture
def question_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


@pytest.fixture
def question_transactions1():
    return [
        {
            "id": 3162071,
            "state": "EXECUTED",
            "date": "2022-11-02T17:44:03Z",
            "amount": 20231,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "American Express 9087124023963879",
            "to": "Visa 0990855089517781",
            "description": "Перевод с карты на карту"
        }
    ]


@pytest.fixture
def question_transactions2():
    return [
        {
            "id": 5305859,
            "state": "CANCELED",
            "date": "2022-02-03T13:43:10Z",
            "amount": 18940,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "American Express 7575628496748633",
            "to": "American Express 8201977224219171",
            "description": "Перевод со счета на счет"
        }
    ]


@pytest.fixture
def question_transactions3():
    return [
        {
            "id": 1740751,
            "state": "EXECUTED",
            "date": "2021-09-08T22:23:31Z",
            "amount": 34518,
            "currency_name": "RUB",
            "currency_code": "RUB",
            "from": "Счет 30907628929571752743",
            "to": "Счет 35863137762112178701",
            "description": "Перевод со счета на счет"
        }
    ]


@pytest.fixture
def question_transactions4():
    return [
        {
            "id": 1738376,
            "state": "CANCELED",
            "date": "2020-10-24T04:37:19Z",
            "amount": 13638,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Discover 5838445654310457",
            "to": "Mastercard 1227184681117045",
            "description": "Перевод с карты на карту"
        }
    ]


@pytest.fixture
def question_transactions5():
    return [
        {
            "id": 671277,
            "state": "CANCELED",
            "date": "2021-10-11T07:33:00Z",
            "amount": 30298,
            "currency_name": "RUB",
            "currency_code": "RUB",
            "from": "Счет 41751976927052945311",
            "to": "Счет 34771784449161833522",
            "description": "Перевод со счета на счет"
        }
    ]


@pytest.fixture
def answer_transactions1():
    return {
            "id": 3162071,
            "state": "EXECUTED",
            "date": "2022-11-02T17:44:03Z",
            "amount": 20231,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "American Express 9087124023963879",
            "to": "Visa 0990855089517781",
            "description": "Перевод с карты на карту"
        }


@pytest.fixture
def answer_transactions2():
    return {
            "id": 5305859,
            "state": "CANCELED",
            "date": "2022-02-03T13:43:10Z",
            "amount": 18940,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "American Express 7575628496748633",
            "to": "American Express 8201977224219171",
            "description": "Перевод со счета на счет"
        }


@pytest.fixture
def answer_transactions3():
    return {
            "id": 1740751,
            "state": "EXECUTED",
            "date": "2021-09-08T22:23:31Z",
            "amount": 34518,
            "currency_name": "RUB",
            "currency_code": "RUB",
            "from": "Счет 30907628929571752743",
            "to": "Счет 35863137762112178701",
            "description": "Перевод со счета на счет"
        }


@pytest.fixture
def answer_transactions4():
    return {
            "id": 1738376,
            "state": "CANCELED",
            "date": "2020-10-24T04:37:19Z",
            "amount": 13638,
            "currency_name": "USD",
            "currency_code": "USD",
            "from": "Discover 5838445654310457",
            "to": "Mastercard 1227184681117045",
            "description": "Перевод с карты на карту"
        }


@pytest.fixture
def answer_transactions5():
    return {
            "id": 671277,
            "state": "CANCELED",
            "date": "2021-10-11T07:33:00Z",
            "amount": 30298,
            "currency_name": "RUB",
            "currency_code": "RUB",
            "from": "Счет 41751976927052945311",
            "to": "Счет 34771784449161833522",
            "description": "Перевод со счета на счет"
        }


@pytest.fixture
def answer_descriptions1():
    return ['Перевод организации', 'Перевод со счета на счет',
            'Перевод со счета на счет', 'Перевод с карты на карту', 'Перевод организации']


@pytest.fixture
def num_gen_start1():
    return 23


@pytest.fixture
def num_gen_finish1():
    return 26


@pytest.fixture
def answer_num_gen1():
    return ['0000 0000 0000 0023', '0000 0000 0000 0024', '0000 0000 0000 0025', '0000 0000 0000 0026']


@pytest.fixture
def log_ansver_001():
    return "my_function ok\n"


@pytest.fixture
def log_ansver_002():
    return "my_function error: ZeroDivisionError. Inputs: (6, 0), {}\n"


@pytest.fixture
def log_ansver_003():
    return "my_function error: TypeError. Inputs: (6, t), {}\n"


@pytest.fixture
def question_transactions_z():
    return [
  {
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
    "id": 366176,
    "state": "EXECUTED",
    "date": "2020-08-02T09:35:18Z",
    "amount": 29482,
    "currency_name": "RUB",
    "currency_code": "RUB",
    "from": "Discover 0325955596714937",
    "to": "Visa 3820488829287420",
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
  },
  {
    "id": 1962667,
    "state": "PENDING",
    "date": "2023-10-22T09:43:32Z",
    "amount": 18588,
    "currency_name": "USD",
    "currency_code": "USD",
    "from": "Discover 5448680041474638",
    "to": "Счет 81509213611289630443",
    "description": "Перевод организации"
  },
  {
    "id": 5294458,
    "state": "PENDING",
    "date": "2022-06-20T18:08:20Z",
    "amount": 16836,
    "currency_name": "RUB",
    "currency_code": "RUB",
    "from": "Visa 2759011965877198",
    "to": "Счет 38287443300766991082",
    "description": "Перевод с карты на карту"
  }
    ]
