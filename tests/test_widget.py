import pytest
from src.widget import mask_account_card
from src.widget import get_date


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


def test_wid_cards(card_name: str) -> str:
    assert mask_account_card(card_name) == "Visa Platinum 1234 12** **** 1234"


def test_wid_cards_err(error_card_name: str) -> str:
    assert mask_account_card(error_card_name) == "Ошибка ввода"


def test_wid_account(account_name: str) -> str:
    assert mask_account_card(account_name) == "Счет **7890"


def test_wid_account_err(error_account_name: str) -> str:
    assert mask_account_card(error_account_name) == "Ошибка ввода"


def test_wid_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11:03:2024"
