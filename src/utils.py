import json
from typing import Any
import logging
import os
from typing import Union


utils_log = logging.getLogger("my_utils")
# Создаем хендлер для вывода в файл
utils_log.setLevel(logging.DEBUG)
path_log = os.path.join(os.path.dirname(__file__), '..', 'logs', 'example.log')
file_handler = logging.FileHandler(path_log, encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
utils_log.addHandler(file_handler)


def json_operation(name_dir: str) -> Union[list, str]:
    '''
    функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях.
    :return:
    '''
    output_operation: list[Any] = []
    try:
        with open(name_dir, 'r', encoding='utf-8') as operation:
            output_operation = json.load(operation)
    except ValueError:
        utils_log.error(f'Не тот тип данных {operation}')
        return f'Не тот тип данных {operation}'
    except FileNotFoundError:
        utils_log.error(f'Файл не найден {name_dir}')
        return f'Файл не найден {name_dir}'
    else:
        utils_log.debug(f'Результат выполнения функции: {output_operation}')
        return output_operation
