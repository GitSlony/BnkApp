import re
from typing import List

from src.widget import get_date_real


def filter_by_state(in_dict_list: List[dict], c_flt_state: str = "EXECUTED") -> List[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению c_flt_state (по умолчанию 'EXECUTED')"""
    ret_dict = [one_dict for one_dict in in_dict_list if one_dict.get("state") == c_flt_state]
    return ret_dict


def sort_by_date(in_dict_list: List[dict], in_reverse: bool = True) -> List[dict]:
    """Функция должна возвращать новый список, отсортированный по дате (date)"""
    ret_dict = sorted(in_dict_list, key=lambda one_rec: get_date_real(one_rec["date"]), reverse=in_reverse)
    return ret_dict


def sort_by_amount(in_dict_list: List[dict], in_reverse: bool = True) -> List[dict]:
    """Функция должна возвращать новый список, отсортированный по дате (date)"""
    ret_dict = sorted(in_dict_list, key=lambda one_rec: float(one_rec["amount"]), reverse=in_reverse)
    return ret_dict


def filter_by_cur(in_dict_list: list[dict], search: str) -> list[dict]:
    ret_dict = [one_dict for one_dict in in_dict_list if one_dict["currency_code"] == search]
    return ret_dict


def filter_by_dscr(in_dict_list: list[dict], search: str) -> list[dict]:
    pattern = re.compile(search)
    return [one_dict for one_dict in in_dict_list if pattern.search(str(one_dict.get("description"))) is not None]
