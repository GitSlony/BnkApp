from typing import Callable, List


def default_msg(x: str, inp_list: List[str]) -> str:
    return f"значение должно быть одно из:{','.join(inp_list)}."


def oper_msg(x: str, inp_list: List[str]) -> str:
    return f"Статус операции {x} недоступен."


def get_input(cText: str, inp_list: List[str], fMsg: Callable = default_msg, cUp: bool = True) -> str:
    print(cText)
    chk_list = inp_list
    if cUp:
        chk_list = [str(one).upper() for one in inp_list]
    while True:
        x = str(input())
        if cUp:
            x = x.upper()
        if x in chk_list:
            return x
        print(fMsg(x, inp_list))
