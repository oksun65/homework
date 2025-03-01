from typing import Any, Dict, List


def filter_by_state(my_data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция на входе принимает словарь аккаунтов (id) со статусами (state) и датой (date)
    и возвращает словарь с определенным статусом, переданным в переменную state"""
    return [item for item in my_data if item.get("state") == state]


def sort_by_date(my_data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Функция на входе принимает словарь аккаунтов (id) со статусами (state) и датой (date)
    и возвращает отсортированный по дате словарь."""
    return sorted(my_data, key=lambda x: x["date"], reverse=descending)
