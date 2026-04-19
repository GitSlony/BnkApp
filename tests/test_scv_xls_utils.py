from src.csv_xls_utils import read_csv_trn, read_xls_trn


def test_read_csv_trn() -> None:
    assert len(read_csv_trn("c://PYTHON_PRJ//bnk_app//data//transactions.csv")) == 1000
    assert read_csv_trn("c://PYTHON_PRJ//bnk_app//data//nonexist.csv") == []


def test_read_xls_trn() -> None:
    assert len(read_xls_trn("c://PYTHON_PRJ//bnk_app//data//transactions_excel.xlsx")) == 1000
    assert read_xls_trn("c://PYTHON_PRJ//bnk_app//data//nonexist.xlsx") == []
