import functools
import logging
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции.

    :param filename: имя файла для логирования. Если None, вывод в консоль.
    :return: декорированная функция
    """
    def decorator(func: Callable) -> Callable:
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            handler: logging.Handler
            if filename:
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler()

            formatter = logging.Formatter('%(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise  # пробрасываем исключение дальше
        return wrapper
    return decorator
