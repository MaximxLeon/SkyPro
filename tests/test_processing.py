from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state,expected_len",
    [
        ("EXECUTED", 2),
        ("CANCELED", 1),
    ],
)
def test_filter_by_state(
    operations_list: List[Dict[str, Any]], state: str, expected_len: int
) -> None:
    result = filter_by_state(operations_list, state)
    assert len(result) == expected_len
    assert all(op["state"] == state for op in result)


def test_sort_by_date_desc(operations_list: List[Dict[str, Any]]) -> None:
    result = sort_by_date(operations_list)
    assert result[0]["date"] == "2024-01-01T00:00:00"


def test_sort_by_date_asc(operations_list: List[Dict[str, Any]]) -> None:
    result = sort_by_date(operations_list, descending=False)
    assert result[0]["date"] == "2022-05-01T08:30:00"
