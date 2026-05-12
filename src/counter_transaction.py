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


def bank_discr_operation3 (list_data:list [dict], categories:list) -> list[dict]:
    quantity_cat = []
    stage = []
    term = {}
    ser = str(list_data)
    for value in categories:
        print(value)
        # pattern_cat = (r"\{\'id\': \d+\.\d+, 'state':\', \'state\': '\w+\',\', \'date\':"
        #                r" \'\d+-\d+-\d+\w\d+:\d+:\d+\w\', \'amount\': \d+\.\d+, \'currency_name\':"
        #                r" \'\w+\', \'currency_code\': \'\w+\', \'from\': \'[a-zA-Z\s0-9]+\', \'to\':"
        #                r" \'[а-яА-Я\s0-9]+\', \'description\': \'") + re.escape(value)+ (r"\'\}")
        # pattern_cat2 = (r"\{\'id\': \d+\.\d+, 'state':\', \'state\': '\w+\',\', \'date\':"
        #                r" \'\d+-\d+-\d+\w\d+:\d+:\d+\w\', \'amount\': \d+\.\d+, \'currency_name\':"
        #                r" \'\w+\', \'currency_code\': \'\w+\', \'from\': \'[a-zA-Z\s0-9]+\', \'to\':"
        #                r" \'[а-яА-Я\s0-9]+\', \'description\': \'[а-яА-Я\s0-9]+\'\}")
        pattern_cat3 = value
        quantity_category = re.findall(pattern_cat3, ser, flags=re.IGNORECASE)
        quantity_cat.append(quantity_category)
        print(quantity_cat)
        set_cat = len(quantity_category)
        term = ({value:set_cat})
        stage.append[term]
    result = stage
    return result


def bank_discr_operation (list_data:list [dict], categories:list) -> list[dict]:
    ser = str(list_data)
    result = {}
    for value in categories:
        pattern_cat = value
        quantity_category = re.findall(pattern_cat, ser, flags=re.IGNORECASE)
        kord = len(quantity_category)
        result [value] = kord
    return result
