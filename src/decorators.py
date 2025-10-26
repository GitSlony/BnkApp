import os
from functools import wraps
from typing import Any, Callable, Mapping, Optional, Tuple


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования"""
    def log_msg(c_msg: str) -> None:
        if filename:
            my_file = open(os.path.join(os.curdir, filename), 'a', encoding='cp1251')
            if my_file.__sizeof__() == 0:
                my_file.write(c_msg)
            else:
                my_file.write('\n' + c_msg)
            my_file.close()
        else:
            print(c_msg)

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Tuple, **kwargs: Mapping) -> Any:
            try:
                result = func(*args, **kwargs)
                log_msg(func.__name__+' Ок')
                return result
            except Exception as e:
                log_msg(f'{func.__name__} error:{str(e)} . Inputs:{args} {kwargs}')
                return None

        return wrapper

    return my_decorator
