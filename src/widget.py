from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime

def mask_account_card(data: str) -> str:
    """
    Принимает строку с типом и номером карты или счёта.
    Пример:
        Visa Platinum 7000792289606361
        Maestro 1596837868705199
        Счет 73654108430135874305

    Возвращает строку с замаскированным номером.
    Для карт использует маску карты, для счетов — маску счета.
    """

    parts = data.split()
    # Последнее слово в строке — это всегда номер
    number = parts[-1]
    # Всё, кроме последнего слова — название карты/счёта
    name = " ".join(parts[:-1])

    # Проверяем, является ли это счетом
    if name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_str: str):
    """
    Преобразует дату формата 'YYYY-MM-DDTHH:MM:SS.mmmmmm'
    в формат 'DD.MM.YYYY'
    """
    # Преобразуем строку в объект datetime
    date_obj = datetime.fromisoformat(date_str)

    # Возвращаем строку в нужном формате
    return date_obj.strftime("%d.%m.%Y")