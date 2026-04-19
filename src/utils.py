import json
from datetime import datetime

from jsonpath_ng import parse  # type: ignore

from src.log_mng import mainLog


def get_json_attr_float(data: dict, path: str) -> float | None:
    """функция получения значения атрибута из json по пути атрибута для float"""
    mainLog().debug(f"Запуск получения значения атрибута из json {path}")
    jsonpath_expression = parse(path)
    matches = jsonpath_expression.find(data)
    if matches == []:
        print(f"{path} not found")
        return None
    else:
        return float(matches[0].value)


def get_json_attr_str(data: dict, path: str) -> str | None:
    """функция получения значения атрибута из json по пути атрибута для строки"""
    mainLog().debug(f"Запуск получения значения атрибута из json {path}")
    jsonpath_expression = parse(path)
    matches = jsonpath_expression.find(data)
    if matches == []:
        print(f"{path} not found")
        return None
    else:
        return str(matches[0].value)


def get_json_attr_date(data: dict, path: str) -> datetime | None:
    """функция получения значения атрибута из json по пути атрибута для даты"""
    mainLog().debug(f"Запуск получения значения атрибута из json {path}")
    jsonpath_expression = parse(path)
    matches = jsonpath_expression.find(data)
    if matches == []:
        print(f"{path} not found")
        return None
    else:
        return datetime.strptime(str(matches[0].value), "%Y-%m-%dT%H:%M:%S.%f")  # 2018-11-23T17:47:33.127140


def read_json_trn(cFileName: str, cEncoding: str = "UTF-8") -> list:
    """Функция чтения JSON из файла"""
    mainLog().debug(f"Запуск чтения JSON из файлa {cFileName}")
    try:
        with open(cFileName, encoding=cEncoding) as f:
            data = list(json.load(f))
            f.close()
            return data
    except json.JSONDecodeError:
        mainLog().error(f"Ошибка чтения JSON из {cFileName}")
        return list()
    except FileNotFoundError:
        mainLog().error(f"Файл {cFileName} не найден")
        return list()
