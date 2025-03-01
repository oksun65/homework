from typing import Any

def filter_by_state(my_data:Any, state:str="EXECUTED") -> Any:
    """функция возвращает словарь по ключу state."""
    return [item for item in my_data if item.get("state") == state]


def sort_by_date(data:Any, descending:bool=True) -> Any:
    """функция возвращает отсортированный по дате словарь."""
    return sorted(data, key=lambda x: x["date"], reverse=descending)
