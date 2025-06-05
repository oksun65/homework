import logging

logging.basicConfig(encoding="utf-8")
logger = logging.getLogger("masks.py")
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(my_card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает маску номера"""
    # card_number = input("Введите номер карты: ").replace(" ", "")
    logger.info("Получили корректный номер карты")
    my_card_number = my_card_number.replace(" ", "")
    if len(my_card_number) != 16:
        logger.error("Ошибка чтения карты")
        raise ValueError("Вы ввели неверный номер карты")

    return f"{my_card_number[:4]} {my_card_number[4:6]}** **** {my_card_number[-4:]}"


def get_mask_account(my_account_number: str) -> str:
    """Функция, которая принимает на вход номер счета и возвращает маску номера"""
    logger.info("Получили корректный номер счета")
    my_account_number = my_account_number.replace(" ", "")
    # account_number = input("Введите номер счета: ").replace(" ", "")
    if len(my_account_number) < 4:
        logger.error("Ошибка чтения номера счета")
        raise ValueError("Номер счета неверный")

    return f"**{my_account_number[-4:]}"
