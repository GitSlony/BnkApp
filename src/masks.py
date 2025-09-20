def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    s_card_num = str(card_number)
    if len(s_card_num) != 16:
        print("Длиннна номера карты должна быть 16 символов!")
        return ""
    return f"{s_card_num[0:4]} {s_card_num[4:6]}** **** {s_card_num[-4:]}"


def get_mask_account(acc_number: int) -> str:
    """Функцию маскировки номера банковского счета"""
    s_acc_num = str(acc_number)
    if len(s_acc_num) != 20:
        print("Длиннна номера счета должна быть 20 символов!")
        return ""
    return f"**{s_acc_num[-4:]}"
