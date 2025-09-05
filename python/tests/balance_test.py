import pytest

## Корректный запрос баланса (баланс больше нуля)
def test_get_balance_positive(balance):
    response = balance.get_balance("acme", "000100")
    resp_balance = response.json().get("available", {}).get("value")
    balance = float(resp_balance)
    assert response.status_code == 200
    assert balance > 0

## Баланс равен нулю
def test_get_balance_zero(balance):
    response = balance.get_balance("acme", "000100")
    resp_balance = response.json().get("available", {}).get("value")
    available_blnc = float(resp_balance)
    assert response.status_code == 200
    assert available_blnc == 0