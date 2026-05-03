# Проект BnkApp

## Описание:

Проект BnkApp - это учебное приложение для SkyPro

## Домашние задания

Включает в себя ДЗ
10.1  
10.2
11.1
11.2
12.1
12.2
13.1
13.2

## Установка:

1. Клонируйте репозиторий: git clone git@github.com:GitSlony/BnkApp.git

2. Установите зависимости: pip install -r requirements.txt

## Использование:

1. Пока нет

## Документация:

Пока нет

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

## Реузльтат автотеста

```
C:\Users\mike\AppData\Local\pypoetry\Cache\virtualenvs\bnk-app-J0wwwQY2-py3.13\Scripts\python.exe C:/app/PyCharmCE/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path C:\PYTHON_PRJ\bnk_app\tests 
Testing started at 18:38 ...
Launching pytest with arguments C:\PYTHON_PRJ\bnk_app\tests --no-header --no-summary -q in C:\PYTHON_PRJ\bnk_app\tests

============================= test session starts =============================
collecting ... collected 46 items

test_decorators.py::test_log 
test_external_api.py::test_get_rate PASSED                                      [  2%]
test_external_api.py::test_fTrnAmount 
test_generators.py::test_filter_by_currency PASSED                               [  4%]https://api.apilayer.com/exchangerates_data/convert
{'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37}, 'info': {'timestamp': 1562198399, 'rate': 63.315897}, 'date': '2019-07-03', 'historical': True, 'result': 520543.416119}
PASSED                             [  6%]Сумма: 8221.37 валюта:USD дата:2019-07-03 18:35:29.512364
https://api.apilayer.com/exchangerates_data/convert
{'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37}, 'info': {'timestamp': 1562198399, 'rate': 63.315897}, 'date': '2019-07-03', 'historical': True, 'result': 520543.416119}

test_generators.py::test_filter_by_currency_excpt 
test_generators.py::test_transaction_descriptions 
test_generators.py::test_transaction_descriptions_expt 
test_generators.py::test_card_number_generator 
test_masks.py::test_get_mask_card_number[1596837868705199-1596 83** **** 5199] PASSED                       [  8%]PASSED                 [ 10%]PASSED                 [ 13%]PASSED            [ 15%]PASSED                    [ 17%]
test_masks.py::test_get_mask_card_number[7158300734726758-7158 30** **** 6758] 
test_masks.py::test_get_mask_card_number[6831982476737658-6831 98** **** 7658] 
test_masks.py::test_get_mask_card_number[8990922113665229-8990 92** **** 5229] 
test_masks.py::test_get_mask_card_number[5999414228426353-5999 41** **** 6353] 
test_masks.py::test_get_mask_card_number[3665229-] 
test_masks.py::test_get_mask_account[64686473678894779589-**9589] 
test_masks.py::test_get_mask_account[35383033474447895560-**5560] 
test_masks.py::test_get_mask_account[73654108430135874305-**4305] 
test_masks.py::test_get_mask_account[0-] 
test_masks.py::test_get_mask_account[736541084301358743464563305-] 
test_processing.py::test_sort_by_date PASSED [ 19%]PASSED [ 21%]PASSED [ 23%]PASSED [ 26%]PASSED [ 28%]PASSED                [ 30%]Длиннна номера карты должна быть 16 символов!
PASSED [ 32%]PASSED [ 34%]PASSED [ 36%]PASSED                          [ 39%]Длиннна номера счета должна быть 20 символов!
PASSED [ 41%]Длиннна номера счета должна быть 20 символов!

test_processing.py::test_sort_by_bad_date 
test_processing.py::test_filter_by_state 
test_processing.py::test_filter_by_bad_state 
test_scv_xls_utils.py::test_read_csv_trn PASSED                             [ 43%]PASSED                         [ 45%]time data '2019-07-03T18' does not match format '%Y-%m-%dT%H:%M:%S.%f'
PASSED                          [ 47%]PASSED                      [ 50%]
test_scv_xls_utils.py::test_read_xls_trn 
test_utils.py::test_read_json_trn PASSED                          [ 52%]PASSED                          [ 54%]['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description']

test_utils.py::test_get_json_attr_float 
test_utils.py::test_get_json_attr_str 
test_utils.py::test_get_json_attr_date 
test_widget.py::test_get_date[2024-03-11T02:26:18.671407-11.03.2024] PASSED                                 [ 56%]PASSED                           [ 58%]$.id not found
$.ABBB not found
PASSED                             [ 60%]$.id not found
$.ABBB not found
PASSED                            [ 63%]$.id not found
$.ABBB not found

test_widget.py::test_get_date[9999-03-11T02:26:18.671407-11.03.9999] 
test_widget.py::test_get_bad_date[-11.03.2024] 
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 64686473678894779589-**9589] 
test_widget.py::test_mask_account_card[MasterCard 7158300734726758-7158 30** **** 6758] 
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 35383033474447895560-**5560] 
test_widget.py::test_mask_account_card[Visa Classic 6831982476737658-6831 98** **** 7658] 
test_widget.py::test_mask_account_card[Visa Platinum 8990922113665229-8990 92** **** 5229] 
test_widget.py::test_mask_account_card[Visa Platinum 8990 9221 1366 5229-8990 92** **** 5229] 
test_widget.py::test_mask_account_card[Visa Gold 5999414228426353-5999 41** **** 6353] 
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 73654108430135874305-**4305] 
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 - ] 
test_widget.py::test_mask_account_card[ - ] 
test_widget.py::test_get_date_real[2024-03-11T02:26:18.671407-2024-03-11T02:26:18.671407] 
test_widget.py::test_get_date_real[9999-03-11T02:26:18.671407-9999-03-11T02:26:18.671407] 

============================= 46 passed in 4.76s ==============================
PASSED [ 65%]PASSED [ 67%]PASSED                    [ 69%]time data '' does not match format '%Y-%m-%dT%H:%M:%S.%f'

test_widget.py::test_get_bad_date[9999-03-11-11.03.9999] PASSED          [ 71%]time data '9999-03-11' does not match format '%Y-%m-%dT%H:%M:%S.%f'

test_widget.py::test_mask_account_card[Maestro 1596837868705199-1596 83** **** 5199] PASSED [ 73%]PASSED [ 76%]PASSED [ 78%]PASSED [ 80%]PASSED [ 82%]PASSED [ 84%]PASSED [ 86%]PASSED [ 89%]PASSED [ 91%]PASSED [ 93%]Строка не содержит нормера счета
PASSED                       [ 95%]Неправильный формат входной строки
PASSED [ 97%]PASSED [100%]
Process finished with exit code 0
```

## Покрытие тестами

```
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> pytest --cov
============================================================================================================================================== test session starts ===============================================================================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\PYTHON_PRJ\bnk_app
configfile: pyproject.toml
plugins: cov-7.0.0
collected 46 items                                                                                                                                                                                                                                                                                                

tests\test_decorators.py .                                                                                                                                                                                                                                                                                  [  2%]
tests\test_external_api.py ..                                                                                                                                                                                                                                                                               [  6%]
tests\test_generators.py .....                                                                                                                                                                                                                                                                              [ 17%]
tests\test_masks.py ...........                                                                                                                                                                                                                                                                             [ 41%]
tests\test_processing.py ....                                                                                                                                                                                                                                                                               [ 50%]
tests\test_scv_xls_utils.py ..                                                                                                                                                                                                                                                                              [ 54%]
tests\test_utils.py ....                                                                                                                                                                                                                                                                                    [ 63%] 
tests\test_widget.py .................                                                                                                                                                                                                                                                                      [100%] 

================================================================================================================================================= tests coverage ================================================================================================================================================= 
________________________________________________________________________________________________________________________________ coverage: platform win32, python 3.13.5-final-0 _________________________________________________________________________________________________________________________________ 

Name                          Stmts   Miss  Cover
-------------------------------------------------
src\__init__.py                   0      0   100%
src\csv_xls_utils.py             26      2    92%
src\decorators.py                24      5    79%
src\external_api.py              25      2    92%
src\generators.py                12      0   100%
src\log_mng.py                   18      8    56%
src\masks.py                     16      0   100%
src\processing.py                18      6    67%
src\utils.py                     41      0   100%
src\widget.py                    27      2    93%
tests\__init__.py                 0      0   100%
tests\conftest.py                20      1    95%
tests\test_decorators.py         21      0   100%
tests\test_external_api.py       14      0   100%
tests\test_generators.py         30      0   100%
tests\test_masks.py               8      0   100%
tests\test_processing.py         16      0   100%
tests\test_scv_xls_utils.py       7      0   100%
tests\test_utils.py              21      0   100%
tests\test_widget.py             17      0   100%
-------------------------------------------------
TOTAL                           361     26    93%
=============================================================================================================================================== 46 passed in 7.51s =============================================================================================================================================== 
```

## Проверка  линтерами

```
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> isort .
Skipped 2 files
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app>  flake8                                                                                                                                                                                                                                                                 
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app>  mypy .
Success: no issues found in 22 source files
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> black .
All done! ✨ 🍰 ✨                                                                                                                                                                                                                                                                                                   
22 files left unchanged.
```