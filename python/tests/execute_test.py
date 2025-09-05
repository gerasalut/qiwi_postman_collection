import pytest

##Исполнение платежа
def test_execute_payment(execute):
    response = execute.execute_payment("acme", "000100", "b100-00100-b200")
    data = response.json()
    assert response.status_code == 200
    assert "paymentId" in data, "Нет paymentId"
    assert "creationDateTime" in data, "Нет creationDateTime"
    assert "expirationDatetime" in data, "Нет expirationDatetime"
    assert "status" in data, "Нет status"
    assert "recipientDetails" in data, "Нет recipientDetails"
    assert "amount" in data, "Нет amount"