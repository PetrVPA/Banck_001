import pytest
from src.generators import filter_by_currency
from src.generators import card_number_generator
from src.generators import transaction_descriptions


def test_filter_by_currency1(transactions1, answer_transactions1):
    key1 = "USD"
    assert filter_by_currency(transactions1, key1) == answer_transactions1


def test_filter_by_currency2(transactions1, answer_transactions2):
    key2 = "RUB"
    assert filter_by_currency(transactions1, key2) == answer_transactions2


def test_filter_by_currency3(transactions2, answer_transactions3):
    key3 = "RUB"
    assert filter_by_currency(transactions2, key3) == answer_transactions3


def test_transaction_descriptions(transactions1):
    assert transaction_descriptions(transactions1) == ['Перевод организации', 'Перевод со счета на счет',
                                                       'Перевод со счета на счет', 'Перевод с карты на карту',
                                                       'Перевод организации']


def test_transaction_descriptions1(transactions2):
    assert transaction_descriptions(transactions2) == []


def test_transaction_descriptions2():
    assert transaction_descriptions([]) == []


def test_card_number_generator1(num_gen_start1, num_gen_finish1, answer_num_gen1):
    assert card_number_generator(num_gen_start1, num_gen_finish1) == answer_num_gen1


@pytest.mark.parametrize('start, finish, answer', [
                         (1, 2, ['0000 0000 0000 0001', '0000 0000 0000 0002']),
    (3, 4, ['0000 0000 0000 0003', '0000 0000 0000 0004']),
    (5, 6, ['0000 0000 0000 0005', '0000 0000 0000 0006'])
])
def test_card_number_generator2(start, finish, answer):
    assert card_number_generator(start, finish) == answer
