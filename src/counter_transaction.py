import re


def bank_counter (list_data:list[dict], search_name:str) -> list[dict]:
    ser = str(list_data)
    pattern = (r"\{\'id\': \d+\.\d+, 'state':"
               r" \'")+ re.escape(search_name)+ (r"\', \'date\': \'\d+-\d+-\d+\w\d+:\d+:\d+\w\', \'amount\':"
                                                 r" \d+\.\d+, \'currency_name\': \'\w+\', \'currency_code\':"
                                                 r" \'\w+\', \'from\': \'[a-zA-Z\s0-9]+\', \'to\':"
                                                 r" \'[а-яА-Я\s0-9]+\', \'description\': \'[а-яА-Я\s0-9]+\'\}")
    result_list2 = re.findall(pattern, ser, flags=re.IGNORECASE)
    return result_list2


def bank_discr_operation (list_data:list [dict], categories:list) -> list[dict]:
    ser = str(list_data)
    result = {}
    for value in categories:
        pattern_cat = value
        quantity_category = re.findall(pattern_cat, ser, flags=re.IGNORECASE)
        kord = len(quantity_category)
        result [value] = kord
    return result
