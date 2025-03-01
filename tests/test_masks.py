from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.widget import mask_card_account, get_date
from src.proccessing import filter_by_state, sort_by_date
from tests.conftest import account_number, card_number, card_number_widget, date_info, account_records


def test_get_mask_card_number(card_number):
    # assert get_mask_card_number(account_number) == "1456 89** **** 1456"
    assert get_mask_card_number(card_number) == "1456 89** **** 1456"
#    assert get_mask_card_number(card_number) == "1456 89** **** 14"


def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "**2147"


def test_mask_card_account(card_number_widget):
    assert mask_card_account(card_number_widget) == "Visa Gold 5999 41** **** 6353"

def test_get_date(date_info):
    assert get_date(date_info) == "11.03.2024"


def test_filter_by_sate(account_records):
    assert filter_by_state(account_records) == [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]

def test_sorted_by_date(account_records):
    assert sort_by_date(account_records) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
