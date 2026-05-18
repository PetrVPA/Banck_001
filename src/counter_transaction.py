import re
from collections import Counter


def bank_counter(list_data: list[dict], search_name: str) -> list[dict]:
    '''
    Функция 1 пункта домашней работы реализующий библитеку re реализует фильтрацию транзакций по статусу CANCELED,
    EXECUTED, PENDING
    :param list_data: предоставляемый перечень транзакций (список словарей)
    :param search_name: выбранный пользователем один из трех статусов
    :return: возвращает отфильтрованный список словарей
    '''
    ser = str(list_data)
    pattern = "{0}{1}{2}".format((r"\{\'id\': \d+\.\d+, 'state':"
                                  r" \'"), re.escape(search_name),
                                 (r"\', \'date\': \'\d+-\d+-\d+\w\d+:\d+:\d+\w\', \'amount\':"
                                  r" \d+\.\d+, \'currency_name\': \'\w+\', \'currency_code\':"
                                  r" \'\w+\', \'from\': \'[a-zA-Z\s0-9]+\', \'to\':"
                                  r" \'[а-яА-Я\s0-9]+\', \'description\': \'[а-яА-Я\s0-9]+\'\}"))
    result_list2 = re.findall(pattern, ser, flags=re.IGNORECASE)
    return result_list2


def bank_discr_operation(list_data: list[dict], search: str) -> list[dict]:
    '''
    Функция 2 пункта домашней работы истользующий ключ "description" показывающая какие и какое количество операций
    выполнено по ключу description
    :param list_data: список словарей транзакций
    :return: result: словарь с типом операций - значение ключа "description" их количество таких операций
    '''
    data = {}
    answer_funk = []

    list_trans = [t['description'] for t in list_data]
    category_count = Counter(list_trans)
    print(category_count)
    pattern = str(search)

    for key, value in category_count.items():
        if re.search(pattern, str(key), re.IGNORECASE):
            data[key] = value
    answer_funk.append(data)
    return answer_funk
