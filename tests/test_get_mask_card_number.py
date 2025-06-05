import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("1456 897 546 32 14 56", "1456 89** **** 1456"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


def test_get_mask_card_number_invalid_num(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


def test_get_mask_card_number_empty_num():
    with pytest.raises(ValueError):
        get_mask_card_number("")
