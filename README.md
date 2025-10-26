# Проект BnkApp

## Описание:

Проект BnkApp - это учебное приложение для SkyPro

## Домашние задания

Включает в себя ДЗ
10.1  
10.2
11.1
11.2


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
Testing started at 20:24 ...
Launching pytest with arguments C:\PYTHON_PRJ\bnk_app\tests --no-header --no-summary -q in C:\PYTHON_PRJ\bnk_app\tests

============================= test session starts =============================
collecting ... collected 38 items

test_decorators.py::test_log PASSED                                      [  2%]
test_generators.py::test_filter_by_currency PASSED                       [  5%]
test_generators.py::test_filter_by_currency_excpt PASSED                 [  7%]
test_generators.py::test_transaction_descriptions PASSED                 [ 10%]
test_generators.py::test_transaction_descriptions_expt PASSED            [ 13%]
test_generators.py::test_card_number_generator PASSED                    [ 15%]
test_masks.py::test_get_mask_card_number[1596837868705199-1596 83** **** 5199] PASSED [ 18%]
test_masks.py::test_get_mask_card_number[7158300734726758-7158 30** **** 6758] PASSED [ 21%]
test_masks.py::test_get_mask_card_number[6831982476737658-6831 98** **** 7658] PASSED [ 23%]
test_masks.py::test_get_mask_card_number[8990922113665229-8990 92** **** 5229] PASSED [ 26%]
test_masks.py::test_get_mask_card_number[5999414228426353-5999 41** **** 6353] PASSED [ 28%]
test_masks.py::test_get_mask_card_number[3665229-] PASSED                [ 31%]Длиннна номера карты должна быть 16 символов!

test_masks.py::test_get_mask_account[64686473678894779589-**9589] PASSED [ 34%]
test_masks.py::test_get_mask_account[35383033474447895560-**5560] PASSED [ 36%]
test_masks.py::test_get_mask_account[73654108430135874305-**4305] PASSED [ 39%]
test_masks.py::test_get_mask_account[0-] PASSED                          [ 42%]Длиннна номера счета должна быть 20 символов!

test_masks.py::test_get_mask_account[736541084301358743464563305-] PASSED [ 44%]Длиннна номера счета должна быть 20 символов!

test_processing.py::test_sort_by_date PASSED                             [ 47%]
test_processing.py::test_sort_by_bad_date PASSED                         [ 50%]time data '2019-07-03T18' does not match format '%Y-%m-%dT%H:%M:%S.%f'

test_processing.py::test_filter_by_state PASSED                          [ 52%]
test_processing.py::test_filter_by_bad_state PASSED                      [ 55%]
test_widget.py::test_get_date[2024-03-11T02:26:18.671407-11.03.2024] PASSED [ 57%]
test_widget.py::test_get_date[9999-03-11T02:26:18.671407-11.03.9999] PASSED [ 60%]
test_widget.py::test_get_bad_date[-11.03.2024] PASSED                    [ 63%]time data '' does not match format '%Y-%m-%dT%H:%M:%S.%f'

test_widget.py::test_get_bad_date[9999-03-11-11.03.9999] PASSED          [ 65%]time data '9999-03-11' does not match format '%Y-%m-%dT%H:%M:%S.%f'

test_widget.py::test_mask_account_card[Maestro 1596837868705199-1596 83** **** 5199] PASSED [ 68%]
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 64686473678894779589-**9589] PASSED [ 71%]
test_widget.py::test_mask_account_card[MasterCard 7158300734726758-7158 30** **** 6758] PASSED [ 73%]
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 35383033474447895560-**5560] PASSED [ 76%]
test_widget.py::test_mask_account_card[Visa Classic 6831982476737658-6831 98** **** 7658] PASSED [ 78%]
test_widget.py::test_mask_account_card[Visa Platinum 8990922113665229-8990 92** **** 5229] PASSED [ 81%]
test_widget.py::test_mask_account_card[Visa Platinum 8990 9221 1366 5229-8990 92** **** 5229] PASSED [ 84%]
test_widget.py::test_mask_account_card[Visa Gold 5999414228426353-5999 41** **** 6353] PASSED [ 86%]
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 73654108430135874305-**4305] PASSED [ 89%]
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 - ] PASSED [ 92%]Строка не содержит нормера счета

test_widget.py::test_mask_account_card[ - ] PASSED                       [ 94%]Неправильный формат входной строки

test_widget.py::test_get_date_real[2024-03-11T02:26:18.671407-2024-03-11T02:26:18.671407] PASSED [ 97%]
test_widget.py::test_get_date_real[9999-03-11T02:26:18.671407-9999-03-11T02:26:18.671407] PASSED [100%]

============================= 38 passed in 0.23s ==============================

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
collected 38 items                                                                                                                                                                                                                                                                                                  

tests\test_decorators.py .                                                                                                                                                                                                                                                                                   [  2%] 
tests\test_generators.py .....                                                                                                                                                                                                                                                                               [ 15%] 
tests\test_masks.py ...........                                                                                                                                                                                                                                                                              [ 44%] 
tests\test_processing.py ....                                                                                                                                                                                                                                                                                [ 55%] 
tests\test_widget.py .................                                                                                                                                                                                                                                                                       [100%] 

================================================================================================================================================= tests coverage ================================================================================================================================================== 
_________________________________________________________________________________________________________________________________ coverage: platform win32, python 3.13.5-final-0 _________________________________________________________________________________________________________________________________ 

Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\decorators.py             24      5    79%
src\generators.py             12      0   100%
src\masks.py                  12      0   100%
src\processing.py              8      0   100%
src\widget.py                 27      2    93%
tests\__init__.py              0      0   100%
tests\conftest.py             17      1    94%
tests\test_decorators.py      21      0   100%
tests\test_generators.py      30      0   100%
tests\test_masks.py            8      0   100%
tests\test_processing.py      16      0   100%
tests\test_widget.py          17      0   100%
----------------------------------------------
TOTAL                        192      8    96%
=============================================================================================================================================== 38 passed in 0.59s ================================================================================================================================================ 
```

## Проверка  линтерами

```
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> isort .
Skipped 2 files
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> flake8                                                                                                                                                                                                                                                                   
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> mypy .
Success: no issues found in 14 source files
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> 
```