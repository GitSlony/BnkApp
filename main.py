from src.log_mng import mainLog
from src.masks import get_mask_account

# from src.processing import filter_by_state, sort_by_date
# from src.widget import get_date, mask_account_card
from src.utils import get_json_attr_float, get_json_attr_str, read_json_trn

lst_trn = read_json_trn("c://PYTHON_PRJ//bnk_app//data//empty.json")
lst_trn = read_json_trn("c://PYTHON_PRJ//bnk_app//data//nonexist.json")
lst_trn = read_json_trn("c://PYTHON_PRJ//bnk_app//data//operations.json")
mainLog().info(f"get_mask_account('123') {get_mask_account(123)}")
mainLog().info(
    f"Сумма какой попало проводки {get_json_attr_float(lst_trn[0], "operationAmount.amount")} "
    + f"{get_json_attr_str(lst_trn[0], "operationAmount.currency.code")}"
)
