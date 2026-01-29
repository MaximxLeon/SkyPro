import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_transaction_to_rub(transaction: dict) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях (float).
    USD и EUR конвертируются через Exchange Rates Data API.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency not in ("USD", "EUR"):
        return 0.0

    headers = {
        "apikey": API_KEY
    }
    params = {
        "base": currency,
        "symbols": "RUB"
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()

    data = response.json()
    rate = float(data["rates"]["RUB"])

    return amount * rate
