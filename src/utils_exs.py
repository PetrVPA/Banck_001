import os
import pandas as pd
import openpyxl


def work_csv(csv_path: str)->list:
    '''
        Функция принимаем в виде строки адрес к CSV файлу с банковскими операциями считывает его как датафрейм и
        преобразует в список словарей
        Переменная csv_path - путь к обрабатываемому файлу
        Переменная csv_operation - обрабатываемый датафрейм
        Переменная csv_result - список словарей с транзакциями
    '''
    csv_operation = pd.read_csv(csv_path)
    csv_result = csv_operation.to_dict('records')
    return csv_result



def work_exel(ex_path: str)->list:
    '''
        Функция принимаем в виде строки адрес к xlsx файлу с банковскими операциями считывает его как датафрейм и
        преобразует в список словарей
        Переменная ex_path - путь к обрабатываемому файлу
        Переменная csv_operation - обрабатываемый датафрейм
        Переменная ex_result - список словарей с транзакциями
        '''
    ex_operation = pd.read_excel(ex_path)
    ex_result = ex_operation.to_dict('records')
    return ex_result


