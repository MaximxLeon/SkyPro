import csv
import json
import logging
from typing import Any, Dict, Hashable, List

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


def load_operations_excel(path: str) -> List[Dict[Hashable, Any]]:
    """
    Загружает финансовые транзакции из Excel-файла.
    """
    logger.debug(f"Попытка загрузки Excel файла: {path}")

    try:
        df = pd.read_excel(path)
        data = df.to_dict(orient="records")

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
