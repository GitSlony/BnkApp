from typing import List

import pytest

from src.processing import filter_by_state, sort_by_date


def test_sort_by_date(test_trn_list_dict: List[dict]) -> None:
    assert sort_by_date(test_trn_list_dict, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert sort_by_date(test_trn_list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_bad_date(test_bad_date_trn_list_dict: List[dict]) -> None:
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(test_bad_date_trn_list_dict)


def test_filter_by_state(test_trn_list_dict: List[dict]) -> None:
    assert filter_by_state(test_trn_list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(test_trn_list_dict, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_bad_state(test_bad_state_trn_list_dict: List[dict]) -> None:
    assert filter_by_state(test_bad_state_trn_list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
    ]
    assert filter_by_state(test_bad_state_trn_list_dict, "CANCELED") == [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]
