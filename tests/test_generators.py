import pytest
from src.generators import card_number_generator
from src.generators import transaction_descriptions
from src.generators import filter_by_currency


def test_filter_by_currency1(question_transactions1, answer_transactions1):
    key1 = "USD"
    nord1 = filter_by_currency(question_transactions1, key1)
    assert next(nord1) == answer_transactions1


def test_filter_by_currency2(question_transactions2, answer_transactions2):
    key2 = "USD"
    nord2 = filter_by_currency(question_transactions2, key2)
    assert next(nord2) == answer_transactions2


def test_filter_by_currency3(question_transactions3, answer_transactions3):
    key3 = "RUB"
    nord3 = filter_by_currency(question_transactions3, key3)
    assert next(nord3) == answer_transactions3


def test_filter_by_currency4(question_transactions4, answer_transactions4):
    key4 = "USD"
    nord4 = filter_by_currency(question_transactions4, key4)
    assert next(nord4) == answer_transactions4


def test_filter_by_currency5(question_transactions5, answer_transactions5):
    key5 = "RUB"
    nord5 = filter_by_currency(question_transactions5, key5)
    assert next(nord5) == answer_transactions5


def test_transaction_descriptions1(question_transactions1):
    forge1 = transaction_descriptions(question_transactions1)
    assert next(forge1) == "Перевод организации"


def test_transaction_descriptions2(question_transactions2):
    forge2 = transaction_descriptions(question_transactions2)
    assert next(forge2) == "Перевод со счета на счет"


def test_card_number_generator1(num_gen_start1, num_gen_finish1, answer_num_gen1):
    assert card_number_generator(num_gen_start1, num_gen_finish1) == answer_num_gen1


@pytest.mark.parametrize('start, finish, answer', [
                         (1, 2, ['0000 0000 0000 0001', '0000 0000 0000 0002']),
                         (3, 4, ['0000 0000 0000 0003', '0000 0000 0000 0004']),
                         (5, 6, ['0000 0000 0000 0005', '0000 0000 0000 0006'])]
                         )
def test_card_number_generator2(start, finish, answer):
    assert card_number_generator(start, finish) == answer
