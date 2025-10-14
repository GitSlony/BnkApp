from typing import Iterator, List

# from collections.abc import Iterator


def filter_by_currency(in_dict_list: List[dict], c_currency: str) -> Iterator[dict]:
    """Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует c_currency"""
    # chk_curr = lambda X:X.get("operationAmount").get("currency").get("code") == c_currency
    # out_list = filter(chk_curr, in_dict_list)
    # for one_trn in out_list:
    #     yield one_trn
    # -----------------------------------------------------------
    out_gen = (one_trn for one_trn in in_dict_list if one_trn["operationAmount"]["currency"]["code"] == c_currency)
    while True:
        yield next(out_gen)
    # -----------------------------------------------------------
    # return (one_trn  for one_trn in in_dict_list if chk_curr(one_trn))


def transaction_descriptions(in_dict_list: List[dict]) -> Iterator[str]:
    """возвращает описание каждой операции по очереди из списка in_dict_list"""
    for one_trn in in_dict_list:
        yield str(one_trn.get("description"))


def card_number_generator(i_from: int, i_to: int) -> Iterator[str]:
    """генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты
    где i_from, i_to начальное и конечное значения для генерации"""

    # out_gen = (f'{card_nn:0>20}' for card_nn in range(i_from,i_to+1))
    # while True:
    #     yield next(out_gen)
    def add_spaces(c_in: str) -> str:
        return c_in[0:4] + " " + c_in[4:8] + " " + c_in[8:12] + " " + c_in[12:]

    return (add_spaces(f"{card_nn:0>16}") for card_nn in range(i_from, i_to + 1))
