from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(card_data: str) -> str:
    '''
    Функция принимает зачение кары или счета в виде Visa Platinum 7000792289606361 или Счет 73654108430135874305
    возвращает маскированные данные карты или счета в виде Visa Platinum 7000 79** **** 6361 для карты и Счет **4305
    для счета.
    card_data переменная принимающая значение введенное пользователем
    card_set переменная контроля алгоритма работы с картой
    account_set преременная контроля алгоритма работы со счетом

    '''
    card_set = card_data[-16:]
    account_set = card_data[-20:]
    change_account = account_set.isdigit()
    change_card = card_set.isdigit()

    if change_account:
        account = int(account_set)
        result_digit_account = get_mask_account(account)
        res_fool = "Счет " + result_digit_account
        return res_fool

    if change_card:
        card = int(card_set)
        result_digit_card = get_mask_card_number(card)
        res_fool = card_data[:-16] + result_digit_card
        return res_fool
    return "Ошибка ввода"


def get_date(input_date: str) -> str:
    '''
    Функция принимает значение в непонятном американском формате переводя его в понятный человеческий
    2024-03-11T02:26:18.671407 -> 11.03.2024
    :input_date переменная принимающая значение
    :dt_years переменная принимающая значение года
    :dt_months переменная принимающая значение месяца
    :dt_days переменная принимающая значение дня
    '''

    dt_years = input_date[0:4]
    dt_months = input_date[5:7]
    dt_days = input_date[8:10]
    return dt_days + ":" + dt_months + ":" + dt_years
