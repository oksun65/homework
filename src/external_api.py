import json
import os
import requests
from dotenv import load_dotenv
from typing import Any
from utils import read_json_file

load_dotenv('.env')

path_to_json = 'data/operations.json'

load_dotenv()

API_KEY = os.getenv('API_KEY')
payload = {}
headers = {"apikey": API_KEY}

currency_code = "RUB"

with open(path_to_json, encoding='utf-8') as file:
    transactions_ = json.load(file)


def convert_to_rub(transactions: list[dict[Any: Any]], code: str) -> Any:
    try:
        final_results = []
        for tran in transactions:
            amount = float(tran.get("operationAmount").get("amount"))
            transact_code = tran.get("operationAmount").get("currency").get("code")
            if transact_code == "USD" or transact_code == "EUR":
                url = f"https://api.apilayer.com/exchangerates_data/convert?to={code}&from={transact_code}&amount={amount}"
                response = requests.request("GET", url, headers={"api_key":API_KEY}, data=payload)
                status_code = response.status_code
                if status_code == 200:
                    result = response.json().get("result")
                    final_results.append(result)
                else:
                    return f"Не успешный запрос, код ошибки: {status_code}"
            elif transact_code == code:
                final_results.append(amount)
        return final_results

    except Exception as e:
        print(Exception("Error"))
        raise Exception


if __name__=="__main__":
    data = read_json_file('data/operations.json')
    x1=convert_to_rub(data, 'RUB')
    print(x1)
