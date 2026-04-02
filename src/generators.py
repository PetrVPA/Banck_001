

def filter_by_currency(list_operation, key_filter):
    '''
    Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    (например, USD)
    return completed_transactions возвращаемый список словарей отвечающих требованию выбранной валюты транзакции
    meaning_key очередная транзакция подвергающаяся анализу
    list_operation перечень (список) всех анализируемых транзакций
    key_filter ключ определяющий выбор валюты для обработки транзакций
    '''
    completed_transactions = [meaning_key for meaning_key in list_operation if meaning_key ["operationAmount"] \
        ["currency"] ["code"] == key_filter]
    return completed_transactions


def transaction_descriptions():
    '''
    генератор
    :return:
    '''
    pass


def card_number_generator(start, finish):
    '''
    генератор формирующий карты в формате октетов с пробелами, начиная от стартового до финишного значений
    range_card формирует карты к шестнадцати разрядной форме номера карты
    list_octet формирует список октетов содержащихся в номере карты
    one_card сформированный номер карты в нужном формате (готовый)
    return output_card список уже готовых карт с номерами от стартового до финишного
    '''
    output_card: list = []
    range_card = [str(x).zfill(16) for x in range(start, finish + 1)]
    for octet in range_card:
        list_octet = [octet[i:i + 4] for i in range(0, len(octet), 4)]
        one_card = " ".join(list_octet)
        output_card.append(one_card)
    return output_card
