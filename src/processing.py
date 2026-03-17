
def filter_by_state(card_info: list, kontr_state: str = 'EXECUTED') -> list:
    '''
    Функция принимает список словарей с данными банковских карт и их статусом
    статус карты не обязательный параметр по умолчанию 'EXECUTED'
    примерный формат словаря {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    :param card_info:переменная принимающая список словарей с данными карт, их статусами
    :param kontr_state:переменная по умолчанию ('EXECUTED') контролирующая статус карты
    :return: answer_list возвращаемый список словарей карт с параметром state == 'EXECUTED' по умолчанию
    '''
    answer_list = []
    for step in card_info:
        for key, value in step.items():
            if key == 'state' and value == kontr_state:
                answer_list.append(step)

    return answer_list


def sort_by_date(card_info: list, sort_wane: bool = True) -> list:
    '''
    Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате
    :param card_info:переменная принимающая список словарей с данными карт, их статусами
    :param sort_wane:переменаая определяющая направление сортировки, по умолчанию убывание
    :return: answer_list возвращаемый список словарей карт отсортированных по дате по умолчанию на убывание
    '''
    answer_list = sorted(card_info, key=lambda x: x['date'], reverse=sort_wane)
    return answer_list
