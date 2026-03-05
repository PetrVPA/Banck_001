

def mask_account_card (card_data: str)->str:
    '''
    Функция принимает зачение кары или счета в виде Visa Platinum 7000792289606361 или Счет 73654108430135874305
    возвращает маскированные данные карты или счета в виде Visa Platinum 7000 79** **** 6361 для карты и Счет **4305
    для счета.

    :param card_data: принимаемое от пользователя значение
    :card_set переменная для идентификации алгоритма для карты
    :account_set переменная для идентификации алгоритма для счета
    :oktet_0..._4 переменные для формирования маски карты
    :mask_account возвращаемое значение для счета
    :mask_card возвращаемое значение для карты
    '''
    card_set = card_data[-16:]
    print (card_set)
    account_set = card_data[-20:]
    print (account_set)
    change_account = account_set.isdigit()
    change_card = card_set.isdigit()
    if change_account:
        set_account = account_set[-4:]
        mask_account = "Счет "+"**"+set_account
        return mask_account
    if change_card:
        oktet_0 = card_data[0:-17]
        oktet_1 = card_set[0:4]
        oktet_2 = card_set[4:6]
        oktet_3 = "****"
        oktet_4 = card_set[12:16]
        mask_card = oktet_0 + " " + oktet_1 + " " + oktet_2 + "*** " + oktet_3 + " " + oktet_4
        return mask_card
    return "Ошибка ввода"


def get_date (input_date: str)->str:
    #2024-03-11T02:26:18.671407 -> 11.03.2024
    dt_years = input_date[0:4]
    dt_months = input_date[5:7]
    dt_days = input_date[8:10]
    return dt_days + ":" + dt_months + ":" + dt_years