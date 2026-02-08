import sys
from datetime import datetime
from typing import Any, Dict, List

from src.utils import (
    load_operations,
    load_operations_csv,
    load_operations_excel,
    process_bank_operations,
    process_bank_search,
)


def format_transaction_date(iso_date: str) -> str:
    """
    Преобразует дату из формата ISO (например, 2023-01-04T13:13:34Z)
    в формат DD.MM.YYYY. Если преобразовать не удалось, возвращает исходное значение.
    """
    if not iso_date:
        return "Дата не указана"

    # Убираем 'Z', если есть
    iso_date = iso_date.rstrip("Z")

    try:
        dt = datetime.fromisoformat(iso_date)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return iso_date


def get_file_choice() -> int:
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    while True:
        choice = input("Ваш выбор: ").strip()
        if choice in {"1", "2", "3"}:
            return int(choice)
        print("Некорректный выбор. Попробуйте снова.")


def get_status_choice() -> str:
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    print(
        f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
        f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}"
    )
    while True:
        status = input("Ваш выбор: ").strip().upper()
        if status in valid_statuses:
            return status
        print(f'Статус операции "{status}" недоступен.')


def ask_yes_no(question: str) -> bool:
    while True:
        answer = input(f"{question} (Да/Нет): ").strip().lower()
        if answer in {"да", "д", "yes", "y"}:
            return True
        elif answer in {"нет", "н", "no", "n"}:
            return False
        print("Пожалуйста, введите Да или Нет.")


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    file_choice = get_file_choice()

    data: List[Dict[str, Any]]

    if file_choice == 1:
        path = input("Введите путь к JSON-файлу: ").strip()
        data = load_operations(path)
    elif file_choice == 2:
        path = input("Введите путь к CSV-файлу: ").strip()
        data = load_operations_csv(path)
    else:
        path = input("Введите путь к XLSX-файлу: ").strip()
        data = load_operations_excel(path)

    if not data:
        print("Файл пустой или не удалось загрузить данные.")
        sys.exit(0)

    status = get_status_choice()
    filtered_data = [op for op in data if str(op.get("state", "")).upper() == status]
    # print(data)

    if not filtered_data:
        print("Не найдено ни одной транзакции, подходящей под выбранный статус.")
        sys.exit(0)

    if ask_yes_no("Отсортировать операции по дате?"):
        ascending = ask_yes_no("Сортировать по возрастанию?")
        filtered_data.sort(key=lambda x: x.get("date", ""), reverse=not ascending)

    if ask_yes_no("Выводить только рублевые транзакции?"):
        if file_choice == 1:
            filtered_data = [
                op for op in filtered_data
                if op.get("operationAmount", {}).get("currency", {}).get("name") == "руб."
            ]
        else:
            filtered_data = [
                op for op in filtered_data
                if op.get("currency_name") == "Ruble"
            ]

    if ask_yes_no("Отфильтровать список транзакций по определенному слову в описании?"):
        keyword = input("Введите слово для фильтрации: ").strip()
        filtered_data = process_bank_search(filtered_data, keyword)

    print("\nРаспечатываю итоговый список транзакций...")
    if not filtered_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print(f"\nВсего банковских операций в выборке: {len(filtered_data)}\n")
    for op in filtered_data:
        date = format_transaction_date(op.get("date", "Дата не указана"))
        desc = op.get("description", "Описание не указано")

        # сумма
        if file_choice == 1:  # JSON
            amount = op.get("operationAmount", {}).get("amount", "Сумма не указана")
            currency = op.get("operationAmount", {}).get("currency", {}).get("name", "")
        else:  # CSV или Excel
            amount = op.get("amount", "Сумма не указана")
            currency = op.get("currency", "")

        # движение средств
        if op.get("from") and op.get("to"):
            movement = f"{op.get('from')} -> {op.get('to')}"
        elif op.get("to"):
            movement = f"-> {op.get('to')}"
        elif op.get("from"):
            movement = f"{op.get('from')} ->"
        else:
            movement = "Отправитель и получатель не указаны"

        print(f"{date} {desc}\nСумма: {amount} {currency}\n{movement}\n")

    # Пример подсчета категорий (дополнительно)
    if ask_yes_no("Хотите подсчитать количество операций по категориям?"):
        categories_input = input("Введите категории через запятую: ")
        categories = [cat.strip() for cat in categories_input.split(",")]
        counts = process_bank_operations(filtered_data, categories)
        print("\nСтатистика по категориям:")
        for cat, count in counts.items():
            print(f"{cat}: {count}")


if __name__ == "__main__":
    main()
