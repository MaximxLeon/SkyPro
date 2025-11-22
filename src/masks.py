from typing import Union


def get_mask_card_number(card_number: Union[int, str]):
    """Маскирует номер банковской карты.
    Оставляет первые 6 цифр и последние 4, остальные заменяет на *.
    """
    str_card_number = str(card_number)

    # Проверка, чтобы номер был не слишком коротким
    if len(str_card_number) < 10:
        raise ValueError("Card number must contain at least 10 digits")

    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account: Union[int, str]):
    """Маскирует номер счёта, оставляет последние 4 цифры."""
    str_account = str(account)

    if len(str_account) < 4:
        raise ValueError("Account number must contain at least 4 digits")

    return f"**{str_account[-4:]}"
