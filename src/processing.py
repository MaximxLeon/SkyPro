from typing import List, Dict, Any, Union


def filter_by_state(
    operations: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует операции по статусу выполнения

    Аргументы:
        operations: Список словарей с данными о банковских операциях
        state: Статус операции для фильтрации (по умолчанию 'EXECUTED')

    Возвращает:
        Новый список словарей, содержащий только операции с указанным статусом
    """
    filtered_operations = []
    for operation in operations:
        if operation.get("state") == state:
            filtered_operations.append(operation)
    return filtered_operations


def sort_by_date(
    operations: List[Dict[str, Any]], descending: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует операции по дате.

    Аргументы:
        operations: Список словарей с данными о банковских операциях
        descending: Порядок сортировки
            True - по убыванию (новые операции сначала)
            False - по возрастанию (старые операции сначала)

    Возвращает:
        Новый список словарей, отсортированный по дате
    """
    def get_date(operation: Dict[str, Any]) -> Union[str, Any]:
        date_value = operation.get("date")
        return date_value if date_value is not None else ""

    return sorted(operations, key=get_date, reverse=descending)


# Примеры использования
if __name__ == "__main__":
    # Тестовые данные
    test_data = [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]

    print("Фильтрация по EXECUTED:")
    print(filter_by_state(test_data))

    print("\nФильтрация по CANCELED:")
    print(filter_by_state(test_data, "CANCELED"))

    print("\nСортировка по убыванию:")
    print(sort_by_date(test_data))

    print("\nСортировка по возрастанию:")
    print(sort_by_date(test_data, False))
