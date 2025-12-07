from src.widget import get_date, mask_account_card


def test_mask_account_card_card() -> None:
    text = "Visa Classic 1234567890123456"
    assert mask_account_card(text) == "Visa Classic 1234 56** **** 3456"


def test_mask_account_card_account() -> None:
    text = "Счет 73654108430135874305"
    assert mask_account_card(text) == "Счет **4305"


def test_get_date() -> None:
    assert get_date("2023-10-10T12:00:00") == "10.10.2023"
