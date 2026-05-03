from src.csv_xls_utils import json2flat, read_csv_trn, read_xls_trn
from src.input_utils import get_input, oper_msg
from src.processing import filter_by_cur, filter_by_dscr, filter_by_state, sort_by_amount, sort_by_date
from src.utils import read_json_trn
from src.widget import mask_account_card

FILE_TYPES = {"1": "JSON", "2": "CSV", "3": "XLSX"}


def main() -> None:
    # ---------------------------------------------------------------------------
    str_1 = get_input(
        "Привет! Добро пожаловать в программу работы \n"
        "с банковскими транзакциями. \n"
        "Выберите необходимый пункт меню:)\n"
        "    1. Получить информацию о транзакциях из JSON-файла\n"
        "    2. Получить информацию о транзакциях из CSV-файла\n"
        "    3. Получить информацию о транзакциях из XLSX-файла\n"
        "    ",
        list(FILE_TYPES.keys()),
    )
    print(f"Для обработки выбран {FILE_TYPES[str_1]}- файл.")
    if str_1 == "1":
        lst_trn = json2flat(read_json_trn("c://PYTHON_PRJ//bnk_app//data//operations.json"))
    elif str_1 == "2":
        lst_trn = read_csv_trn("c://PYTHON_PRJ//bnk_app//data//transactions.csv")
    else:
        lst_trn = read_xls_trn("c://PYTHON_PRJ//bnk_app//data//transactions_excel.xlsx")
    print(lst_trn[0])
    # ---------------------------------------------------------------------------
    str_1 = get_input(
        "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
        + "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING ",
        ["EXECUTED", "CANCELED", "PENDING"],
        fMsg=oper_msg,
        cUp=True,
    )
    lst_trn = filter_by_state(lst_trn, str_1)
    print(f"Операции отфильтрованы по статусу {str_1}")
    # ---------------------------------------------------------------------------
    str_1 = get_input("Отсортировать операции по дате? Да / Нет", ["Да", "Нет"], cUp=True)
    if str_1 == "ДА":
        lst_trn = sort_by_date(lst_trn)
        print("Операции отсортированы по дате")
    # ---------------------------------------------------------------------------
    str_1 = get_input(
        "Отсортировать по возрастанию или по убыванию?",
        ["возрастанию", "убыванию"],  # саздизм в чистом виде - почему не выбирать цифры везде?
        cUp=True,
    )
    if str_1 == "ВОЗРАСТАНИЮ":
        lst_trn = sort_by_amount(lst_trn)
        print("Операции отсортированы по возрастанию")
    else:
        lst_trn = sort_by_amount(lst_trn, True)
        print("Операции отсортированы по убыванию")
    # ---------------------------------------------------------------------------
    str_1 = get_input("Выводить только рублевые транзакции? Да/Нет", ["Да", "Нет"], cUp=True)
    if str_1 == "ДА":
        lst_trn = filter_by_cur(lst_trn, "RUB")
        print("Операции отфильтрованы по валюте = 'RUB'")
    # ---------------------------------------------------------------------------
    str_1 = get_input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет", ["Да", "Нет"], cUp=True
    )
    if str_1 == "ДА":
        str_1 = ""
        while len(str_1) == 0:
            str_1 = str(input("Введите слово"))
        lst_trn = filter_by_dscr(lst_trn, str_1)
        print(f"Операции отфильтрованы по слову = '{str_1}'")
    # ---------------------------------------------------------------------------
    if len(lst_trn) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(lst_trn)}")
    for trn in lst_trn:
        print(f"{trn["date"]} {trn["description"]}")
        print(f"{mask_account_card(trn["from"])} --> {mask_account_card(trn["to"])}")
        print(f"Сумма:{mask_account_card(trn["from"])} --> {mask_account_card(trn["to"])}")


main()
