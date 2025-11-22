from typing import Union


def get_mask_card_number(card_number: Union[int, str]):
    """Маскирует номер банковской карты, оставляет первые 6 цифр и последнии 4, остальные меняет на *"""
    str_card_number = str(card_number)
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account: Union[int, str]):
    """Маскирует номер счёта, оставляет последнии 4 цифры"""
    str_account = str(account)
    return f"**{str_account[-4:]}"
