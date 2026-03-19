from src.widget import mask_account_card
from src.widget import get_date

def test_wid_cards():
    assert mask_account_card("Visa Platinum 1234123412341234") == "Visa Platinum 1234 12** **** 1234"


def test_wid_cards_err():
    assert mask_account_card("Visa Platinum 1234123u12341234") == "Ошибка ввода"


def test_wid_account():
    assert mask_account_card("Счет 12345678901234567890") == "Счет **7890"


def test_wid_account_err():
    assert mask_account_card("Счет 123456789u1234567890") == "Ошибка ввода"


def test_wid_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11:03:2024"