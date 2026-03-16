
def filter_by_state(card_info:list, kontr_state:str = 'EXECUTED')-> list:
    stend = []
    for tik in card_info:
        for key, value in tik.items():
            if key == 'state' and value == kontr_state:
                stend.append(tik)

    return stend

