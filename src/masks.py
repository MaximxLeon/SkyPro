import logging
from typing import Union

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Маскирует номер банковской карты.
    """
    logger.debug("Вызов get_mask_card_number")

    str_card_number = str(card_number)
    logger.debug(f"Номер карты преобразован в строку: {str_card_number}")

    if len(str_card_number) < 10:
        logger.error("Длина номера карты меньше 10 символов")
        raise ValueError("Card number must contain at least 10 digits")

    masked = (
        f"{str_card_number[:4]} "
        f"{str_card_number[4:6]}** **** "
        f"{str_card_number[-4:]}"
    )

    logger.info("Номер карты успешно замаскирован")
    return masked


def get_mask_account(account: Union[int, str]) -> str:
    """
    Маскирует номер банковского счёта.
    """
    logger.debug("Вызов get_mask_account")

    str_account = str(account)
    logger.debug(f"Номер счёта преобразован в строку: {str_account}")

    if len(str_account) < 5:
        logger.error("Длина номера счёта меньше 5 символов")
        raise ValueError("Account number must contain at least 4 digits")

    masked = f"**{str_account[-4:]}"
    logger.info("Номер счёта успешно замаскирован")

    return masked
