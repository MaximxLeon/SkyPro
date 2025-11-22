from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Маскирует номер банковской карты.

    Формат: первые 6 цифр остаются видимыми, затем блок из скрытых символов,
    и последние 4 цифры.

    Пример:
        1234567890123456 -> "1234 56** **** 3456"
    """
    str_card_number = str(card_number)

    if len(str_card_number) < 10:
        raise ValueError("Card number must contain at least 10 digits")

    masked = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
    return masked


def get_mask_account(account: Union[int, str]) -> str:
    """
    Маскирует номер банковского счёта.

    Формат:
        **XXXX  — где XXXX последние 4 цифры.
    """
    str_account = str(account)

    if len(str_account) < 4:
        raise ValueError("Account number must contain at least 4 digits")

    return f"**{str_account[-4:]}"
