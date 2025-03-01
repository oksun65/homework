import pytest
from src.widget import get_date
from tests.conftest import date_info


@pytest.mark.parametrize('input, output', [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(input, output):
    assert get_date(input) == output

def test_get_date_empty_data():
    with pytest.raises(ValueError):
        get_date('')

def test_get_date_invalid_data(date_info):
    with pytest.raises(ValueError):
        get_date(date_info)

