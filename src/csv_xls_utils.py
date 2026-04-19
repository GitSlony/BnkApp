from csv import DictReader

import pandas as pd

from src.log_mng import mainLog


def read_csv_trn(cFileName: str, cEncoding: str = "UTF-8", cDelimiter: str = ";") -> list:
    """Функция чтения транзакций из файла"""
    mainLog().debug(f"Запуск чтения транзакций из CSV файлa {cFileName}")
    try:
        with open(cFileName, encoding=cEncoding) as f:
            data = list(DictReader(f, delimiter=cDelimiter))
            f.close()
            return data
    except FileNotFoundError:
        mainLog().error(f"Файл {cFileName} не найден")
        return list()


def read_xls_trn(cFileName: str) -> list:
    """Функция чтения транзакций из файла"""
    mainLog().debug(f"Запуск чтения транзакций из XLS файлa {cFileName}")
    try:
        df = pd.read_excel(cFileName)
        # frame_shape = data_frame.shape
        print(df.columns.to_list())
        # data = [(one for one in data_frame.columns)]
        return df.reset_index().to_dict("records")
    except FileNotFoundError:
        mainLog().error(f"Файл {cFileName} не найден")
        return list()
