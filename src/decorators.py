import functools
import logging
import sys
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции.

    :param filename: имя файла для логирования. Если None, вывод в консоль.
    :return: декорированная функция
    """
    def decorator(func: Callable) -> Callable:
        logger_name = f"{__name__}.{func.__name__}"
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)

        # Добавляем хендлер только если его нет
        if not logger.handlers:
            if filename:
                handler: logging.Handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler(sys.stdout)

            formatter = logging.Formatter('%(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    logger.info(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")  # <-- print вместо logger
                return result
            except Exception as e:
                if filename:
                    logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
        return wrapper
    return decorator
