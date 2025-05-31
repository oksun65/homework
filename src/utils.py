import json


def read_json_file(input_file):
    """Функция для чтения json файла с транзакциями"""
    with open(input_file, "r", encoding="UTF-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

        if data == "":
            return []

        return data
