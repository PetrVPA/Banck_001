import logging

utils_log = logging.getLogger("my_mask")
# Создаем хендлер для вывода в файл
utils_log.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/example.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
utils_log.addHandler(file_handler)


def get_mask_card_number(number_card: int) -> str:
    """ Принимает номер карты 16 чисел и выдает замаскированый ответ: 1234 12** **** 1234
    number_card int переменная принимающая значение вводимое пользователем
    mask_card str   возвращаемое значение функции
    index_card str  строковая переменная с которой проходит работа по выделению октетов маски карты
    lenght_digit_card int  переменная контролирующая правильное количество введенных цифр пользователем
    check_digit bool  переменная контролирующая что введенные пользователем значения = только цифры
    oktet_1...4 str  переменные октеты для формирования строки ответа функции
    oktet_2 и oktet_3 в полном виде закоментированы на случай оперативного изменения маски
    """
    mask_card: str = ""
    index_card = str(number_card)
    lenght_digit_card = len(index_card)
    check_digit = index_card.isdigit()
    if lenght_digit_card == 16 and check_digit:
        oktet_1 = index_card[0:4]
        oktet_2 = index_card[4:6] + "**"
        # oktet_2 = index_card[4:8]
        oktet_3 = "****"
        # oktet_3 = index_card[8:12]
        oktet_4 = index_card[12:16]
        mask_card = oktet_1 + " " + oktet_2 + " " + oktet_3 + " " + oktet_4
        utils_log.debug('Формирование маски БК выполнено')
    else:
        if lenght_digit_card != 16 and check_digit:
            print("Неверное количество цифр")
            utils_log.debug('Неверное количество цифр')
        if not check_digit:
            print("Введены символы отличные от цифры")
            utils_log.debug'Введены не только цифры')
    return str(mask_card)


def get_mask_account(number_account: int) -> str:
    """ Принимает номер счета 20 чисел и выдает замаскированый ответ: **1234
    number_account int  переменная принимающее значение водимое пользователем
    mask_account str  возвращаемая функцией строковая переменная маскированного счета
    index_account str   переменная строковая для операций формирования маски счета
    index_account int   переменная контролирующая количество вводимых символов
    check_digit bool  переменная контролирующая что пользователь ввел = только цифры
    """
    mask_account: str = ""
    index_account = str(number_account)
    lenght_digit_account = len(index_account)
    check_digit = index_account.isdigit()
    if lenght_digit_account == 20 and check_digit:
        mask_account = "**" + index_account[16:21]
        utils_log.debug('Формирование маски счета выполнено')
    else:
        if lenght_digit_account != 20 and check_digit:
            print("Неверное колличество цифр")
            utils_log.debug('Неверное количество цифр')
        if not check_digit:
            print("Введены символы отличные от цифры")
            utils_log.debug('Введены не только цифры')
    return str(mask_account)
