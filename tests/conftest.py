import os
import sys
from typing import Any, Dict, List

import pytest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PATH = os.path.join(BASE_DIR, "src")
sys.path.append(SRC_PATH)


@pytest.fixture
def operations_list() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-10T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2022-05-01T08:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
    ]


@pytest.fixture
def card_number() -> str:
    return "1234567890123456"


@pytest.fixture
def account_number() -> str:
    return "73654108430135874305"


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
        },
    ]
