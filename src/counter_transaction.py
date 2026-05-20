import re
from collections import Counter


def bank_counter(list_data: list[dict], search_name: str) -> list[dict]:
    '''
    Функция 1 пункта домашней работы реализующий библитеку re реализует фильтрацию транзакций по строке содержащей
    значение CANCELED, EXECUTED или PENDING. Любое другое значение вернет список пустого словаря.
    :param list_data: предоставляемый перечень транзакций (список словарей)
    :param search_name: выбранный пользователем один из трех статусов
    :return: возвращает отфильтрованный список словарей
    '''
    result_list = []
    search_name = str(search_name)
    search_name = search_name.upper()
    if search_name == 'CANCELED' or search_name == 'PENDING' or search_name == 'EXECUTED':
        for stend in list_data:
            tez = str(stend)
            result_list2 = re.search(search_name, tez, flags=re.IGNORECASE)
            if result_list2:
                result_list.append(stend)
        return result_list
    else:
        return [{}]


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
    search = str(search)

    for key, value in category_count.items():
        if re.search(search, str(key), re.IGNORECASE):
            data[key] = value
    answer_funk.append(data)
    return answer_funk
