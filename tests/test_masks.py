import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_num, expected_result", [
        (1596837868705199, "1596 83** **** 5199"),
        (7158300734726758, "7158 30** **** 6758"),
        (6831982476737658, "6831 98** **** 7658"),
        (8990922113665229, "8990 92** **** 5229"),
        (5999414228426353, "5999 41** **** 6353"),
        (3665229, "")])
def test_get_mask_card_number(card_num: int, expected_result: str) -> None:
    assert get_mask_card_number(card_num) == expected_result


@pytest.mark.parametrize(
    "acc_num, expected_result", [
        (64686473678894779589, "**9589"),
        (35383033474447895560, "**5560"),
        (73654108430135874305, "**4305"),
        (0, ""),
        (736541084301358743464563305, "")])
def test_get_mask_account(acc_num: int, expected_result: str) -> None:
    assert get_mask_account(acc_num) == expected_result
