import json
from typing import Any, Dict, List


def load_operations(path: str) -> List[Dict[str, Any]]:
    """
    Загружает финансовые транзакции из JSON-файла.

    :param path: путь к JSON-файлу
    :return: список словарей с транзакциями или пустой список
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            data: Any = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
