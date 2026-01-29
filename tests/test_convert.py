from src.external_api.convert import convert_transaction_to_rub
from unittest.mock import patch, Mock

def test_rub_transaction():
    transaction = {
        "operationAmount": {"amount": "1500", "currency": {"code": "RUB"}}
    }
    result = convert_transaction_to_rub(transaction)
    assert result == 1500.0

@patch("external_api.convert.requests.get")
def test_usd_transaction(mock_get):
    # Мокаем ответ API
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 90.0}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {"amount": "10", "currency": {"code": "USD"}}
    }

    result = convert_transaction_to_rub(transaction)
    assert result == 900.0
    mock_get.assert_called_once()

@patch("external_api.convert.requests.get")
def test_eur_transaction(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"rates": {"RUB": 95.0}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {"amount": "5", "currency": {"code": "EUR"}}
    }

    result = convert_transaction_to_rub(transaction)
    assert result == 475.0
    mock_get.assert_called_once()

def test_unknown_currency():
    transaction = {
        "operationAmount": {"amount": "100", "currency": {"code": "JPY"}}
    }
    result = convert_transaction_to_rub(transaction)
    assert result == 0.0
