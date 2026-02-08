import json
from typing import Any, Dict, Hashable, List
from unittest.mock import mock_open, patch

import pandas as pd

from src.utils import (
    load_operations,
    load_operations_csv,
    load_operations_excel,
    process_bank_operations,
    process_bank_search,
)


def test_load_operations_success():
    mock_data = [
        {"id": 1, "operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}},
        {"id": 2, "operationAmount": {"amount": "50", "currency": {"code": "USD"}}}
    ]
    m = mock_open(read_data=json.dumps(mock_data))

    with patch("builtins.open", m):
        result = load_operations("dummy.json")
        assert result == mock_data


def test_load_operations_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_operations("nonexistent.json")
        assert result == []


def test_load_operations_invalid_json():
    m = mock_open(read_data="invalid json")
    with patch("builtins.open", m):
        result = load_operations("dummy.json")
        assert result == []


def test_load_operations_not_list():
    m = mock_open(read_data=json.dumps({"id": 1}))
    with patch("builtins.open", m):
        result = load_operations("dummy.json")
        assert result == []


def test_load_operations_csv_success():
    mock_csv_data = (
        "id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;"
        "Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации"
    )

    m = mock_open(read_data=mock_csv_data)

    with patch("builtins.open", m):
        result = load_operations_csv("transactions.csv")

        expected = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

        assert result == expected


def test_load_operations_excel_success():
    mock_df = pd.DataFrame(
        [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )

    with patch("src.utils.pd.read_excel", return_value=mock_df):
        result = load_operations_excel("transactions.xlsx")

        expected = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

        assert result == expected


# Пример тестовых данных
mock_data: List[Dict[Hashable, Any]] = [
    {"id": 1, "description": "Перевод организации"},
    {"id": 2, "description": "Открытие вклада"},
    {"id": 3, "description": "Перевод на карту"},
    {"id": 4, "description": "Закрытие вклада"},
]


def test_process_bank_search_found():
    result = process_bank_search(mock_data, "вклад")
    assert len(result) == 2
    assert all("вклад" in op["description"].lower() for op in result)


def test_process_bank_search_not_found():
    result = process_bank_search(mock_data, "не существует")
    assert result == []


def test_process_bank_search_case_insensitive():
    result = process_bank_search(mock_data, "ВКЛАД")
    assert len(result) == 2
    assert all("вклад" in op["description"].lower() for op in result)


def test_process_bank_operations_counts():
    categories = ["Перевод", "вклад", "Другое"]
    result = process_bank_operations(mock_data, categories)
    assert result == {"Перевод": 2, "вклад": 2, "Другое": 0}


def test_process_bank_operations_empty_data():
    result = process_bank_operations([], ["Перевод"])
    assert result == {"Перевод": 0}


def test_process_bank_operations_empty_categories():
    result = process_bank_operations(mock_data, [])
    assert result == {}
