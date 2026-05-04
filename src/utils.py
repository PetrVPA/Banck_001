import json
from typing import Any
import logging


utils_log = logging.getLogger("my_utils")
# Создаем хендлер для вывода в файл
utils_log.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/example.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
utils_log.addHandler(file_handler)


def json_operation(name_dir: str) -> list:
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
        return []
    except FileNotFoundError:
        utils_log.error(f'Файл не найден {name_dir}')
        return []
    else:
        utils_log.debug('Все получилось')
        return output_operation
