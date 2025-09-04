import pytest

from src.widget import mask_card_account


@pytest.mark.parametrize(
    "input, output",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_account_card(input, output):
    assert mask_card_account(input) == output


def test_mask_account_card_invalid_data(card_number_widget):
    with pytest.raises(ValueError):
        mask_card_account(card_number_widget)
