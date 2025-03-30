def filter_by_currency(transactions, currency_name):
    for tran in transactions:
        if tran.get("operationAmount", {}).get("currency", {}).get("code") == currency_name:
            yield tran


def transaction_descriptions(transactions):
    for tran in transactions:
        yield tran.get("description")


def card_number_generator(start, finish):

    for num in range(start, finish + 1):
        str_num = str(num)
        ful_num = str_num.zfill(16)
        yield f"{ful_num[:4]} {ful_num[4:8]} {ful_num[8:12]} {ful_num[12:16]}"
