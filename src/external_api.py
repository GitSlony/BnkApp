import os
from datetime import datetime

import requests  # type: ignore
from dotenv import load_dotenv

from src.utils import get_json_attr_date, get_json_attr_float, get_json_attr_str


def get_rate(nAmount: float, cCur: str, dOp: datetime) -> float | None:
    """функция получения значения курса через API api.apilayer.com"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    print(url)
    load_dotenv()
    hdr = {"apikey": os.getenv("tkn_apilayer")}
    par = {"to": "RUB", "from": cCur, "amount": nAmount, "date": dOp.strftime("%Y-%m-%d")}
    response = requests.get(url, headers=hdr, params=par)  #
    if response.status_code == 200:
        json_rate = response.json()
        print(json_rate)
        return get_json_attr_float(json_rate, "$.result")
    else:
        return None


def fTrnAmount(trn: dict) -> float | None:
    """функция получения суммы проводки в рублях из JSON"""
    nAmount = get_json_attr_float(trn, "$.operationAmount.amount")
    cCur = get_json_attr_str(trn, "$.operationAmount.currency.code")
    dOp = get_json_attr_date(trn, "$.date")
    if cCur is None or nAmount is None or dOp is None:
        return None
    else:
        # dOp = datetime(dOp).replace(microsecond=0)  # обнуляем hour = 0, minute = 0, second = 0,
        print(f"Сумма: {nAmount} валюта:{cCur} дата:{dOp}")  # :%Y-%m-%d
        return get_rate(nAmount, cCur, dOp)
