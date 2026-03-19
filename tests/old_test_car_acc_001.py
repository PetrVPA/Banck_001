
from src.widget import mask_account_card
from src.widget import get_date

tor = input ("введите номер каты или счета: ")
print(mask_account_card (tor))

dat = input ("введите дату в американском формате: ")
print(get_date (dat))
