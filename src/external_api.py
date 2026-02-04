import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY: str | None = os.getenv("API_KEY")
BASE_URL: str = "https://api.apilayer.com/exchangerates_data/convert"


def convert_transaction_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях (float).
    USD и EUR конвертируются через Exchange Rates Data API.
    """
    amount: float = float(transaction["operationAmount"]["amount"])
    currency: str = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency not in ("USD", "EUR"):
        return 0.0

    if not API_KEY:
        raise RuntimeError("API_KEY not found in environment variables")

    headers: dict[str, str] = {"apikey": API_KEY}
    params: dict[str, str] = {
        "from": currency,
        "to": "RUB",
        "amount": str(amount),
    }

    response: requests.Response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()

    data: Dict[str, Any] = response.json()
    converted_amount: float = float(data["result"])

    return converted_amount
