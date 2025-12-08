import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number,expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_get_mask_account(account_number: str = "73654108430135874305") -> None:
    assert get_mask_account(account_number) == "**4305"


@pytest.mark.parametrize("card_number", ["12345", "111"])
def test_get_mask_card_number_short_error(card_number: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("acc", ["12", "1234"])
def test_get_mask_account_short_error(acc: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(acc)
