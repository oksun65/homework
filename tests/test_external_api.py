from unittest.mock import patch

from src.external_api import convert_to_rub

data = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    },
]


@patch("requests.request")
def test_external_api(mock_request):
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = {"result": 10000.00}

    result = convert_to_rub(data, "RUB")
    assert result == [31957.58, 10000.00]
