from src.masks import get_mask_card_number


number_card = input("Введите 16-ти значный номер банковской карты ->")
print(get_mask_card_number (number_card))
print('//////////////////////////')
print (get_mask_card_number("1234123412341234"))