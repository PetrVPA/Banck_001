from src.utils_exs import work_csv
from src.utils_exs import work_exel
from src.utils import json_operation
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.generators import transaction_descriptions
from src.generators import filter_by_currency
from src.widget import get_date
from src.widget import mask_account_card
import os


if __name__ == '__main__':
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n ")
    print("Выберите необходимый пункт меню: \n ")
    print("1. Получить информацию о транзакциях из JSON - файла ")
    print("2. Получить информацию о транзакциях из CSV - файла ")
    print("3. Получить информацию о транзакциях из XLSX - файла\n ")

    while True:
        type_file = int(input("Введите пункт меню: "))
        if type_file != 1 and type_file != 2 and type_file != 3:
            print("Вы ошиблись при вводе...")
        else:
            break

    print("Введите статус, по которому необходимо выполнить фильтрацию операций")
    print("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING")

    while True:
        name_filtr = input("Введите статус: ")
        name_filtr = name_filtr.upper()
        if name_filtr != "EXECUTED" and name_filtr != "CANCELED" and name_filtr != "PENDING":
            print("Вы ошиблись при вводе...")
        else:
            break

    print("Отсортировать операцию по дате. да/нет\n")

    while True:
        date_choice = input("Ваш выбор: ")
        date_choice = date_choice.upper()
        if date_choice == "ДА":
            print("Отсортировать операцию по возрастанию или по убыванию. да/нет\n")

            while True:
                increasing_choice = input("Ваш выбор: ")
                increasing_choice = increasing_choice.upper()
                if increasing_choice != "ДА" and increasing_choice != "НЕТ":
                    print("Вы ошиблись при вводе...")
                else:
                    break

        if date_choice != "ДА" and date_choice != "НЕТ":
            print("Вы ошиблись при вводе...")
        else:
            break

    print("Выводить только рублевые транзакции. да/нет\n")

    while True:
        rub_choice = input("Ваш выбор: ")
        rub_choice = rub_choice.upper()
        if rub_choice != "ДА" and rub_choice != "НЕТ":
            print("Вы ошиблись при вводе...")
        else:
            break

    print("Отфильтровать список транзакций по определенному слову в описании? . да/нет\n")

    while True:
        word_choice = input("Ваш выбор: ")
        word_choice = word_choice.upper()
        if word_choice != "ДА" and word_choice != "НЕТ":
            print("Вы ошиблись при вводе...")
        else:
            break

    if word_choice == "ДА":
        print("Выберите тип интересуюших операций.")
        print("1. Перевод со счета на счет.")
        print("2. Открытие вклада.")
        print("3. Перевод с карты на карту.")
        print("4. Перевод организации.\n")

        while True:
            word_type = int(input("Ваш выбор: "))
            if word_type != 1 and word_type != 2 and word_type != 3 and word_type != 4:
                print("Вы ошиблись при вводе...")
            else:
                break
    else:
        word_type = 0

    if type_file == 1:
        answer_file = json_operation(os.path.join(os.path.dirname(__file__), '..', 'data', 'transactions.json'))

    if type_file == 2:
        answer_file = work_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'transactions.csv'))

    if type_file == 3:
        answer_file = work_exel(os.path.join(os.path.dirname(__file__), '..', 'data', 'transactions_excel.xlsx'))

    best = filter_by_state(answer_file, name_filtr)
    answer_file = list(best)

    if date_choice == "ДА":
        if increasing_choice == "ДА":
            revers_direction = False
        else:
            revers_direction = True
        answer_file = sort_by_date(answer_file, revers_direction)

    if rub_choice == "ДА":
        valut = "RUB"
        dancig = filter_by_currency(answer_file, valut)
        answer_file = list(dancig)

    if word_choice == "ДА":
        if word_type == 1:
            word_filtr = "Перевод со счета на счет"
            answer_file = transaction_descriptions(answer_file, word_filtr)
            answer_file = list(answer_file)

        if word_type == 2:
            word_filtr = "Открытие вклада"
            answer_file = transaction_descriptions(answer_file, word_filtr)
            answer_file = list(answer_file)

        if word_type == 3:
            word_filtr = "Перевод с карты на карту"
            answer_file = transaction_descriptions(answer_file, word_filtr)
            answer_file = list(answer_file)

        if word_type == 4:
            word_filtr = "Перевод организации"
            answer_file = transaction_descriptions(answer_file, word_filtr)
            answer_file = list(answer_file)
    print("Распечатываю итоговый список транзакций...\n")

    quantity_transaction = len(answer_file)

    if quantity_transaction == 0:
        print("Не найдено ни одной транзакции подходящие под Ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций: {quantity_transaction}\n")

        for answer in answer_file:
            dat_operacion = answer['date']
            dat_operacion = get_date(dat_operacion)
            type_operacion = answer['description']
            print(f"{dat_operacion} {type_operacion}")
            if (type_operacion == "Перевод с карты на карту" or
                    type_operacion == "Перевод со счета на счет" or type_operacion == "Перевод организации"):
                donor = answer['from']
                acceptor = answer['to']
                donor = mask_account_card(donor)
                acceptor = mask_account_card(acceptor)
                print(f"{donor} -> {acceptor}")
                adding = answer['amount']
                name_valut = answer['currency_code']
                if name_valut == "RUB":
                    name_valut = "руб."
                print(f"Сумма: {adding} {name_valut}\n")

            if type_operacion == "Открытие вклада":
                acceptor = answer['to']
                acceptor = mask_account_card(acceptor)
                print(f"Счет: {acceptor}")
                adding = answer['amount']
                name_valut = answer['currency_code']
                if name_valut == "RUB":
                    name_valut = "руб."
                print(f"Сумма: {adding} {name_valut}\n")
