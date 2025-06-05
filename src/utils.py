import json
import logging

logging.basicConfig(encoding="utf-8")
logger = logging.getLogger("utils.py")
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_json_file(input_file):
    """Функция для чтения json файла с транзакциями"""
    with open(input_file, "r", encoding="UTF-8") as f:
        logger.info("File is opened")
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            logger.error("Error")
            return []

        if data == "":
            logging.INFO("Empty data")
            return []

        return data
