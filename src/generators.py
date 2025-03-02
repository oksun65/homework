import random


def filter_by_currency(transactions, currency_name):
    for tran in transactions:
        if tran.get("currency_name") == currency_name:
            yield tran


def transaction_descriptions(transactions):
    for tran in transactions:
        yield tran.get("description")


def card_number_generator(start=1, finish=9999):
    while True:
        # Генерация 16 случайных цифр
        card_number = " ".join(f"{random.randint(start, finish):04d}" for _ in range(4))
        yield card_number
