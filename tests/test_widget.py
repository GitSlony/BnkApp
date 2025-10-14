from datetime import datetime

import pytest

from src.widget import get_date, get_date_real, mask_account_card


@pytest.mark.parametrize(
    "str_date, expected_result",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("9999-03-11T02:26:18.671407", "11.03.9999")],
)
def test_get_date(str_date: str, expected_result: str) -> None:
    assert get_date(str_date) == expected_result


@pytest.mark.parametrize("str_date, expected_result", [("", "11.03.2024"), ("9999-03-11", "11.03.9999")])
def test_get_bad_date(str_date: str, expected_result: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_date(str_date)


@pytest.mark.parametrize(
    "acc_card, expected_result",
    [
        ("Maestro 1596837868705199", "1596 83** **** 5199"),
        ("Счет 64686473678894779589", "**9589"),
        ("MasterCard 7158300734726758", "7158 30** **** 6758"),
        ("Счет 35383033474447895560", "**5560"),
        ("Visa Classic 6831982476737658", "6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "8990 92** **** 5229"),
        ("Visa Platinum 8990 9221 1366 5229", "8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "5999 41** **** 6353"),
        ("Счет 73654108430135874305", "**4305"),
        ("Счет ", " "),
        (" ", " "),
    ],
)
def test_mask_account_card(acc_card: str, expected_result: str) -> None:
    assert mask_account_card(acc_card) == expected_result


@pytest.mark.parametrize(
    "str_date, expected_result",
    [
        ("2024-03-11T02:26:18.671407", "2024-03-11T02:26:18.671407"),
        ("9999-03-11T02:26:18.671407", "9999-03-11T02:26:18.671407"),
    ],
)
def test_get_date_real(str_date: str, expected_result: str) -> None:
    assert get_date_real(str_date) == datetime.strptime(expected_result, "%Y-%m-%dT%H:%M:%S.%f")
