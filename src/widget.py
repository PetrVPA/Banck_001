

def mask_account_card (card_data: str)->str:
    card_set = card_data[-16:]
    print (card_set)
    account_set = card_data[-20:]
    print (account_set)
    change_account = account_set.isdigit()
    change_card = card_set.isdigit()
    if change_account:
        set_account = account_set[-4:]
        mask_account = "Счет "+"**"+set_account
        return mask_account
    if change_card:
        oktet_0 = card_data[0:-17]
        oktet_1 = card_set[0:4]
        oktet_2 = card_set[4:6]
        oktet_3 = "****"
        oktet_4 = card_set[12:16]
        mask_card = oktet_0 + " " + oktet_1 + " " + oktet_2 + "*** " + oktet_3 + " " + oktet_4
        return mask_card
    return "Ошибка ввода"