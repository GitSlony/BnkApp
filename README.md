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
Testing started at 19:02 ...
Launching pytest with arguments C:\PYTHON_PRJ\bnk_app\tests --no-header --no-summary -q in C:\PYTHON_PRJ\bnk_app\tests

============================= test session starts =============================
collecting ... collected 46 items

test_decorators.py::test_log 
test_external_api.py::test_get_rate PASSED                                      [  2%]
test_external_api.py::test_fTrnAmount 
test_generators.py::test_filter_by_currency PASSED                               [  4%]https://api.apilayer.com/exchangerates_data/convert
{'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37}, 'info': {'timestamp': 1562198399, 'rate': 63.315897}, 'date': '2019-07-03', 'historical': True, 'result': 520543.416119}
2026-04-19 19:02:29,205 DEBUG lgr.main 11: Запуск получения значения атрибута из json $.result
PASSED                             [  6%]Сумма: 8221.37 валюта:USD дата:2019-07-03 18:35:29.512364
https://api.apilayer.com/exchangerates_data/convert
{'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37}, 'info': {'timestamp': 1562198399, 'rate': 63.315897}, 'date': '2019-07-03', 'historical': True, 'result': 520543.416119}
2026-04-19 19:02:29,246 DEBUG lgr.main 11: Запуск получения значения атрибута из json $.operationAmount.amount
2026-04-19 19:02:29,262 DEBUG lgr.main 23: Запуск получения значения атрибута из json $.operationAmount.currency.code
2026-04-19 19:02:29,275 DEBUG lgr.main 35: Запуск получения значения атрибута из json $.date
2026-04-19 19:02:30,309 DEBUG lgr.main 11: Запуск получения значения атрибута из json $.result

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
test_processing.py::test_sort_by_date PASSED [ 19%]2026-04-19 19:02:30,351 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED [ 21%]2026-04-19 19:02:30,356 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED [ 23%]2026-04-19 19:02:30,362 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED [ 26%]2026-04-19 19:02:30,365 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED [ 28%]2026-04-19 19:02:30,371 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED                [ 30%]Длиннна номера карты должна быть 16 символов!
2026-04-19 19:02:30,377 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED [ 32%]2026-04-19 19:02:30,384 DEBUG lgr.main 16: Запуск Функцию маскировки номера банковского счета
PASSED [ 34%]2026-04-19 19:02:30,391 DEBUG lgr.main 16: Запуск Функцию маскировки номера банковского счета
PASSED [ 36%]2026-04-19 19:02:30,403 DEBUG lgr.main 16: Запуск Функцию маскировки номера банковского счета
PASSED                          [ 39%]Длиннна номера счета должна быть 20 символов!
2026-04-19 19:02:30,410 DEBUG lgr.main 16: Запуск Функцию маскировки номера банковского счета
2026-04-19 19:02:30,411 ERROR lgr.main 20: Длиннна номера счета должна быть 20 символов!
PASSED [ 41%]Длиннна номера счета должна быть 20 символов!
2026-04-19 19:02:30,423 DEBUG lgr.main 16: Запуск Функцию маскировки номера банковского счета
2026-04-19 19:02:30,423 ERROR lgr.main 20: Длиннна номера счета должна быть 20 символов!

test_processing.py::test_sort_by_bad_date 
test_processing.py::test_filter_by_state 
test_processing.py::test_filter_by_bad_state 
test_scv_xls_utils.py::test_read_csv_trn PASSED                             [ 43%]PASSED                         [ 45%]time data '2019-07-03T18' does not match format '%Y-%m-%dT%H:%M:%S.%f'
PASSED                          [ 47%]PASSED                      [ 50%]
test_scv_xls_utils.py::test_read_xls_trn 
test_utils.py::test_read_json_trn PASSED                          [ 52%]2026-04-19 19:02:30,468 DEBUG lgr.main 8: Запуск чтения транзакций из CSV файлa c://PYTHON_PRJ//bnk_app//data//transactions.csv
2026-04-19 19:02:30,478 DEBUG lgr.main 8: Запуск чтения транзакций из CSV файлa c://PYTHON_PRJ//bnk_app//data//nonexist.csv
2026-04-19 19:02:30,485 ERROR lgr.main 15: Файл c://PYTHON_PRJ//bnk_app//data//nonexist.csv не найден
PASSED                          [ 54%]['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description']
2026-04-19 19:02:30,503 DEBUG lgr.main 21: Запуск чтения транзакций из XLS файлa c://PYTHON_PRJ//bnk_app//data//transactions_excel.xlsx
2026-04-19 19:02:31,498 DEBUG lgr.main 21: Запуск чтения транзакций из XLS файлa c://PYTHON_PRJ//bnk_app//data//nonexist.xlsx
2026-04-19 19:02:31,499 ERROR lgr.main 29: Файл c://PYTHON_PRJ//bnk_app//data//nonexist.xlsx не найден

test_utils.py::test_get_json_attr_float 
test_utils.py::test_get_json_attr_str 
test_utils.py::test_get_json_attr_date 
test_widget.py::test_get_date[2024-03-11T02:26:18.671407-11.03.2024] PASSED                                 [ 56%]2026-04-19 19:02:31,504 DEBUG lgr.main 47: Запуск чтения JSON из файлa c://PYTHON_PRJ//bnk_app//data//operations.json
2026-04-19 19:02:31,505 DEBUG lgr.main 47: Запуск чтения JSON из файлa c://PYTHON_PRJ//bnk_app//data//empty.json
2026-04-19 19:02:31,506 ERROR lgr.main 54: Ошибка чтения JSON из c://PYTHON_PRJ//bnk_app//data//empty.json
2026-04-19 19:02:31,506 DEBUG lgr.main 47: Запуск чтения JSON из файлa c://PYTHON_PRJ//bnk_app//data//nonexist.json
2026-04-19 19:02:31,506 ERROR lgr.main 57: Файл c://PYTHON_PRJ//bnk_app//data//nonexist.json не найден
PASSED                           [ 58%]$.id not found
$.ABBB not found
2026-04-19 19:02:31,510 DEBUG lgr.main 11: Запуск получения значения атрибута из json $.operationAmount.amount
2026-04-19 19:02:31,525 DEBUG lgr.main 11: Запуск получения значения атрибута из json $.id
2026-04-19 19:02:31,538 DEBUG lgr.main 11: Запуск получения значения атрибута из json $.id
2026-04-19 19:02:31,550 DEBUG lgr.main 11: Запуск получения значения атрибута из json $.ABBB
PASSED                             [ 60%]$.id not found
$.ABBB not found
2026-04-19 19:02:31,578 DEBUG lgr.main 23: Запуск получения значения атрибута из json $.operationAmount.currency.code
2026-04-19 19:02:31,592 DEBUG lgr.main 23: Запуск получения значения атрибута из json $.id
2026-04-19 19:02:31,610 DEBUG lgr.main 23: Запуск получения значения атрибута из json $.id
2026-04-19 19:02:31,624 DEBUG lgr.main 23: Запуск получения значения атрибута из json $.ABBB
PASSED                            [ 63%]$.id not found
$.ABBB not found
2026-04-19 19:02:31,640 DEBUG lgr.main 35: Запуск получения значения атрибута из json $.date
2026-04-19 19:02:31,652 DEBUG lgr.main 35: Запуск получения значения атрибута из json $.id
2026-04-19 19:02:31,665 DEBUG lgr.main 35: Запуск получения значения атрибута из json $.ABBB

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

============================= 46 passed in 5.15s ==============================
PASSED [ 65%]PASSED [ 67%]PASSED                    [ 69%]time data '' does not match format '%Y-%m-%dT%H:%M:%S.%f'

test_widget.py::test_get_bad_date[9999-03-11-11.03.9999] PASSED          [ 71%]time data '9999-03-11' does not match format '%Y-%m-%dT%H:%M:%S.%f'

test_widget.py::test_mask_account_card[Maestro 1596837868705199-1596 83** **** 5199] PASSED [ 73%]2026-04-19 19:02:31,708 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED [ 76%]2026-04-19 19:02:31,718 DEBUG lgr.main 16: Запуск Функцию маскировки номера банковского счета
PASSED [ 78%]2026-04-19 19:02:31,728 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED [ 80%]2026-04-19 19:02:31,748 DEBUG lgr.main 16: Запуск Функцию маскировки номера банковского счета
PASSED [ 82%]2026-04-19 19:02:31,761 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED [ 84%]2026-04-19 19:02:31,778 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED [ 86%]2026-04-19 19:02:31,790 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED [ 89%]2026-04-19 19:02:31,801 DEBUG lgr.main 6: Запуск Функция маскировки номера банковской карты
PASSED [ 91%]2026-04-19 19:02:31,805 DEBUG lgr.main 16: Запуск Функцию маскировки номера банковского счета
PASSED [ 93%]Строка не содержит нормера счета
PASSED                       [ 95%]Неправильный формат входной строки
PASSED [ 97%]PASSED [100%]
Process finished with exit code 0
```

## Покрытие тестами

```
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app>  pytest --cov                                                                                                                                                                                                                                                            
=============================================================================================================================================== test session starts ===============================================================================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\PYTHON_PRJ\bnk_app
configfile: pyproject.toml
plugins: cov-7.0.0
collected 46 items                                                                                                                                                                                                                                                                                                 

tests\test_decorators.py .                                                                                                                                                                                                                                                                                   [  2%] 
tests\test_external_api.py ..                                                                                                                                                                                                                                                                                [  6%]
tests\test_generators.py .....                                                                                                                                                                                                                                                                               [ 17%] 
tests\test_masks.py ...........                                                                                                                                                                                                                                                                              [ 41%] 
tests\test_processing.py ....                                                                                                                                                                                                                                                                                [ 50%]
tests\test_scv_xls_utils.py ..                                                                                                                                                                                                                                                                               [ 54%]
tests\test_utils.py ....                                                                                                                                                                                                                                                                                     [ 63%] 
tests\test_widget.py .................                                                                                                                                                                                                                                                                       [100%] 

================================================================================================================================================= tests coverage ================================================================================================================================================== 
_________________________________________________________________________________________________________________________________ coverage: platform win32, python 3.13.5-final-0 _________________________________________________________________________________________________________________________________ 

Name                          Stmts   Miss  Cover
-------------------------------------------------
src\__init__.py                   0      0   100%
src\csv_xls_utils.py             22      0   100%
src\decorators.py                24      5    79%
src\external_api.py              25      2    92%
src\generators.py                12      0   100%
src\log_mng.py                   19      0   100%
src\masks.py                     16      0   100%
src\processing.py                 8      0   100%
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
TOTAL                           348     10    97%
=============================================================================================================================================== 46 passed in 8.71s ================================================================================================================================================ 
```

## Проверка  линтерами

```
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> isort .
Skipped 2 files
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app>  flake8                                                                                                                                                                                                                                                                  
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app>  mypy .
Success: no issues found in 21 source files
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> black .
reformatted C:\PYTHON_PRJ\bnk_app\main.py

All done! ✨ 🍰 ✨
1 file reformatted, 20 files left unchanged.
```