import pytest
from src.widget import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize("input_set, output_set", [
    ("1234123412341234", "1234 12** **** 1234"),
    ("12341234123412344", ""),
    ("123412341234123t", ""),
    ("123412342341234", "")
])
def test_get_mask_card_number(input_set, output_set):
    assert get_mask_card_number(input_set) == output_set


@pytest.mark.parametrize("input_set, output_set", [
    ("12345678901234567890", "**7890"),
    ("123456789012p3456790", ""),
    ("123456789012534567890", ""),
    ("1234567843901253790", "")
])
def test_get_mask_account(input_set, output_set):
    assert get_mask_account(input_set) == output_set
