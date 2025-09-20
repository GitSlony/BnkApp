import re
from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(in_str: str) -> str:
    """Функция  для обработки информации как о картах, так и о счетах"""
    if "Счет" in in_str:
        l_acc_num = re.search(r"\d+", in_str)
        if l_acc_num:
            return get_mask_account(int(l_acc_num[0]))
        else:
            print("Строка не содержит нормера счета")
            return " "
    elif "Visa" in in_str or "Maestro" in in_str or "MasterCard" in in_str:
        l_card_num = re.search(r"\d{4,4}\s\d{4,4}\s\d{4,4}\s\d{4,4}", in_str)
        if not l_card_num:
            l_card_num = re.search(r"\d+", in_str)
            if l_card_num:
                return get_mask_card_number(int(l_card_num[0]))
            else:
                print("Строка не содержит нормера карты")
                return " "
        else:
            return get_mask_card_number(int(l_card_num[0].replace(" ", "")))
    else:
        print("Неправильный формат входной строки")
        return " "


def get_date(in_str: str) -> str:
    """Преобразует строку с датой вида 2024-03-11T02:26:18.671407 к виду 11.03.2024"""
    intr_date = datetime.strptime(in_str, "%Y-%m-%dT%H:%M:%S.%f")
    return intr_date.strftime("%d.%m.%Y")
