import json
import os
import sys
from typing import Any

import requests
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

load_dotenv(".env")

path_to_json = "data/operations.json"

API_KEY = os.getenv("API_KEY")
payload = {}
headers = {"apikey": API_KEY}

currency_code = "RUB"

with open(path_to_json, encoding="utf-8") as file:
    transactions_ = json.load(file)


def convert_to_rub(transactions: list[dict[Any:Any]], code: str) -> Any:
    """Функция для вывода сумм транзакций в рублях.
    Если транзакция в валюте отличной от рубля функция обращается к внешнему API источнику и конвертирует сумму в рубли
    """
    try:
        final_results = []
        for tran in transactions:
            amount = float(tran.get("operationAmount", {}).get("amount", 0))
            transact_code = tran.get("operationAmount", {}).get("currency", {}).get("code", {})
            if transact_code == "USD" or transact_code == "EUR":
                url = f"https://api.apilayer.com/exchangerates_data/convert?to={code}&from={transact_code}&amount={amount}"
                response = requests.request("GET", url, headers={"apikey": API_KEY}, data=payload)
                status_code = response.status_code
                if status_code == 200:
                    result = response.json().get("result")
                    final_results.append(result)
                else:
                    return f"Не успешный запрос, код ошибки: {status_code} {response.json()}"

            elif transact_code == code:
                final_results.append(amount)
        return final_results

    except Exception as e:
        print(Exception("Error"))
        raise e
