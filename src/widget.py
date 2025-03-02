from .masks import get_mask_account, get_mask_card_number


def mask_card_account(my_info: str) -> str:
    """Функция, для вывода маски номера счета или номера карты"""
    if "Счет" in my_info:
        return f"Счет {get_mask_account(my_info)}"
    else:
        new_info = my_info.split()
        if len(new_info) == 3:
            masked_account_num = get_mask_card_number(new_info[2])
            return new_info[0] + " " + new_info[1] + " " + masked_account_num
        else:
            masked_account_num = get_mask_card_number(new_info[1])
            return new_info[0] + " " + masked_account_num


def get_date(date_info: str) -> str:
    """Функция для корректного вывода даты"""
    key_date = date_info.split("T")[0]
    year, month, day = key_date.split("-")
    if year >= "2026" or month >= "13" or day >= "31":
        return "Неверные данные"
    elif "T" not in date_info:
        return "Ошибочные данные"

    else:
        return f"{day}.{month}.{year}"
