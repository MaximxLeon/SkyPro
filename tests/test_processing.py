from typing import Dict, List

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(operations_list: List[Dict[str, str]]) -> None:
    result = filter_by_state(operations_list, "EXECUTED")
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)


def test_filter_by_state_canceled(operations_list: List[Dict[str, str]]) -> None:
    result = filter_by_state(operations_list, "CANCELED")
    assert len(result) == 1
    assert result[0]["state"] == "CANCELED"


def test_sort_by_date_desc(operations_list: List[Dict[str, str]]) -> None:
    result = sort_by_date(operations_list)
    assert result[0]["date"] == "2024-01-01T00:00:00"


def test_sort_by_date_asc(operations_list: List[Dict[str, str]]) -> None:
    result = sort_by_date(operations_list, descending=False)
    assert result[0]["date"] == "2022-05-01T08:30:00"
