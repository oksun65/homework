def filter_by_state(my_id, state="EXECUTED"):
    """ функция возвращает словарь по ключу state."""
    return [item for item in my_id if item.get('state') == state]


def sort_by_date(data, descending=True):
    """функция возвращает отсортированный по дате словарь."""
    return sorted(data, key=lambda x: x['date'], reverse=descending)
