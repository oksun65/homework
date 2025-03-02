import pytest

from src.masks import get_mask_account


@pytest.mark.parametrize(
    "value, expected",
    [
        ("985632 147", "**2147"),
    ],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


def test_get_mask_account_invalid_num(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)


def test_get_mask_account_empty_num():
    with pytest.raises(ValueError):
        get_mask_account("")
