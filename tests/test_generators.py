import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency_usd(transactions):
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert all(
        tx["operationAmount"]["currency"]["code"] == "USD"
        for tx in result
    )


def test_filter_by_currency_no_matches(transactions):
    result = list(filter_by_currency(transactions, "EUR"))
    assert result == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
    ]


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
        (
            9999_9999_9999_9998,
            9999_9999_9999_9999,
            [
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected
