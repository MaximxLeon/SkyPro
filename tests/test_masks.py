from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number: str) -> None:
    assert get_mask_card_number(card_number) == "1234 56** **** 3456"


def test_get_mask_account(account_number: str) -> None:
    assert get_mask_account(account_number) == "**4305"


def test_get_mask_card_number_short_error() -> None:
    try:
        get_mask_card_number("12345")
    except ValueError:
        assert True
    else:
        assert False


def test_get_mask_account_short_error() -> None:
    try:
        get_mask_account("12")
    except ValueError:
        assert True
    else:
        assert False
