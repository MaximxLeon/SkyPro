import json
from unittest.mock import mock_open, patch

from src.utils import load_operations


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
