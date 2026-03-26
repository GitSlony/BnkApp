from typing import List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(test_transactions: List[dict]) -> None:
    trn = filter_by_currency(test_transactions, "USD")
    assert next(trn) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(trn) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(trn) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_excpt(test_transactions: List[dict]) -> None:
    trn = filter_by_currency(test_transactions, "XAU")
    with pytest.raises(RuntimeError) as exc_info:
        next(trn)
    assert str(exc_info.value) == "generator raised StopIteration"


def test_transaction_descriptions(test_transactions: List[dict]) -> None:
    trn = transaction_descriptions(test_transactions)
    assert next(trn) == "Перевод организации"
    assert next(trn) == "Перевод со счета на счет"


def test_transaction_descriptions_expt(test_transactions: List[dict]) -> None:
    trn = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(trn)


def test_card_number_generator() -> None:
    card_nums = card_number_generator(1, 5)
    assert next(card_nums) == "0000 0000 0000 0001"
    assert next(card_nums) == "0000 0000 0000 0002"
    assert next(card_nums) == "0000 0000 0000 0003"
    assert next(card_nums) == "0000 0000 0000 0004"
    assert next(card_nums) == "0000 0000 0000 0005"
    with pytest.raises(StopIteration):
        next(card_nums)
