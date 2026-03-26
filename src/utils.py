import json
from datetime import datetime

from jsonpath_ng import parse  # type: ignore


def get_json_attr_float(data: dict, path: str) -> float | None:
    """функция получения значения атрибута из json по пути атрибута для float"""
    jsonpath_expression = parse(path)
    matches = jsonpath_expression.find(data)
    if matches == []:
        print(f"{path} not found")
        return None
    else:
        return float(matches[0].value)


def get_json_attr_str(data: dict, path: str) -> str | None:
    """функция получения значения атрибута из json по пути атрибута для строки"""
    jsonpath_expression = parse(path)
    matches = jsonpath_expression.find(data)
    if matches == []:
        print(f"{path} not found")
        return None
    else:
        return str(matches[0].value)


def get_json_attr_date(data: dict, path: str) -> datetime | None:
    """функция получения значения атрибута из json по пути атрибута для даты"""
    jsonpath_expression = parse(path)
    matches = jsonpath_expression.find(data)
    if matches == []:
        print(f"{path} not found")
        return None
    else:
        return datetime.strptime(str(matches[0].value), "%Y-%m-%dT%H:%M:%S.%f")  # 2018-11-23T17:47:33.127140


def read_json_trn(cFileName: str, cEncoding: str = "UTF-8") -> list:
    """Функция чтения JSON из файла"""
    try:
        with open(cFileName, encoding=cEncoding) as f:
            data = list(json.load(f))
            f.close()
            return data
    except json.JSONDecodeError:
        return list()
    except FileNotFoundError:
        return list()
