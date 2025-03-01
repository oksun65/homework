import pytest

@pytest.fixture
def account_number():
    return "98"

@pytest.fixture
def card_number():
    return "14561234 897 546 32 14 56"

@pytest.fixture
def card_number_widget():
    return "Visa 2635312365489665412365479"

@pytest.fixture
def date_info():
    return "12-10"

@pytest.fixture
def account_records():
    return [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

