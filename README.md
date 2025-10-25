# Проект BnkApp

## Описание:

Проект BnkApp - это учебное приложение для SkyPro

## Домашние задания

Включает в себя ДЗ
10.1  
10.2
11.1


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
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> pytest --cov                                                                                                                                                       
============================================================================================ test session starts ============================================================================================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\PYTHON_PRJ\bnk_app
configfile: pyproject.toml
plugins: cov-7.0.0
collected 37 items                                                                                                                                                                                           

tests\test_generators.py .....                                                                                                                                                                         [ 13%] 
tests\test_masks.py ...........                                                                                                                                                                        [ 43%]
tests\test_processing.py ....                                                                                                                                                                          [ 54%] 
tests\test_widget.py .................                                                                                                                                                                 [100%] 

============================================================================================== tests coverage =============================================================================================== 
______________________________________________________________________________ coverage: platform win32, python 3.13.5-final-0 ______________________________________________________________________________ 

Name                       Stmts   Miss  Cover
----------------------------------------------
src\__init__.py                0      0   100%
src\generators.py             12      0   100%
src\masks.py                  12      0   100%
src\processing.py              8      0   100%
src\widget.py                 27      2    93%
tests\__init__.py              0      0   100%
tests\conftest.py             17      1    94%
tests\test_generators.py      30      0   100%
tests\test_masks.py            8      0   100%
tests\test_processing.py      16      0   100%
tests\test_widget.py          17      0   100%
----------------------------------------------
TOTAL                        147      3    98%
============================================================================================ 37 passed in 0.48s ============================================================================================= 
```

## Проверка  линтерами

```
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> isort .
Skipped 2 files
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> flake8                                                                                                                                                             
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> mypy .
Success: no issues found in 12 source files
(bnk-app-py3.13) PS C:\PYTHON_PRJ\bnk_app> 
```