from datetime import datetime
from typing import List

from src.utils import get_json_attr_date, get_json_attr_float, get_json_attr_str, read_json_trn


def test_read_json_trn() -> None:
    assert len(read_json_trn("c://PYTHON_PRJ//bnk_app//data//operations.json")) == 101
    assert read_json_trn("c://PYTHON_PRJ//bnk_app//data//empty.json") == []
    assert read_json_trn("c://PYTHON_PRJ//bnk_app//data//nonexist.json") == []


def test_get_json_attr_float(test_json_trn: List[dict]) -> None:
    assert get_json_attr_float(test_json_trn[1], "$.operationAmount.amount") == 8221.37
    assert get_json_attr_float(test_json_trn[1], "$.id") == 41428829
    assert get_json_attr_float({}, "$.id") is None
    assert get_json_attr_float(test_json_trn[1], "$.ABBB") is None


def test_get_json_attr_str(test_json_trn: List[dict]) -> None:
    assert get_json_attr_str(test_json_trn[1], "$.operationAmount.currency.code") == "USD"
    assert get_json_attr_str(test_json_trn[1], "$.id") == "41428829"
    assert get_json_attr_str({}, "$.id") is None
    assert get_json_attr_str(test_json_trn[1], "$.ABBB") is None


def test_get_json_attr_date(test_json_trn: List[dict]) -> None:
    assert get_json_attr_date(test_json_trn[1], "$.date") == datetime(
        year=2019, month=7, day=3, hour=18, minute=35, second=29, microsecond=512364
    )
    assert get_json_attr_date({}, "$.id") is None
    assert get_json_attr_date(test_json_trn[1], "$.ABBB") is None
