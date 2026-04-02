

def filter_by_currency():
    '''
    новая функция
    :return:
    '''
    pass


def transaction_descriptions():
    '''
    генератор
    :return:
    '''
    pass


def card_number_generator(start, finish):
    '''
    генератор
    :return:
    '''
    output_card: list = []
    range_card = [str(x).zfill(16) for x in range(start, finish + 1)]
    for octet in range_card:
        list_octet = [octet[i:i + 4] for i in range(0, len(octet), 4)]
        one_card = " ".join(list_octet)
        output_card.append(one_card)
    return output_card

