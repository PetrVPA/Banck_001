from src.widget import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("1234123412341234") == "1234 12** **** 1234"


def test_get_mask_card_number_err1():
    assert get_mask_card_number("12341234123412344") == ""


def test_get_mask_card_number_err2():
    assert get_mask_card_number("123412341234123t") == ""


def test_get_mask_account():
    assert get_mask_account("12345678901234567890") == "**7890"


def test_get_mask_account_err1():
    assert get_mask_account("123456789012p34567890") == ""


def test_get_mask_account_err2():
    assert get_mask_account("123456789012534567890") == ""
