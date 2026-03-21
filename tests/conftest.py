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