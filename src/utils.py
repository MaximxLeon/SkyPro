import csv
import json
import logging
import re
from typing import Any, Dict, List

import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def load_operations(path: str) -> List[Dict[str, Any]]:
    """
    Загружает финансовые транзакции из JSON-файла.
    """
    logger.debug(f"Попытка загрузки файла: {path}")

    try:
        with open(path, "r", encoding="utf-8") as file:
            data: Any = json.load(file)

            if isinstance(data, list):
                logger.info(
                    f"Файл {path} успешно загружен, операций: {len(data)}"
                )
                return data

            logger.error("JSON не является списком")
            return []

    except FileNotFoundError:
        logger.error(f"Файл не найден: {path}")
        return []

    except json.JSONDecodeError as error:
        logger.error(f"Ошибка декодирования JSON: {error}")
        return []


def load_operations_csv(path: str) -> List[Dict[str, Any]]:
    logger.debug(f"Попытка загрузки CSV файла: {path}")

    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            data = list(reader)

            logger.info(
                f"CSV файл {path} успешно загружен, операций: {len(data)}"
            )
            return data

    except FileNotFoundError:
        logger.error(f"Файл не найден: {path}")
        return []

    except Exception as error:
        logger.error(f"Ошибка при загрузке CSV файла: {error}")
        return []


def load_operations_excel(path: str) -> List[Dict[str, Any]]:
    """
    Загружает финансовые транзакции из Excel-файла.
    """
    logger.debug(f"Попытка загрузки Excel файла: {path}")

    try:
        df = pd.read_excel(path)
        data: List[Dict[str, Any]] = [
            {str(k): v for k, v in record.items()} for record in df.to_dict(orient="records")
        ]

        logger.info(
            f"Excel файл {path} успешно загружен, операций: {len(data)}"
        )
        return data

    except FileNotFoundError:
        logger.error(f"Файл не найден: {path}")
        return []

    except Exception as error:
        logger.error(f"Ошибка при загрузке Excel файла: {error}")
        return []


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по ключевому слову в описании.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [operation for operation in data if "description" in operation and pattern.search(operation["description"])]


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций в каждой категории по описанию.
    """
    result: Dict[str, int] = {category: 0 for category in categories}
    for operation in data:
        description = str(operation.get("description", ""))
        for category in categories:
            if category.lower() in description.lower():
                result[category] += 1
    return result
