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
            amount = float(tran.get("operationAmount",{}).get("amount", 0))
            transact_code = tran.get("operationAmount", {}).get("currency", {}).get("code", {})
            if transact_code == "USD" or transact_code == "EUR":
                url = f"https://api.apilayer.com/exchangerates_data/convert?to={code}&from={transact_code}&amount={amount}"
                response = requests.request("GET", url, headers={"apikey":API_KEY}, data=payload)
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
        raise Exception


if __name__=="__main__":
    # data = read_json_file('data/operations.json')
    data = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]
    x1=convert_to_rub(data, 'RUB')
    print(x1)
