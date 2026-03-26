from datetime import datetime
from typing import List
from unittest.mock import MagicMock, Mock, patch

from src.external_api import fTrnAmount, get_rate


@patch("requests.get")
def test_get_rate(mock_get: Mock) -> None:
    resp = MagicMock()
    resp.status_code = 200
    resp.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1562198399, "rate": 63.315897},
        "date": "2019-07-03",
        "historical": True,
        "result": 520543.416119,
    }
    mock_get.return_value = resp
    assert get_rate(nAmount=8221.37, cCur="USD", dOp=datetime(year=2019, month=7, day=3)) == 520543.416119
    mock_get.assert_called_once()


def test_fTrnAmount(test_json_trn: List[dict]) -> None:
    assert fTrnAmount(test_json_trn[1]) == 520543.416119
