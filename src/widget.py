import masks


def mask_card_account(my_info: str) -> str:
    """Функция, для вывода маски номера счета или номера карты"""
    if "Счет" in my_info:
        return f"Счет {masks.get_mask_card_number(my_info)}"
    else:
        new_info = my_info.split()
        if len(new_info) == 3:
            masked_account_num = masks.get_mask_card_number(new_info[2])
            return new_info[0] + " " + new_info[1] + " " + masked_account_num
        else:
            masked_account_num = masks.get_mask_card_number(new_info[1])
            return new_info[0] + " " + masked_account_num


def get_date(date_info: str) -> str:
    """Функция для корректного вывода даты"""
    key_date = date_info.split("T")[0]
    year, month, day = key_date.split("-")
    return f"{day}.{month}.{year}"


info_date = "2024-03-11T02:26:18.671407"
input_info = "Visa Gold 5999414228426353"
print(mask_card_account(input_info))
print(get_date(info_date))
