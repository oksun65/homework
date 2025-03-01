from typing import Any, Dict, List


def filter_by_state(my_data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция на входе принимает словарь аккаунтов (id) со статусами (state) и датой (date)
    и возвращает словарь с определенным статусом, переданным в переменную state"""
    return [item for item in my_data if item.get("state") == state]


def sort_by_date(my_data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Функция на входе принимает словарь аккаунтов (id) со статусами (state) и датой (date)
    и возвращает отсортированный по дате словарь."""
    return sorted(my_data, key=lambda x: x["date"], reverse=descending)


data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(filter_by_state(data, state="CANCELED"))
print(sort_by_date(data, descending=False))
