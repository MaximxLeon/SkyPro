import json
import logging
from typing import Any, Dict, List

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
