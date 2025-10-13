# Проект BnkApp

## Описание:

Проект BnkApp - это учебное приложение для SkyPro

## Установка:

1. Клонируйте репозиторий: git clone git@github.com:GitSlony/BnkApp.git

2. Установите зависимости: pip install -r requirements.txt

## Использование:

1. Пока нет

## Документация:

Пока нет

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).

## Покрытие тестами

```
===================================================================================== test session starts ======================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\PYTHON_PRJ\bnk_app
configfile: pyproject.toml
plugins: cov-7.0.0
collected 32 items                                                                                                                                                                              

tests\test_masks.py ...........                                                                                                                                                           [ 34%] 
tests\test_processing.py ....                                                                                                                                                             [ 46%]
tests\test_widget.py .................                                                                                                                                                    [100%] 

======================================================================================== tests coverage ======================================================================================== 
_______________________________________________________________________ coverage: platform win32, python 3.13.5-final-0 ________________________________________________________________________ 

Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\masks.py                  12      0   100%
src\processing.py              8      0   100%
src\widget.py                 27      2    93%
tests\__init__.py              0      0   100%
tests\conftest.py             14      1    93%
tests\test_masks.py            8      0   100%
tests\test_processing.py      15      0   100%
tests\test_widget.py          16      0   100%
----------------------------------------------
TOTAL                        100      3    97%
====================================================================================== 32 passed in 0.40s ====================================================================================== 
```

## Реузльтат автотеста

```
============================= test session starts =============================
collecting ... collected 32 items

test_masks.py::test_get_mask_card_number[1596837868705199-1596 83** **** 5199] PASSED [  3%]
test_masks.py::test_get_mask_card_number[7158300734726758-7158 30** **** 6758] PASSED [  6%]
test_masks.py::test_get_mask_card_number[6831982476737658-6831 98** **** 7658] PASSED [  9%]
test_masks.py::test_get_mask_card_number[8990922113665229-8990 92** **** 5229] PASSED [ 12%]
test_masks.py::test_get_mask_card_number[5999414228426353-5999 41** **** 6353] PASSED [ 15%]
test_masks.py::test_get_mask_card_number[3665229-] PASSED                [ 18%]Длиннна номера карты должна быть 16 символов!

test_masks.py::test_get_mask_account[64686473678894779589-**9589] PASSED [ 21%]
test_masks.py::test_get_mask_account[35383033474447895560-**5560] PASSED [ 25%]
test_masks.py::test_get_mask_account[73654108430135874305-**4305] PASSED [ 28%]
test_masks.py::test_get_mask_account[0-] PASSED                          [ 31%]Длиннна номера счета должна быть 20 символов!

test_masks.py::test_get_mask_account[736541084301358743464563305-] PASSED [ 34%]Длиннна номера счета должна быть 20 символов!

test_processing.py::test_sort_by_date PASSED                             [ 37%]
test_processing.py::test_sort_by_bad_date PASSED                         [ 40%]
test_processing.py::test_filter_by_state PASSED                          [ 43%]
test_processing.py::test_filter_by_bad_state PASSED                      [ 46%]
test_widget.py::test_get_date[2024-03-11T02:26:18.671407-11.03.2024] PASSED [ 50%]
test_widget.py::test_get_date[9999-03-11T02:26:18.671407-11.03.9999] PASSED [ 53%]
test_widget.py::test_get_bad_date[-11.03.2024] PASSED                    [ 56%]
test_widget.py::test_get_bad_date[9999-03-11-11.03.9999] PASSED          [ 59%]
test_widget.py::test_mask_account_card[Maestro 1596837868705199-1596 83** **** 5199] PASSED [ 62%]
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 64686473678894779589-**9589] PASSED [ 65%]
test_widget.py::test_mask_account_card[MasterCard 7158300734726758-7158 30** **** 6758] PASSED [ 68%]
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 35383033474447895560-**5560] PASSED [ 71%]
test_widget.py::test_mask_account_card[Visa Classic 6831982476737658-6831 98** **** 7658] PASSED [ 75%]
test_widget.py::test_mask_account_card[Visa Platinum 8990922113665229-8990 92** **** 5229] PASSED [ 78%]
test_widget.py::test_mask_account_card[Visa Platinum 8990 9221 1366 5229-8990 92** **** 5229] PASSED [ 81%]
test_widget.py::test_mask_account_card[Visa Gold 5999414228426353-5999 41** **** 6353] PASSED [ 84%]
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 73654108430135874305-**4305] PASSED [ 87%]
test_widget.py::test_mask_account_card[\u0421\u0447\u0435\u0442 - ] PASSED [ 90%]Строка не содержит нормера счета

test_widget.py::test_mask_account_card[ - ] PASSED                       [ 93%]Неправильный формат входной строки

test_widget.py::test_get_date_real[2024-03-11T02:26:18.671407-2024-03-11T02:26:18.671407] PASSED [ 96%]
test_widget.py::test_get_date_real[9999-03-11T02:26:18.671407-9999-03-11T02:26:18.671407] PASSED [100%]

============================= 32 passed in 0.21s ==============================

Process finished with exit code 0
```

## Проверка  линтерами

```
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> isort .
Fixing C:\PYTHON_PRJ\bnk_app\tests\test_processing.py
Fixing C:\PYTHON_PRJ\bnk_app\tests\test_widget.py
Skipped 2 files
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> flake8                                                                                                                                                
.\tests\test_processing.py:22:39: F841 local variable 'exc_info' is assigned to but never used
.\tests\test_widget.py:21:39: F841 local variable 'exc_info' is assigned to but never used
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> mypy .
Success: no issues found in 10 source files
```