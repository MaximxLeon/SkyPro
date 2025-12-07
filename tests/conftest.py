import pytest
import sys
import os

# Добавляем в sys.path путь к папке src
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PATH = os.path.join(BASE_DIR, "src")
sys.path.append(SRC_PATH)


@pytest.fixture
def operations_list():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-10T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2022-05-01T08:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
    ]


@pytest.fixture
def card_number():
    return "1234567890123456"


@pytest.fixture
def account_number():
    return "73654108430135874305"
