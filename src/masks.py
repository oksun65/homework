def get_mask_card_number(my_card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает маску номера"""
    # card_number = input("Введите номер карты: ").replace(" ", "")
    my_card_number = my_card_number.replace(" ", "")
    if len(my_card_number) != 16:
        raise ValueError("Вы ввели неверный номер карты")

    return f"{my_card_number[:4]} {my_card_number[4:6]}** **** {my_card_number[-4:]}"


def get_mask_account(my_account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает маску номера"""
    my_account_number = my_account_number.replace(" ", "")
    # account_number = input("Введите номер счета: ").replace(" ", "")
    if len(my_account_number) < 4:
        raise ValueError("Номер счета неверный")

    return f"**{my_account_number[-4:]}"

#
# card_number = "1456 897 546 32 14 56"
# account_number = "985632 147"
# print(get_mask_card_number(card_number))
# print(get_mask_account(account_number))
