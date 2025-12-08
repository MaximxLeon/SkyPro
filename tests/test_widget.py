from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("text,expected", [
("Visa Classic 1234567890123456", "Visa Classic 1234 56** **** 3456"),
("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(text, expected):
    assert mask_account_card(text) == expected


def test_get_date():
    assert get_date("2023-10-10T12:00:00") == "10.10.2023"
