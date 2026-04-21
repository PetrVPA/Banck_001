import json


def json_operation (name_dir):
    '''
    функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях.
    :return:
    '''
    try:
        with open(name_dir, 'r', encoding='utf-8') as operation:
            output_operation = json.load(operation)
    except ValueError:
        return []
    except FileNotFoundError:
        return []
    else:
        return output_operation
