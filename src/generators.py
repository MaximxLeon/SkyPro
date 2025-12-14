from typing import Any, Dict, Iterable, Iterator


def filter_by_currency(
    transactions: Iterable[Dict[str, Any]],
    currency_code: str,
) -> Iterator[Dict[str, Any]]:
    """
    Генератор, возвращающий транзакции с заданной валютой.
    """
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(
    transactions: Iterable[Dict[str, Any]],
) -> Iterator[str]:
    """
    Генератор описаний транзакций.
    """
    for transaction in transactions:
        description = transaction.get("description")
        if description is not None:
            yield description


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        yield " ".join(
            card_number[i:i + 4] for i in range(0, 16, 4)
        )
